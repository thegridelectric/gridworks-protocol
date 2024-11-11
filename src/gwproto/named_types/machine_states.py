"""Type machine.states, version 000"""

from typing import List, Literal

from pydantic import BaseModel, model_validator
from typing_extensions import Self

from gwproto.property_format import (
    HandleName,
    LeftRightDotStr,
    UTCMilliseconds,
)


class MachineStates(BaseModel):
    """ """

    MachineHandle: HandleName
    StateEnum: LeftRightDotStr
    StateList: List[str]
    UnixMsList: List[UTCMilliseconds]
    TypeName: Literal["machine.states"] = "machine.states"
    Version: Literal["000"] = "000"

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: List Length Consistency.
        StateList and UnixMsList must have the same length
        """
        # Implement check for axiom 1"
        return self

    @model_validator(mode="after")
    def check_axiom_2(self) -> Self:
        """
        Axiom 2: If StateEnum is a recognized GridWorks enum, then the StateList elements are all values of that enum..

        """
        # Implement check for axiom 2"
        return self
