import json
import typing
from typing import Any
from typing import Literal

from gwproto.data_classes.cacs.fibaro_tank_temp_sensor_cac import (
    FibaroTankTempSensorCac,
)
from gwproto.data_classes.component_attribute_class import ComponentAttributeClass
from gwproto.types.rest_poller_cac_gt import RESTPollerCacGt


class FibaroTankTempSensorCacGt(RESTPollerCacGt):
    TypeName: Literal[
        "fibaro.tank.temp.sensor.cac.gt"
    ] = "fibaro.tank.temp.sensor.cac.gt"
    Version: str = "000"

    @classmethod
    def from_data_class(
        cls, cac: FibaroTankTempSensorCac
    ) -> "FibaroTankTempSensorCacGt":
        return FibaroTankTempSensorCacGt(
            ComponentAttributeClassId=cac.component_attribute_class_id,
            DisplayName=cac.display_name,
        )

    def to_data_class(self) -> FibaroTankTempSensorCac:
        cac = ComponentAttributeClass.by_id.get(self.ComponentAttributeClassId, None)
        if cac is not None:
            return typing.cast(FibaroTankTempSensorCac, cac)
        return FibaroTankTempSensorCac(
            component_attribute_class_id=self.ComponentAttributeClassId,
            display_name=self.DisplayName,
        )

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))


class FibaroTankTempSensorCacGt_Maker:
    type_name: str = FibaroTankTempSensorCacGt.__fields__["TypeName"].default
    version = "000"
    tuple: FibaroTankTempSensorCacGt

    def __init__(self, cac: FibaroTankTempSensorCac):
        self.tuple = FibaroTankTempSensorCacGt.from_data_class(cac)

    @classmethod
    def tuple_to_type(cls, tpl: FibaroTankTempSensorCacGt) -> str:
        return tpl.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> FibaroTankTempSensorCacGt:
        return cls.dict_to_tuple(json.loads(t))

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> FibaroTankTempSensorCacGt:
        return FibaroTankTempSensorCacGt(**d)

    @classmethod
    def tuple_to_dc(cls, t: FibaroTankTempSensorCacGt) -> FibaroTankTempSensorCac:
        return t.to_data_class()

    @classmethod
    def dc_to_tuple(cls, dc: FibaroTankTempSensorCac) -> FibaroTankTempSensorCacGt:
        return FibaroTankTempSensorCacGt.from_data_class(dc)

    @classmethod
    def type_to_dc(cls, t: str) -> FibaroTankTempSensorCac:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: FibaroTankTempSensorCac) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> FibaroTankTempSensorCac:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
