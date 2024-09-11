"""SCADA Component Class Definition"""

from typing import Generic, TypeVar

from pydantic import BaseModel

from gwproto.types import ComponentAttributeClassGt, ComponentGt

ComponentT = TypeVar("ComponentT", bound=ComponentGt)
CacT = TypeVar("CacT", bound=ComponentAttributeClassGt)


class Component(BaseModel, Generic[ComponentT, CacT]):
    gt: ComponentT
    cac: CacT

    def __repr__(self) -> str:
        return f"<{self.gt.DisplayName}>  ({self.cac.MakeModel.value})"


class ComponentOnly(Component[ComponentGt, Component]): ...
