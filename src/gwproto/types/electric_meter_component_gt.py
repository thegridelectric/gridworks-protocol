"""Type electric.meter.component.gt, version 000"""

from typing import List, Literal, Optional, Self

from pydantic import PositiveInt, field_validator, model_validator

from gwproto.types import ComponentGt
from gwproto.types.electric_meter_channel_config import ElectricMeterChannelConfig


class ElectricMeterComponentGt(ComponentGt):
    ModbusHost: Optional[str] = None
    ModbusPort: Optional[PositiveInt] = None
    ConfigList: List[ElectricMeterChannelConfig]
    TypeName: Literal["electric.meter.component.gt"] = "electric.meter.component.gt"

    @field_validator("ConfigList")
    @classmethod
    def check_config_list(
        cls, v: List[ElectricMeterChannelConfig]
    ) -> List[ElectricMeterChannelConfig]:
        """
        Axiom 1: Channel Name uniqueness. Data Channel names are
        unique in the config list

        Axiom 2: Egauge Config consistency. If one of the ElectricMeterChannelConfigs
        has an EgaugeRegisterConfig, then they all do.
        """
        # Implement Axiom(s)
        return v

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 3: Modbus consistency.
        ModbusHost is None if and only if ModbusPort is None
        """
        # Implement check for axiom 1"
        return self

    @model_validator(mode="after")
    def check_axiom_2(self) -> Self:
        """
        Axiom 4: Egauge4030 Means Modbus.
        If any of the ElectricMeterChannelConfigs have EgaugeRegisterConfig, then the ModbusHost
        is not None
        """
        # Implement check for axiom 2"
        return self
