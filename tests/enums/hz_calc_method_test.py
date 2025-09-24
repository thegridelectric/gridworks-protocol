"""
Tests for enum hz.calc.method.000 from the GridWorks Type Registry.
"""

from gwproto.enums import HzCalcMethod


def test_hz_calc_method() -> None:
    assert set(HzCalcMethod.values()) == {
        "BasicExpWeightedAvg",
        "BasicButterWorth",
        "UniformWindow",
    }

    assert HzCalcMethod.default() == HzCalcMethod.BasicExpWeightedAvg
    assert HzCalcMethod.enum_name() == "hz.calc.method"
    assert HzCalcMethod.enum_version() == "001"
