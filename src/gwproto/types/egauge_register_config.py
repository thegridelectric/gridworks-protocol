"""Type egauge.register.config, version 000"""

from typing import Literal

from pydantic import BaseModel

from gwproto.property_format import ReallyAnInt


class EgaugeRegisterConfig(BaseModel):
    """
    Used to translate eGauge's Modbus Map.

    This type captures the information provided by eGauge in its modbus csv map, when reading
    current, power, energy, voltage, frequency etc from an eGauge 4030.
    """

    Address: ReallyAnInt
    Name: str
    Description: str
    Type: str
    Denominator: ReallyAnInt
    Unit: str
    TypeName: Literal["egauge.register.config"] = "egauge.register.config"
    Version: Literal["000"] = "000"

    @classmethod
    def type_name_value(cls) -> str:
        return "egauge.register.config"
