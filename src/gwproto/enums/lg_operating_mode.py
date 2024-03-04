from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class LgOperatingMode(StrEnum):
    """
    LG ThermaV and HydroKit heat pumps have the concept of being in different operating modes.
    This is used for a double-throw relay, so it can only ever have two states.

    Enum lg.operating.mode version 000 in the GridWorks Type registry.

    Used by used by multiple Application Shared Languages (ASLs), including but not limited to
    gwproto. For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#lgoperatingmode)

    Values (with symbols in parens):
      - Dhw (00000000): The LG Therma V or HydroKit is in Domestic Hot Water Mode - it requires a
        temp sensor to work.
      - Heat (4f96e480): The LG is in Heating mode.
    """

    Dhw = auto()
    Heat = auto()

    @classmethod
    def default(cls) -> "LgOperatingMode":
        """
        Returns default value (in this case Heat)
        """
        return cls.Heat

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def version(cls, value: str) -> str:
        """
        Returns the version of an enum value.

        Once a value belongs to one version of the enum, it belongs
        to all future versions.

        Args:
            value (str): The candidate enum value.

        Raises:
            ValueError: If value is not one of the enum values.

        Returns:
            str: The earliest version of the enum containing value.
        """
        if not isinstance(value, str):
            raise ValueError(f"This method applies to strings, not enums")
        if value not in value_to_version.keys():
            raise ValueError(f"Unknown enum value: {value}")
        return value_to_version[value]

    @classmethod
    def enum_name(cls) -> str:
        """
        The name in the GridWorks Type Registry (lg.operating.mode)
        """
        return "lg.operating.mode"

    @classmethod
    def enum_version(cls) -> str:
        """
        The version in the GridWorks Type Registry (000)
        """
        return "000"

    @classmethod
    def symbol_to_value(cls, symbol: str) -> str:
        """
        Given the symbol sent in a serialized message, returns the encoded enum.

        Args:
            symbol (str): The candidate symbol.

        Returns:
            str: The encoded value associated to that symbol. If the symbol is not
            recognized - which could happen if the actor making the symbol is using
            a later version of this enum, returns the default value of "Heat".
        """
        if symbol not in symbol_to_value.keys():
            return cls.default().value
        return symbol_to_value[symbol]

    @classmethod
    def value_to_symbol(cls, value: str) -> str:
        """
        Provides the encoding symbol for a LgOperatingMode enum to send in seriliazed messages.

        Args:
            symbol (str): The candidate value.

        Returns:
            str: The symbol encoding that value. If the value is not recognized -
            which could happen if the actor making the message used a later version
            of this enum than the actor decoding the message, returns the default
            symbol of "4f96e480".
        """
        if value not in value_to_symbol.keys():
            return value_to_symbol[cls.default().value]
        return value_to_symbol[value]

    @classmethod
    def symbols(cls) -> List[str]:
        """
        Returns a list of the enum symbols
        """
        return [
            "00000000",
            "4f96e480",
        ]


symbol_to_value = {
    "00000000": "Dhw",
    "4f96e480": "Heat",
}

value_to_symbol = {value: key for key, value in symbol_to_value.items()}

value_to_version = {
    "Dhw": "000",
    "Heat": "000",
}
