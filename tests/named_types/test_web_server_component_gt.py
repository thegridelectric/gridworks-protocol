"""Tests web.server.component.gt type, version 000"""

from gwproto.named_types import WebServerComponentGt


def test_web_server_component_gt_generated() -> None:
    d = {
        "TypeName": "web.server.component.gt",
        "Version": "000",
    }

    d2 = WebServerComponentGt.from_dict(d).to_dict()

    assert d2 == d
