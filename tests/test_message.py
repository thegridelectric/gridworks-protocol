import enum
from typing import Any, Literal

import pytest
from gw.named_types import GwBase
from pydantic import ValidationError

from gwproto import Header, Message, as_enum


class E(enum.Enum):
    a = 1
    b = 2


def test_as_enum() -> None:
    assert as_enum(1, E) == E.a
    assert as_enum(2, E) == E.b
    assert as_enum(3, E) is None
    assert as_enum(3, E, E.a) == E.a


class SomePayload(GwBase):
    x: int
    type_name: Literal["some.payload"] = "some.payload"


def test_naive_payload() -> None:
    assert Message.type_name_value() == "gw"

    # Explicit src, message_type fields, pydantic-known-type payload
    x = 1
    src = "foo"
    message_type = "some.payload"
    m: Message[Any] = Message(
        src=src,
        message_type=SomePayload.type_name_value,
        payload=SomePayload(x=1),
    )
    assert m.src() == src
    assert m.message_type() == message_type
    assert m.mqtt_topic() == f"gw/{src}/to//some-payload"
    assert m.payload.x == 1
    assert m.header.src == src
    assert m.header.dst == ""
    assert m.header.message_type == message_type
    assert m.header.message_id == ""
    assert m.header.ack_required is False
    assert m.header.type_name == "gridworks.header"

    # Explicit Header, naive payload
    m2: Message[Any] = Message(
        header=Header(
            src=src,
            message_type=message_type,
        ),
        payload=SomePayload(x=1),
    )
    assert m == m2
    assert m.to_dict() == m2.to_dict()

    # All header fields in kwargs
    dst = "bar"
    message_id = "bla"
    ack_required = True
    m = Message(
        src=src,
        message_type=message_type,
        payload=SomePayload(x=1),
        dst=dst,
        message_id=message_id,
        ack_required=ack_required,
    )
    assert m.src() == src
    assert m.message_type() == message_type
    assert m.mqtt_topic() == f"gw/{src}/to/{dst}/some-payload"
    assert m.payload.x == x
    assert m.header.src == src
    assert m.header.dst == dst
    assert m.header.message_type == message_type
    assert m.header.message_id == message_id
    assert m.header.ack_required == ack_required
    assert m.header.type_name == "gridworks.header"


class PayloadProvides(SomePayload):
    src: str
    type_name: Literal["payload.provides"] = "payload.provides"


class PayloadProvidesMore(PayloadProvides):
    dst: str = ""
    message_id: str = ""
    ack_required: bool = False
    type_name: Literal["payload.provides.more"] = "payload.provides.more"  # type: ignore[assignment]


def test_from_payload() -> None:
    message_type = "payload.provides"
    src = "foo"

    # Payload object provides fields
    m: Message[Any] = Message(payload=PayloadProvides(src="foo", x=1))
    assert m.src() == src
    assert m.message_type() == message_type
    assert m.mqtt_topic() == f"gw/{src}/to//{message_type}".replace(".", "-")
    assert m.payload.x == 1
    assert m.header.src == src
    assert m.header.dst == ""
    assert m.header.message_type == message_type
    assert m.header.message_id == ""
    assert m.header.ack_required is False
    assert m.header.type_name == "gridworks.header"

    # *All* header fields from payload object
    dst = "bar"
    message_id = "bla"
    ack_required = True
    message_type = "payload.provides.more"
    p = PayloadProvidesMore(
        src=src,
        dst=dst,
        message_id=message_id,
        ack_required=ack_required,
        x=1,
    )
    m = Message(payload=p)
    assert m.src() == src
    assert m.message_type() == message_type
    assert m.mqtt_topic() == f"gw/{src}/to/{dst}/{message_type}".replace(".", "-")
    assert m.payload.x == 1
    assert m.header.src == src
    assert m.header.dst == dst
    assert m.header.message_type == message_type
    assert m.header.message_id == message_id
    assert m.header.ack_required == ack_required
    assert m.header.type_name == "gridworks.header"


def test_errors() -> None:
    # no Payload
    with pytest.raises(TypeError):
        Message()

    # No Src
    with pytest.raises(ValidationError):
        Message(payload=SomePayload(x=1))

    # Conflicting message type: goes with payload
    m = Message(message_type="foo", src="bar", payload=SomePayload(x=1))
    assert m.header.message_type == "some.payload"

    # Non GwBase payload
    with pytest.raises(AttributeError):
        Message[Any](src="foo", payload=1)
