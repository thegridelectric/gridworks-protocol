"""Type ads111x.based.component.gt, version 000"""

from typing import List, Literal

from pydantic import field_validator, model_validator
from typing_extensions import Self

from gwproto.property_format import (
    check_is_near5,
)
from gwproto.types.component_gt import ComponentGt
from gwproto.types.thermistor_data_processing_config import (
    ThermistorDataProcessingConfig,
)


class Ads111xBasedComponentGt(ComponentGt):
    OpenVoltageByAds: List[float]
    ThermistorConfigList: List[ThermistorDataProcessingConfig]
    TypeName: Literal["ads111x.based.component.gt"] = "ads111x.based.component.gt"
    Version: Literal["000"] = "000"

    @field_validator("OpenVoltageByAds")
    @classmethod
    def _check_open_voltage_by_ads(cls, v: List[float]) -> List[float]:
        try:
            for elt in v:
                check_is_near5(elt)
        except ValueError as e:
            raise ValueError(
                f"OpenVoltageByAds element failed Near5 format validation: {e}",
            ) from e
        return v

    @field_validator("ThermistorConfigList")
    @classmethod
    def check_thermistor_config_list(
        cls, v: List[ThermistorDataProcessingConfig]
    ) -> List[ThermistorDataProcessingConfig]:
        """
            Axiom 1: Terminal Block consistency and Channel Name uniqueness..
            Terminal Block consistency and Channel Name uniqueness. - Each TerminalBlockIdx occurs at
        most once in the ThermistorConfigList - Each data channel occurs at most once in the ThermistorConfigList
        """
        # Implement Axiom(s)
        return v

    @model_validator(mode="after")
    def check_axiom_2(self) -> Self:
        """
        Axiom 2: ThermistorConfig, ChannelConfig consistency.
        set(map(lambda x: x.ChannelName, ThermistorConfigList)) is equal to
        set(map(lambda x: x.ChannelName, ConfigList))
        """
        # Implement check for axiom 2"
        return self

    @classmethod
    def type_name_value(cls) -> str:
        return "ads111x.based.component.gt"
