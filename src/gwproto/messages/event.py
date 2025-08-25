import time
import uuid
from enum import Enum
from typing import Any, Generic, Literal, Optional, TypeVar

from gw.named_types import GwBase
from pydantic import ConfigDict, Field, field_validator

from gwproto.message import Message, as_enum
from gwproto.named_types import Report
from gwproto.property_format import UTCMilliseconds


class EventBase(GwBase):
    message_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    time_created_ms: UTCMilliseconds = Field(
        default_factory=lambda: int(time.time() * 1000)
    )
    src: str = ""


class AnyEvent(EventBase):
    # catch-all bucket: accept unknown fields from arbitrary events
    model_config = ConfigDict(extra="allow")


EventT = TypeVar("EventT", bound=EventBase)


class EventMessage(Message[EventT], Generic[EventT]):
    def __init__(self, AckRequired: bool = True, **kwargs: Any) -> None:  # noqa: ANN401, FBT001, FBT002, N803
        super().__init__(AckRequired=AckRequired, **kwargs)


class StartupEvent(EventBase):
    type_name: Literal["gridworks.event.startup"] = "gridworks.event.startup"


class ShutdownEvent(EventBase):
    reason: str
    type_name: Literal["gridworks.event.shutdown"] = "gridworks.event.shutdown"
    version: str = "001"


class Problems(Enum):
    error = "error"
    warning = "warning"


class ProblemEvent(EventBase):
    problem_type: Problems
    summary: str
    details: str = ""
    type_name: Literal["gridworks.event.problem"] = "gridworks.event.problem"
    version: str = "001"

    @field_validator("problem_type", mode="before")
    @classmethod
    def problem_type_value(cls, v: Any) -> Optional[Problems]:  # noqa: ANN401
        return as_enum(v, Problems, Problems.error)


class CommEvent(EventBase):
    peer_name: str
    type_name: Literal["comm.event"] = "comm.event"


class MQTTCommEvent(CommEvent):
    type_name: Literal["mqtt.comm.event"] = "mqtt.comm.event"


class MQTTConnectEvent(MQTTCommEvent):
    type_name: Literal["gridworks.event.comm.mqtt.connect"] = (
        "gridworks.event.comm.mqtt.connect"
    )
    version: str = "001"


class MQTTConnectFailedEvent(MQTTCommEvent):
    type_name: Literal["gridworks.event.comm.mqtt.connect.failed"] = (
        "gridworks.event.comm.mqtt.connect.failed"
    )
    version: str = "001"


class MQTTDisconnectEvent(MQTTCommEvent):
    type_name: Literal["gridworks.event.comm.mqtt.disconnect"] = (
        "gridworks.event.comm.mqtt.disconnect"
    )
    version: str = "001"


class MQTTFullySubscribedEvent(CommEvent):
    type_name: Literal["gridworks.event.comm.mqtt.fully.subscribed"] = (
        "gridworks.event.comm.mqtt.fully.subscribed"
    )
    version: str = "001"


class ResponseTimeoutEvent(CommEvent):
    type_name: Literal["gridworks.event.comm.response.timeout"] = (
        "gridworks.event.comm.response.timeout"
    )
    version: str = "001"


class PeerActiveEvent(CommEvent):
    type_name: Literal["gridworks.event.comm.peer.active"] = (
        "gridworks.event.comm.peer.active"
    )
    version: str = "001"


class ReportEvent(EventBase):
    report: Report
    type_name: Literal["report.event"] = "report.event"
    version: Literal["002"] = "002"
