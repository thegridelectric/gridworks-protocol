import time
import uuid
from enum import Enum
from typing import Any, Generic, Literal, Optional, TypeVar

from pydantic import BaseModel, Field, field_validator

from gwproto.message import Message, as_enum
from gwproto.property_format import UTCMilliseconds
from gwproto.types import MyChannels, Report


class EventBase(BaseModel):
    MessageId: str = Field(default_factory=lambda: str(uuid.uuid4()))
    TimeCreatedMs: UTCMilliseconds = Field(
        default_factory=lambda: int(time.time() * 1000)
    )
    Src: str = ""
    TypeName: str


class AnyEvent(EventBase, extra="allow"):
    MessageId: str
    TimeCreatedMs: int = Field(default_factory=lambda: int(time.time() * 1000))
    Src: str
    TypeName: str


EventT = TypeVar("EventT", bound=EventBase)


class EventMessage(Message[EventT], Generic[EventT]):
    def __init__(self, AckRequired: bool = True, **kwargs: Any) -> None:  # noqa: ANN401, FBT001, FBT002, N803
        super().__init__(AckRequired=AckRequired, **kwargs)


class StartupEvent(EventBase):
    TypeName: Literal["gridworks.event.startup"] = "gridworks.event.startup"


class ShutdownEvent(EventBase):
    Reason: str
    TypeName: Literal["gridworks.event.shutdown"] = "gridworks.event.shutdown"
    Version: Literal["001"] = "001"


class Problems(Enum):
    error = "error"
    warning = "warning"


class ProblemEvent(EventBase):
    ProblemType: Problems
    Summary: str
    Details: str = ""
    TypeName: Literal["gridworks.event.problem"] = "gridworks.event.problem"
    Version: Literal["001"] = "001"

    @field_validator("ProblemType", mode="before")
    @classmethod
    def problem_type_value(cls, v: Any) -> Optional[Problems]:  # noqa: ANN401
        return as_enum(v, Problems, Problems.error)


class CommEvent(EventBase):
    PeerName: str


class MQTTCommEvent(CommEvent): ...


class MQTTConnectEvent(MQTTCommEvent):
    TypeName: Literal["gridworks.event.comm.mqtt.connect"] = (
        "gridworks.event.comm.mqtt.connect"
    )
    Version: Literal["001"] = "001"


class MQTTConnectFailedEvent(MQTTCommEvent):
    TypeName: Literal["gridworks.event.comm.mqtt.connect.failed"] = (
        "gridworks.event.comm.mqtt.connect.failed"
    )
    Version: Literal["001"] = "001"


class MQTTDisconnectEvent(MQTTCommEvent):
    TypeName: Literal["gridworks.event.comm.mqtt.disconnect"] = (
        "gridworks.event.comm.mqtt.disconnect"
    )
    Version: Literal["001"] = "001"


class MQTTFullySubscribedEvent(CommEvent):
    TypeName: Literal["gridworks.event.comm.mqtt.fully.subscribed"] = (
        "gridworks.event.comm.mqtt.fully.subscribed"
    )
    Version: Literal["001"] = "001"


class ResponseTimeoutEvent(CommEvent):
    TypeName: Literal["gridworks.event.comm.response.timeout"] = (
        "gridworks.event.comm.response.timeout"
    )
    Version: Literal["001"] = "001"


class PeerActiveEvent(CommEvent):
    TypeName: Literal["gridworks.event.comm.peer.active"] = (
        "gridworks.event.comm.peer.active"
    )
    Version: Literal["001"] = "001"


class ReportEvent(EventBase):
    Report: Report
    TypeName: Literal["report.event"] = "report.event"
    Version: Literal["000"] = "000"

    def __init__(self, **data: dict[str, Any]) -> None:
        super().__init__(**data)
        self.MessageId = self.Report.Id
        self.TimeCreatedMs = self.Report.MessageCreatedMs


class MyChannelsEvent(EventBase):
    MyChannels: MyChannels
    TypeName: Literal["my.channels.event"] = "my.channels.event"
    Version: Literal["000"] = "000"

    def __init__(self, **data: dict[str, Any]) -> None:
        super().__init__(**data)
        self.MessageId = self.MyChannels.MessageId
        self.TimeCreatedMs = self.MyChannels.MessageCreatedMs
