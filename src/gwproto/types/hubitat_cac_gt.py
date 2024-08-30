import typing
from typing import Literal

from gwproto.data_classes.cacs.hubitat_cac import HubitatCac
from gwproto.data_classes.component_attribute_class import ComponentAttributeClass
from gwproto.types.component_attribute_class_gt import ComponentAttributeClassGt


class HubitatCacGt(ComponentAttributeClassGt):
    TypeName: Literal["hubitat.cac.gt"] = "hubitat.cac.gt"
    Version: Literal["000"] = "000"

    @classmethod
    def from_data_class(cls, cac: HubitatCac) -> "HubitatCacGt":
        return HubitatCacGt(
            ComponentAttributeClassId=cac.component_attribute_class_id,
            DisplayName=cac.display_name,
        )

    def to_data_class(self) -> HubitatCac:
        cac = ComponentAttributeClass.by_id.get(self.ComponentAttributeClassId, None)
        if cac is not None:
            return typing.cast(HubitatCac, cac)
        return HubitatCac(
            component_attribute_class_id=self.ComponentAttributeClassId,
            display_name=self.DisplayName,
        )

    def __hash__(self) -> int:
        return hash((type(self), *tuple(self.__dict__.values())))
