import time
import uuid
from enum import Enum
from typing import Any, Generic, Literal, Optional, TypeVar

from pydantic import BaseModel, Field, field_validator

from gwproto.message import Message, as_enum
from gwproto.types import BatchedReadings, SnapshotSpaceheat


class EventBase(BaseModel):
    MessageId: str = Field(default_factory=lambda: str(uuid.uuid4()))
    TimeNS: int = Field(default_factory=time.time_ns)
    Src: str = ""
    TypeName: str
    Version: str


class AnyEvent(EventBase, extra="allow"):
    MessageId: str
    TimeNS: int
    Src: str
    TypeName: str
    Version: str


EventT = TypeVar("EventT", bound=EventBase)


class EventMessage(Message[EventT], Generic[EventT]):
    def __init__(self, **data: Any):
        if "AckRequired" not in data:
            data["AckRequired"] = True
        super().__init__(**data)


class StartupEvent(EventBase):
    TypeName: Literal["gridworks.event.startup"] = "gridworks.event.startup"
    Version: Literal["001"] = "001"


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
    def problem_type_value(cls, v: Any) -> Optional[Problems]:
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


class BatchedReadingsEvent(EventBase):
    Batch: BatchedReadings | dict
    TypeName: Literal["gridworks.event.batched.readings"] = (
        "gridworks.event.batched.readings"
    )
    Version: Literal["001"] = "000"


class SnapshotSpaceheatEvent(EventBase):
    Snap: SnapshotSpaceheat | dict
    TypeName: Literal["gridworks.event.snapshot.spaceheat"] = (
        "gridworks.event.snapshot.spaceheat"
    )
    Version: Literal["001"] = "001"
