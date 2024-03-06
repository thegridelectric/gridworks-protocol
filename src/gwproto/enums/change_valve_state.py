from fastapi_utils.enums import StrEnum
from enum import auto


class ChangeValveState(StrEnum):
    """
    
    """
    OpenValve = auto()
    CloseValve = auto()

    @classmethod
    def default(cls) -> "ChangeValveState":
        return cls.OpenValve

    @classmethod
    def enum_name(cls) -> str:
        return "change.valve.state"
