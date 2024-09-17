"""Tests rest.poller.component.gt type, version 000"""

from gwproto.types.rest_poller_component_gt import RESTPollerComponentGt


def test_rest_poller_component_gt_generated() -> None:
    d = {
        "TypeName": "rest.poller.component.gt",
        "Version": "000",
    }

    t = RESTPollerComponentGt(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d
