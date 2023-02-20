from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class TelemetryName(StrEnum):
    """
    Specifies the name of sensed data reported by SCADA

    Choices and descriptions:
    
      * Unknown: 
      * PowerW: 
      * RelayState: 
      * WaterTempCTimes1000: 
      * WaterTempFTimes1000: 
      * GpmTimes100: 
      * CurrentRmsMicroAmps: 
      * GallonsTimes100: 
      * VoltageRmsMilliVolts: 
      * MilliWattHours: 
      * FrequencyMicroHz: 
      * AirTempCTimes1000: 
      * AirTempFTimes1000: 
    """
    Unknown = auto()
    PowerW = auto()
    MilliWattHours = auto()
    FrequencyMicroHz = auto()
    AirTempCTimes1000 = auto()
    AirTempFTimes1000 = auto()
    RelayState = auto()
    WaterTempCTimes1000 = auto()
    WaterTempFTimes1000 = auto()
    GpmTimes100 = auto()
    CurrentRmsMicroAmps = auto()
    GallonsTimes100 = auto()
    VoltageRmsMilliVolts = auto()
    
    @classmethod
    def default(cls) -> "TelemetryName":
        """
        Returns default value Unknown
        """
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
