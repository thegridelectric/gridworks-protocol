"""Type telemetry.snapshot.spaceheat, version 000"""
import json
from enum import auto
from typing import Any
from typing import Dict
from typing import List
from typing import Literal

from fastapi_utils.enums import StrEnum
from pydantic import BaseModel
from pydantic import Field
from pydantic import root_validator
from pydantic import validator

from gwproto.enums import TelemetryName
from gwproto.errors import SchemaError
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
    def type_to_local(cls, symbol: str) -> TelemetryName:
        if not SpaceheatTelemetryName000SchemaEnum.is_symbol(symbol):
            raise SchemaError(
                f"{symbol} must belong to SpaceheatTelemetryName000 symbols"
            )
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, TelemetryName, TelemetryName.default())

    @classmethod
    def local_to_type(cls, telemetry_name: TelemetryName) -> str:
        if not isinstance(telemetry_name, TelemetryName):
            raise SchemaError(f"{telemetry_name} must be of type {TelemetryName}")
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
    """Checks LeftRightDot Format

    LeftRightDot format: Lowercase alphanumeric words separated by periods,
    most significant word (on the left) starting with an alphabet character.

    Args:
        v (str): the candidate

    Raises:
        ValueError: if v is not LeftRightDot format
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


def check_is_reasonable_unix_time_ms(v: int) -> None:
    """Checks ReasonableUnixTimeMs format

    ReasonableUnixTimeMs format: unix milliseconds between Jan 1 2000 and Jan 1 3000

    Args:
        v (int): the candidate

    Raises:
        ValueError: if v is not ReasonableUnixTimeMs format
    """
    import pendulum

    if pendulum.parse("2000-01-01T00:00:00Z").int_timestamp * 1000 > v:  # type: ignore[union-attr]
        raise ValueError(f"{v} must be after Jan 1 2000")
    if pendulum.parse("3000-01-01T00:00:00Z").int_timestamp * 1000 < v:  # type: ignore[union-attr]
        raise ValueError(f"{v} must be before Jan 1 3000")


class TelemetrySnapshotSpaceheat(BaseModel):
    """Snapshot of Telemetry Data from a SpaceHeat SCADA.

    A snapshot of all current sensed states, sent from a spaceheat SCADA to its
    AtomicTNode. The nth element of each of the three lists refer to the same reading
    (i.e., what is getting read, what the value is, what the TelemetryNames are.)
    [More info](https://gridworks-protocol.readthedocs.io/en/latest/spaceheat-node.html).
    """

    ReportTimeUnixMs: int = Field(
        title="ReportTimeUnixMs",
        description="The time, in unix ms, that the SCADA creates this type. It may not be when the SCADA sends the type to the atn (for example if Internet is down).",
    )
    AboutNodeAliasList: List[str] = Field(
        title="AboutNodeAliases",
        description="The list of Spaceheat nodes in the snapshot. [More info](https://gridworks-protocol.readthedocs.io/en/latest/spaceheat-node.html).",
    )
    ValueList: List[int] = Field(
        title="ValueList",
    )
    TelemetryNameList: List[TelemetryName] = Field(
        title="TelemetryNameList",
        description=" [More info](https://gridworks-protocol.readthedocs.io/en/latest/telemetry-name.html).",
    )
    TypeName: Literal["telemetry.snapshot.spaceheat"] = "telemetry.snapshot.spaceheat"
    Version: str = "000"

    @validator("ReportTimeUnixMs")
    def _check_report_time_unix_ms(cls, v: int) -> int:
        try:
            check_is_reasonable_unix_time_ms(v)
        except ValueError as e:
            raise ValueError(
                f"ReportTimeUnixMs failed ReasonableUnixTimeMs format validation: {e}"
            )
        return v

    @validator("AboutNodeAliasList")
    def _check_about_node_alias_list(cls, v: List) -> List:
        for elt in v:
            try:
                check_is_left_right_dot(elt)
            except ValueError as e:
                raise ValueError(
                    f"AboutNodeAliasList element {elt} failed LeftRightDot format validation: {e}"
                )
        return v

    @validator("TelemetryNameList")
    def _check_telemetry_name_list(
        cls, v: SpaceheatTelemetryName000
    ) -> [SpaceheatTelemetryName000]:
        if not isinstance(v, List):
            raise ValueError("TelemetryNameList must be a list!")
        enum_list = []
        for elt in v:
            enum_list.append(as_enum(elt, TelemetryName, TelemetryName.Unknown))
        return enum_list

    @root_validator
    def check_axiom_1(cls, v: dict) -> dict:
        """
        Axiom 1: ListLengthConsistency.
        AboutNodeAliasList, ValueList and TelemetryNameList must all have the same length.
        """
        alias_list: List[str] = v.get("AboutNodeAliasList", None)
        value_list: List[int] = v.get("ValueList", None)
        tn_list: List[TelemetryName] = v.get("TelemetryNameList", None)
        if (len(value_list) != len(alias_list)) or (len(value_list) != len(tn_list)):
            raise ValueError(
                "Axiom 1: AboutNodeAliasList, ValueList and TelemetryNameList must all have the same length."
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        del d["TelemetryNameList"]
        telemetry_name_list = []
        for elt in self.TelemetryNameList:
            telemetry_name_list.append(TelemetryNameMap.local_to_type(elt))
        d["TelemetryNameList"] = telemetry_name_list
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class TelemetrySnapshotSpaceheat_Maker:
    type_name = "telemetry.snapshot.spaceheat"
    version = "000"

    def __init__(
        self,
        report_time_unix_ms: int,
        about_node_alias_list: List[str],
        value_list: List[int],
        telemetry_name_list: List[TelemetryName],
    ):
        self.tuple = TelemetrySnapshotSpaceheat(
            ReportTimeUnixMs=report_time_unix_ms,
            AboutNodeAliasList=about_node_alias_list,
            ValueList=value_list,
            TelemetryNameList=telemetry_name_list,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: TelemetrySnapshotSpaceheat) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> TelemetrySnapshotSpaceheat:
        """
        Given a serialized JSON type object, returns the Python class object
        """
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> TelemetrySnapshotSpaceheat:
        d2 = dict(d)
        if "ReportTimeUnixMs" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ReportTimeUnixMs")
        if "AboutNodeAliasList" not in d2.keys():
            raise SchemaError(f"dict {d2} missing AboutNodeAliasList")
        if "ValueList" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ValueList")
        if "TelemetryNameList" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TelemetryNameList")
        telemetry_name_list = []
        if not isinstance(d2["TelemetryNameList"], List):
            raise SchemaError("TelemetryNameList must be a List!")
        for elt in d2["TelemetryNameList"]:
            if elt in SpaceheatTelemetryName000SchemaEnum.symbols:
                v = TelemetryNameMap.type_to_local(elt)
            else:
                v = SpaceheatTelemetryName000.Unknown  #

            telemetry_name_list.append(v)
        d2["TelemetryNameList"] = telemetry_name_list
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return TelemetrySnapshotSpaceheat(
            ReportTimeUnixMs=d2["ReportTimeUnixMs"],
            AboutNodeAliasList=d2["AboutNodeAliasList"],
            ValueList=d2["ValueList"],
            TelemetryNameList=d2["TelemetryNameList"],
            TypeName=d2["TypeName"],
            Version="000",
        )
