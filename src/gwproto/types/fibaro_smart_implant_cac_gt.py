import json
import typing
from typing import Any
from typing import Literal

from pydantic import UUID4
from pydantic import BaseModel
from pydantic import Extra
from pydantic import validator

from gwproto.data_classes.cacs.fibaro_smart_implant_cac import FibaroSmartImplantCac
from gwproto.data_classes.component_attribute_class import ComponentAttributeClass


class FibaroSmartImplantCacGt(BaseModel):
    ComponentAttributeClassId: str
    DisplayName: typing.Optional[str] = None
    Model: str = ""
    TypeName: Literal["fibaro.smart.implant.cac.gt"] = "fibaro.smart.implant.cac.gt"
    Version: str = "000"

    class Config:
        extra = Extra.allow

    @validator("ComponentAttributeClassId")
    def _check_component_attribute_class_id(cls, v: str) -> str:
        return str(UUID4(v))

    def as_dict(self) -> typing.Dict[str, Any]:
        return self.dict(exclude_unset=True)

    def as_type(self) -> str:
        return json.dumps(self.as_dict())

    @classmethod
    def from_data_class(cls, cac: FibaroSmartImplantCac) -> "FibaroSmartImplantCacGt":
        return FibaroSmartImplantCacGt(
            ComponentAttributeClassId=cac.component_attribute_class_id,
            DisplayName=cac.display_name,
        )

    def to_data_class(self) -> FibaroSmartImplantCac:
        cac = ComponentAttributeClass.by_id.get(self.ComponentAttributeClassId, None)
        if cac is not None:
            return typing.cast(FibaroSmartImplantCac, cac)
        return FibaroSmartImplantCac(
            component_attribute_class_id=self.ComponentAttributeClassId,
            display_name=self.DisplayName,
        )

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))


class FibaroSmartImplantCacGt_Maker:
    type_name: str = FibaroSmartImplantCacGt.__fields__["TypeName"].default
    version = "000"
    tuple: FibaroSmartImplantCacGt

    def __init__(self, cac: FibaroSmartImplantCac):
        self.tuple = FibaroSmartImplantCacGt.from_data_class(cac)

    @classmethod
    def tuple_to_type(cls, tpl: FibaroSmartImplantCacGt) -> str:
        return tpl.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> FibaroSmartImplantCacGt:
        return cls.dict_to_tuple(json.loads(t))

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> FibaroSmartImplantCacGt:
        return FibaroSmartImplantCacGt(**d)

    @classmethod
    def tuple_to_dc(cls, t: FibaroSmartImplantCacGt) -> FibaroSmartImplantCac:
        return t.to_data_class()

    @classmethod
    def dc_to_tuple(cls, dc: FibaroSmartImplantCac) -> FibaroSmartImplantCacGt:
        return FibaroSmartImplantCacGt.from_data_class(dc)

    @classmethod
    def type_to_dc(cls, t: str) -> FibaroSmartImplantCac:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: FibaroSmartImplantCac) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> FibaroSmartImplantCac:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
