from enum import auto
from typing import List, Optional

from gw.enums import GwStrEnum


class AlertPriority(GwStrEnum):
    """
    The GridWorks in-house enum for prioritizing alerts in a context where distributed equipment
    maintenance affects people's comfort and well-being.

    Enum alert.priority version 000 in the GridWorks Type registry.

    Used by multiple Application Shared Languages (ASLs). For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#alertpriority)

    Values (with symbols in parens):
      - P1Critical (66485e07): Critical alerts represent situations where immediate action is required
        to prevent significant impact or harm. These alerts should be addressed immediately,
        as they have the potential to cause significant disruption or endangerment to people's
        comfort and well-being.
      - P2High (13d7c23b): High-priority alerts represent situations that require urgent attention
        to prevent significant impact or harm. While not as critical as P1 alerts, P2 alerts
        still require prompt action to address the issue and prevent further escalation.
      - P3Medium (00000000): Medium-priority alerts represent situations that require attention to
        prevent potential impact or harm. These alerts should be addressed in a timely manner
        to prevent any negative impact on people's comfort and well-being.
      - P4Low (b2d668a0): Low-priority alerts represent situations that require attention but are
        not urgent. While not as critical as P1, P2, or P3 alerts, P4 alerts should still be
        addressed in a reasonable timeframe to prevent any negative impact on people's comfort
        and well-being.
      - P5Info (5ad8f63b): Informational alerts provide general information and do not require immediate
        action. These alerts may include notifications, status updates, or routine maintenance
        reminders.
    """

    P1Critical = auto()
    P2High = auto()
    P3Medium = auto()
    P4Low = auto()
    P5Info = auto()

    @classmethod
    def default(cls) -> "AlertPriority":
        """
        Returns default value (in this case P3Medium)
        """
        return cls.P3Medium

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
        The name in the GridWorks Type Registry (alert.priority)
        """
        return "alert.priority"

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
            a later version of this enum, returns the default value of "P3Medium".
        """
        if symbol not in symbol_to_value.keys():
            return cls.default().value
        return symbol_to_value[symbol]

    @classmethod
    def value_to_symbol(cls, value: str) -> str:
        """
        Provides the encoding symbol for a AlertPriority enum to send in seriliazed messages.

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
            "66485e07",
            "13d7c23b",
            "00000000",
            "b2d668a0",
            "5ad8f63b",
        ]


symbol_to_value = {
    "66485e07": "P1Critical",
    "13d7c23b": "P2High",
    "00000000": "P3Medium",
    "b2d668a0": "P4Low",
    "5ad8f63b": "P5Info",
}

value_to_symbol = {value: key for key, value in symbol_to_value.items()}

value_to_version = {
    "P1Critical": "000",
    "P2High": "000",
    "P3Medium": "000",
    "P4Low": "000",
    "P5Info": "000",
}
