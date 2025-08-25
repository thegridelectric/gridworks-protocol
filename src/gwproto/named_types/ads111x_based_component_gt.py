"""Type ads111x.based.component.gt, version 000"""

from typing import Literal

from pydantic import ConfigDict, model_validator
from typing_extensions import Self

from gwproto.named_types.ads_channel_config import AdsChannelConfig
from gwproto.named_types.component_gt import ComponentGt
from gwproto.property_format import (
    check_is_near5,
)


class Ads111xBasedComponentGt(ComponentGt):
    """ASL schema of record [ads111x.based.component.gt v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/ads111x.based.component.gt.000.yaml)"""

    open_voltage_by_ads: list[float]
    config_list: list[AdsChannelConfig]
    type_name: Literal["ads111x.based.component.gt"] = "ads111x.based.component.gt"
    version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")

    @model_validator(mode="after")
    def _check_open_voltage_by_ads(self) -> Self:
        try:
            for elt in self.open_voltage_by_ads:
                check_is_near5(elt)
        except ValueError as e:
            raise ValueError(
                f"OpenVoltageByAds element failed Near5 format validation: {e}",
            ) from e
        return self

    @model_validator(mode="after")
    def check_config_list(self) -> Self:
        """
            Axiom 1: Terminal Block consistency and Channel Name uniqueness..
            Terminal Block consistency and Channel Name uniqueness. - Each TerminalBlockIdx occurs at
        most once in the ThermistorConfigList - Each data channel occurs at most once in the ThermistorConfigList
        """
        # Implement Axiom(s)
        return self
