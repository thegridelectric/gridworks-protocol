"""Type component.attribute.class.gt, version 001"""
import json
import logging
from typing import Any
from typing import Dict
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import Extra
from pydantic import Field
from pydantic import root_validator
from pydantic import validator
from gwproto.data_classes.component_attribute_class import ComponentAttributeClass
from gwproto.enums import MakeModel as EnumMakeModel
from gwproto.errors import SchemaError

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


CACS_BY_MAKE_MODEL: Dict[EnumMakeModel, str] = {
        EnumMakeModel.EGAUGE__4030: "739a6e32-bb9c-43bc-a28d-fb61be665522",
        EnumMakeModel.NCD__PR814SPST: "c6e736d8-8078-44f5-98bb-d72ca91dc773",
        EnumMakeModel.ADAFRUIT__642: "43564cd2-0e78-41a2-8b67-ad80c02161e8",
        EnumMakeModel.GRIDWORKS__WATERTEMPHIGHPRECISION: "7937eb7e-24d5-4d52-990f-cca063484df9",
        EnumMakeModel.GRIDWORKS__SIMPM1: "28897ac1-ea42-4633-96d3-196f63f5a951",
        EnumMakeModel.SCHNEIDERELECTRIC__IEM3455: "6bcdc388-de10-40e6-979a-8d66bfcfe9ba",
        EnumMakeModel.GRIDWORKS__SIMBOOL30AMPRELAY: "69f101fc-22e4-4caa-8103-50b8aeb66028",
        EnumMakeModel.OPENENERGY__EMONPI: "357b9b4f-2550-4380-aa6b-d2cd9c7ba0f9",
        EnumMakeModel.GRIDWORKS__SIMTSNAP1: "b9f7135e-07a9-42f8-b847-a9bb3ea3770a",
        EnumMakeModel.ATLAS__EZFLO: "13d916dc-8764-4b16-b85d-b8ead3e2fc80",
        EnumMakeModel.HUBITAT__C7__LAN1: "62528da5-b510-4ac2-82c1-3782842eae07",
        EnumMakeModel.GRIDWORKS__TANK_MODULE_1: "60ac199d-679a-49f7-9142-8ca3e6428a5f",
        EnumMakeModel.FIBARO__ANALOG_TEMP_SENSOR: "7ce0ce69-14c6-4cb7-a33f-2aeca91e0680",
        EnumMakeModel.AMPHENOL__NTC_10K_THERMISTOR_MA100GG103BN: "2821c81d-054d-4003-9b07-2c295aef40f5",
        EnumMakeModel.YHDC__SCT013100: "812761ba-6544-4796-9aad-e1c979f58734",
        EnumMakeModel.MAGNELAB__SCT0300050: "cf312bd6-7ca5-403b-a61b-b2e817ea1e22",
        EnumMakeModel.GRIDWORKS__MULTITEMP1: "432073b8-4d2b-4e36-9229-73893f33f846",
        EnumMakeModel.KRIDA__EMR16I2CV3: "018d9ffb-89d1-4cc4-95c0-f170711b5ffa",
        EnumMakeModel.OMEGA__FTB8007HWPT: "8cf6c726-e38a-4900-9cfe-ae6f053aafdf",
        EnumMakeModel.ISTEC_4440: "62ed724c-ba62-4302-ae30-d52b20d42ad9",
        EnumMakeModel.OMEGA__FTB8010HWPT: "d9f225f8-eeb5-4cb7-b314-5551b925ea27",
        EnumMakeModel.BELIMO__BALLVALVE232VS: "a2236d8c-7c9b-403f-9c55-733c62971d09",
        EnumMakeModel.BELIMO__DIVERTERB332L: "f3261ed0-3fb1-4def-b60b-246960bf85ef",
        EnumMakeModel.TACO__0034EPLUS: "3880ba73-61e5-4b35-9df1-e154a03a3335",
        EnumMakeModel.TACO__007E: "198ebac8-e0b9-4cee-ae91-2ee6db708491",
        EnumMakeModel.ARMSTRONG__COMPASSH: "ff6863e1-d5f7-4066-8579-2768162321a6",
        EnumMakeModel.HONEYWELL__T6ZWAVETHERMOSTAT: "03533a1f-3cb9-4a1f-8d57-690c0ad0475b",
        EnumMakeModel.PRMFILTRATION__WM075: "61d5c12d-eeca-4835-9a11-e61167d82e0d",
        EnumMakeModel.BELLGOSSETT__ECOCIRC20_18: "0d2ccc36-d2b8-405d-a257-3917111607c5",
        EnumMakeModel.TEWA__TT0P10KC3T1051500: "20779dbb-0302-4c36-9d60-e1962857c2f3",
        EnumMakeModel.EKM__HOTSPWM075HD: "e52cb571-913a-4614-90f4-5cc81f8e7fe5"
    }

class ComponentAttributeClassGt(BaseModel):
    """
    Component Attribute Class Gt.

    Authority for the attributes of the component.attribute.class.gt.000 belongs to the WorldRegistry.
    The WorldRegistry is part of the GridWorks 'BackOffice' structure for managing relational
    device data. Generally speaking, a component attribute class is meant to specify WHAT you
    might order from a plumbing supply store to 'get the same part.' The Component refers to
    something that will have a specific serial number. Add optional MakeModel and MinPollPeriodMs;
    allow extra.

    [More info](https://g-node-registry.readthedocs.io/en/latest/component-attribute-class.html)
    """

    ComponentAttributeClassId: str = Field(
        title="ComponentAttributeClassId",
        description=(
            "Unique identifier for the device class (aka 'cac' or Component Attribute Class). "
            "This identifier is used to associate a make/model with a specific component (i.e. "
            "the component will point to its ComponentAttributeClassId)."
        ),
    )
    MakeModel: EnumMakeModel = Field(
        title="MakeModel",
        description="MakeModel of the component.",
    )
    DisplayName: Optional[str] = Field(
        title="DisplayName",
        description=(
            "Optional Mutable field to include manufacturer's model name. Note that several different "
            "models may be given the same spaceheat.make.model enum name."
        ),
        default=None,
    )
    MinPollPeriodMs: Optional[int] = Field(
        title="Min Poll Period Ms",
        description="The minimum amount of time between polls of this device.",
        default=None,
    )
    TypeName: Literal["component.attribute.class.gt"] = "component.attribute.class.gt"
    Version: Literal["001"] = "001"

    class Config:
        extra = Extra.allow

    @validator("ComponentAttributeClassId")
    def _check_component_attribute_class_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"ComponentAttributeClassId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("MinPollPeriodMs")
    def _check_min_poll_period_ms(cls, v: Optional[int]) -> Optional[int]:
        if v is None:
            return v
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"MinPollPeriodMs failed PositiveInteger format validation: {e}"
            )
        return v

    @root_validator
    def check_axiom_(cls, v: dict) -> dict:
        """
        Axiom : Component Attribute Classes captured by spaceheat.make.model v 002.
        If cac is a ComponentAttributeClassGt of type 001, 
        then 
           - EITHER  its (MakeModel, ComponentAttributeClassId) must be a key,value pair in
        CACS_BY_MAKE_MODEL (below)
           - XOR its MakeModel is MakeModel.UNKNOWNMAKE__UNKNOWNMODEL

        CACS_BY_MAKE_MODEL: Dict[MakeModel, str] = {
                MakeModel.EGAUGE__4030: "739a6e32-bb9c-43bc-a28d-fb61be665522",
                MakeModel.NCD__PR814SPST: "c6e736d8-8078-44f5-98bb-d72ca91dc773",
                MakeModel.ADAFRUIT__642: "43564cd2-0e78-41a2-8b67-ad80c02161e8",
                MakeModel.GRIDWORKS__WATERTEMPHIGHPRECISION: "7937eb7e-24d5-4d52-990f-cca063484df9",
                MakeModel.GRIDWORKS__SIMPM1: "28897ac1-ea42-4633-96d3-196f63f5a951",
                MakeModel.SCHNEIDERELECTRIC__IEM3455: "6bcdc388-de10-40e6-979a-8d66bfcfe9ba",
                MakeModel.GRIDWORKS__SIMBOOL30AMPRELAY: "69f101fc-22e4-4caa-8103-50b8aeb66028",
                MakeModel.OPENENERGY__EMONPI: "357b9b4f-2550-4380-aa6b-d2cd9c7ba0f9",
                MakeModel.GRIDWORKS__SIMTSNAP1: "b9f7135e-07a9-42f8-b847-a9bb3ea3770a",
                MakeModel.ATLAS__EZFLO: "13d916dc-8764-4b16-b85d-b8ead3e2fc80",
                MakeModel.HUBITAT__C7__LAN1: "62528da5-b510-4ac2-82c1-3782842eae07",
                MakeModel.GRIDWORKS__TANK_MODULE_1: "60ac199d-679a-49f7-9142-8ca3e6428a5f",
                MakeModel.FIBARO__ANALOG_TEMP_SENSOR: "7ce0ce69-14c6-4cb7-a33f-2aeca91e0680",
                MakeModel.AMPHENOL__NTC_10K_THERMISTOR_MA100GG103BN: "2821c81d-054d-4003-9b07-2c295aef40f5",
                MakeModel.YHDC__SCT013100: "812761ba-6544-4796-9aad-e1c979f58734",
                MakeModel.MAGNELAB__SCT0300050: "cf312bd6-7ca5-403b-a61b-b2e817ea1e22",
                MakeModel.GRIDWORKS__MULTITEMP1: "432073b8-4d2b-4e36-9229-73893f33f846",
                MakeModel.KRIDA__EMR16I2CV3: "018d9ffb-89d1-4cc4-95c0-f170711b5ffa",
                MakeModel.OMEGA__FTB8007HWPT: "8cf6c726-e38a-4900-9cfe-ae6f053aafdf",
                MakeModel.ISTEC_4440: "62ed724c-ba62-4302-ae30-d52b20d42ad9",
                MakeModel.OMEGA__FTB8010HWPT: "d9f225f8-eeb5-4cb7-b314-5551b925ea27",
                MakeModel.BELIMO__BALLVALVE232VS: "a2236d8c-7c9b-403f-9c55-733c62971d09",
                MakeModel.BELIMO__DIVERTERB332L: "f3261ed0-3fb1-4def-b60b-246960bf85ef",
                MakeModel.TACO__0034EPLUS: "3880ba73-61e5-4b35-9df1-e154a03a3335",
                MakeModel.TACO__007E: "198ebac8-e0b9-4cee-ae91-2ee6db708491",
                MakeModel.ARMSTRONG__COMPASSH: "ff6863e1-d5f7-4066-8579-2768162321a6",
                MakeModel.HONEYWELL__T6ZWAVETHERMOSTAT: "03533a1f-3cb9-4a1f-8d57-690c0ad0475b",
                MakeModel.PRMFILTRATION__WM075: "61d5c12d-eeca-4835-9a11-e61167d82e0d",
                MakeModel.BELLGOSSETT__ECOCIRC20_18: "0d2ccc36-d2b8-405d-a257-3917111607c5",
                MakeModel.TEWA__TT0P10KC3T1051500: "20779dbb-0302-4c36-9d60-e1962857c2f3",
                MakeModel.EKM__HOTSPWM075HD: "e52cb571-913a-4614-90f4-5cc81f8e7fe5"
            }
        """
        if "ComponentAttributeClassId" not in v.keys() or "MakeModel" not in v.keys():
            raise ValueError(f"Missing keys!")
        id = v["ComponentAttributeClassId"]
        model = v["MakeModel"]
        if model == EnumMakeModel.UNKNOWNMAKE__UNKNOWNMODEL:
            if id in CACS_BY_MAKE_MODEL.values():
                correct_model = next(key for key, value in CACS_BY_MAKE_MODEL.items() if value == id)
                raise ValueError(f"cac id <{id}> is for MakeModel <{correct_model.value}>, "
                                 "not UNKNOWNMAKE__UNKNOWNMODEL")
        else:
            if model not in CACS_BY_MAKE_MODEL.keys():
                raise ValueError(f"model <{model}> must be in CACS_BY_MAKE_MODEL: \n"
                                f"{CACS_BY_MAKE_MODEL}")
            if id != CACS_BY_MAKE_MODEL[model]:
                raise ValueError(f"There can only be one cac with MakeModel <{model}> "
                                f" and it has id <{CACS_BY_MAKE_MODEL[model]}>, NOT {id}")
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        component.attribute.class.gt.001 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        component.attribute.class.gt.001 type. Unlike the standard python dict method,
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
        Serialize to the component.attribute.class.gt.001 representation.

        Instances in the class are python-native representations of component.attribute.class.gt.001
        objects, while the actual component.attribute.class.gt.001 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is ComponentAttributeClassGt.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class ComponentAttributeClassGt_Maker:
    type_name = "component.attribute.class.gt"
    version = "001"

    def __init__(
        self,
        component_attribute_class_id: str,
        make_model: EnumMakeModel,
        display_name: Optional[str],
        min_poll_period_ms: Optional[int],
    ):
        self.tuple = ComponentAttributeClassGt(
            ComponentAttributeClassId=component_attribute_class_id,
            MakeModel=make_model,
            DisplayName=display_name,
            MinPollPeriodMs=min_poll_period_ms,
        )

    @classmethod
    def tuple_to_type(cls, tuple: ComponentAttributeClassGt) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> ComponentAttributeClassGt:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> ComponentAttributeClassGt:
        """
        Deserialize a dictionary representation of a component.attribute.class.gt.001 message object
        into a ComponentAttributeClassGt python object for internal use.

        This is the near-inverse of the ComponentAttributeClassGt.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a ComponentAttributeClassGt object.

        Returns:
            ComponentAttributeClassGt
        """
        d2 = dict(d)
        if "ComponentAttributeClassId" not in d2.keys():
            raise SchemaError(f"dict missing ComponentAttributeClassId: <{d2}>")
        if "MakeModelGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"MakeModelGtEnumSymbol missing from dict <{d2}>")
        value = EnumMakeModel.symbol_to_value(d2["MakeModelGtEnumSymbol"])
        d2["MakeModel"] = EnumMakeModel(value)
        del d2["MakeModelGtEnumSymbol"]
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "001":
            LOGGER.debug(
                f"Attempting to interpret component.attribute.class.gt version {d2['Version']} as version 001"
            )
            d2["Version"] = "001"
        return ComponentAttributeClassGt(**d2)

    @classmethod
    def tuple_to_dc(cls, t: ComponentAttributeClassGt) -> ComponentAttributeClass:
        if t.ComponentAttributeClassId in ComponentAttributeClass.by_id.keys():
            dc = ComponentAttributeClass.by_id[t.ComponentAttributeClassId]
        else:
            dc = ComponentAttributeClass(
                component_attribute_class_id=t.ComponentAttributeClassId,
                make_model=t.MakeModel,
                display_name=t.DisplayName,
                min_poll_period_ms=t.MinPollPeriodMs,
            )
        return dc

    @classmethod
    def dc_to_tuple(cls, dc: ComponentAttributeClass) -> ComponentAttributeClassGt:
        t = ComponentAttributeClassGt_Maker(
            component_attribute_class_id=dc.component_attribute_class_id,
            make_model=dc.make_model,
            display_name=dc.display_name,
            min_poll_period_ms=dc.min_poll_period_ms,
        ).tuple
        return t

    @classmethod
    def type_to_dc(cls, t: str) -> ComponentAttributeClass:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: ComponentAttributeClass) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> ComponentAttributeClass:
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
