from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class ChangeRelayState(StrEnum):
    """
    This is meant for relays in either NormallyOpen or NormallyClosed configuration (i.e. not
    configured as DoubleThrow). It provides the natural Finite State Machine actions that go
    along with simple.relay.state states of RelayOpen and RelayClosed. Open = PowerOff = 0 and
    Closed = PowerOn = 1

    Enum change.relay.state version 000 in the GridWorks Type registry.

    Used by used by multiple Application Shared Languages (ASLs), including but not limited to
    gwproto. For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#changerelaystate)

    Values (with symbols in parens):
      - TurnOn ()
      - TurnOff ()
    """

    TurnOn = auto()
    TurnOff = auto()

    @classmethod
    def default(cls) -> "ChangeRelayState":
        """
        Returns default value (in this case TurnOff)
        """
        return cls.TurnOff

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
        The name in the GridWorks Type Registry (change.relay.state)
        """
        return "change.relay.state"

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
            a later version of this enum, returns the default value of "TurnOff".
        """
        if symbol not in symbol_to_value.keys():
            return cls.default().value
        return symbol_to_value[symbol]

    @classmethod
    def value_to_symbol(cls, value: str) -> str:
        """
        Provides the encoding symbol for a ChangeRelayState enum to send in seriliazed messages.

        Args:
            symbol (str): The candidate value.

        Returns:
            str: The symbol encoding that value. If the value is not recognized -
            which could happen if the actor making the message used a later version
            of this enum than the actor decoding the message, returns the default
            symbol of "".
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
            "",
            "",
        ]


symbol_to_value = {
    "": "TurnOn",
    "": "TurnOff",
}

value_to_symbol = {value: key for key, value in symbol_to_value.items()}

value_to_version = {
    "TurnOn": "000",
    "TurnOff": "000",
}
