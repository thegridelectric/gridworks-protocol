"""Type component.gt, version 001"""

from typing import Literal, Optional

from gw.named_types import GwBase
from pydantic import ConfigDict, model_validator
from typing_extensions import Self

from gwproto.named_types.channel_config import ChannelConfig
from gwproto.property_format import (
    UUID4Str,
)


class ComponentGt(GwBase):
    component_id: UUID4Str
    component_attribute_class_id: UUID4Str
    config_list: list[ChannelConfig]
    display_name: Optional[str] = None
    hw_uid: Optional[str] = None
    type_name: Literal["component.gt"] = "component.gt"
    version: Literal["001"] = "001"

    model_config = ConfigDict(extra="allow")

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: Channel Name Uniqueness.
        Data Channel names are unique in the config list
        """
        # Implement check for axiom 1"
        return self
