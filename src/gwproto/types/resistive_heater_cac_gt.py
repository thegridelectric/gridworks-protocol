"""Type resistive.heater.cac.gt, version 000"""

import json
import logging
from typing import Any
from typing import Dict
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gwproto.data_classes.cacs.resistive_heater_cac import ResistiveHeaterCac
from gwproto.enums import MakeModel as EnumMakeModel
from gwproto.errors import SchemaError


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class ResistiveHeaterCacGt(BaseModel):
    """
    Type for tracking Resistive Heater ComponentAttributeClasses.

    GridWorks Spaceheat SCADA uses the GridWorks GNodeRegistry structures and abstractions for
    managing relational device data. The Cac, or ComponentAttributeClass, is part of this structure.

    [More info](https://g-node-registry.readthedocs.io/en/latest/component-attribute-class.html)
    """

    ComponentAttributeClassId: str = Field(
        title="ComponentAttributeClassId",
        description=(
            "Unique identifier for the device class (aka 'cac' or Component Attribute Class). "
            "Authority is maintained by the World Registry."
        ),
    )
    MakeModel: EnumMakeModel = Field(
        title="MakeModel",
    )
    DisplayName: Optional[str] = Field(
        title="DisplayName",
        default=None,
    )
    NameplateMaxPowerW: int = Field(
        title="NameplateMaxPowerW",
    )
    RatedVoltageV: int = Field(
        title="RatedVoltageV",
    )
    TypeName: Literal["resistive.heater.cac.gt"] = "resistive.heater.cac.gt"
    Version: Literal["000"] = "000"

    @validator("ComponentAttributeClassId")
    def _check_component_attribute_class_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"ComponentAttributeClassId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("RatedVoltageV")
    def _check_rated_voltage_v(cls, v: int) -> int:
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"RatedVoltageV failed PositiveInteger format validation: {e}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        resistive.heater.cac.gt.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        resistive.heater.cac.gt.000 type. Unlike the standard python dict method,
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
        del d["MakeModel"]
        d["MakeModelGtEnumSymbol"] = EnumMakeModel.value_to_symbol(self.MakeModel)
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the resistive.heater.cac.gt.000 representation.

        Instances in the class are python-native representations of resistive.heater.cac.gt.000
        objects, while the actual resistive.heater.cac.gt.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is ResistiveHeaterCacGt.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class ResistiveHeaterCacGt_Maker:
    type_name = "resistive.heater.cac.gt"
    version = "000"

    def __init__(
        self,
        component_attribute_class_id: str,
        make_model: EnumMakeModel,
        display_name: Optional[str],
        nameplate_max_power_w: int,
        rated_voltage_v: int,
    ):
        self.tuple = ResistiveHeaterCacGt(
            ComponentAttributeClassId=component_attribute_class_id,
            MakeModel=make_model,
            DisplayName=display_name,
            NameplateMaxPowerW=nameplate_max_power_w,
            RatedVoltageV=rated_voltage_v,
        )

    @classmethod
    def tuple_to_type(cls, tuple: ResistiveHeaterCacGt) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> ResistiveHeaterCacGt:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> ResistiveHeaterCacGt:
        """
        Deserialize a dictionary representation of a resistive.heater.cac.gt.000 message object
        into a ResistiveHeaterCacGt python object for internal use.

        This is the near-inverse of the ResistiveHeaterCacGt.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a ResistiveHeaterCacGt object.

        Returns:
            ResistiveHeaterCacGt
        """
        d2 = dict(d)
        if "ComponentAttributeClassId" not in d2.keys():
            raise SchemaError(f"dict missing ComponentAttributeClassId: <{d2}>")
        if "MakeModelGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"MakeModelGtEnumSymbol missing from dict <{d2}>")
        value = EnumMakeModel.symbol_to_value(d2["MakeModelGtEnumSymbol"])
        d2["MakeModel"] = EnumMakeModel(value)
        if "NameplateMaxPowerW" not in d2.keys():
            raise SchemaError(f"dict missing NameplateMaxPowerW: <{d2}>")
        if "RatedVoltageV" not in d2.keys():
            raise SchemaError(f"dict missing RatedVoltageV: <{d2}>")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret resistive.heater.cac.gt version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return ResistiveHeaterCacGt(**d2)

    @classmethod
    def tuple_to_dc(cls, t: ResistiveHeaterCacGt) -> ResistiveHeaterCac:
        if t.ComponentAttributeClassId in ResistiveHeaterCac.by_id.keys():
            dc = ResistiveHeaterCac.by_id[t.ComponentAttributeClassId]
        else:
            dc = ResistiveHeaterCac(
                component_attribute_class_id=t.ComponentAttributeClassId,
                make_model=t.MakeModel,
                display_name=t.DisplayName,
                nameplate_max_power_w=t.NameplateMaxPowerW,
                rated_voltage_v=t.RatedVoltageV,
            )
        return dc

    @classmethod
    def dc_to_tuple(cls, dc: ResistiveHeaterCac) -> ResistiveHeaterCacGt:
        t = ResistiveHeaterCacGt_Maker(
            component_attribute_class_id=dc.component_attribute_class_id,
            make_model=dc.make_model,
            display_name=dc.display_name,
            nameplate_max_power_w=dc.nameplate_max_power_w,
            rated_voltage_v=dc.rated_voltage_v,
        ).tuple
        return t

    @classmethod
    def type_to_dc(cls, t: str) -> ResistiveHeaterCac:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: ResistiveHeaterCac) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> ResistiveHeaterCac:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))


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
