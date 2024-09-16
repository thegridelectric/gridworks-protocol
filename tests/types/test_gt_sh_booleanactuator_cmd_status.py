"""Tests gt.sh.booleanactuator.cmd.status type, version 100"""

from gwproto.types import GtShBooleanactuatorCmdStatus


def test_gt_sh_booleanactuator_cmd_status_generated() -> None:
    d = {
        "ShNodeAlias": "a.elt1.relay",
        "RelayStateCommandList": [0],
        "CommandTimeUnixMsList": [1656443704800],
        "TypeName": "gt.sh.booleanactuator.cmd.status",
        "Version": "100",
    }
    assert GtShBooleanactuatorCmdStatus.model_validate(d).model_dump() == d
