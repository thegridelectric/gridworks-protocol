from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class FsmEventType(StrEnum):
    """
    The name of a set of events for a particular Spaceheat finite state machine.

    Enum sh.fsm.event.type version 000 in the GridWorks Type registry.

    Used by used by multiple Application Shared Languages (ASLs), including but not limited to
    gwproto. For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#shfsmeventtype)
      - [More Info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)

    Values (with symbols in parens):
      - ChangeRelayState (00000000)
      - SetAnalog010V (bbef899f)
      - SetAnalog420mA (aa4b0c96)
      - ChangeValveState (c234ee7a)
      - ChangeStoreFlowDirection (1efc9909)
      - ChangeHeatcallSource (c5717e64)
      - ChangeBoilerControl (0066a412)
      - ChangeHeatPumpControl (50ea0661)
      - ChangeLgOperatingMode (89a98375)
      - TimerFinished (9e44ab43)
    """

    ChangeRelayState = auto()
    SetAnalog010V = auto()
    SetAnalog420mA = auto()
    ChangeValveState = auto()
    ChangeStoreFlowDirection = auto()
    ChangeHeatcallSource = auto()
    ChangeBoilerControl = auto()
    ChangeHeatPumpControl = auto()
    ChangeLgOperatingMode = auto()
    TimerFinished = auto()
    ChangeRelayPin = auto()

    @classmethod
    def default(cls) -> "FsmEventType":
        """
        Returns default value (in this case ChangeRelayState)
        """
        return cls.ChangeRelayState

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
        The name in the GridWorks Type Registry (sh.fsm.event.type)
        """
        return "sh.fsm.event.type"

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
            a later version of this enum, returns the default value of "ChangeRelayState".
        """
        if symbol not in symbol_to_value.keys():
            return cls.default().value
        return symbol_to_value[symbol]

    @classmethod
    def value_to_symbol(cls, value: str) -> str:
        """
        Provides the encoding symbol for a FsmEventType enum to send in seriliazed messages.

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
            "bbef899f",
            "aa4b0c96",
            "c234ee7a",
            "1efc9909",
            "c5717e64",
            "0066a412",
            "50ea0661",
            "89a98375",
            "9e44ab43",
            "b6706976",
        ]


symbol_to_value = {
    "00000000": "ChangeRelayState",
    "bbef899f": "SetAnalog010V",
    "aa4b0c96": "SetAnalog420mA",
    "c234ee7a": "ChangeValveState",
    "1efc9909": "ChangeStoreFlowDirection",
    "c5717e64": "ChangeHeatcallSource",
    "0066a412": "ChangeBoilerControl",
    "50ea0661": "ChangeHeatPumpControl",
    "89a98375": "ChangeLgOperatingMode",
    "9e44ab43": "TimerFinished",
    "b6706976": "ChangeRelayPin",
}

value_to_symbol = {value: key for key, value in symbol_to_value.items()}

value_to_version = {
    "ChangeRelayState": "000",
    "SetAnalog010V": "000",
    "SetAnalog420mA": "000",
    "ChangeValveState": "000",
    "ChangeStoreFlowDirection": "000",
    "ChangeHeatcallSource": "000",
    "ChangeBoilerControl": "000",
    "ChangeHeatPumpControl": "000",
    "ChangeLgOperatingMode": "000",
    "TimerFinished": "000",
    "ChangeRelayPin": "000",
}
