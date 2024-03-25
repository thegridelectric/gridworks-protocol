"""Type spaceheat.node.gt, version 200"""
import json
import logging
from typing import Any
from typing import Dict
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import root_validator
from pydantic import validator

from gwproto.data_classes.sh_node import ShNode
from pydantic import Extra
from gwproto.enums import ActorClass as EnumActorClass
from gwproto.errors import SchemaError


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

    ShNodeId: str = Field(
        title="Id",
        description=(
            "Immutable identifier for one of the Spaceheat Nodes of a Terminal Asset. Globally "
            "unique - i.e. across all Space Heat Nodes for all Terminal Assets."
        ),
    )
    Name: str = Field(
        title="Name",
        description=(
            "Most human readable locally unique identifier. Immutable. Words (separated by dots) "
            "shows actor startup hierarchy. That is, if the node 's.analog-temp' has an actor, "
            "then that actor is spawned by node 's'."
        ),
    )
    Handle: Optional[str] = Field(
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
    ActorClass: EnumActorClass = Field(
        title="Actor Class",
        description="Used to select the actor's code.",
    )
    DisplayName: Optional[str] = Field(
        title="Display Name",
        description="For user interfaces that don't want to show the local name or handle.",
        default=None,
    )
    ComponentId: Optional[str] = Field(
        title="Unique identifier for Spaceheat Node's Component",
        description="Used if a Spaceheat Node is associated with a physical device.",
        default=None,
    )
    InPowerMetering: Optional[bool] = Field(
        title="In Power Metering",
        description=(
            "This exists and is True if the SpaceheatNode is part of the power metering that "
            "is used for market participation. Small loads like circulator pumps and fans may "
            "be metered to determine their behavior but are are likely NOT part of the power "
            "metering used for market participation."
        ),
        default=None,
    )
    TypeName: Literal["spaceheat.node.gt"] = "spaceheat.node.gt"
    Version: Literal["200"] = "200"

    class Config:
        extra = Extra.allow

    @validator("ShNodeId")
    def _check_sh_node_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"ShNodeId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("Name")
    def _check_name(cls, v: str) -> str:
        try:
            check_is_spaceheat_name(v)
        except ValueError as e:
            raise ValueError(f"Name failed SpaceheatName format validation: {e}")
        return v

    @validator("Handle")
    def _check_handle(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        try:
            check_is_spaceheat_name(v)
        except ValueError as e:
            raise ValueError(f"Handle failed SpaceheatName format validation: {e}")
        return v

    @root_validator
    def check_axiom_1(cls, v: dict) -> dict:
        """
        Axiom 1: InPowerMetering requirements.
        If InPowerMetering exists and is true, then NameplatePowerW and RatedVoltageV must both exist
        """
        # TODO: Implement check for axiom 1"
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        spaceheat.node.gt.200 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        spaceheat.node.gt.200 type. Unlike the standard python dict method,
        it makes the following substantive changes:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.
        """
        d = {
            key: value
            for key, value in self.dict(
                include=self.__fields_set__ | {"TypeName", "Version"}
            ).items()
            if value is not None
        }
        del d["ActorClass"]
        d["ActorClassGtEnumSymbol"] = EnumActorClass.value_to_symbol(self.ActorClass)
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the spaceheat.node.gt.200 representation.

        Instances in the class are python-native representations of spaceheat.node.gt.200
        objects, while the actual spaceheat.node.gt.200 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is SpaceheatNodeGt.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class SpaceheatNodeGt_Maker:
    type_name = "spaceheat.node.gt"
    version = "200"

    @classmethod
    def tuple_to_type(cls, tuple: SpaceheatNodeGt) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> SpaceheatNodeGt:
        """
        Given a serialized JSON type object, returns the Python class object.
        """
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing <{t}> must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> SpaceheatNodeGt:
        """
        Deserialize a dictionary representation of a spaceheat.node.gt.200 message object
        into a SpaceheatNodeGt python object for internal use.

        This is the near-inverse of the SpaceheatNodeGt.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a SpaceheatNodeGt object.

        Returns:
            SpaceheatNodeGt
        """
        d2 = dict(d)
        if "ShNodeId" not in d2.keys():
            raise SchemaError(f"dict missing ShNodeId: <{d2}>")
        if "Name" not in d2.keys():
            raise SchemaError(f"dict missing Name: <{d2}>")
        if "ActorClassGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"ActorClassGtEnumSymbol missing from dict <{d2}>")
        value = EnumActorClass.symbol_to_value(d2["ActorClassGtEnumSymbol"])
        d2["ActorClass"] = EnumActorClass(value)
        del d2["ActorClassGtEnumSymbol"]
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "200":
            LOGGER.debug(
                f"Attempting to interpret spaceheat.node.gt version {d2['Version']} as version 200"
            )
            d2["Version"] = "200"
        return SpaceheatNodeGt(**d2)

    @classmethod
    def tuple_to_dc(cls, t: SpaceheatNodeGt) -> ShNode:
        if t.ShNodeId in ShNode.by_id.keys():
            dc = ShNode.by_id[t.ShNodeId]
        else:
            dc = ShNode(
                sh_node_id=t.ShNodeId,
                name=t.Name,
                handle=t.Handle,
                actor_class=t.ActorClass,
                display_name=t.DisplayName,
                component_id=t.ComponentId,
                in_power_metering=t.InPowerMetering,
            )
        return dc

    @classmethod
    def dc_to_tuple(cls, dc: ShNode) -> SpaceheatNodeGt:
        return SpaceheatNodeGt(
            ShNodeId=dc.sh_node_id,
            Name=dc.name,
            Handle=dc.handle,
            ActorClass=dc.actor_class,
            DisplayName=dc.display_name,
            ComponentId=dc.component_id,
            InPowerMetering=dc.in_power_metering,
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
    Lowercase words separated by periods, where word characters can be alphanumeric
    or a hyphen, and the first word starts with an alphabet character.

    Args:
        candidate (str): The string to be validated.

    Raises:
        ValueError: If the provided string is not in SpaceheatName format.
    """
    from typing import List

    try:
        x: List[str] = v.split(".")
    except:
        raise ValueError(f"Failed to seperate <{v}> into words with split'.'")
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
    try:
        x = v.split("-")
    except AttributeError as e:
        raise ValueError(f"Failed to split on -: {e}")
    if len(x) != 5:
        raise ValueError(f"<{v}> split by '-' did not have 5 words")
    for hex_word in x:
        try:
            int(hex_word, 16)
        except ValueError:
            raise ValueError(f"Words of <{v}> are not all hex")
    if len(x[0]) != 8:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[1]) != 4:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[2]) != 4:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[3]) != 4:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[4]) != 12:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
