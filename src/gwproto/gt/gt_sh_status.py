"""gt.sh.status type"""
import json
from typing import List
from typing import Literal

from pydantic import BaseModel
from pydantic import validator

import gwproto.property_format as property_format
from gwproto.errors import SchemaError
from gwproto.gt.gt_sh_booleanactuator_cmd_status import GtShBooleanactuatorCmdStatus
from gwproto.gt.gt_sh_booleanactuator_cmd_status import (
    GtShBooleanactuatorCmdStatus_Maker,
)
from gwproto.gt.gt_sh_multipurpose_telemetry_status import (
    GtShMultipurposeTelemetryStatus,
)
from gwproto.gt.gt_sh_multipurpose_telemetry_status import (
    GtShMultipurposeTelemetryStatus_Maker,
)
from gwproto.gt.gt_sh_simple_telemetry_status import GtShSimpleTelemetryStatus
from gwproto.gt.gt_sh_simple_telemetry_status import GtShSimpleTelemetryStatus_Maker
from gwproto.property_format import predicate_validator


class GtShStatus(BaseModel):
    SlotStartUnixS: int  #
    SimpleTelemetryList: List[GtShSimpleTelemetryStatus]
    AboutGNodeAlias: str  #
    BooleanactuatorCmdList: List[GtShBooleanactuatorCmdStatus]
    FromGNodeAlias: str  #
    MultipurposeTelemetryList: List[GtShMultipurposeTelemetryStatus]
    FromGNodeId: str  #
    StatusUid: str  #
    ReportingPeriodS: int  #
    TypeAlias: Literal["gt.sh.status"] = "gt.sh.status"

    _validator_slot_start_unix_s = predicate_validator("SlotStartUnixS", property_format.is_reasonable_unix_time_s)

    @validator("SimpleTelemetryList")
    def _validator_simple_telemetry_list(cls, v: List) -> List:
        for elt in v:
            if not isinstance(elt, GtShSimpleTelemetryStatus):
                raise ValueError(
                        f"elt {elt} of SimpleTelemetryList must have type GtShSimpleTelemetryStatus."
                    )
        return v

    _validator_about_g_node_alias = predicate_validator("AboutGNodeAlias", property_format.is_lrd_alias_format)

    @validator("BooleanactuatorCmdList")
    def _validator_booleanactuator_cmd_list(cls, v: List) -> List:
        for elt in v:
            if not isinstance(elt, GtShBooleanactuatorCmdStatus):
                raise ValueError(
                        f"elt {elt} of BooleanactuatorCmdList must have type GtShBooleanactuatorCmdStatus."
                    )
        return v

    _validator_from_g_node_alias = predicate_validator("FromGNodeAlias", property_format.is_lrd_alias_format)

    @validator("MultipurposeTelemetryList")
    def _validator_multipurpose_telemetry_list(cls, v: List) -> List:
        for elt in v:
            if not isinstance(elt, GtShMultipurposeTelemetryStatus):
                raise ValueError(
                        f"elt {elt} of MultipurposeTelemetryList must have type GtShMultipurposeTelemetryStatus."
                    )
        return v

    _validator_from_g_node_id = predicate_validator("FromGNodeId", property_format.is_uuid_canonical_textual)

    _validator_status_uid = predicate_validator("StatusUid", property_format.is_uuid_canonical_textual)

    def asdict(self):
        d = self.dict()

        # Recursively call asdict() for the SubTypes
        simple_telemetry_list = []
        for elt in self.SimpleTelemetryList:
            simple_telemetry_list.append(elt.asdict())
        d["SimpleTelemetryList"] = simple_telemetry_list

        # Recursively call asdict() for the SubTypes
        booleanactuator_cmd_list = []
        for elt in self.BooleanactuatorCmdList:
            booleanactuator_cmd_list.append(elt.asdict())
        d["BooleanactuatorCmdList"] = booleanactuator_cmd_list

        # Recursively call asdict() for the SubTypes
        multipurpose_telemetry_list = []
        for elt in self.MultipurposeTelemetryList:
            multipurpose_telemetry_list.append(elt.asdict())
        d["MultipurposeTelemetryList"] = multipurpose_telemetry_list
        return d

    def as_type(self):
        return json.dumps(self.asdict())


class GtShStatus_Maker:
    type_alias = "gt.sh.status"

    def __init__(self,
                    slot_start_unix_s: int,
                    simple_telemetry_list: List[GtShSimpleTelemetryStatus],
                    about_g_node_alias: str,
                    booleanactuator_cmd_list: List[GtShBooleanactuatorCmdStatus],
                    from_g_node_alias: str,
                    multipurpose_telemetry_list: List[GtShMultipurposeTelemetryStatus],
                    from_g_node_id: str,
                    status_uid: str,
                    reporting_period_s: int):

        self.tuple = GtShStatus(
            SlotStartUnixS=slot_start_unix_s,
            SimpleTelemetryList=simple_telemetry_list,
            AboutGNodeAlias=about_g_node_alias,
            BooleanactuatorCmdList=booleanactuator_cmd_list,
            FromGNodeAlias=from_g_node_alias,
            MultipurposeTelemetryList=multipurpose_telemetry_list,
            FromGNodeId=from_g_node_id,
            StatusUid=status_uid,
            ReportingPeriodS=reporting_period_s,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: GtShStatus) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtShStatus:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtShStatus:
        d2 = dict(d)
        if "TypeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeAlias")
        if "SimpleTelemetryList" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SimpleTelemetryList")
        simple_telemetry_list = []
        if not isinstance(d2["SimpleTelemetryList"], List):
            raise SchemaError("SimpleTelemetryList must be a List!")
        for elt in d2["SimpleTelemetryList"]:
            if not isinstance(elt, dict):
                raise SchemaError(
                    f"elt {elt} of SimpleTelemetryList must be "
                    "GtShSimpleTelemetryStatus but not even a dict!"
                )
            simple_telemetry_list.append(
                GtShSimpleTelemetryStatus_Maker.dict_to_tuple(elt)
            )
        d2["SimpleTelemetryList"] = simple_telemetry_list
        if "BooleanactuatorCmdList" not in d2.keys():
            raise SchemaError(f"dict {d2} missing BooleanactuatorCmdList")
        booleanactuator_cmd_list = []
        if not isinstance(d2["BooleanactuatorCmdList"], List):
            raise SchemaError("BooleanactuatorCmdList must be a List!")
        for elt in d2["BooleanactuatorCmdList"]:
            if not isinstance(elt, dict):
                raise SchemaError(
                    f"elt {elt} of BooleanactuatorCmdList must be "
                    "GtShBooleanactuatorCmdStatus but not even a dict!"
                )
            booleanactuator_cmd_list.append(
                GtShBooleanactuatorCmdStatus_Maker.dict_to_tuple(elt)
            )
        d2["BooleanactuatorCmdList"] = booleanactuator_cmd_list
        if "MultipurposeTelemetryList" not in d2.keys():
            raise SchemaError(f"dict {d2} missing MultipurposeTelemetryList")
        multipurpose_telemetry_list = []
        if not isinstance(d2["MultipurposeTelemetryList"], List):
            raise SchemaError("MultipurposeTelemetryList must be a List!")
        for elt in d2["MultipurposeTelemetryList"]:
            if not isinstance(elt, dict):
                raise SchemaError(
                    f"elt {elt} of MultipurposeTelemetryList must be "
                    "GtShMultipurposeTelemetryStatus but not even a dict!"
                )
            multipurpose_telemetry_list.append(
                GtShMultipurposeTelemetryStatus_Maker.dict_to_tuple(elt)
            )
        d2["MultipurposeTelemetryList"] = multipurpose_telemetry_list

        return GtShStatus(
            TypeAlias=d2["TypeAlias"],
            SlotStartUnixS=d2["SlotStartUnixS"],
            SimpleTelemetryList=d2["SimpleTelemetryList"],
            AboutGNodeAlias=d2["AboutGNodeAlias"],
            BooleanactuatorCmdList=d2["BooleanactuatorCmdList"],
            FromGNodeAlias=d2["FromGNodeAlias"],
            MultipurposeTelemetryList=d2["MultipurposeTelemetryList"],
            FromGNodeId=d2["FromGNodeId"],
            StatusUid=d2["StatusUid"],
            ReportingPeriodS=d2["ReportingPeriodS"],
            #
        )
