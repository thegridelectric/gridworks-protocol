"""Type resistive.heater.cac.gt, version 001"""

from typing import Literal

from pydantic import PositiveInt, StrictInt

from gwproto.named_types.component_attribute_class_gt import ComponentAttributeClassGt


class ResistiveHeaterCacGt(ComponentAttributeClassGt):
    """ASL schema of record [resistive.heater.cac.gt v001](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/resistive.heater.cac.gt.001.yaml)"""

    nameplate_max_power_w: StrictInt
    rated_voltage_v: PositiveInt
    type_name: Literal["resistive.heater.cac.gt"] = "resistive.heater.cac.gt"
    version: Literal["001"] = "001"
