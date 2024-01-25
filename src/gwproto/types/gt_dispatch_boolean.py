"""Type gt.dispatch.boolean, version 111"""
import json
import logging
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gwproto.errors import SchemaError


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class GtDispatchBoolean(BaseModel):
    """
    GridWorks Type Boolean Dispatch.

    Boolean dispatch command designed to be sent from an AtomicTNode to a SCADA.
    """

    ToGNodeAlias: str = Field(
        title="GNodeAlias of the SCADA",
        description="[More info](https://gridworks.readthedocs.io/en/latest/scada.html)",
    )
    FromGNodeAlias: str = Field(
        title="GNodeAlias of AtomicTNode",
        description="[More info](https://gridworks.readthedocs.io/en/latest/atomic-t-node.html)",
    )
    FromGNodeInstanceId: str = Field(
        title="GNodeInstance of the AtomicTNode",
    )
    AboutNodeName: str = Field(
        title="About Node Name",
        description="The name of the Spaceheat Node that the dispatch request is for.",
    )
    RelayState: int = Field(
        title="Relay State (0 or 1)",
        description=(
            "This is not applicable for double-throw relays that do anything other than open "
            "or close a circuit. A Relay State of `0` indicates the relay is OPEN (off). A Relay "
            "State of `1` indicates the relay is CLOSED (on). Note that `0` means the relay is "
            "open whether or not the relay is normally open or normally closed (For a normally "
            "open relay, the relay is ENERGIZED when it is in state `0` and DE-ENERGIZED when "
            "it is in state `1`.)"
            "[More info](https://gridworks.readthedocs.io/en/latest/relay-state.html)"
        ),
    )
    SendTimeUnixMs: int = Field(
        title="Time the AtomicTNode sends the dispatch, by its clock",
    )
    TypeName: Literal["gt.dispatch.boolean"] = "gt.dispatch.boolean"
    Version: Literal["111"] = "111"

    @validator("ToGNodeAlias")
    def _check_to_g_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(f"ToGNodeAlias failed LeftRightDot format validation: {e}")
        return v

    @validator("FromGNodeAlias")
    def _check_from_g_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(
                f"FromGNodeAlias failed LeftRightDot format validation: {e}"
            )
        return v

    @validator("FromGNodeInstanceId")
    def _check_from_g_node_instance_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"FromGNodeInstanceId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("AboutNodeName")
    def _check_about_node_name(cls, v: str) -> str:
        try:
            check_is_spaceheat_name(v)
        except ValueError as e:
            raise ValueError(
                f"AboutNodeName failed SpaceheatName format validation: {e}"
            )
        return v

    @validator("RelayState", pre=True)
    def _check_relay_state(cls, v: int) -> int:
        try:
            check_is_bit(v)
        except ValueError as e:
            raise ValueError(f"RelayState failed Bit format validation: {e}")
        return v

    @validator("SendTimeUnixMs")
    def _check_send_time_unix_ms(cls, v: int) -> int:
        try:
            check_is_reasonable_unix_time_ms(v)
        except ValueError as e:
            raise ValueError(
                f"SendTimeUnixMs failed ReasonableUnixTimeMs format validation: {e}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        gt.dispatch.boolean.111 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        gt.dispatch.boolean.111 type. Unlike the standard python dict method,
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
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the gt.dispatch.boolean.111 representation.

        Instances in the class are python-native representations of gt.dispatch.boolean.111
        objects, while the actual gt.dispatch.boolean.111 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is GtDispatchBoolean.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class GtDispatchBoolean_Maker:
    type_name = "gt.dispatch.boolean"
    version = "111"

    def __init__(
        self,
        to_g_node_alias: str,
        from_g_node_alias: str,
        from_g_node_instance_id: str,
        about_node_name: str,
        relay_state: int,
        send_time_unix_ms: int,
    ):
        self.tuple = GtDispatchBoolean(
            ToGNodeAlias=to_g_node_alias,
            FromGNodeAlias=from_g_node_alias,
            FromGNodeInstanceId=from_g_node_instance_id,
            AboutNodeName=about_node_name,
            RelayState=relay_state,
            SendTimeUnixMs=send_time_unix_ms,
        )

    @classmethod
    def tuple_to_type(cls, tuple: GtDispatchBoolean) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> GtDispatchBoolean:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> GtDispatchBoolean:
        """
        Deserialize a dictionary representation of a gt.dispatch.boolean.111 message object
        into a GtDispatchBoolean python object for internal use.

        This is the near-inverse of the GtDispatchBoolean.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a GtDispatchBoolean object.

        Returns:
            GtDispatchBoolean
        """
        d2 = dict(d)
        if "ToGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict missing ToGNodeAlias: <{d2}>")
        if "FromGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict missing FromGNodeAlias: <{d2}>")
        if "FromGNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict missing FromGNodeInstanceId: <{d2}>")
        if "AboutNodeName" not in d2.keys():
            raise SchemaError(f"dict missing AboutNodeName: <{d2}>")
        if "RelayState" not in d2.keys():
            raise SchemaError(f"dict missing RelayState: <{d2}>")
        if "SendTimeUnixMs" not in d2.keys():
            raise SchemaError(f"dict missing SendTimeUnixMs: <{d2}>")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "111":
            LOGGER.debug(
                f"Attempting to interpret gt.dispatch.boolean version {d2['Version']} as version 111"
            )
            d2["Version"] = "111"
        return GtDispatchBoolean(**d2)
