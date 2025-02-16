"""
Tests for enum thermistor.data.method.000 from the GridWorks Type Registry.
"""

from gwproto.enums import ThermistorDataMethod


def test_thermistor_data_method() -> None:
    assert set(ThermistorDataMethod.values()) == {
        "SimpleBeta",
        "BetaWithExponentialAveraging",
    }

    assert ThermistorDataMethod.default() == ThermistorDataMethod.SimpleBeta
    assert ThermistorDataMethod.enum_name() == "thermistor.data.method"
    assert ThermistorDataMethod.enum_version() == "000"
