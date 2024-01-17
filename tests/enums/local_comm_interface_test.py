"""
Tests for enum local.comm.interface.000 from the GridWorks Type Registry.
"""
from gwproto.enums import LocalCommInterface


def test_local_comm_interface() -> None:
    assert set(LocalCommInterface.values()) == set(
        [
            "UNKNOWN",
            "I2C",
            "ETHERNET",
            "ONEWIRE",
            "RS485",
            "SIMRABBIT",
            "WIFI",
            "ANALOG_4_20_MA",
            "RS232",
        ]
    )

    assert LocalCommInterface.default() == LocalCommInterface.UNKNOWN
    assert LocalCommInterface.enum_name() == "local.comm.interface"
    assert LocalCommInterface.enum_version() == "000"

    assert LocalCommInterface.version("UNKNOWN") == "000"
    assert LocalCommInterface.version("I2C") == "000"
    assert LocalCommInterface.version("ETHERNET") == "000"
    assert LocalCommInterface.version("ONEWIRE") == "000"
    assert LocalCommInterface.version("RS485") == "000"
    assert LocalCommInterface.version("SIMRABBIT") == "000"
    assert LocalCommInterface.version("WIFI") == "000"
    assert LocalCommInterface.version("ANALOG_4_20_MA") == "000"
    assert LocalCommInterface.version("RS232") == "000"

    for value in LocalCommInterface.values():
        symbol = LocalCommInterface.value_to_symbol(value)
        assert LocalCommInterface.symbol_to_value(symbol) == value
