"""Type spaceheat.node.gt, version 200"""

from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, model_validator
from typing_extensions import Self

from gwproto.enums import ActorClass
from gwproto.property_format import (
    HandleName,
    ReallyAnInt,
    SpaceheatName,
    UUID4Str,
)


class SpaceheatNodeGt(BaseModel):
    """
    Spaceheat Node.

    A SpaceheatNode, or ShNode, is an organizing principal for the SCADA software. ShNodes can
    represent both underlying physical objects (water tank), measurements of these objects (temperature
    sensing at the top of a water tank), and actors within the code (an actor measuring multiple
    temperatures, or an actor responsible for filtering/smoothing temperature data for the purposes
    of thermostatic control). BIG CHANGES: Alias -> Name. The Property Format changes from LeftRightDot
    to SpaceheatNode. Remove Role. (Require numerous changes, in both code and hardware layout.)
    MEDIUM CHANGE: Remove ReportingSamplePeriodS. (Requires change for SimpleSensor). Smaller
    changes include removing NameplatePowerW, RatedVoltageV.

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/spaceheat-node.html)
    """

    Name: SpaceheatName
    ActorHierarchyName: Optional[HandleName] = None
    Handle: Optional[HandleName] = None
    ActorClass: ActorClass
    DisplayName: Optional[str] = None
    ComponentId: Optional[str] = None
    NameplatePowerW: Optional[ReallyAnInt] = None
    InPowerMetering: Optional[bool] = None
    ShNodeId: UUID4Str
    TypeName: Literal["spaceheat.node.gt"] = "spaceheat.node.gt"
    Version: Literal["200"] = "200"

    model_config = ConfigDict(extra="allow")

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: InPowerMetering requirements.
        If InPowerMetering exists and is true, then NameplatePowerW must exist
        """
        # Implement check for axiom 1"
        return self

    @classmethod
    def type_name_value(cls) -> str:
        return "spaceheat.node.gt"
