"""Type i2c.flow.totalizer.component.gt, version 000"""

import json
import logging
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import root_validator
from pydantic import validator

from gwproto.data_classes.components.i2c_flow_totalizer_component import (
    I2cFlowTotalizerComponent,
)
from gwproto.enums import MakeModel
from gwproto.errors import SchemaError
from gwproto.types.channel_config import ChannelConfig
from gwproto.types.channel_config import ChannelConfig_Maker


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)

CONVERSION_FACTOR_BY_MODEL: Dict[MakeModel, float] = {
    MakeModel.ISTEC_4440: 0.268132,
    MakeModel.OMEGA__FTB8007HWPT: 0.134066,
    MakeModel.OMEGA__FTB8010HWPT: 1.34066,
    MakeModel.PRMFILTRATION__WM075: 1.34066,
    MakeModel.EKM__HOTSPWM075HD: 0.08322,
}


class I2cFlowTotalizerComponentGt(BaseModel):
    """
    I2C Flow Totalizer Component.

    A specific instance of a component with multiple chips that integrate pulse count flow meters and reports the result
    as I2C, with a single totalizer component per i2c address.
    """

    ComponentId: str = Field(
        title="Component Id",
        description=(
            "Primary GridWorks identifier for a specific physical instance of a PipeFlowSensor, "
            "and also as a more generic Component."
        ),
    )
    ComponentAttributeClassId: str = Field(
        title="ComponentAttributeClass",
        description=(
            "Unique identifier for the device class. Authority for these, as well as the relationship "
            "between Components and ComponentAttributeClasses (Cacs) is maintained by the World "
            "Registry."
        ),
    )
    I2cAddressList: List[int] = Field(
        title="I2cAddress",
        description=(
            "The list of I2cAddresses on the I2cBus. The assumption is each i2c address is reading "
            "from one Pulse Flow Meter."
        ),
    )
    ConfigList: List[ChannelConfig] = Field(
        title="Config List",
        description="A list of the ChannelConfigs for the data channels reported by this actor.",
    )
    PulseFlowMeterMakeModelList: List[MakeModel] = Field(
        title="Pulse Flow Meter MakeModel",
        description="The list of MakeModels of the pulse flow meters getting read.",
    )
    ConversionFactorList: List[float] = Field(
        title="ConversionFactor",
        description=(
            "The factor that the cumulative output must be multiplied by in order to read gallons."
        ),
    )
    DisplayName: Optional[str] = Field(
        title="Display Name",
        description="Sample: Pipe Flow Meter Component <dist-flow>",
        default=None,
    )
    HwUid: Optional[str] = Field(
        title="Hardware Unique Id",
        default=None,
    )
    TypeName: Literal["i2c.flow.totalizer.component.gt"] = (
        "i2c.flow.totalizer.component.gt"
    )
    Version: Literal["000"] = "000"

    @validator("ComponentId")
    def _check_component_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"ComponentId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("ComponentAttributeClassId")
    def _check_component_attribute_class_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"ComponentAttributeClassId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @root_validator
    def check_axiom_1(cls, v: dict) -> dict:
        """
        Axiom 1: I2cAddressList, PulseFlowMeterMakeModel, ConversionFactorList Consistency.
        All three lists must have the same length.

        For the nth PulseFlowMeterMakeModel and ConversionFactor:
        If the PulseFlowMeterMakeModel m is a key in the dict CONVERSION_FACTOR_BY_MODEL, then
                the ConversionFactor must be CONVERSION_FACTOR_BY_MODEL[m]

                CONVERSION_FACTOR_BY_MODEL: Dict[MakeModel, float] = {
                                    MakeModel.ISTEC_4440: 0.268132,
                                    MakeModel.OMEGA__FTB8007HWPT: 0.134066,
                                    MakeModel.OMEGA__FTB8010HWPT: 1.34066,
                                    MakeModel.PRMFILTRATION__WM075: 1.34066,
                                    MakeModel.EKM__HOTSPWM075HD: 0.08322,
                                }
        """
        if (
            "I2cAddressList" not in v.keys()
            or "PulseFlowMeterMakeModelList" not in v.keys()
            or "ConversionFactorList" not in v.keys()
        ):
            raise ValueError(f"Missing keys: {v.keys()}")
        i2c_address_list = v["I2cAddressList"]
        model_list = v["PulseFlowMeterMakeModelList"]
        cf_list = v["ConversionFactorList"]
        if len(i2c_address_list) != len(set(i2c_address_list)):
            raise Exception("Axiom 1 violated: duplicate i2c addresses")
        if len(i2c_address_list) != len(model_list):
            raise Exception(
                "Axiom 1 violated: I2cAddressList and PulseFlowMeterMakeModel List must be the same length!"
            )
        if len(i2c_address_list) != len(cf_list):
            raise Exception(
                "Axiom 1 violated: I2cAddressList and ConversionFactorList List must be the same length!"
            )

        for i in range(len(model_list)):
            model = model_list[i]
            cf = cf_list[i]
            if model in CONVERSION_FACTOR_BY_MODEL.keys():
                if cf != CONVERSION_FACTOR_BY_MODEL[model]:
                    raise ValueError(
                        f"Axiom 1 violated! Conversion factor for {model} must "
                        f"be CONVERSION_FACTOR_BY_MODEL[{model}] = {cf}"
                    )
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        i2c.flow.totalizer.component.gt.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        i2c.flow.totalizer.component.gt.000 type. Unlike the standard python dict method,
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
        # Recursively calling as_dict()
        config_list = []
        for elt in self.ConfigList:
            config_list.append(elt.as_dict())
        d["ConfigList"] = config_list
        del d["PulseFlowMeterMakeModelList"]
        pulse_flow_meter_make_model_list = []
        for elt in self.PulseFlowMeterMakeModelList:
            pulse_flow_meter_make_model_list.append(
                MakeModel.value_to_symbol(elt.value)
            )
        d["PulseFlowMeterMakeModelList"] = pulse_flow_meter_make_model_list
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the i2c.flow.totalizer.component.gt.000 representation.

        Instances in the class are python-native representations of i2c.flow.totalizer.component.gt.000
        objects, while the actual i2c.flow.totalizer.component.gt.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is I2cFlowTotalizerComponentGt.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class I2cFlowTotalizerComponentGt_Maker:
    type_name = "i2c.flow.totalizer.component.gt"
    version = "000"

    @classmethod
    def tuple_to_type(cls, tuple: I2cFlowTotalizerComponentGt) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> I2cFlowTotalizerComponentGt:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> I2cFlowTotalizerComponentGt:
        """
        Deserialize a dictionary representation of a i2c.flow.totalizer.component.gt.000 message object
        into a I2cFlowTotalizerComponentGt python object for internal use.

        This is the near-inverse of the I2cFlowTotalizerComponentGt.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a I2cFlowTotalizerComponentGt object.

        Returns:
            I2cFlowTotalizerComponentGt
        """
        d2 = dict(d)
        if "ComponentId" not in d2.keys():
            raise SchemaError(f"dict missing ComponentId: <{d2}>")
        if "ComponentAttributeClassId" not in d2.keys():
            raise SchemaError(f"dict missing ComponentAttributeClass: <{d2}>")
        if "I2cAddressList" not in d2.keys():
            raise SchemaError(f"dict missing I2cAddressList: <{d2}>")
        if "ConfigList" not in d2.keys():
            raise SchemaError(f"dict missing ConfigList: <{d2}>")
        if not isinstance(d2["ConfigList"], List):
            raise SchemaError(f"ConfigList <{d2['ConfigList']}> must be a List!")
        config_list = []
        for elt in d2["ConfigList"]:
            if not isinstance(elt, dict):
                raise SchemaError(
                    f"ConfigList <{d2['ConfigList']}> must be a List of ChannelConfig types"
                )
            t = ChannelConfig_Maker.dict_to_tuple(elt)
            config_list.append(t)
        d2["ConfigList"] = config_list
        if "PulseFlowMeterMakeModelList" not in d2.keys():
            raise SchemaError(f"dict <{d2}> missing PulseFlowMeterMakeModelList")
        if not isinstance(d2["PulseFlowMeterMakeModelList"], List):
            raise SchemaError("PulseFlowMeterMakeModelList must be a List!")
        pulse_flow_meter_make_model_list = []
        for elt in d2["PulseFlowMeterMakeModelList"]:
            value = MakeModel.symbol_to_value(elt)
            pulse_flow_meter_make_model_list.append(MakeModel(value))
        d2["PulseFlowMeterMakeModelList"] = pulse_flow_meter_make_model_list
        if "ConversionFactorList" not in d2.keys():
            raise SchemaError(f"dict missing ConversionFactorList: <{d2}>")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret i2c.flow.totalizer.component.gt version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return I2cFlowTotalizerComponentGt(**d2)

    @classmethod
    def tuple_to_dc(cls, t: I2cFlowTotalizerComponentGt) -> I2cFlowTotalizerComponent:
        if t.ComponentId in I2cFlowTotalizerComponent.by_id.keys():
            dc = I2cFlowTotalizerComponent.by_id[t.ComponentId]
        else:
            dc = I2cFlowTotalizerComponent(
                component_id=t.ComponentId,
                component_attribute_class_id=t.ComponentAttributeClassId,
                i2c_address_list=t.I2cAddressList,
                config_list=t.ConfigList,
                pulse_flow_meter_make_model_list=t.PulseFlowMeterMakeModelList,
                conversion_factor_list=t.ConversionFactorList,
                display_name=t.DisplayName,
                hw_uid=t.HwUid,
            )
        return dc

    @classmethod
    def dc_to_tuple(cls, dc: I2cFlowTotalizerComponent) -> I2cFlowTotalizerComponentGt:
        return I2cFlowTotalizerComponentGt(
            ComponentId=dc.component_id,
            ComponentAttributeClassId=dc.component_attribute_class_id,
            I2cAddressList=dc.i2c_address_list,
            ConfigList=dc.config_list,
            PulseFlowMeterMakeModelList=dc.pulse_flow_meter_make_model_list,
            ConversionFactorList=dc.conversion_factor_list,
            DisplayName=dc.display_name,
            HwUid=dc.hw_uid,
        )

    @classmethod
    def type_to_dc(cls, t: str) -> I2cFlowTotalizerComponent:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: I2cFlowTotalizerComponent) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> I2cFlowTotalizerComponent:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))


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
