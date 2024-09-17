"""Tests web.server.component.gt type, version 000"""

from gwproto.types import WebServerComponentGt


def test_web_server_component_gt_generated() -> None:
    d = {
        "TypeName": "web.server.component.gt",
        "Version": "000",
    }

    t = WebServerComponentGt(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d
