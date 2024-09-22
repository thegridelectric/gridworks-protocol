import json
import uuid
from pathlib import Path

from pydantic import ValidationError

from gwproto import Message
from gwproto.messages import (
    Ack,
    AnyEvent,
    GtShStatusEvent,
    MQTTConnectEvent,
    MQTTConnectFailedEvent,
    MQTTDisconnectEvent,
    MQTTFullySubscribedEvent,
    PeerActiveEvent,
    PingMessage,
    ProblemEvent,
    Problems,
    ResponseTimeoutEvent,
    ShutdownEvent,
    SnapshotSpaceheatEvent,
    StartupEvent,
)
from gwproto.types import (
    GtShCliAtnCmd,
    GtShStatus,
    PowerWatts,
    SnapshotSpaceheat,
)
from tests.dummy_decoders import CHILD, PARENT
from tests.dummy_decoders.child.codec import ChildMQTTCodec
from tests.dummy_decoders.parent.codec import ParentMQTTCodec

from .decode_utils import MessageCase, assert_encode_decode

TEST_DATA_DIR = Path(__file__).parent / "data"


def get_stored_message_dicts() -> dict:
    return {}


def child_to_parent_payload_dicts() -> dict:
    d = {}
    for prefix in ["status", "snapshot"]:
        with (TEST_DATA_DIR / f"{prefix}_message.json").open() as f:
            d[prefix] = json.loads(f.read())
            d[prefix]["Header"]["Src"] = CHILD
    return d


def child_to_parent_messages() -> list[MessageCase]:
    stored_message_dicts = child_to_parent_payload_dicts()
    status_message_dict = stored_message_dicts["status"]
    gt_sh_status = GtShStatus.model_validate(status_message_dict["Payload"])
    gt_sh_status_event = GtShStatusEvent(Src=CHILD, status=gt_sh_status)
    unrecognized_status_event = AnyEvent(**gt_sh_status_event.model_dump())
    unrecognized_status_event.TypeName += ".foo"
    unrecognized_event = AnyEvent(
        TypeName="gridworks.event.bar", MessageId="1", TimeNS=1, Src="1"
    )
    unrecognizeable_not_event_type = AnyEvent(
        **dict(
            gt_sh_status_event.model_dump(),
            TypeName="bla",
        )
    )
    unrecognizeable_bad_event_content = {"TypeName": "gridworks.event.baz"}
    snap_message_dict = stored_message_dicts["snapshot"]
    snapshot_spaceheat = SnapshotSpaceheat.model_validate(snap_message_dict["Payload"])
    snapshot_event = SnapshotSpaceheatEvent(Src=CHILD, snap=snapshot_spaceheat)

    return [
        # PowerWatts
        MessageCase(
            "PowerWatts",
            Message(Src=CHILD, MessageType="power.watts", Payload=PowerWatts(Watts=1)),
        ),
        # status
        # QUESTION: why does this fail when replacing "gt.sh.status.110" with "gt.sh.status"?
        MessageCase(
            "status-payload-obj",
            Message(Src=CHILD, MessageType="gt.sh.status.110", Payload=gt_sh_status),
            None,
            gt_sh_status,
        ),
        MessageCase(
            "status-payload-dict",
            Message(Src=CHILD, Payload=status_message_dict["Payload"]),
            None,
            gt_sh_status,
        ),
        MessageCase(
            "status-payload-as_dict",
            Message(Src=CHILD, Payload=gt_sh_status),
            None,
            gt_sh_status,
        ),
        # snapshot
        MessageCase("snap", Message(**snap_message_dict), None, snapshot_spaceheat),
        MessageCase(
            "snap-payload-dict",
            Message(Src=CHILD, Payload=snap_message_dict["Payload"]),
            None,
            snapshot_spaceheat,
        ),
        MessageCase(
            "snap-payload-as_dict",
            Message(Src=CHILD, Payload=snapshot_spaceheat),
            None,
            snapshot_spaceheat,
        ),
        # events
        MessageCase("event-status", Message(Src=CHILD, Payload=gt_sh_status_event)),
        MessageCase(
            "event-unrecognized-status",
            Message(Src=CHILD, Payload=unrecognized_status_event),
        ),
        MessageCase(
            "event-unrecognized", Message(Src=CHILD, Payload=unrecognized_event)
        ),
        MessageCase(
            "unrecognized-not-event",
            Message(
                Src=CHILD,
                Payload=unrecognizeable_not_event_type,
            ),
            exp_exceptions=[ValidationError],
        ),
        MessageCase(
            "unrecognizeable-bad-event",
            Message(
                Src=CHILD,
                Payload=unrecognizeable_bad_event_content,
            ),
            exp_exceptions=[ValidationError],
        ),
        MessageCase("snap-payload-obj", Message(Src=CHILD, Payload=snapshot_event)),
        MessageCase("startup-event", Message(Src=CHILD, Payload=StartupEvent())),
        MessageCase(
            "shutdown-event", Message(Src=CHILD, Payload=ShutdownEvent(Reason="foo"))
        ),
        MessageCase(
            "problem-event",
            Message(
                Src=CHILD,
                Payload=ProblemEvent(ProblemType=Problems.error, Summary="foo"),
            ),
        ),
        MessageCase(
            "mqtt-connect-event",
            Message(Src=CHILD, Payload=MQTTConnectEvent(PeerName=PARENT)),
        ),
        MessageCase(
            "mqtt-conenct-failed-event",
            Message(Src=CHILD, Payload=MQTTConnectFailedEvent(PeerName=PARENT)),
        ),
        MessageCase(
            "mqtt-disconnect-event",
            Message(Src=CHILD, Payload=MQTTDisconnectEvent(PeerName=PARENT)),
        ),
        MessageCase(
            "mqtt-fully-subscribed-event",
            Message(Src=CHILD, Payload=MQTTFullySubscribedEvent(PeerName=PARENT)),
        ),
        MessageCase(
            "response-timeout-event",
            Message(Src=CHILD, Payload=ResponseTimeoutEvent(PeerName=PARENT)),
        ),
        MessageCase(
            "peer-active-event",
            Message(Src=CHILD, Payload=PeerActiveEvent(PeerName=PARENT)),
        ),
        # misc messages
        MessageCase("ping", PingMessage(Src=CHILD)),
        MessageCase("ack", Message(Src=CHILD, Payload=Ack(AckMessageID="1"))),
    ]


def parent_to_child_messages() -> list[MessageCase]:
    snapshot_request = GtShCliAtnCmd(
        FromGNodeAlias="a.b.c",
        FromGNodeId=str(uuid.uuid4()),
        SendSnapshot=True,
    )
    return [
        # misc messages
        MessageCase("ping", PingMessage(Src=PARENT)),
        MessageCase("ack", Message(Src=PARENT, Payload=Ack(AckMessageID="1"))),
        MessageCase(
            "snap",
            Message(Src=PARENT, Payload=snapshot_request),
            None,
            snapshot_request,
        ),
    ]


def test_decoder_simple() -> None:
    child_codec = ChildMQTTCodec()
    parent_codec = ParentMQTTCodec()
    assert_encode_decode(child_codec, parent_codec, child_to_parent_messages())
    assert_encode_decode(parent_codec, child_codec, parent_to_child_messages())
