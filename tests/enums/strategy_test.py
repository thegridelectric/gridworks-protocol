"""
Tests for enum spaceheat.strategy.000 from the GridWorks Type Registry.
"""

from gwproto.enums import Strategy


def test_strategy() -> None:
    assert set(Strategy.values()) == {
        "Ha2Oil",
        "Ha1",
    }

    assert Strategy.default() == Strategy.Ha1
    assert Strategy.enum_name() == "spaceheat.strategy"
    assert Strategy.enum_version() == "000"
