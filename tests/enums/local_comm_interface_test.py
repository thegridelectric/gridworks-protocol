"""Tests for schema enum local.comm.interface.000"""
from gwproto.enums import LocalCommInterface


def test_local_comm_interface() -> None:
    assert set(LocalCommInterface.values()) == {
        "UNKNOWN",
        "I2C",
        "ETHERNET",
        "ONEWIRE",
        "RS485",
        "SIMRABBIT",
        "WIFI",
        "ANALOG_4_20_MA",
        "RS232",
    }

    assert LocalCommInterface.default() == LocalCommInterface.UNKNOWN
