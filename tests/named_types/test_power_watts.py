"""Tests power.watts type, version 000"""

from gwproto.named_types import PowerWatts


def test_power_watts_generated() -> None:
    d = {
        "Watts": 4500,
        "TypeName": "power.watts",
        "Version": "000",
    }
    d2 = PowerWatts.from_dict(d).to_dict()
    assert d2 == d
