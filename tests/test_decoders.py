import json
import time
import uuid
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import Any
from typing import Optional
from typing import Type

from pydantic import ValidationError

from gwproto.messages import AnyEvent


try:
    from rich import print
except ImportError:
    pass

from gwproto import Message
from gwproto import MQTTCodec
from gwproto.messages import Ack
from gwproto.messages import BatchedReadings_Maker
from gwproto.messages import BatchedReadingsEvent
from gwproto.messages import GtShCliAtnCmd_Maker
from gwproto.messages import MQTTConnectEvent
from gwproto.messages import MQTTConnectFailedEvent
from gwproto.messages import MQTTDisconnectEvent
from gwproto.messages import MQTTFullySubscribedEvent
from gwproto.messages import PeerActiveEvent
from gwproto.messages import PingMessage
from gwproto.messages import PowerWatts_Maker
from gwproto.messages import ProblemEvent
from gwproto.messages import Problems
from gwproto.messages import ResponseTimeoutEvent
from gwproto.messages import ShutdownEvent
from gwproto.messages import Snapshot_Maker
from gwproto.messages import SnapshotSpaceheatEvent
from gwproto.messages import StartupEvent
from tests.dummy_decoders import CHILD
from tests.dummy_decoders import PARENT
from tests.dummy_decoders.child.codec import ChildMQTTCodec
from tests.dummy_decoders.parent.codec import ParentMQTTCodec


TEST_DATA_DIR = Path(__file__).parent / "data"


def get_stored_message_dicts() -> dict:
    d = {}
    return d


def child_to_parent_payload_dicts() -> dict:
    d = {}
    for prefix in ["batched_readings", "snapshot"]:
        with (TEST_DATA_DIR / f"{prefix}_message.json").open() as f:
            d[prefix] = json.loads(f.read())
            d[prefix]["Header"]["Src"] = CHILD
    return d


@dataclass
class MessageCase:
    src_message: Message
    exp_message: Optional[Message] = None
    exp_payload: Any = None
    exp_exceptions: list[Type[Exception]] = field(default_factory=list)


def child_to_parent_messages() -> list[MessageCase]:
    stored_message_dicts = child_to_parent_payload_dicts()
    batched_readings_dict = stored_message_dicts["batched_readings"]
    batched_readings = BatchedReadings_Maker.dict_to_tuple(
        batched_readings_dict["Payload"]
    )
    batched_readings_event = BatchedReadingsEvent(
        Src=CHILD, batched_readings=batched_readings
    )
    unrecognized_status_event = AnyEvent(**batched_readings_event.dict())
    unrecognized_status_event.TypeName += ".foo"
    unrecognized_event = AnyEvent(
        TypeName="gridworks.event.bar", MessageId="1", TimeNS=1, Src="1"
    )
    unrecognizeable_not_event_type = AnyEvent(
        **dict(
            batched_readings_event.dict(),
            TypeName="bla",
        )
    )
    unrecognizeable_bad_event_content = dict(TypeName="gridworks.event.baz")
    snap_message_dict = stored_message_dicts["snapshot"]
    snapshot = Snapshot_Maker.dict_to_tuple(snap_message_dict["Payload"])
    snapshot_event = SnapshotSpaceheatEvent(Src=CHILD, snap=snapshot)

    return [
        # Gs Pwr
        MessageCase(
            Message(
                Src=CHILD, MessageType="power.watts", Payload=PowerWatts_Maker(1).tuple
            )
        ),
        # status
        # QUESTION: why does this fail when replacing "gt.sh.status.110" with "gt.sh.status"?
        MessageCase(
            Message(
                Src=CHILD, MessageType="batched.readings", Payload=batched_readings
            ),
            None,
            batched_readings,
        ),
        MessageCase(
            Message(Src=CHILD, Payload=batched_readings_dict["Payload"]),
            None,
            batched_readings,
        ),
        MessageCase(
            Message(Src=CHILD, Payload=batched_readings.as_dict()),
            None,
            batched_readings,
        ),
        # snapshot
        MessageCase(Message(**snap_message_dict), None, snapshot),
        MessageCase(
            Message(Src=CHILD, Payload=snap_message_dict["Payload"]),
            None,
            snapshot,
        ),
        MessageCase(
            Message(Src=CHILD, Payload=snapshot.as_dict()),
            None,
            snapshot,
        ),
        # events
        MessageCase(Message(Src=CHILD, Payload=batched_readings_event)),
        MessageCase(Message(Src=CHILD, Payload=unrecognized_status_event)),
        MessageCase(Message(Src=CHILD, Payload=unrecognized_event)),
        MessageCase(
            Message(
                Src=CHILD,
                Payload=unrecognizeable_not_event_type,
            ),
            exp_exceptions=[ValidationError],
        ),
        MessageCase(
            Message(
                Src=CHILD,
                Payload=unrecognizeable_bad_event_content,
            ),
            exp_exceptions=[ValidationError],
        ),
        MessageCase(Message(Src=CHILD, Payload=snapshot_event)),
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
    # TODO: add finite state machine event messages
    return [
        # misc messages
        MessageCase(PingMessage(Src=PARENT)),
        MessageCase(Message(Src=PARENT, Payload=Ack(AckMessageID="1"))),
        MessageCase(
            Message(Src=PARENT, Payload=snapshot_request.as_dict()),
            None,
            snapshot_request,
        ),
    ]


def assert_encode_decode(
    src_codec: MQTTCodec,
    dst_codec: MQTTCodec,
    messages: list[MessageCase],
):
    errors = []
    for i, case in enumerate(messages):
        path_dbg = 0
        # old_len = len(errors)
        try:
            decoded = dst_codec.decode(
                case.src_message.mqtt_topic(),
                src_codec.encode(case.src_message),
            )
        except Exception as e:
            path_dbg |= 0x00000001
            if type(e) in case.exp_exceptions:
                path_dbg |= 0x00000002
                continue
            else:
                path_dbg |= 0x00000004
                errors.append(i)
                if len(errors) == 1:
                    path_dbg |= 0x00000008
                    print(f"FIRST ERROR, at index {i}")
                    print(f"exp expected exception in {case.exp_exceptions}")
                    print(f"got: <{type(e)}> <{e}>")

        else:
            path_dbg |= 0x00000010
            if case.exp_exceptions:
                path_dbg |= 0x00000020
                errors.append(i)
                if len(errors) == 1:
                    path_dbg |= 0x00000040
                    print(f"FIRST ERROR, at index {i}")
                    print(f"exp expected exception in {case.exp_exceptions}")
                    print(f"got: {decoded}")
            else:
                path_dbg |= 0x00000080
                decoded = dst_codec.decode(
                    case.src_message.mqtt_topic(),
                    src_codec.encode(case.src_message),
                )
                if case.exp_message is not None:
                    path_dbg |= 0x00000100
                    if decoded != case.exp_message:
                        path_dbg |= 0x00000040
                        errors.append(i)
                        if len(errors) == 1:
                            path_dbg |= 0x00000200
                            print(f"FIRST ERROR, at index {i}")
                            print(f"exp: {case.exp_message}")
                            print(f"got: {decoded}")
                else:
                    path_dbg |= 0x00000400
                    if case.exp_payload is None:
                        path_dbg |= 0x00000800
                        exp_payload = case.src_message.Payload
                    else:
                        path_dbg |= 0x00001000
                        exp_payload = case.exp_payload
                    if decoded.Payload != exp_payload:
                        path_dbg |= 0x00000400
                        errors.append(i)
                        if len(errors) == 1:
                            path_dbg |= 0x00002000
                            print(f"FIRST ERROR, at index {i}")
                            print(f"exp: {case.exp_payload}")
                            print(f"got: {decoded.Payload}")
        # print(f"{decoded.message_type():50s}: path:0x{path_dbg:08X}  {len(errors) == old_len}")
    if errors:
        raise ValueError(f"ERROR. Got codec matching errors at indices {errors}")


def test_decoder_simple():
    child_codec = ChildMQTTCodec()
    parent_codec = ParentMQTTCodec()

    # TODO: figure out how to get encoding to correctly add GtEnumSymbol
    # assert_encode_decode(child_codec, parent_codec, child_to_parent_messages())

    assert_encode_decode(parent_codec, child_codec, parent_to_child_messages())
