import json
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from typing import Optional


try:
    from rich import print
except ImportError:
    pass

from gwproto import Message
from gwproto import MQTTCodec
from gwproto.gs import GsPwr_Maker
from gwproto.messages import Ack
from gwproto.messages import GtShStatusEvent
from gwproto.messages import MQTTConnectEvent
from gwproto.messages import MQTTConnectFailedEvent
from gwproto.messages import MQTTDisconnectEvent
from gwproto.messages import MQTTFullySubscribedEvent
from gwproto.messages import PeerActiveEvent
from gwproto.messages import PingMessage
from gwproto.messages import ProblemEvent
from gwproto.messages import Problems
from gwproto.messages import ResponseTimeoutEvent
from gwproto.messages import ShutdownEvent
from gwproto.messages import SnapshotSpaceheatEvent
from gwproto.messages import StartupEvent
from gwproto.types import GtDispatchBoolean_Maker
from gwproto.types import GtShCliAtnCmd_Maker
from gwproto.types import GtShStatus_Maker
from gwproto.types import SnapshotSpaceheat_Maker
from tests.dummy_decoders import CHILD
from tests.dummy_decoders import PARENT
from tests.dummy_decoders.child.codec import ChildMQTTCodec
from tests.dummy_decoders.parent.codec import ParentMQTTCodec


TEST_DATA_DIR = Path(__file__).parent / "data"


def get_stored_message_dicts() -> dict:
    d = {}
    return d


@dataclass
class MessageCase:
    src_message: Message
    exp_message: Optional[Message] = None
    exp_payload: Any = None


def child_to_parent_messages() -> list[MessageCase]:
    stored_message_dicts = {}
    for prefix in ["status", "snapshot"]:
        with (TEST_DATA_DIR / f"{prefix}_message.json").open() as f:
            stored_message_dicts[prefix] = json.loads(f.read())
        stored_message_dicts[prefix]["Header"]["Src"] = CHILD
    status_message_dict = stored_message_dicts["status"]
    gt_sh_status = GtShStatus_Maker.dict_to_tuple(status_message_dict["Payload"])
    gt_sh_status_event = GtShStatusEvent(Src=CHILD, status=gt_sh_status)
    exp_status_event = GtShStatusEvent(
        Src=CHILD,
        MessageId=gt_sh_status_event.MessageId,
        TimeNS=gt_sh_status_event.TimeNS,
        status=gt_sh_status.as_dict(),
    )
    snap_message_dict = stored_message_dicts["snapshot"]
    snapshot_spaceheat = SnapshotSpaceheat_Maker.dict_to_tuple(
        snap_message_dict["Payload"]
    )
    snapshot_event = SnapshotSpaceheatEvent(Src=CHILD, snap=snapshot_spaceheat)
    exp_snap_event = SnapshotSpaceheatEvent(
        Src=CHILD,
        MessageId=snapshot_event.MessageId,
        TimeNS=snapshot_event.TimeNS,
        snap=snapshot_spaceheat.as_dict(),
    )

    return [
        # Gs Pwr
        MessageCase(Message(Src=CHILD, MessageType="p", Payload=GsPwr_Maker(1).tuple)),
        # status
        MessageCase(Message(**status_message_dict), None, gt_sh_status),
        MessageCase(
            Message(Src=CHILD, Payload=status_message_dict["Payload"]),
            None,
            gt_sh_status,
        ),
        MessageCase(
            Message(Src=CHILD, Payload=gt_sh_status.as_dict()), None, gt_sh_status
        ),
        # snapshot
        MessageCase(Message(**snap_message_dict), None, snapshot_spaceheat),
        MessageCase(
            Message(Src=CHILD, Payload=snap_message_dict["Payload"]),
            None,
            snapshot_spaceheat,
        ),
        MessageCase(
            Message(Src=CHILD, Payload=snapshot_spaceheat.as_dict()),
            None,
            snapshot_spaceheat,
        ),
        # events
        MessageCase(
            Message(Src=CHILD, Payload=gt_sh_status_event), None, exp_status_event
        ),
        MessageCase(Message(Src=CHILD, Payload=snapshot_event), None, exp_snap_event),
        MessageCase(Message(Src=CHILD, Payload=StartupEvent())),
        MessageCase(Message(Src=CHILD, Payload=ShutdownEvent(Reason="foo"))),
        MessageCase(
            Message(
                Src=CHILD,
                Payload=ProblemEvent(ProblemType=Problems.error, Summary="foo"),
            )
        ),
        MessageCase(Message(Src=CHILD, Payload=MQTTConnectEvent(PeerName=PARENT))),
        MessageCase(
            Message(Src=CHILD, Payload=MQTTConnectFailedEvent(PeerName=PARENT))
        ),
        MessageCase(Message(Src=CHILD, Payload=MQTTDisconnectEvent(PeerName=PARENT))),
        MessageCase(
            Message(Src=CHILD, Payload=MQTTFullySubscribedEvent(PeerName=PARENT))
        ),
        MessageCase(Message(Src=CHILD, Payload=ResponseTimeoutEvent(PeerName=PARENT))),
        MessageCase(Message(Src=CHILD, Payload=PeerActiveEvent(PeerName=PARENT))),
        # misc messages
        MessageCase(PingMessage(Src=CHILD)),
        MessageCase(Message(Src=CHILD, Payload=Ack(AckMessageID="1"))),
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
        MessageCase(PingMessage(Src=PARENT)),
        MessageCase(Message(Src=PARENT, Payload=Ack(AckMessageID="1"))),
        MessageCase(
            Message(Src=PARENT, Payload=snapshot_request.as_dict()),
            None,
            snapshot_request,
        ),
        MessageCase(Message(Src=PARENT, Payload=set_relay.as_dict()), None, set_relay),
    ]


def assert_encode_decode(
    src_codec: MQTTCodec,
    dst_codec: MQTTCodec,
    messages: list[MessageCase],
):
    errors = []
    for i, case in enumerate(messages):
        decoded = dst_codec.decode(
            case.src_message.mqtt_topic(),
            src_codec.encode(case.src_message),
        )
        path_dbg = 0
        # old_len = len(errors)
        if case.exp_message is not None:
            path_dbg |= 0x00000001
            if decoded != case.exp_message:
                path_dbg |= 0x00000002
                errors.append(i)
                if len(errors) == 1:
                    path_dbg |= 0x00000004
                    print(f"FIRST ERROR, at index {i}")
                    print(f"exp: {case.exp_message}")
                    print(f"got: {decoded}")
        else:
            path_dbg |= 0x00000008
            if case.exp_payload is None:
                path_dbg |= 0x00000010
                exp_payload = case.src_message.Payload
            else:
                path_dbg |= 0x00000020
                exp_payload = case.exp_payload
            if decoded.Payload != exp_payload:
                path_dbg |= 0x00000040
                errors.append(i)
                if len(errors) == 1:
                    path_dbg |= 0x00000080
                    print(f"FIRST ERROR, at index {i}")
                    print(f"exp: {case.exp_payload}")
                    print(f"got: {decoded.Payload}")
        # print(f"{decoded.message_type():50s}: path:0x{path_dbg:08X}  {len(errors) == old_len}")
    if errors:
        raise ValueError(f"ERROR. Got codec matching errors at indices {errors}")


def test_decoder_simple():
    child_codec = ChildMQTTCodec()
    parent_codec = ParentMQTTCodec()

    assert_encode_decode(child_codec, parent_codec, child_to_parent_messages())

    assert_encode_decode(parent_codec, child_codec, parent_to_child_messages())
