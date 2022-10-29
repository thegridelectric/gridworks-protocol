"""Schema enum spaceheat.telemetry.name.110 definition.

Look in enums/spaceheat_telemetry_name_110 for:
    - the local python enum TelemetryName
    - the SchemaEnum SpaceheatTelemetryName110SchemaEnum

The SchemaEnum is a list of symbols sent in API/ABI messages. Its symbols
are not supposed to be human readable.

The LocalEnum are intended to be human readable."""

from abc import ABC
from enum import auto
from typing import Dict
from typing import List

from fastapi_utils.enums import StrEnum

from gwproto.errors import SchemaError


class TelemetryName(StrEnum):
    """
    CurrentRmsMicroAmps,
    WaterFlowGpmTimes100,
    WaterTempCTimes1000,
    PhaseAngleDegreesTimes10,
    WattHours,
    Unknown,
    VoltageRmsMilliVolts,
    PowerW,
    CurrentRmsMilliAmps,
    RelayState,
    GallonsPerMinuteTimes10,
    WaterTempFTimes1000,
    
    This is the enum intended for the local application. It is forwards and backwards
    compatible with TelemetryName enums used in types.
    """

    @classmethod
    def values(cls):
        return [elt.value for elt in cls]

    CurrentRmsMicroAmps = auto()
    WaterFlowGpmTimes100 = auto()
    WaterTempCTimes1000 = auto()
    PhaseAngleDegreesTimes10 = auto()
    WattHours = auto()
    Unknown = auto()
    VoltageRmsMilliVolts = auto()
    PowerW = auto()
    CurrentRmsMilliAmps = auto()
    RelayState = auto()
    GallonsPerMinuteTimes10 = auto()
    WaterTempFTimes1000 = auto()
    


class TelemetryNameMap:
    """ Handles the bijection
        "ad19e79c" -  CurrentRmsMicroAmps,
        "d70cce28" -  WaterFlowGpmTimes100,
        "c89d0ba1" -  WaterTempCTimes1000,
        "e0bb014b" -  PhaseAngleDegreesTimes10,
        "337b8659" -  WattHours,
        "00000000" -  Unknown,
        "bb6fdd59" -  VoltageRmsMilliVolts,
        "af39eec9" -  PowerW,
        "aeed9c8e" -  CurrentRmsMilliAmps,
        "5a71d4b3" -  RelayState,
        "329a68c0" -  GallonsPerMinuteTimes10,
        "793505aa" -  WaterTempFTimes1000,
    """
    type_name = "spaceheat.telemetry.name.110"

    symbols: List[str] = [
        "ad19e79c",
        "d70cce28",
        "c89d0ba1",
        "e0bb014b",
        "337b8659",
        "00000000",
        "bb6fdd59",
        "af39eec9",
        "aeed9c8e",
        "5a71d4b3",
        "329a68c0",
        "793505aa",
        #
    ]

    @classmethod
    def is_symbol(cls, candidate) -> bool:
        if candidate in cls.symbols:
            return True
        return False

    @classmethod
    def type_to_local(cls, symbol):
        if not cls.is_symbol(symbol):
            raise SchemaError(
                f"{symbol} must belong to key of {TelemetryNameMap.type_to_local_dict}"
            )
        return cls.type_to_local_dict[symbol]

    @classmethod
    def local_to_type(cls, telemetry_name):
        if not isinstance(telemetry_name, TelemetryName):
            raise SchemaError(f"{telemetry_name} must be of type {TelemetryName}")
        return cls.local_to_type_dict[telemetry_name]

    type_to_local_dict: Dict[str, TelemetryName] = {
        "ad19e79c": TelemetryName.CurrentRmsMicroAmps,
        "d70cce28": TelemetryName.WaterFlowGpmTimes100,
        "c89d0ba1": TelemetryName.WaterTempCTimes1000,
        "e0bb014b": TelemetryName.PhaseAngleDegreesTimes10,
        "337b8659": TelemetryName.WattHours,
        "00000000": TelemetryName.Unknown,
        "bb6fdd59": TelemetryName.VoltageRmsMilliVolts,
        "af39eec9": TelemetryName.PowerW,
        "aeed9c8e": TelemetryName.CurrentRmsMilliAmps,
        "5a71d4b3": TelemetryName.RelayState,
        "329a68c0": TelemetryName.GallonsPerMinuteTimes10,
        "793505aa": TelemetryName.WaterTempFTimes1000,
    }

    local_to_type_dict: Dict[TelemetryName, str] = {
        TelemetryName.CurrentRmsMicroAmps: "ad19e79c",
        TelemetryName.WaterFlowGpmTimes100: "d70cce28",
        TelemetryName.WaterTempCTimes1000: "c89d0ba1",
        TelemetryName.PhaseAngleDegreesTimes10: "e0bb014b",
        TelemetryName.WattHours: "337b8659",
        TelemetryName.Unknown: "00000000",
        TelemetryName.VoltageRmsMilliVolts: "bb6fdd59",
        TelemetryName.PowerW: "af39eec9",
        TelemetryName.CurrentRmsMilliAmps: "aeed9c8e",
        TelemetryName.RelayState: "5a71d4b3",
        TelemetryName.GallonsPerMinuteTimes10: "329a68c0",
        TelemetryName.WaterTempFTimes1000: "793505aa",
        #
    }
