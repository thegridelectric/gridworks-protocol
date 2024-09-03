"""Tests relay.cac.gt type, version 000"""

from gwproto.types import RelayCacGt
from tests.cac_load_utils import CacCase, assert_cac_load


def test_relay_cac_gt_load() -> None:
    d = {
        "ComponentAttributeClassId": "69f101fc-22e4-4caa-8103-50b8aeb66028",
        # "MakeModelGtEnumSymbol": "9cc57878",
        "MakeModel": "GRIDWORKS__SIMBOOL30AMPRELAY",
        "DisplayName": "Gridworks Simulated Boolean Actuator",
        "TypicalResponseTimeMs": 400,
        "TypeName": "relay.cac.gt",
        "Version": "000",
    }
    assert_cac_load([CacCase("RelayCacGt", d, RelayCacGt)])
