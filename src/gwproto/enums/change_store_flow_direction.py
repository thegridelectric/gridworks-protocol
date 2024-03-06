from fastapi_utils.enums import StrEnum
from enum import auto


class ChangeStoreFlowDirection(StrEnum):
    """
    Request/action in changing store.flow.direction state
    """
    Discharge = auto()
    Charge = auto()

    @classmethod
    def default(cls) -> "ChangeStoreFlowDirection":
        return cls.Discharge

    @classmethod
    def enum_name(cls) -> str:
        return "change.store.flow.direction"
