"""Schema enum spaceheat.unit.110 definition.

Look in enums/spaceheat_unit_110 for:
    - the local python enum Unit
    - the SchemaEnum SpaceheatUnit110SchemaEnum

The SchemaEnum is a list of symbols sent in API/ABI messages. Its symbols
are not supposed to be human readable.

The LocalEnum are intended to be human readable."""

from abc import ABC
from enum import auto
from typing import Dict
from typing import List

from fastapi_utils.enums import StrEnum

from gwproto.errors import SchemaError


class Unit(StrEnum):
    """
    Fahrenheit,
    AmpsRms,
    Celcius,
    Wh,
    VoltsRms,
    Gpm,
    W,
    Unitless,
    
    This is the enum intended for the local application. It is forwards and backwards
    compatible with Unit enums used in types.
    """

    @classmethod
    def values(cls):
        return [elt.value for elt in cls]

    Fahrenheit = auto()
    AmpsRms = auto()
    Celcius = auto()
    Wh = auto()
    VoltsRms = auto()
    Gpm = auto()
    W = auto()
    Unitless = auto()
    


class UnitMap:
    """ Handles the bijection
        "8e6dd6dd" -  Fahrenheit,
        "018904c8" -  AmpsRms,
        "44d15aca" -  Celcius,
        "d66f1622" -  Wh,
        "e5d7555c" -  VoltsRms,
        "ed2236f1" -  Gpm,
        "8355e623" -  W,
        "1ad379fc" -  Unitless,
    """
    type_name = "spaceheat.unit.110"

    symbols: List[str] = [
        "8e6dd6dd",
        "018904c8",
        "44d15aca",
        "d66f1622",
        "e5d7555c",
        "ed2236f1",
        "8355e623",
        "1ad379fc",
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
                f"{symbol} must belong to key of {UnitMap.type_to_local_dict}"
            )
        return cls.type_to_local_dict[symbol]

    @classmethod
    def local_to_type(cls, unit):
        if not isinstance(unit, Unit):
            raise SchemaError(f"{unit} must be of type {Unit}")
        return cls.local_to_type_dict[unit]

    type_to_local_dict: Dict[str, Unit] = {
        "8e6dd6dd": Unit.Fahrenheit,
        "018904c8": Unit.AmpsRms,
        "44d15aca": Unit.Celcius,
        "d66f1622": Unit.Wh,
        "e5d7555c": Unit.VoltsRms,
        "ed2236f1": Unit.Gpm,
        "8355e623": Unit.W,
        "1ad379fc": Unit.Unitless,
    }

    local_to_type_dict: Dict[Unit, str] = {
        Unit.Fahrenheit: "8e6dd6dd",
        Unit.AmpsRms: "018904c8",
        Unit.Celcius: "44d15aca",
        Unit.Wh: "d66f1622",
        Unit.VoltsRms: "e5d7555c",
        Unit.Gpm: "ed2236f1",
        Unit.W: "8355e623",
        Unit.Unitless: "1ad379fc",
        #
    }
