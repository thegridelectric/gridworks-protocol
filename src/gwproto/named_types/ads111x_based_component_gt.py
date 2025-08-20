"""Type ads111x.based.component.gt, version 000"""

from typing import Literal, Optional

from gw.named_types import GwBase
from pydantic import ConfigDict, model_validator
from typing_extensions import Self

from gwproto.named_types.ads_channel_config import AdsChannelConfig
from gwproto.named_types.channel_config import ChannelConfig
from gwproto.property_format import (
    UUID4Str,
    check_is_near5,
)


class Ads111xBasedComponentGt(GwBase):
    """
    TI ADS111x Based Temp Sensing Component.

    Designed for specific instances of a temp sensor based on the Texas Instrument ADS111X series
    of chips used w 10K thermistors for reading temperature.

    [More info](https://drive.google.com/drive/u/0/folders/1oFvs4-kvwyzt220eYlFnwdzEgVCIbbt6)
    """

    component_id: UUID4Str
    component_attribute_class_id: UUID4Str
    display_name: Optional[str] = None
    open_voltage_by_ads: list[float]
    config_list: list[ChannelConfig]
    thermistor_config_list: list[AdsChannelConfig]
    hw_uid: Optional[str] = None
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
    def check_thermistor_config_list(self) -> Self:
        """
            Axiom 1: Terminal Block consistency and Channel Name uniqueness..
            Terminal Block consistency and Channel Name uniqueness. - Each TerminalBlockIdx occurs at
        most once in the ThermistorConfigList - Each data channel occurs at most once in the ThermistorConfigList
        """
        # Implement Axiom(s)
        return self
