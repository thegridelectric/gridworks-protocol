"""Type i2c.flow.totalizer.component.gt, version 000"""
import json
import logging
from typing import Any
from typing import Dict
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator
from gwproto.data_classes.components.i2c_flow_totalizer_component import I2cFlowTotalizerComponent
from gwproto.enums import MakeModel
from gwproto.errors import SchemaError

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class I2cFlowTotalizerComponentGt(BaseModel):
    """
    I2C Flow Totalizer Component.

    A specific instance of a chip that integates pulse count flow meters and reports the result
    as I2C.
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
    I2cAddress: int = Field(
        title="I2cAddress",
    )
    ConversionFactor: float = Field(
        title="ConversionFactor",
    )
    PulseFlowMeterType: MakeModel = Field(
        title="PulseFlowMeterType",
    )
    DisplayName: Optional[str] = Field(
        title="DisplayName",
        description="Sample: Pipe Flow Meter Component <dist-flow>",
        default=None,
    )
    HwUid: Optional[str] = Field(
        title="Hardware Unique Id",
        default=None,
    )
    TypeName: Literal["i2c.flow.totalizer.component.gt"] = "i2c.flow.totalizer.component.gt"
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
        del d["PulseFlowMeterType"]
        d["PulseFlowMeterTypeGtEnumSymbol"] = MakeModel.value_to_symbol(self.PulseFlowMeterType)
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

    def __init__(
        self,
        component_id: str,
        component_attribute_class_id: str,
        i2c_address: int,
        conversion_factor: float,
        pulse_flow_meter_type: MakeModel,
        display_name: Optional[str],
        hw_uid: Optional[str],
    ):
        self.tuple = I2cFlowTotalizerComponentGt(
            ComponentId=component_id,
            ComponentAttributeClassId=component_attribute_class_id,
            I2cAddress=i2c_address,
            ConversionFactor=conversion_factor,
            PulseFlowMeterType=pulse_flow_meter_type,
            DisplayName=display_name,
            HwUid=hw_uid,
        )

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
        if "I2cAddress" not in d2.keys():
            raise SchemaError(f"dict missing I2cAddress: <{d2}>")
        if "ConversionFactor" not in d2.keys():
            raise SchemaError(f"dict missing ConversionFactor: <{d2}>")
        if "PulseFlowMeterTypeGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"PulseFlowMeterTypeGtEnumSymbol missing from dict <{d2}>")
        value = MakeModel.symbol_to_value(d2["PulseFlowMeterTypeGtEnumSymbol"])
        d2["PulseFlowMeterType"] = MakeModel(value)
        del d2["PulseFlowMeterTypeGtEnumSymbol"]
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
                i2c_address=t.I2cAddress,
                conversion_factor=t.ConversionFactor,
                pulse_flow_meter_type=t.PulseFlowMeterType,
                display_name=t.DisplayName,
                hw_uid=t.HwUid,
            )
        return dc

    @classmethod
    def dc_to_tuple(cls, dc: I2cFlowTotalizerComponent) -> I2cFlowTotalizerComponentGt:
        t = I2cFlowTotalizerComponentGt_Maker(
            component_id=dc.component_id,
            component_attribute_class_id=dc.component_attribute_class_id,
            i2c_address=dc.i2c_address,
            conversion_factor=dc.conversion_factor,
            pulse_flow_meter_type=dc.pulse_flow_meter_type,
            display_name=dc.display_name,
            hw_uid=dc.hw_uid,
        ).tuple
        return t

    @classmethod
    def type_to_dc(cls, t: str) -> I2cFlowTotalizerComponent:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: I2cFlowTotalizerComponent) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> I2cFlowTotalizerComponent:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
