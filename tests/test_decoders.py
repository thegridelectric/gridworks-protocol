import json
import time
import uuid
from pathlib import Path

from gwproto import Message
from gwproto.messages import (
    Ack,
    AnyEvent,
    GtDispatchBoolean_Maker,
    GtShCliAtnCmd_Maker,
    GtShStatus_Maker,
    GtShStatusEvent,
    MQTTConnectEvent,
    MQTTConnectFailedEvent,
    MQTTDisconnectEvent,
    MQTTFullySubscribedEvent,
    PeerActiveEvent,
    PingMessage,
    PowerWatts_Maker,
    ProblemEvent,
    Problems,
    ResponseTimeoutEvent,
    ShutdownEvent,
    SnapshotSpaceheat_Maker,
    SnapshotSpaceheatEvent,
    StartupEvent,
)
from pydantic import ValidationError

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
    gt_sh_status = GtShStatus_Maker.dict_to_tuple(status_message_dict["Payload"])
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
    snapshot_spaceheat = SnapshotSpaceheat_Maker.dict_to_tuple(
        snap_message_dict["Payload"]
    )
    snapshot_event = SnapshotSpaceheatEvent(Src=CHILD, snap=snapshot_spaceheat)

    return [
        # Gs Pwr
        MessageCase(
            "GsPwr",
            Message(
                Src=CHILD, MessageType="power.watts", Payload=PowerWatts_Maker(1).tuple
            ),
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
            Message(Src=CHILD, Payload=gt_sh_status.as_dict()),
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
            Message(Src=CHILD, Payload=snapshot_spaceheat.as_dict()),
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
    snapshot_request = GtShCliAtnCmd_Maker(
        from_g_node_alias="a.b.c",
        from_g_node_id=str(uuid.uuid4()),
        send_snapshot=True,
    ).tuple
    set_relay = GtDispatchBoolean_Maker(
        about_node_name="a.b.c",
        to_g_node_alias="a.b.c",
        from_g_node_alias="a.b.c",
        from_g_node_instance_id=str(uuid.uuid4()),
        relay_state=1,
        send_time_unix_ms=int(time.time() * 1000),
    ).tuple
    return [
        # misc messages
        MessageCase("ping", PingMessage(Src=PARENT)),
        MessageCase("ack", Message(Src=PARENT, Payload=Ack(AckMessageID="1"))),
        MessageCase(
            "snap",
            Message(Src=PARENT, Payload=snapshot_request.as_dict()),
            None,
            snapshot_request,
        ),
        MessageCase(
            "set-relay",
            Message(Src=PARENT, Payload=set_relay.as_dict()),
            None,
            set_relay,
        ),
    ]


def test_decoder_simple() -> None:
    child_codec = ChildMQTTCodec()
    parent_codec = ParentMQTTCodec()
    assert_encode_decode(child_codec, parent_codec, child_to_parent_messages())
    assert_encode_decode(parent_codec, child_codec, parent_to_child_messages())
