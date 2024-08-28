"""Type relay.actor.config, version 000"""

import json
import logging
import os
from typing import Any, Dict, Literal

import dotenv
from gw.errors import GwTypeError
from gw.utils import is_pascal_case, pascal_to_snake, snake_to_pascal
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from typing_extensions import Self

from gwproto.enums import (
    ChangeAquastatControl,
    ChangeHeatcallSource,
    ChangeHeatPumpControl,
    ChangeLgOperatingMode,
    ChangeRelayState,
    ChangeStoreFlowDirection,
    ChangeValveState,
    FsmEventType,
    RelayWiringConfig,
)

EVENT_ENUM_BY_NAME = {
    FsmEventType.ChangeRelayState.value: ChangeRelayState,
    FsmEventType.ChangeValveState.value: ChangeValveState,
    FsmEventType.ChangeStoreFlowDirection.value: ChangeStoreFlowDirection,
    FsmEventType.ChangeHeatcallSource.value: ChangeHeatcallSource,
    FsmEventType.ChangeAquastatControl.value: ChangeAquastatControl,
    FsmEventType.ChangeHeatPumpControl.value: ChangeHeatPumpControl,
    FsmEventType.ChangeLgOperatingMode.value: ChangeLgOperatingMode,
}

dotenv.load_dotenv()

ENCODE_ENUMS = int(os.getenv("ENUM_ENCODE", "1"))

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class RelayActorConfig(BaseModel):
    """
    Relay Actor Config.

    Used to associate individual relays on a multi-channel relay board to specific SpaceheatNode
    actors. Each actor managed by the Spaceheat SCADA has an associated SpaceheatNode. That
    Node will be associated to a relay board component with multiple relays. Th relay board
    will have a list of relay actor configs so that the actor can identify which relay it has
    purview over.

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/spaceheat-actor.html)
    """

    relay_idx: int = Field(
        title="Relay Index",
    )
    actor_name: str = Field(
        title="Name of the Actor's SpaceheatNode",
        description="[More info](https://gridworks-protocol.readthedocs.io/en/latest/spaceheat-actor.html)",
    )
    wiring_config: RelayWiringConfig = Field(
        title="Wiring Config",
        description=(
            "Is the relay a simple Normally Open or Normally Closed or is it a double throw relay?"
        ),
    )
    event_type: FsmEventType = Field(
        title="Finite State Machine Event Type",
        description=(
            "Every pair of energization/de-energization actions for a relay are associated with "
            "two events for an associated finite state event."
        ),
    )
    de_energizing_event: str = Field(
        title="DeEnergizing Action",
        description=(
            "Which of the two choices provided by the EventType is intended to result in de-energizing "
            "the pin for the relay?"
        ),
    )
    type_name: Literal["relay.actor.config"] = "relay.actor.config"
    version: Literal["000"] = "000"
    model_config = ConfigDict(populate_by_name=True, alias_generator=snake_to_pascal)

    @field_validator("relay_idx")
    @classmethod
    def _check_relay_idx(cls, v: int) -> int:
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"RelayIdx failed PositiveInteger format validation: {e}"
            ) from e
        return v

    @field_validator("actor_name")
    @classmethod
    def _check_actor_name(cls, v: str) -> str:
        try:
            check_is_spaceheat_name(v)
        except ValueError as e:
            raise ValueError(
                f"ActorName failed SpaceheatName format validation: {e}"
            ) from e
        return v

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
                Axiom 1: EventType, DeEnergizingEvent consistency.
                a) The EventType must belong to one of the boolean choices for FsmEventType (for example, it is NOT SetAnalog010V):
            ChangeRelayState    ChangeValveState
            ChangeStoreFlowDirection
            ChangeHeatcallSource
            ChangeBoilerControl
            ChangeHeatPumpControl
            ChangeLgOperatingMode

        b) The DeEnergizingEvent string must be one of the two choices for the EventType as an enum. For example,  if the EventType is ChangeValveState then the  DeEnergizingEvent  must either be OpenValve or CloseValve.

        c) If the EventType is ChangeRelayState, then i) the WiringConfig cannot be DoubleThrow ii) if the Wiring Config is NormallyOpen then the DeEnergizingEvent must be OpenRelay and iii) if the WiringConfig is NormallyClosed then the DeEnergizingEvent must be CloseRelay.
        """

        # 1.a The EventType must belong to one of the boolean choices
        boolean_event_types = [
            FsmEventType.ChangeRelayState,
            FsmEventType.ChangeValveState,
            FsmEventType.ChangeStoreFlowDirection,
            FsmEventType.ChangeHeatcallSource,
            FsmEventType.ChangeAquastatControl,
            FsmEventType.ChangeHeatPumpControl,
            FsmEventType.ChangeLgOperatingMode,
        ]
        if self.event_type not in boolean_event_types:
            raise ValueError(
                f"Axiom 1 violated. EventType {self.event_type} must be a boolean FsmEventType:\n {boolean_event_types}"
            )

        # 1.b The DeEnergizingEvent string must be one of the two choices for the EventType as an enum.

        event_enum = EVENT_ENUM_BY_NAME[self.event_type.value]
        if self.de_energizing_event not in event_enum.values():
            raise ValueError(
                f"Axiom 1b violated. DeEnergizingEvent {self.de_energizing_event} must be "
                f"one of the values for {self.event_type.value}: {event_enum.values()} "
            )
        if self.event_type is FsmEventType.ChangeRelayState:
            if self.wiring_config is RelayWiringConfig.DoubleThrow:
                raise ValueError(
                    "Axiom 1.c.i violated. If the EventType is ChangeRelayState, "
                    "then the WiringConfig cannot be DoubleThrow"
                )
            elif self.wiring_config is RelayWiringConfig.NormallyOpen:
                if self.de_energizing_event != "OpenRelay":
                    raise ValueError(
                        "Axiom 1c.ii violated. I the EventType is ChangeRelayState "
                        "and Wiring Config is NormallyOpen then the DeEnergizingEvent "
                        "must be OpenRelay"
                    )
            elif self.wiring_config is RelayWiringConfig.NormallyClosed:
                if self.de_energizing_event != "CloseRelay":
                    raise ValueError(
                        "Axiom 1c.iii violated. I the EventType is ChangeRelayState "
                        "and Wiring Config is NormallyClosed then the DeEnergizingEvent "
                        "must be CloseRelay"
                    )
        return self

    def as_dict(self) -> Dict[str, Any]:
        """
        Main step in serializing the object. Encodes enums as their 8-digit random hex symbol if
        settings.encode_enums = 1.
        """
        if ENCODE_ENUMS:
            return self.enum_encoded_dict()
        else:
            return self.plain_enum_dict()

    def plain_enum_dict(self) -> Dict[str, Any]:
        """
        Returns enums as their values.
        """
        d = {
            snake_to_pascal(key): value
            for key, value in self.model_dump().items()
            if value is not None
        }
        d["WiringConfig"] = d["WiringConfig"].value
        d["EventType"] = d["EventType"].value
        return d

    def enum_encoded_dict(self) -> Dict[str, Any]:
        """
        Encodes enums as their 8-digit random hex symbol
        """
        d = {
            snake_to_pascal(key): value
            for key, value in self.model_dump().items()
            if value is not None
        }
        del d["WiringConfig"]
        d["WiringConfigGtEnumSymbol"] = RelayWiringConfig.value_to_symbol(
            self.wiring_config
        )
        del d["EventType"]
        d["EventTypeGtEnumSymbol"] = FsmEventType.value_to_symbol(self.event_type)
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the relay.actor.config.000 representation designed to send in a message.

        Recursively encodes enums as hard-to-remember 8-digit random hex symbols
        unless settings.encode_enums is set to 0.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class RelayActorConfigMaker:
    type_name = "relay.actor.config"
    version = "000"

    @classmethod
    def tuple_to_type(cls, tuple: RelayActorConfig) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> RelayActorConfig:
        """
        Given the bytes in a message, returns the corresponding class object.

        Args:
            b (bytes): candidate type instance

        Raises:
           GwTypeError: if the bytes are not a relay.actor.config.000 type

        Returns:
            RelayActorConfig instance
        """
        try:
            d = json.loads(b)
        except TypeError as e:
            raise GwTypeError("Type must be string or bytes!") from e
        if not isinstance(d, dict):
            raise GwTypeError(f"Deserializing  must result in dict!\n <{b}>")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> RelayActorConfig:
        """
        Translates a dict representation of a relay.actor.config.000 message object
        into the Python class object.
        """
        for key in d.keys():
            if not is_pascal_case(key):
                raise GwTypeError(f"Key '{key}' is not PascalCase")
        d2 = dict(d)
        if "RelayIdx" not in d2.keys():
            raise GwTypeError(f"dict missing RelayIdx: <{d2}>")
        if "ActorName" not in d2.keys():
            raise GwTypeError(f"dict missing ActorName: <{d2}>")
        if "WiringConfigGtEnumSymbol" in d2.keys():
            value = RelayWiringConfig.symbol_to_value(d2["WiringConfigGtEnumSymbol"])
            d2["WiringConfig"] = RelayWiringConfig(value)
            del d2["WiringConfigGtEnumSymbol"]
        elif "WiringConfig" in d2.keys():
            if d2["WiringConfig"] not in RelayWiringConfig.values():
                d2["WiringConfig"] = RelayWiringConfig.default()
            else:
                d2["WiringConfig"] = RelayWiringConfig(d2["WiringConfig"])
        else:
            raise GwTypeError(
                f"both WiringConfigGtEnumSymbol and WiringConfig missing from dict <{d2}>",
            )
        if "EventTypeGtEnumSymbol" in d2.keys():
            value = FsmEventType.symbol_to_value(d2["EventTypeGtEnumSymbol"])
            d2["EventType"] = FsmEventType(value)
            del d2["EventTypeGtEnumSymbol"]
        elif "EventType" in d2.keys():
            if d2["EventType"] not in FsmEventType.values():
                d2["EventType"] = FsmEventType.default()
            else:
                d2["EventType"] = FsmEventType(d2["EventType"])
        else:
            raise GwTypeError(
                f"both EventTypeGtEnumSymbol and EventType missing from dict <{d2}>",
            )
        if "DeEnergizingEvent" not in d2.keys():
            raise GwTypeError(f"dict missing DeEnergizingEvent: <{d2}>")
        if "TypeName" not in d2.keys():
            raise GwTypeError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise GwTypeError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret relay.actor.config version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        d3 = {pascal_to_snake(key): value for key, value in d2.items()}
        return RelayActorConfig(**d3)


def check_is_positive_integer(v: int) -> None:
    """
    Must be positive when interpreted as an integer. Interpretation as an
    integer follows the pydantic rules for this - which will round down
    rational numbers. So 1.7 will be interpreted as 1 and is also fine,
    while 0.5 is interpreted as 0 and will raise an exception.

    Args:
        v (int): the candidate

    Raises:
        ValueError: if v < 1
    """
    v2 = int(v)
    if v2 < 1:
        raise ValueError(f"<{v}> is not PositiveInteger")


def check_is_spaceheat_name(v: str) -> None:
    """Check SpaceheatName Format.

    Validates if the provided string adheres to the SpaceheatName format:
    Lowercase alphanumeric words separated by hypens

    Args:
        candidate (str): The string to be validated.

    Raises:
        ValueError: If the provided string is not in SpaceheatName format.
    """
    try:
        x = v.split("-")
    except Exception as e:
        raise ValueError(f"Failed to seperate <{v}> into words with split'-'") from e
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(
            f"Most significant word of <{v}> must start with alphabet char."
        )
    for word in x:
        if not word.isalnum():
            raise ValueError(f"words of <{v}> split by by '-' must be alphanumeric.")
    if not v.islower():
        raise ValueError(f"All characters of <{v}> must be lowercase.")
