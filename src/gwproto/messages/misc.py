# ruff: noqa: ANN401

import uuid
from typing import Any, Literal

from gw.named_types import GwBase
from pydantic import Field

from gwproto.message import Message


class Ack(GwBase):
    ack_message_id: str
    type_name: Literal["gridworks.ack"] = "gridworks.ack"


class Ping(GwBase):
    message_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type_name: Literal["gridworks.ping"] = "gridworks.ping"


class PingMessage(Message[Ping]):
    def __init__(self, *, ack_required: bool = True, **kwargs: Any) -> None:  # noqa: N803
        if "Payload" not in kwargs:
            kwargs["Payload"] = Ping()
        super().__init__(ack_required=ack_required, **kwargs)
