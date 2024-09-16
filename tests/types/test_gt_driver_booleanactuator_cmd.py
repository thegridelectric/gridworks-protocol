"""Tests gt.driver.booleanactuator.cmd type, version 100"""

from gwproto.types import GtDriverBooleanactuatorCmd


def test_gt_driver_booleanactuator_cmd_generated() -> None:
    d = {
        "RelayState": 0,
        "ShNodeAlias": "a.elt1.relay",
        "CommandTimeUnixMs": 1656869326637,
        "TypeName": "gt.driver.booleanactuator.cmd",
        "Version": "100",
    }
    payload = GtDriverBooleanactuatorCmd.model_validate(d)
    assert payload.model_dump() == d
