"""Tests power.watts type, version 000"""

from gwproto.types import PowerWatts


def test_power_watts_generated() -> None:
    d = {
        "Watts": 4500,
        "TypeName": "power.watts",
        "Version": "000",
    }

    d2 = PowerWatts.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
