"""Tests relay.component.gt type, version 000"""

from gwproto.data_classes.components import RelayComponent
from gwproto.types import RelayComponentGt
from tests.component_load_utils import ComponentCase, assert_component_load


def test_relay_component_gt_generated() -> None:
    d = {
        "ComponentId": "798fe14a-4073-41eb-bce2-075906aee6bb",
        "ComponentAttributeClassId": "69f101fc-22e4-4caa-8103-50b8aeb66028",
        "DisplayName": "relay for first elt in tank",
        "Gpio": 0,
        "HwUid": "abc123",
        "NormallyOpen": True,
        "TypeName": "relay.component.gt",
        "Version": "000",
    }
    assert_component_load(
        [ComponentCase("RelayComponentGt", d, RelayComponentGt, RelayComponent)],
    )
