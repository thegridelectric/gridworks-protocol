"""gt.sh.status type"""
import json
from typing import List
from typing import Literal

from pydantic import BaseModel
from pydantic import validator

import gwproto.property_format as property_format
from gwproto.gt.gt_sh_booleanactuator_cmd_status import GtShBooleanactuatorCmdStatus
from gwproto.gt.gt_sh_multipurpose_telemetry_status import (
    GtShMultipurposeTelemetryStatus,
)
from gwproto.gt.gt_sh_simple_telemetry_status import GtShSimpleTelemetryStatus
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

    _validator_about_g_node_alias = predicate_validator("AboutGNodeAlias", property_format.is_lrd_alias_format)

    @validator("BooleanactuatorCmdList")
    def _validator_booleanactuator_cmd_list(cls, v: List) -> List:
        for elt in v:
            if not isinstance(elt, GtShBooleanactuatorCmdStatus):
                raise ValueError(
                        f"elt {elt} of BooleanactuatorCmdList must have type GtShBooleanactuatorCmdStatus."
                    )

    _validator_from_g_node_alias = predicate_validator("FromGNodeAlias", property_format.is_lrd_alias_format)

    @validator("MultipurposeTelemetryList")
    def _validator_multipurpose_telemetry_list(cls, v: List) -> List:
        for elt in v:
            if not isinstance(elt, GtShMultipurposeTelemetryStatus):
                raise ValueError(
                        f"elt {elt} of MultipurposeTelemetryList must have type GtShMultipurposeTelemetryStatus."
                    )

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
