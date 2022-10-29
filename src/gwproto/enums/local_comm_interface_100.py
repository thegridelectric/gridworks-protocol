"""Schema enum local.comm.interface.100 definition.

Look in enums/local_comm_interface_100 for:
    - the local python enum LocalCommInterface
    - the SchemaEnum LocalCommInterface100SchemaEnum

The SchemaEnum is a list of symbols sent in API/ABI messages. Its symbols
are not supposed to be human readable.

The LocalEnum are intended to be human readable."""

from abc import ABC
from enum import auto
from typing import Dict
from typing import List

from fastapi_utils.enums import StrEnum

from gwproto.errors import SchemaError


class LocalCommInterface(StrEnum):
    """
    Analog_4_20_mA,
    RS232,
    I2C,
    Wifi,
    SimRabbit,
    Unknown,
    Ethernet,
    OneWire,
    RS485,
    
    This is the enum intended for the local application. It is forwards and backwards
    compatible with LocalCommInterface enums used in types.
    """

    @classmethod
    def values(cls):
        return [elt.value for elt in cls]

    Analog_4_20_mA = auto()
    RS232 = auto()
    I2C = auto()
    Wifi = auto()
    SimRabbit = auto()
    Unknown = auto()
    Ethernet = auto()
    OneWire = auto()
    RS485 = auto()
    


class LocalCommInterfaceMap:
    """ Handles the bijection
        "653c73b8" -  Analog_4_20_mA,
        "0843a726" -  RS232,
        "9ec8bc49" -  I2C,
        "46ac6589" -  Wifi,
        "efc144cd" -  SimRabbit,
        "829549d1" -  Unknown,
        "c1e7a955" -  Ethernet,
        "ae2d4cd8" -  OneWire,
        "a6a4ac9f" -  RS485,
    """
    type_name = "local.comm.interface.100"

    symbols: List[str] = [
        "653c73b8",
        "0843a726",
        "9ec8bc49",
        "46ac6589",
        "efc144cd",
        "829549d1",
        "c1e7a955",
        "ae2d4cd8",
        "a6a4ac9f",
        #
    ]

    @classmethod
    def is_symbol(cls, candidate) -> bool:
        if candidate in cls.symbols:
            return True
        return False

    @classmethod
    def type_to_local(cls, symbol):
        if not cls.is_symbol(symbol):
            raise SchemaError(
                f"{symbol} must belong to key of {LocalCommInterfaceMap.type_to_local_dict}"
            )
        return cls.type_to_local_dict[symbol]

    @classmethod
    def local_to_type(cls, local_comm_interface):
        if not isinstance(local_comm_interface, LocalCommInterface):
            raise SchemaError(f"{local_comm_interface} must be of type {LocalCommInterface}")
        return cls.local_to_type_dict[local_comm_interface]

    type_to_local_dict: Dict[str, LocalCommInterface] = {
        "653c73b8": LocalCommInterface.Analog_4_20_mA,
        "0843a726": LocalCommInterface.RS232,
        "9ec8bc49": LocalCommInterface.I2C,
        "46ac6589": LocalCommInterface.Wifi,
        "efc144cd": LocalCommInterface.SimRabbit,
        "829549d1": LocalCommInterface.Unknown,
        "c1e7a955": LocalCommInterface.Ethernet,
        "ae2d4cd8": LocalCommInterface.OneWire,
        "a6a4ac9f": LocalCommInterface.RS485,
    }

    local_to_type_dict: Dict[LocalCommInterface, str] = {
        LocalCommInterface.Analog_4_20_mA: "653c73b8",
        LocalCommInterface.RS232: "0843a726",
        LocalCommInterface.I2C: "9ec8bc49",
        LocalCommInterface.Wifi: "46ac6589",
        LocalCommInterface.SimRabbit: "efc144cd",
        LocalCommInterface.Unknown: "829549d1",
        LocalCommInterface.Ethernet: "c1e7a955",
        LocalCommInterface.OneWire: "ae2d4cd8",
        LocalCommInterface.RS485: "a6a4ac9f",
        #
    }
