"""Tests gt.sh.cli.atn.cmd type, version 110"""

from gwproto.types import GtShCliAtnCmd


def test_gt_sh_cli_atn_cmd_generated() -> None:
    d = {
        "FromGNodeAlias": "dwtest.isone.ct.newhaven.orange1",
        "SendSnapshot": True,
        "FromGNodeId": "e7f7d6cc-08b0-4b36-bbbb-0a1f8447fd32",
        "TypeName": "gt.sh.cli.atn.cmd",
        "Version": "110",
    }

    d2 = GtShCliAtnCmd.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
