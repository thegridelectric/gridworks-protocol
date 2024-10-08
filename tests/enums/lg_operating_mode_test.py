"""
Tests for enum lg.operating.mode.000 from the GridWorks Type Registry.
"""

from gwproto.enums import LgOperatingMode


def test_lg_operating_mode() -> None:
    assert set(LgOperatingMode.values()) == {
        "Dhw",
        "Heat",
    }

    assert LgOperatingMode.default() == LgOperatingMode.Heat
    assert LgOperatingMode.enum_name() == "lg.operating.mode"
