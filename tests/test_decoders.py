import json
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from gwproto import Message
from gwproto.messages import (
    Ack,
    AnyEvent,
    MQTTConnectEvent,
    MQTTConnectFailedEvent,
    MQTTDisconnectEvent,
    MQTTFullySubscribedEvent,
    PeerActiveEvent,
    PingMessage,
    ProblemEvent,
    Problems,
    ReportEvent,
    ResponseTimeoutEvent,
    ShutdownEvent,
    StartupEvent,
)
from gwproto.named_types import (
    PowerWatts,
    Report,
    SendSnap,
)
from tests.dummy_decoders import CHILD, PARENT
from tests.dummy_decoders.child.codec import ChildMQTTCodec
from tests.dummy_decoders.parent.codec import ParentMQTTCodec

from .decode_utils import MessageCase, assert_encode_decode

TEST_DATA_DIR = Path(__file__).parent / "data"


def get_stored_message_dicts() -> dict[str, Any]:
    return {}


def child_to_parent_payload_dicts() -> dict[str, Any]:
    d = {}
    for prefix in ["report", "snapshot"]:
        with (TEST_DATA_DIR / f"{prefix}_message.json").open() as f:
            d[prefix] = json.loads(f.read())
            d[prefix]["Header"]["Src"] = CHILD
            d[prefix]["Header"]["Dst"] = PARENT
    return d


def child_to_parent_messages() -> list[MessageCase]:
    stored_message_dicts = child_to_parent_payload_dicts()
    report_event_dict = stored_message_dicts["report"]
    report = Report.model_validate(report_event_dict["Payload"]["Report"])
    report_event = ReportEvent.model_validate(report_event_dict["Payload"])
    unrecognized_report_event = AnyEvent(**report_event.model_dump(exclude_none=True))
    unrecognized_report_event.TypeName += ".foo"
    unrecognized_event = AnyEvent(
        TypeName="gridworks.event.bar",
        MessageId="1",
        TimeCreatedMs=1728754878213,
        Src="1",
    )
    unrecognizeable_not_event_type = AnyEvent(
        **dict(
            report_event.model_dump(),
            TypeName="bla",
        )
    )
    unrecognizeable_bad_event_content = {"TypeName": "gridworks.event.baz"}

    return [
        MessageCase(
            "power-watts",
            Message(
                Src=CHILD,
                Dst=PARENT,
                MessageType="power.watts",
                Payload=PowerWatts(Watts=1),
            ),
        ),
        # Report
        MessageCase(
            "report",
            Message(Src=CHILD, Dst=PARENT, MessageType="report", Payload=report),
            None,
            report,
        ),
        MessageCase(
            "report-as_dict",
            Message(Src=CHILD, Dst=PARENT, Payload=report),
            None,
            report,
        ),
        # # events
        MessageCase(
            "report-event",
            Message(Src=CHILD, Dst=PARENT, Payload=report_event_dict["Payload"]),
            None,
            report_event,
        ),
        # MessageCase(
        #     "event-unrecognized-status",
        #     Message(Src=CHILD, Dst=PARENT, Payload=unrecognized_report_event),
        # ),
        MessageCase(
            "event-unrecognized",
            Message(Src=CHILD, Dst=PARENT, Payload=unrecognized_event),
        ),
        MessageCase(
            "unrecognized-not-event",
            Message(
                Src=CHILD,
                Dst=PARENT,
                Payload=unrecognizeable_not_event_type,
            ),
            exp_exceptions=[ValidationError],
        ),
        MessageCase(
            "unrecognizeable-bad-event",
            Message(
                Src=CHILD,
                Dst=PARENT,
                Payload=unrecognizeable_bad_event_content,
            ),
            exp_exceptions=[ValidationError],
        ),
        MessageCase(
            "startup-event", Message(Src=CHILD, Dst=PARENT, Payload=StartupEvent())
        ),
        MessageCase(
            "shutdown-event",
            Message(Src=CHILD, Dst=PARENT, Payload=ShutdownEvent(Reason="foo")),
        ),
        MessageCase(
            "problem-event",
            Message(
                Src=CHILD,
                Dst=PARENT,
                Payload=ProblemEvent(ProblemType=Problems.error, Summary="foo"),
            ),
        ),
        MessageCase(
            "mqtt-connect-event",
            Message(Src=CHILD, Dst=PARENT, Payload=MQTTConnectEvent(PeerName=PARENT)),
        ),
        MessageCase(
            "mqtt-conenct-failed-event",
            Message(
                Src=CHILD, Dst=PARENT, Payload=MQTTConnectFailedEvent(PeerName=PARENT)
            ),
        ),
        MessageCase(
            "mqtt-disconnect-event",
            Message(
                Src=CHILD, Dst=PARENT, Payload=MQTTDisconnectEvent(PeerName=PARENT)
            ),
        ),
        MessageCase(
            "mqtt-fully-subscribed-event",
            Message(
                Src=CHILD, Dst=PARENT, Payload=MQTTFullySubscribedEvent(PeerName=PARENT)
            ),
        ),
        MessageCase(
            "response-timeout-event",
            Message(
                Src=CHILD, Dst=PARENT, Payload=ResponseTimeoutEvent(PeerName=PARENT)
            ),
        ),
        MessageCase(
            "peer-active-event",
            Message(Src=CHILD, Dst=PARENT, Payload=PeerActiveEvent(PeerName=PARENT)),
        ),
        # # misc messages
        MessageCase("ping", PingMessage(Src=CHILD, Dst=PARENT)),
        MessageCase(
            "ack", Message(Src=CHILD, Dst=PARENT, Payload=Ack(AckMessageID="1"))
        ),
    ]


def parent_to_child_messages() -> list[MessageCase]:
    snapshot_request = SendSnap(
        FromGNodeAlias="a.b.c",
    )
    # set_relay = GtDispatchBoolean(
    #     AboutNodeName="a.b.c",
    #     ToGNodeAlias="a.b.c",
    #     FromGNodeAlias="a.b.c",
    #     FromGNodeInstanceId=str(uuid.uuid4()),
    #     RelayState=True,
    #     SendTimeUnixMs=int(time.time() * 1000),
    # )
    return [
        # misc messages
        MessageCase("ping", PingMessage(Src=PARENT, Dst=CHILD)),
        MessageCase(
            "ack", Message(Src=PARENT, Dst=CHILD, Payload=Ack(AckMessageID="1"))
        ),
        MessageCase(
            "snap",
            Message(Src=PARENT, Dst=CHILD, Payload=snapshot_request),
            None,
            snapshot_request,
        ),
        # MessageCase(
        #     "set-relay",
        #     Message(Src=PARENT, Dst=CHILD, Payload=set_relay),
        #     None,
        #     set_relay,
        # ),
    ]


def test_decoder_simple() -> None:
    child_codec = ChildMQTTCodec()
    parent_codec = ParentMQTTCodec()
    assert_encode_decode(child_codec, parent_codec, child_to_parent_messages())
    assert_encode_decode(parent_codec, child_codec, parent_to_child_messages())
