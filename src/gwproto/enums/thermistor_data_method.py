from enum import auto
from typing import List, Optional

from gw.enums import GwStrEnum


class ThermistorDataMethod(GwStrEnum):
    """
    What method is used to go from raw voltage readings to captured temperature readings.

    Enum thermistor.data.method version 000 in the GridWorks Type registry.

    Used by multiple Application Shared Languages (ASLs). For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#thermistordatamethod)

    Values (with symbols in parens):
      - SimpleBeta (00000000): Using the beta formula with a calibrated open voltage reading, transmitting
        raw polled data.
      - BetaWithExponentialAveraging (2c13f809): Using the beta formula with a calibrated open voltage
        reading, and then some sort of exponential weighted averaging on polled data.
    """

    SimpleBeta = auto()
    BetaWithExponentialAveraging = auto()

    @classmethod
    def default(cls) -> "ThermistorDataMethod":
        """
        Returns default value (in this case SimpleBeta)
        """
        return cls.SimpleBeta

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def version(cls, value: Optional[str] = None) -> str:
        """
        Returns the version of the class (default) used by this package or the
        version of a candidate enum value (always less than or equal to the version
        of the class)

        Args:
            value (Optional[str]): None (for version of the Enum itself) or
            the candidate enum value.

        Raises:
            ValueError: If the value is not one of the enum values.

        Returns:
            str: The version of the enum used by this code (if given no
            value) OR the earliest version of the enum containing the value.
        """
        if value is None:
            return "000"
        if not isinstance(value, str):
            raise ValueError("This method applies to strings, not enums")
        if value not in value_to_version.keys():
            raise ValueError(f"Unknown enum value: {value}")
        return value_to_version[value]

    @classmethod
    def enum_name(cls) -> str:
        """
        The name in the GridWorks Type Registry (thermistor.data.method)
        """
        return "thermistor.data.method"

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
            a later version of this enum, returns the default value of "SimpleBeta".
        """
        if symbol not in symbol_to_value.keys():
            return cls.default().value
        return symbol_to_value[symbol]

    @classmethod
    def value_to_symbol(cls, value: str) -> str:
        """
        Provides the encoding symbol for a ThermistorDataMethod enum to send in seriliazed messages.

        Args:
            symbol (str): The candidate value.

        Returns:
            str: The symbol encoding that value. If the value is not recognized -
            which could happen if the actor making the message used a later version
            of this enum than the actor decoding the message, returns the default
            symbol of "00000000".
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
            "2c13f809",
        ]


symbol_to_value = {
    "00000000": "SimpleBeta",
    "2c13f809": "BetaWithExponentialAveraging",
}

value_to_symbol = {value: key for key, value in symbol_to_value.items()}

value_to_version = {
    "SimpleBeta": "000",
    "BetaWithExponentialAveraging": "000",
}
