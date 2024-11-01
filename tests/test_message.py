import enum
from typing import Literal

import pytest
from pydantic import BaseModel, ValidationError

from gwproto import Header, Message, as_enum
from gwproto.message import PAYLOAD_TYPE_FIELDS


class E(enum.Enum):
    a = 1
    b = 2


def test_as_enum() -> None:
    assert as_enum(1, E) == E.a
    assert as_enum(2, E) == E.b
    assert as_enum(3, E) is None
    assert as_enum(3, E, E.a) == E.a


class NaivePayload(BaseModel):
    x: int


def test_naive_payload() -> None:
    assert Message.type_name() == "gw"

    # Explicit src, message_type fields, pydantic-known-type payload
    x = 1
    src = "foo"
    message_type = "primitive"
    m = Message(
        Src=src,
        MessageType=message_type,
        Payload=1,
    )
    assert m.src() == src
    assert m.message_type() == message_type
    assert m.mqtt_topic() == f"gw/{src}/to//{message_type}"
    assert m.Payload == x
    assert m.Header.Src == src
    assert m.Header.Dst == ""
    assert m.Header.MessageType == message_type
    assert m.Header.MessageId == ""
    assert m.Header.AckRequired is False
    assert m.Header.TypeName == "gridworks.header"

    # Explicit src, message_type fields, naive payload
    m = Message(
        Src=src,
        MessageType=message_type,
        Payload=NaivePayload(x=1),
    )
    assert m.src() == src
    assert m.message_type() == message_type
    assert m.mqtt_topic() == f"gw/{src}/to//{message_type}"
    assert m.Payload.x == x
    assert m.Header.Src == src
    assert m.Header.Dst == ""
    assert m.Header.MessageType == message_type
    assert m.Header.MessageId == ""
    assert m.Header.AckRequired is False
    assert m.Header.TypeName == "gridworks.header"

    # Explicit Header, naive payload
    m2 = Message(
        Header=Header(
            Src=src,
            MessageType=message_type,
        ),
        Payload=NaivePayload(x=1),
    )
    assert m == m2
    assert m.model_dump() == m2.model_dump()

    # Explicit header from dict, naive payload
    m2 = Message(
        Header=Header(
            Src=src,
            MessageType=message_type,
        ).model_dump(),
        Payload=NaivePayload(x=1),
    )
    assert m == m2
    assert m.model_dump() == m2.model_dump()

    # All header fields in kwargs
    dst = "bar"
    message_id = "bla"
    ack_required = True
    m = Message(
        Src=src,
        MessageType=message_type,
        Payload=NaivePayload(x=1),
        Dst=dst,
        MessageId=message_id,
        AckRequired=ack_required,
    )
    assert m.src() == src
    assert m.message_type() == message_type
    assert m.mqtt_topic() == f"gw/{src}/to/{dst}/{message_type}"
    assert m.Payload.x == x
    assert m.Header.Src == src
    assert m.Header.Dst == dst
    assert m.Header.MessageType == message_type
    assert m.Header.MessageId == message_id
    assert m.Header.AckRequired == ack_required
    assert m.Header.TypeName == "gridworks.header"


class PayloadProvides(NaivePayload):
    Src: str
    TypeName: Literal["payload.provides"] = "payload.provides"


class PayloadProvidesMore(PayloadProvides):
    Dst: str = ""
    MessageId: str = ""
    AckRequired: bool = False
    TypeName: Literal["payload.provides.more"] = "payload.provides.more"


def test_from_payload() -> None:
    x = 1
    src = "foo"
    message_type = "payload.provides"

    # Payload object provides fields
    m = Message(Payload=PayloadProvides(Src=src, x=1))
    assert m.src() == src
    assert m.message_type() == message_type
    assert m.mqtt_topic() == f"gw/{src}/to//{message_type}".replace(".", "-")
    assert m.Payload.x == x
    assert m.Header.Src == src
    assert m.Header.Dst == ""
    assert m.Header.MessageType == message_type
    assert m.Header.MessageId == ""
    assert m.Header.AckRequired is False
    assert m.Header.TypeName == "gridworks.header"

    # Payload dict provides fields
    m2 = Message(Payload=PayloadProvides(Src=src, x=1).model_dump())
    assert m.model_dump() == m2.model_dump()
    m3 = Message[PayloadProvides](Payload=m2.Payload)
    assert m == m3

    # *All* header fields from payload object
    dst = "bar"
    message_id = "bla"
    ack_required = True
    message_type = "payload.provides.more"
    p = PayloadProvidesMore(
        Src=src,
        Dst=dst,
        MessageId=message_id,
        AckRequired=ack_required,
        x=x,
    )
    m = Message(Payload=p)
    assert m.src() == src
    assert m.message_type() == message_type
    assert m.mqtt_topic() == f"gw/{src}/to/{dst}/{message_type}".replace(".", "-")
    assert m.Payload.x == x
    assert m.Header.Src == src
    assert m.Header.Dst == dst
    assert m.Header.MessageType == message_type
    assert m.Header.MessageId == message_id
    assert m.Header.AckRequired == ack_required
    assert m.Header.TypeName == "gridworks.header"

    # *All* header fields from payload dict
    m2 = Message(Payload=p.model_dump())
    assert m.model_dump() == m2.model_dump()
    m3 = Message[PayloadProvidesMore](Payload=m2.Payload)
    assert m == m3

    # other message type fields
    for message_type_field_name in PAYLOAD_TYPE_FIELDS:
        payload_dict = p.model_dump()
        del payload_dict["TypeName"]
        payload_dict[message_type_field_name] = p.TypeName
        m3 = Message(Payload=payload_dict)
        assert m.Header == m3.Header


def test_errors() -> None:
    # no Payload
    with pytest.raises(ValidationError):
        Message()

    # No Src
    with pytest.raises(ValidationError):
        Message(MessageType="foo", Payload=NaivePayload(x=1))

    # No MessageType
    with pytest.raises(ValidationError):
        Message(Src="foo", Payload=NaivePayload(x=1))

    # Bad payload
    with pytest.raises(ValidationError):
        Message[list](Src="foo", MessageType="bar", Payload=1)
