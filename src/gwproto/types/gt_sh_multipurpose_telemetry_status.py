"""Type gt.sh.multipurpose.telemetry.status, version 100"""
import json
from enum import auto
from typing import Any
from typing import Dict
from typing import List
from typing import Literal

from fastapi_utils.enums import StrEnum
from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gwproto.enums import TelemetryName as EnumTelemetryName
from gwproto.errors import MpSchemaError
from gwproto.message import as_enum


class SpaceheatTelemetryName000SchemaEnum:
    enum_name: str = "spaceheat.telemetry.name.000"
    symbols: List[str] = [
        "00000000",
        "af39eec9",
        "5a71d4b3",
        "c89d0ba1",
        "793505aa",
        "d70cce28",
        "ad19e79c",
        "329a68c0",
        "bb6fdd59",
        "e0bb014b",
        "337b8659",
        "0f627faa",
        "4c3f8c78",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class SpaceheatTelemetryName000(StrEnum):
    Unknown = auto()
    PowerW = auto()
    RelayState = auto()
    WaterTempCTimes1000 = auto()
    WaterTempFTimes1000 = auto()
    GpmTimes100 = auto()
    CurrentRmsMicroAmps = auto()
    GallonsTimes100 = auto()
    VoltageRmsMilliVolts = auto()
    MilliWattHours = auto()
    FrequencyMicroHz = auto()
    AirTempCTimes1000 = auto()
    AirTempFTimes1000 = auto()

    @classmethod
    def default(cls) -> "SpaceheatTelemetryName000":
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class TelemetryNameMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> EnumTelemetryName:
        if not SpaceheatTelemetryName000SchemaEnum.is_symbol(symbol):
            raise MpSchemaError(
                f"{symbol} must belong to SpaceheatTelemetryName000 symbols"
            )
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, EnumTelemetryName, EnumTelemetryName.default())

    @classmethod
    def local_to_type(cls, telemetry_name: EnumTelemetryName) -> str:
        if not isinstance(telemetry_name, EnumTelemetryName):
            raise MpSchemaError(f"{telemetry_name} must be of type {EnumTelemetryName}")
        versioned_enum = as_enum(
            telemetry_name,
            SpaceheatTelemetryName000,
            SpaceheatTelemetryName000.default(),
        )
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, SpaceheatTelemetryName000] = {
        "00000000": SpaceheatTelemetryName000.Unknown,
        "af39eec9": SpaceheatTelemetryName000.PowerW,
        "5a71d4b3": SpaceheatTelemetryName000.RelayState,
        "c89d0ba1": SpaceheatTelemetryName000.WaterTempCTimes1000,
        "793505aa": SpaceheatTelemetryName000.WaterTempFTimes1000,
        "d70cce28": SpaceheatTelemetryName000.GpmTimes100,
        "ad19e79c": SpaceheatTelemetryName000.CurrentRmsMicroAmps,
        "329a68c0": SpaceheatTelemetryName000.GallonsTimes100,
        "bb6fdd59": SpaceheatTelemetryName000.VoltageRmsMilliVolts,
        "e0bb014b": SpaceheatTelemetryName000.MilliWattHours,
        "337b8659": SpaceheatTelemetryName000.FrequencyMicroHz,
        "0f627faa": SpaceheatTelemetryName000.AirTempCTimes1000,
        "4c3f8c78": SpaceheatTelemetryName000.AirTempFTimes1000,
    }

    versioned_enum_to_type_dict: Dict[SpaceheatTelemetryName000, str] = {
        SpaceheatTelemetryName000.Unknown: "00000000",
        SpaceheatTelemetryName000.PowerW: "af39eec9",
        SpaceheatTelemetryName000.RelayState: "5a71d4b3",
        SpaceheatTelemetryName000.WaterTempCTimes1000: "c89d0ba1",
        SpaceheatTelemetryName000.WaterTempFTimes1000: "793505aa",
        SpaceheatTelemetryName000.GpmTimes100: "d70cce28",
        SpaceheatTelemetryName000.CurrentRmsMicroAmps: "ad19e79c",
        SpaceheatTelemetryName000.GallonsTimes100: "329a68c0",
        SpaceheatTelemetryName000.VoltageRmsMilliVolts: "bb6fdd59",
        SpaceheatTelemetryName000.MilliWattHours: "e0bb014b",
        SpaceheatTelemetryName000.FrequencyMicroHz: "337b8659",
        SpaceheatTelemetryName000.AirTempCTimes1000: "0f627faa",
        SpaceheatTelemetryName000.AirTempFTimes1000: "4c3f8c78",
    }


def check_is_left_right_dot(v: str) -> None:
    """
    LeftRightDot format: Lowercase alphanumeric words separated by periods,
    most significant word (on the left) starting with an alphabet character.

    Raises:
        ValueError: if not LeftRightDot format
    """
    from typing import List

    try:
        x: List[str] = v.split(".")
    except:
        raise ValueError(f"Failed to seperate {v} into words with split'.'")
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(f"Most significant word of {v} must start with alphabet char.")
    for word in x:
        if not word.isalnum():
            raise ValueError(f"words of {v} split by by '.' must be alphanumeric.")
    if not v.islower():
        raise ValueError(f"All characters of {v} must be lowercase.")


def check_is_reasonable_unix_time_ms(v: str) -> None:
    """
    ReasonableUnixTimeMs format: time in unix milliseconds between Jan 1 2000 and Jan 1 3000

    Raises:
        ValueError: if not ReasonableUnixTimeMs format
    """
    import pendulum

    if pendulum.parse("2000-01-01T00:00:00Z").int_timestamp * 1000 > v:  # type: ignore[attr-defined]
        raise ValueError(f"{v} must be after Jan 1 2000")
    if pendulum.parse("3000-01-01T00:00:00Z").int_timestamp * 1000 < v:  # type: ignore[attr-defined]
        raise ValueError(f"{v} must be before Jan 1 3000")


class GtShMultipurposeTelemetryStatus(BaseModel):
    """ """

    AboutNodeAlias: str = Field(
        title="AboutNodeAlias",
    )
    TelemetryName: EnumTelemetryName = Field(
        title="TelemetryName",
    )
    ValueList: List[int] = Field(
        title="ValueList",
    )
    ReadTimeUnixMsList: List[int] = Field(
        title="ReadTimeUnixMsList",
    )
    SensorNodeAlias: str = Field(
        title="SensorNodeAlias",
    )
    TypeName: Literal[
        "gt.sh.multipurpose.telemetry.status"
    ] = "gt.sh.multipurpose.telemetry.status"
    Version: str = "100"

    @validator("AboutNodeAlias")
    def _check_about_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(
                f"AboutNodeAlias failed LeftRightDot format validation: {e}"
            )
        return v

    @validator("TelemetryName")
    def _check_telemetry_name(cls, v: EnumTelemetryName) -> EnumTelemetryName:
        return as_enum(v, EnumTelemetryName, EnumTelemetryName.Unknown)

    @validator("ReadTimeUnixMsList")
    def _check_read_time_unix_ms_list(cls, v: List) -> List:
        for elt in v:
            try:
                check_is_reasonable_unix_time_ms(elt)
            except ValueError as e:
                raise ValueError(
                    f"ReadTimeUnixMsList element {elt} failed ReasonableUnixTimeMs format validation: {e}"
                )
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        del d["TelemetryName"]
        TelemetryName = as_enum(
            self.TelemetryName, EnumTelemetryName, EnumTelemetryName.default()
        )
        d["TelemetryNameGtEnumSymbol"] = TelemetryNameMap.local_to_type(TelemetryName)
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class GtShMultipurposeTelemetryStatus_Maker:
    type_name = "gt.sh.multipurpose.telemetry.status"
    version = "100"

    def __init__(
        self,
        about_node_alias: str,
        telemetry_name: EnumTelemetryName,
        value_list: List[int],
        read_time_unix_ms_list: List[int],
        sensor_node_alias: str,
    ):
        self.tuple = GtShMultipurposeTelemetryStatus(
            AboutNodeAlias=about_node_alias,
            TelemetryName=telemetry_name,
            ValueList=value_list,
            ReadTimeUnixMsList=read_time_unix_ms_list,
            SensorNodeAlias=sensor_node_alias,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: GtShMultipurposeTelemetryStatus) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtShMultipurposeTelemetryStatus:
        """
        Given a serialized JSON type object, returns the Python class object
        """
        try:
            d = json.loads(t)
        except TypeError:
            raise MpSchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise MpSchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> GtShMultipurposeTelemetryStatus:
        d2 = dict(d)
        if "AboutNodeAlias" not in d2.keys():
            raise MpSchemaError(f"dict {d2} missing AboutNodeAlias")
        if "TelemetryNameGtEnumSymbol" not in d2.keys():
            raise MpSchemaError(f"dict {d2} missing TelemetryNameGtEnumSymbol")
        if (
            d2["TelemetryNameGtEnumSymbol"]
            in SpaceheatTelemetryName000SchemaEnum.symbols
        ):
            d2["TelemetryName"] = TelemetryNameMap.type_to_local(
                d2["TelemetryNameGtEnumSymbol"]
            )
        else:
            d2["TelemetryName"] = EnumTelemetryName.default()
        if "ValueList" not in d2.keys():
            raise MpSchemaError(f"dict {d2} missing ValueList")
        if "ReadTimeUnixMsList" not in d2.keys():
            raise MpSchemaError(f"dict {d2} missing ReadTimeUnixMsList")
        if "SensorNodeAlias" not in d2.keys():
            raise MpSchemaError(f"dict {d2} missing SensorNodeAlias")
        if "TypeName" not in d2.keys():
            raise MpSchemaError(f"dict {d2} missing TypeName")

        return GtShMultipurposeTelemetryStatus(
            AboutNodeAlias=d2["AboutNodeAlias"],
            TelemetryName=d2["TelemetryName"],
            ValueList=d2["ValueList"],
            ReadTimeUnixMsList=d2["ReadTimeUnixMsList"],
            SensorNodeAlias=d2["SensorNodeAlias"],
            TypeName=d2["TypeName"],
            Version="100",
        )
