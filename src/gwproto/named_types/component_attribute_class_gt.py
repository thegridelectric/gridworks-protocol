"""Type component.attribute.class.gt, version 001"""

from typing import Optional

from gw.named_types import GwBase
from pydantic import PositiveInt, model_validator
from typing_extensions import Self

from gwproto.enums import MakeModel
from gwproto.property_format import UUID4Str
from gwproto.type_helpers import CACS_BY_MAKE_MODEL


class ComponentAttributeClassGt(GwBase):
    component_attribute_class_id: UUID4Str
    display_name: Optional[str] = None
    make_model: MakeModel
    min_poll_period_ms: Optional[PositiveInt] = None
    type_name: str = "component.attribute.class.gt"
    version: str = "001"

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: Component Attribute Classes captured by MakeModel
                If cac is a ComponentAttributeClassGt,
        then
           - EITHER  its (MakeModel, ComponentAttributeClassId) must be a key,value pair in
        CACS_BY_MAKE_MODEL (below)
           - XOR its MakeModel is MakeModel.UNKNOWNMAKE__UNKNOWNMODEL
        """
        if (
            self.MakeModel not in CACS_BY_MAKE_MODEL
            and self.MakeModel is not MakeModel.default().value
        ):
            raise ValueError(
                "Axiom 1 violated! If MakeModel not in this list, "
                f"must be UNKNOWN: {CACS_BY_MAKE_MODEL}"
            )
        if self.MakeModel is MakeModel.default().value:
            if self.ComponentAttributeClassId in CACS_BY_MAKE_MODEL.values():
                raise ValueError(
                    f"Id {self.ComponentAttributeClassId} already used by known MakeModel!"
                )
        elif self.ComponentAttributeClassId != CACS_BY_MAKE_MODEL[self.MakeModel]:
            raise ValueError(
                f"Axiom 1 violated! MakeModel {self.MakeModel} must have "
                f"id {CACS_BY_MAKE_MODEL[self.MakeModel]}!"
            )
        return self
