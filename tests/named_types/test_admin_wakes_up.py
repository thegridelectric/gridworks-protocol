"""Tests admin.wakes.up type, version 000"""

from gwproto.named_types import AdminWakesUp


def test_admin_wakes_up_generated() -> None:
    d = {
        "FromName": "admin",
        "ToName": "s",
        "TypeName": "admin.wakes.up",
        "Version": "000",
    }

    d2 = AdminWakesUp.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
