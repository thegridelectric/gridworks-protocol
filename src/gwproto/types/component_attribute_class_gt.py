"""Type component.attribute.class.gt, version 001"""

import json
import logging
import os
from typing import Any, Dict, Literal, Optional

import dotenv
from gw.errors import GwTypeError
from gw.utils import is_pascal_case, pascal_to_snake, snake_to_pascal
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from typing_extensions import Self

from gwproto.data_classes.component_attribute_class import ComponentAttributeClass
from gwproto.enums import MakeModel
from gwproto.type_helpers import CACS_BY_MAKE_MODEL

dotenv.load_dotenv()

ENCODE_ENUMS = int(os.getenv("ENUM_ENCODE", "1"))

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


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

    component_attribute_class_id: str = Field(
        title="ComponentAttributeClassId",
        description=(
            "Unique identifier for the device class (aka 'cac' or Component Attribute Class). "
            "This identifier is used to associate a make/model with a specific component (i.e. "
            "the component will point to its ComponentAttributeClassId)."
        ),
    )
    make_model: MakeModel = Field(
        title="MakeModel",
        description="MakeModel of the component.",
    )
    display_name: Optional[str] = Field(
        title="DisplayName",
        description=(
            "Optional Mutable field to include manufacturer's model name. Note that several different "
            "models may be given the same spaceheat.make.model enum name."
        ),
        default=None,
    )
    min_poll_period_ms: Optional[int] = Field(
        title="Min Poll Period Ms",
        description="The minimum amount of time between polls of this device.",
        default=None,
    )
    type_name: Literal["component.attribute.class.gt"] = "component.attribute.class.gt"
    version: Literal["001"] = "001"
    model_config = ConfigDict(
        extra="allow", populate_by_name=True, alias_generator=snake_to_pascal
    )

    @field_validator("component_attribute_class_id")
    @classmethod
    def _check_component_attribute_class_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"ComponentAttributeClassId failed UuidCanonicalTextual format validation: {e}",
            ) from e
        return v

    @field_validator("min_poll_period_ms")
    @classmethod
    def _check_min_poll_period_ms(cls, v: Optional[int]) -> Optional[int]:
        if v is None:
            return v
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"MinPollPeriodMs failed PositiveInteger format validation: {e}",
            ) from e
        return v

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: Component Attribute Classes captured by spaceheat.make.model v 002.
        If cac is a ComponentAttributeClassGt of type 001,
        then
           - EITHER  its (MakeModel, ComponentAttributeClassId) must be a key,value pair in
        CACS_BY_MAKE_MODEL (below)
           - XOR its MakeModel is MakeModel.UNKNOWNMAKE__UNKNOWNMODEL

        CACS_BY_MAKE_MODEL: Dict[MakeModel, str] = {
            MakeModel.EGAUGE__4030: '739a6e32-bb9c-43bc-a28d-fb61be665522',
            MakeModel.NCD__PR814SPST: 'c6e736d8-8078-44f5-98bb-d72ca91dc773',
            MakeModel.ADAFRUIT__642: '43564cd2-0e78-41a2-8b67-ad80c02161e8',
            MakeModel.GRIDWORKS__WATERTEMPHIGHPRECISION: '7937eb7e-24d5-4d52-990f-cca063484df9',
            MakeModel.GRIDWORKS__SIMPM1: '28897ac1-ea42-4633-96d3-196f63f5a951',
            MakeModel.SCHNEIDERELECTRIC__IEM3455: '6bcdc388-de10-40e6-979a-8d66bfcfe9ba',
            MakeModel.GRIDWORKS__SIMBOOL30AMPRELAY: '69f101fc-22e4-4caa-8103-50b8aeb66028',
            MakeModel.OPENENERGY__EMONPI: '357b9b4f-2550-4380-aa6b-d2cd9c7ba0f9',
            MakeModel.GRIDWORKS__SIMTSNAP1: 'b9f7135e-07a9-42f8-b847-a9bb3ea3770a',
            MakeModel.ATLAS__EZFLO: '13d916dc-8764-4b16-b85d-b8ead3e2fc80',
            MakeModel.HUBITAT__C7__LAN1: '62528da5-b510-4ac2-82c1-3782842eae07',
            MakeModel.GRIDWORKS__TANK_MODULE_1: '60ac199d-679a-49f7-9142-8ca3e6428a5f',
            MakeModel.FIBARO__ANALOG_TEMP_SENSOR: '7ce0ce69-14c6-4cb7-a33f-2aeca91e0680',
            MakeModel.AMPHENOL__NTC_10K_THERMISTOR_MA100GG103BN: '2821c81d-054d-4003-9b07-2c295aef40f5',
            MakeModel.YHDC__SCT013100: '812761ba-6544-4796-9aad-e1c979f58734',
            MakeModel.MAGNELAB__SCT0300050: 'cf312bd6-7ca5-403b-a61b-b2e817ea1e22',
            MakeModel.GRIDWORKS__MULTITEMP1: '432073b8-4d2b-4e36-9229-73893f33f846',
            MakeModel.KRIDA__EMR16I2CV3: '018d9ffb-89d1-4cc4-95c0-f170711b5ffa',
            MakeModel.OMEGA__FTB8007HWPT: '8cf6c726-e38a-4900-9cfe-ae6f053aafdf',
            MakeModel.ISTEC_4440: '62ed724c-ba62-4302-ae30-d52b20d42ad9',
            MakeModel.OMEGA__FTB8010HWPT: 'd9f225f8-eeb5-4cb7-b314-5551b925ea27',
            MakeModel.BELIMO__BALLVALVE232VS: 'a2236d8c-7c9b-403f-9c55-733c62971d09',
            MakeModel.BELIMO__DIVERTERB332L: 'f3261ed0-3fb1-4def-b60b-246960bf85ef',
            MakeModel.TACO__0034EPLUS: '3880ba73-61e5-4b35-9df1-e154a03a3335',
            MakeModel.TACO__007E: '198ebac8-e0b9-4cee-ae91-2ee6db708491',
            MakeModel.ARMSTRONG__COMPASSH: 'ff6863e1-d5f7-4066-8579-2768162321a6',
            MakeModel.HONEYWELL__T6ZWAVETHERMOSTAT: '03533a1f-3cb9-4a1f-8d57-690c0ad0475b',
            MakeModel.PRMFILTRATION__WM075: '61d5c12d-eeca-4835-9a11-e61167d82e0d',
            MakeModel.BELLGOSSETT__ECOCIRC20_18: '0d2ccc36-d2b8-405d-a257-3917111607c5',
            MakeModel.TEWA__TT0P10KC3T1051500: '20779dbb-0302-4c36-9d60-e1962857c2f3',
            MakeModel.EKM__HOTSPWM075HD: 'e52cb571-913a-4614-90f4-5cc81f8e7fe5',
            MakeModel.GRIDWORKS__SIMMULTITEMP: '627ac482-24fe-46b2-ba8c-3d6f1e1ee069',
            MakeModel.GRIDWORKS__SIMTOTALIZER: 'a88f8f4c-fe1e-4645-a7f4-249912131dc8',
            MakeModel.KRIDA__DOUBLEEMR16I2CV3: '29eab8b1-100f-4230-bb44-3a2fcba33cc3'.
        }
        """
        if self.make_model == MakeModel.UNKNOWNMAKE__UNKNOWNMODEL:
            return self

        if self.make_model.value not in CACS_BY_MAKE_MODEL.keys():
            raise GwTypeError(
                f"self.make_model must be unknown or in CACS_BY_MAKE_MODEL.keys(). Got {self.make_model}"
            )

        if CACS_BY_MAKE_MODEL[self.make_model] != self.component_attribute_class_id:
            raise ValueError(
                "Violates Axiom 1: (MakeModel, ComponentAttributeClassId) must be a"
                f"key,value pair in CACS_BY_MAKE_MODEL: <{self.make_model}, {self.component_attribute_class_id}>"
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
        d["MakeModel"] = d["MakeModel"].value
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
        del d["MakeModel"]
        d["MakeModelGtEnumSymbol"] = MakeModel.value_to_symbol(self.make_model)
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the component.attribute.class.gt.001 representation designed to send in a message.

        Recursively encodes enums as hard-to-remember 8-digit random hex symbols
        unless settings.encode_enums is set to 0.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class ComponentAttributeClassGtMaker:
    type_name = "component.attribute.class.gt"
    version = "001"

    @classmethod
    def tuple_to_type(cls, tuple: ComponentAttributeClassGt) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> ComponentAttributeClassGt:
        """
        Given the bytes in a message, returns the corresponding class object.

        Args:
            b (bytes): candidate type instance

        Raises:
           GwTypeError: if the bytes are not a component.attribute.class.gt.001 type

        Returns:
            ComponentAttributeClassGt instance
        """
        try:
            d = json.loads(b)
        except TypeError as e:
            raise GwTypeError("Type must be string or bytes!") from e
        if not isinstance(d, dict):
            raise GwTypeError(f"Deserializing  must result in dict!\n <{b}>")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> ComponentAttributeClassGt:
        """
        Translates a dict representation of a component.attribute.class.gt.001 message object
        into the Python class object.
        """
        for key in d.keys():
            if not is_pascal_case(key):
                raise GwTypeError(f"Key '{key}' is not PascalCase")
        d2 = dict(d)
        if "ComponentAttributeClassId" not in d2.keys():
            raise GwTypeError(f"dict missing ComponentAttributeClassId: <{d2}>")
        if "MakeModelGtEnumSymbol" in d2.keys():
            value = MakeModel.symbol_to_value(d2["MakeModelGtEnumSymbol"])
            d2["MakeModel"] = MakeModel(value)
            del d2["MakeModelGtEnumSymbol"]
        elif "MakeModel" in d2.keys():
            if d2["MakeModel"] not in MakeModel.values():
                d2["MakeModel"] = MakeModel.default()
            else:
                d2["MakeModel"] = MakeModel(d2["MakeModel"])
        else:
            raise GwTypeError(
                f"both MakeModelGtEnumSymbol and MakeModel missing from dict <{d2}>",
            )
        if "TypeName" not in d2.keys():
            raise GwTypeError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise GwTypeError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "001":
            LOGGER.debug(
                f"Attempting to interpret component.attribute.class.gt version {d2['Version']} as version 001"
            )
            d2["Version"] = "001"
        d3 = {pascal_to_snake(key): value for key, value in d2.items()}
        return ComponentAttributeClassGt(**d3)

    @classmethod
    def tuple_to_dc(cls, t: ComponentAttributeClassGt) -> ComponentAttributeClass:
        if t.component_attribute_class_id in ComponentAttributeClass.by_id.keys():
            dc = ComponentAttributeClass.by_id[t.component_attribute_class_id]
        else:
            dc = ComponentAttributeClass(
                component_attribute_class_id=t.component_attribute_class_id,
                make_model=t.make_model,
                display_name=t.display_name,
                min_poll_period_ms=t.min_poll_period_ms,
            )
        return dc

    @classmethod
    def dc_to_tuple(cls, dc: ComponentAttributeClass) -> ComponentAttributeClassGt:
        return ComponentAttributeClassGt(
            component_attribute_class_id=dc.component_attribute_class_id,
            make_model=dc.make_model,
            display_name=dc.display_name,
            min_poll_period_ms=dc.min_poll_period_ms,
        )

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
