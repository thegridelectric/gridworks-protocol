from gwproto.enums import FsmEventType
from gwproto.type_helpers import EVENT_ENUM_BY_NAME

assert set(FsmEventType.values()) - set(EVENT_ENUM_BY_NAME.keys()) == {
    "TimerFinished",
    "SetAnalog010V",
    "SetAnalog420mA",
}
