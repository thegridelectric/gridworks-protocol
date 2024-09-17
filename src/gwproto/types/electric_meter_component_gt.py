"""Type electric.meter.component.gt, version 001"""

from typing import List, Literal, Optional

from pydantic import PositiveInt, model_validator
from typing_extensions import Self

from gwproto.types.component_gt import ComponentGt
from gwproto.types.egauge_io import EgaugeIo


class ElectricMeterComponentGt(ComponentGt):
    ModbusHost: Optional[str] = None
    ModbusPort: Optional[PositiveInt] = None
    EgaugeIoList: List[EgaugeIo]
    TypeName: Literal["electric.meter.component.gt"] = "electric.meter.component.gt"
    Version: Literal["001"] = "001"

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: Modbus consistency.
        ModbusHost is None if and only if ModbusPort is None
        """
        # Implement check for axiom 1"
        return self

    @model_validator(mode="after")
    def check_axiom_2(self) -> Self:
        """
        Axiom 2: Egauge4030 Means Modbus.
        If the EgaugeIoList has non-zero length, then the ModbusHost is not None
        """
        # Implement check for axiom 2"
        return self

    @model_validator(mode="after")
    def check_axiom_3(self) -> Self:
        """
        Axiom 3: Channel Name Consistency.
        If the EgaugeIoList has non-zero length:
          1) Len(EgaugeIoList) == Len(ConfigList)
          2) There are no duplicates of ChannelName in the ConfigList or EgaugeIoList
          3) The set of ChannelNames in IoConfig is equal to the set of ChannelNames in ConfigList
        """
        # Implement check for axiom 3"
        return self

    @classmethod
    def type_name_value(cls) -> str:
        return "electric.meter.component.gt"
