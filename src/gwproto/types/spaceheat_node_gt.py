"""Type spaceheat.node.gt, version 200"""

import json
import logging
import os
from typing import Any, Dict, Literal, Optional

import dotenv
from gw.errors import GwTypeError
from gw.utils import is_pascal_case, pascal_to_snake, snake_to_pascal
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from typing_extensions import Self

from gwproto.data_classes.sh_node import ShNode
from gwproto.enums import ActorClass

dotenv.load_dotenv()

ENCODE_ENUMS = int(os.getenv("ENUM_ENCODE", "1"))

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class SpaceheatNodeGt(BaseModel):
    """
    Spaceheat Node.

    A SpaceheatNode, or ShNode, is an organizing principal for the SCADA software. ShNodes can
    represent both underlying physical objects (water tank), measurements of these objects (temperature
    sensing at the top of a water tank), and actors within the code (an actor measuring multiple
    temperatures, or an actor responsible for filtering/smoothing temperature data for the purposes
    of thermostatic control). BIG CHANGES: Alias -> Name. The Property Format changes from LeftRightDot
    to SpaceheatNode. Remove Role. (Require numerous changes, in both code and hardware layout.)
    MEDIUM CHANGE: Remove ReportingSamplePeriodS. (Requires change for SimpleSensor). Smaller
    changes include removing NameplatePowerW, RatedVoltageV.

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/spaceheat-node.html)
    """

    name: str = Field(
        title="Name",
        description=(
            "Human readable immutable identifier. alpha-numeric words, first wording starting "
            "with an alphabet character, separated by hyphens. No dots."
        ),
    )
    actor_hierarchy_name: Optional[str] = Field(
        title="ActorHierarchy",
        description=(
            "This shows the parent-child chain of responsibility for ShNodes that are actors. "
            "For example, if h.aquastat-ctrl-relay is the ActorHierarchy, then the actor whose "
            "ActorHierarchyName is `h` is responsible for spawning, monitoring, killing and restarting "
            "this actor."
        ),
        default=None,
    )
    handle: Optional[str] = Field(
        title="Handle",
        description=(
            "Word structure shows Terminal Asset Finite State Machine hierarchy. Locally unique, "
            "but mutable. If there is a dot, then the predecessor handle (handle with the final "
            "word removed) is the handle for the 'boss' node. Only nodes with actors that can "
            "take actions that change the state of the Terminal Asset have dots in their handles. "
            "For example, the analog temperature sensor in the LocalName description above does "
            "NOT take actions and its handle would likely be analog-temp. If a node's actor CAN "
            "take actions that change the state of the TerminalAsset, it only takes commands "
            "from its boss node. For example, a relay actor will only agree to energize or de-energize "
            "its relay as a result of a command from its (current) boss."
        ),
        default=None,
    )
    actor_class: ActorClass = Field(
        title="Actor Class",
        description="Used to select the actor's code.",
    )
    display_name: Optional[str] = Field(
        title="Display Name",
        description="For user interfaces that don't want to show the local name or handle.",
        default=None,
    )
    component_id: Optional[str] = Field(
        title="Unique identifier for Spaceheat Node's Component",
        description="Used if a Spaceheat Node is associated with a physical device.",
        default=None,
    )
    nameplate_power_w: Optional[int] = Field(
        title="NameplatePowerW",
        description="The nameplate power of the Spaceheat Node.",
        default=None,
    )
    in_power_metering: Optional[bool] = Field(
        title="In Power Metering",
        description=(
            "This exists and is True if the SpaceheatNode is part of the power metering that "
            "is used for market participation. Small loads like circulator pumps and fans may "
            "be metered to determine their behavior but are are likely NOT part of the power "
            "metering used for market participation."
        ),
        default=None,
    )
    sh_node_id: str = Field(
        title="Id",
        description=(
            "Immutable identifier for one of the Spaceheat Nodes of a Terminal Asset. Globally "
            "unique - i.e. across all Space Heat Nodes for all Terminal Assets."
        ),
    )
    type_name: Literal["spaceheat.node.gt"] = "spaceheat.node.gt"
    version: Literal["200"] = "200"
    model_config = ConfigDict(
        extra="allow", populate_by_name=True, alias_generator=snake_to_pascal
    )

    @field_validator("name")
    @classmethod
    def _check_name(cls, v: str) -> str:
        try:
            check_is_spaceheat_name(v)
        except ValueError as e:
            raise ValueError(f"Name failed SpaceheatName format validation: {e}") from e
        return v

    @field_validator("actor_hierarchy_name")
    @classmethod
    def _check_actor_hierarchy_name(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        try:
            check_is_handle_name(v)
        except ValueError as e:
            raise ValueError(
                f"ActorHierarchyName failed HandleName format validation: {e}",
            ) from e
        return v

    @field_validator("handle")
    @classmethod
    def _check_handle(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        try:
            check_is_handle_name(v)
        except ValueError as e:
            raise ValueError(f"Handle failed HandleName format validation: {e}") from e
        return v

    @field_validator("sh_node_id")
    @classmethod
    def _check_sh_node_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"ShNodeId failed UuidCanonicalTextual format validation: {e}",
            ) from e
        return v

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: InPowerMetering requirements.
        If InPowerMetering exists and is true, then NameplatePowerW must exist
        """
        if self.in_power_metering:
            if self.nameplate_power_w is None:
                raise ValueError(
                    "If InPowerMetering exists, then NameplatePowerW must also exist!"
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
        d["ActorClass"] = d["ActorClass"].value
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
        del d["ActorClass"]
        d["ActorClassGtEnumSymbol"] = ActorClass.value_to_symbol(self.actor_class)
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the spaceheat.node.gt.200 representation designed to send in a message.

        Recursively encodes enums as hard-to-remember 8-digit random hex symbols
        unless settings.encode_enums is set to 0.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class SpaceheatNodeGtMaker:
    type_name = "spaceheat.node.gt"
    version = "200"

    @classmethod
    def tuple_to_type(cls, tuple: SpaceheatNodeGt) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> SpaceheatNodeGt:
        """
        Given the bytes in a message, returns the corresponding class object.

        Args:
            b (bytes): candidate type instance

        Raises:
           GwTypeError: if the bytes are not a spaceheat.node.gt.200 type

        Returns:
            SpaceheatNodeGt instance
        """
        try:
            d = json.loads(b)
        except TypeError as e:
            raise GwTypeError("Type must be string or bytes!") from e
        if not isinstance(d, dict):
            raise GwTypeError(f"Deserializing  must result in dict!\n <{b}>")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> SpaceheatNodeGt:
        """
        Translates a dict representation of a spaceheat.node.gt.200 message object
        into the Python class object.
        """
        for key in d.keys():
            if not is_pascal_case(key):
                raise GwTypeError(f"Key '{key}' is not PascalCase")
        d2 = dict(d)
        if "Name" not in d2.keys():
            raise GwTypeError(f"dict missing Name: <{d2}>")
        if "ActorClassGtEnumSymbol" in d2.keys():
            value = ActorClass.symbol_to_value(d2["ActorClassGtEnumSymbol"])
            d2["ActorClass"] = ActorClass(value)
            del d2["ActorClassGtEnumSymbol"]
        elif "ActorClass" in d2.keys():
            if d2["ActorClass"] not in ActorClass.values():
                d2["ActorClass"] = ActorClass.default()
            else:
                d2["ActorClass"] = ActorClass(d2["ActorClass"])
        else:
            raise GwTypeError(
                f"both ActorClassGtEnumSymbol and ActorClass missing from dict <{d2}>",
            )
        if "ShNodeId" not in d2.keys():
            raise GwTypeError(f"dict missing ShNodeId: <{d2}>")
        if "TypeName" not in d2.keys():
            raise GwTypeError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise GwTypeError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "200":
            LOGGER.debug(
                f"Attempting to interpret spaceheat.node.gt version {d2['Version']} as version 200"
            )
            d2["Version"] = "200"
        d3 = {pascal_to_snake(key): value for key, value in d2.items()}
        return SpaceheatNodeGt(**d3)

    @classmethod
    def tuple_to_dc(cls, t: SpaceheatNodeGt) -> ShNode:
        if t.sh_node_id in ShNode.by_id.keys():
            dc = ShNode.by_id[t.sh_node_id]
        else:
            dc = ShNode(
                name=t.name,
                actor_hierarchy_name=t.actor_hierarchy_name,
                handle=t.handle,
                actor_class=t.actor_class,
                display_name=t.display_name,
                component_id=t.component_id,
                nameplate_power_w=t.nameplate_power_w,
                in_power_metering=t.in_power_metering,
                sh_node_id=t.sh_node_id,
            )
        return dc

    @classmethod
    def dc_to_tuple(cls, dc: ShNode) -> SpaceheatNodeGt:
        return SpaceheatNodeGt(
            name=dc.name,
            actor_hierarchy_name=dc.actor_hierarchy_name,
            handle=dc.handle,
            actor_class=dc.actor_class,
            display_name=dc.display_name,
            component_id=dc.component_id,
            nameplate_power_w=dc.nameplate_power_w,
            in_power_metering=dc.in_power_metering,
            sh_node_id=dc.sh_node_id,
        )

    @classmethod
    def type_to_dc(cls, t: str) -> ShNode:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: ShNode) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> ShNode:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))


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


def check_is_handle_name(v: str) -> None:
    """Check HandleName Format.

    Validates if the provided string adheres to the HandleName format:
    words separated by periods, where the worlds are lowercase alphanumeric plus hyphens

    Args:
        candidate (str): The string to be validated.

    Raises:
        ValueError: If the provided string is not in HandleName format.
    """
    try:
        x = v.split(".")
    except Exception as e:
        raise ValueError(f"Failed to seperate <{v}> into words with split'.'") from e
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(
            f"Most significant word of <{v}> must start with alphabet char."
        )
    for word in x:
        for char in word:
            if not (char.isalnum() or char == "-"):
                raise ValueError(
                    f"words of <{v}> split by by '.' must be alphanumeric or hyphen."
                )
    if not v.islower():
        raise ValueError(f"<{v}> must be lowercase.")


def check_is_uuid_canonical_textual(v: str) -> None:
    """Checks UuidCanonicalTextual format

    UuidCanonicalTextual format:  A string of hex words separated by hyphens
    of length 8-4-4-4-12.

    Args:
        v (str): the candidate

    Raises:
        ValueError: if v is not UuidCanonicalTextual format
    """
    phi_fun_check_it_out = 5
    two_cubed_too_cute = 8
    bachets_fun_four = 4
    the_sublime_twelve = 12
    try:
        x = v.split("-")
    except AttributeError as e:
        raise ValueError(f"Failed to split on -: {e}") from e
    if len(x) != phi_fun_check_it_out:
        raise ValueError(f"<{v}> split by '-' did not have 5 words")
    for hex_word in x:
        try:
            int(hex_word, 16)
        except ValueError as e:
            raise ValueError(f"Words of <{v}> are not all hex") from e
    if len(x[0]) != two_cubed_too_cute:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[1]) != bachets_fun_four:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[2]) != bachets_fun_four:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[3]) != bachets_fun_four:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[4]) != the_sublime_twelve:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
