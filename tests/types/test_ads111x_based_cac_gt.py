"""Tests ads111x.based.cac.gt type, version 000"""

from gwproto.enums import MakeModel
from gwproto.types import Ads111xBasedCacGt


def test_ads111x_based_cac_gt_generated() -> None:
    d = {
        "ComponentAttributeClassId": "432073b8-4d2b-4e36-9229-73893f33f846",
        "MinPollPeriodMs": 200,
        "MakeModel": "GRIDWORKS__MULTITEMP1",
        "AdsI2cAddressList": ["0x4b", "0x48", "0x49"],
        "TotalTerminalBlocks": 12,
        "TelemetryNameList": ["c89d0ba1", "0f627faa"],
        "DisplayName": "Gridworks 12-channel MultiTemp Ads Sensor",
        "TypeName": "ads111x.based.cac.gt",
        "Version": "000",
    }

    t = Ads111xBasedCacGt(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d

    ######################################
    # Behavior on unknown enum values: sends to default
    ######################################

    d2 = dict(d, MakeModel="unknown_enum_thing")
    assert Ads111xBasedCacGt(**d2).make_model == MakeModel.default()
