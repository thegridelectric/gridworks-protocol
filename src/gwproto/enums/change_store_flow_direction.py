from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class ChangeStoreFlowDirection(StrEnum):
    """
    Request/action in changing store.flow.direction state
    """
    Discharge = auto()
    Charge = auto()

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def default(cls) -> "ChangeStoreFlowDirection":
        return cls.Discharge

    @classmethod
    def enum_name(cls) -> str:
        return "change.store.flow.direction"
