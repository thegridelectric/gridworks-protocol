"""Type i2c.multichannel.dt.relay.component.gt, version 000"""
import json
import logging
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gwproto.data_classes.components.i2c_multichannel_dt_relay_component import (
    I2cMultichannelDtRelayComponent,
)
from gwproto.errors import SchemaError


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class I2cMultichannelDtRelayComponentGt(BaseModel):
    """
    I2c Multichannel Double Throw Relay Component.

    A specific instance of a board with multiple double-throw electromechanical relays. The
    board is expected to be addressable over i2c, with that address being configurable to a
    finite number of choices via dipswitches.
    """

    TypeName: Literal[
        "i2c.multichannel.dt.relay.component.gt"
    ] = "i2c.multichannel.dt.relay.component.gt"
    Version: Literal["000"] = "000"

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        i2c.multichannel.dt.relay.component.gt.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        i2c.multichannel.dt.relay.component.gt.000 type. Unlike the standard python dict method,
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
        Serialize to the i2c.multichannel.dt.relay.component.gt.000 representation.

        Instances in the class are python-native representations of i2c.multichannel.dt.relay.component.gt.000
        objects, while the actual i2c.multichannel.dt.relay.component.gt.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is I2cMultichannelDtRelayComponentGt.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class I2cMultichannelDtRelayComponentGt_Maker:
    type_name = "i2c.multichannel.dt.relay.component.gt"
    version = "000"

    def __init__(
        self,
    ):
        self.tuple = I2cMultichannelDtRelayComponentGt()

    @classmethod
    def tuple_to_type(cls, tuple: I2cMultichannelDtRelayComponentGt) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> I2cMultichannelDtRelayComponentGt:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> I2cMultichannelDtRelayComponentGt:
        """
        Deserialize a dictionary representation of a i2c.multichannel.dt.relay.component.gt.000 message object
        into a I2cMultichannelDtRelayComponentGt python object for internal use.

        This is the near-inverse of the I2cMultichannelDtRelayComponentGt.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a I2cMultichannelDtRelayComponentGt object.

        Returns:
            I2cMultichannelDtRelayComponentGt
        """
        d2 = dict(d)
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret i2c.multichannel.dt.relay.component.gt version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return I2cMultichannelDtRelayComponentGt(**d2)

    @classmethod
    def tuple_to_dc(
        cls, t: I2cMultichannelDtRelayComponentGt
    ) -> I2cMultichannelDtRelayComponent:
        if t.ComponentId in I2cMultichannelDtRelayComponent.by_id.keys():
            dc = I2cMultichannelDtRelayComponent.by_id[t.ComponentId]
        else:
            dc = I2cMultichannelDtRelayComponent()
        return dc

    @classmethod
    def dc_to_tuple(
        cls, dc: I2cMultichannelDtRelayComponent
    ) -> I2cMultichannelDtRelayComponentGt:
        t = I2cMultichannelDtRelayComponentGt_Maker().tuple
        return t

    @classmethod
    def type_to_dc(cls, t: str) -> I2cMultichannelDtRelayComponent:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: I2cMultichannelDtRelayComponent) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> I2cMultichannelDtRelayComponent:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
