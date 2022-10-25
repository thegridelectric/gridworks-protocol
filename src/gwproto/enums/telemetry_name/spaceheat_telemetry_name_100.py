"""spaceheat.telemetry.name.100 definition"""
import enum
from abc import ABC
from typing import List


class TelemetryName(enum.Enum):
    @classmethod
    def values(cls):
        return [elt.value for elt in cls]

    UNKNOWN = "Unknown"
    POWER_W = "PowerW"
    RELAY_STATE = "RelayState"
    WATER_TEMP_C_TIMES1000 = "WaterTempCTimes1000"
    WATER_TEMP_F_TIMES1000 = "WaterTempFTimes1000"
    WATER_FLOW_GPM_TIMES100 = "WaterFlowGpmTimes100"
    CURRENT_RMS_MICRO_AMPS = "CurrentRmsMicroAmps"
    GALLONS_PER_MINUTE_TIMES10 = "GallonsPerMinuteTimes10"
    #


class SpaceheatTelemetryName100GtEnum(ABC):
    symbols: List[str] = [
        "00000000",
        "af39eec9",
        "5a71d4b3",
        "c89d0ba1",
        "793505aa",
        "d70cce28",
        "ad19e79c",
        "329a68c0",
        #
    ]
