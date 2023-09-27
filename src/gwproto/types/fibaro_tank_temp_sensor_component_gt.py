"""Code for actors that use a simple rest interaction, converting the response to one or more
REST commands into a message posted to main processing thread.

"""
import json
import typing
from typing import Any
from typing import Dict

from pydantic import validator

from gwproto.data_classes.component import Component
from gwproto.data_classes.components.fibaro_tank_temp_sensor_component import (
    FibaroTankTempSensorComponent,
)
from gwproto.data_classes.components.rest_poller_component import RESTPollerComponent
from gwproto.enums import TelemetryName as EnumTelemetryName
from gwproto.types.rest_poller_component_gt import RESTPollerComponentGt
from gwproto.types.simple_temp_sensor_cac_gt import TelemetryNameMap


class FibaroTankTempSensorComponentGt(RESTPollerComponentGt):
    Exponent: int
    TelemetryNameGtEnumSymbol: str
    TypeName: typing.Literal[
        "fibaro.tank.temp.sensor.component.gt"
    ] = "fibaro.tank.temp.sensor.component.gt"

    @validator("TelemetryNameGtEnumSymbol")
    def _check_telemetry_name_symbol(cls, v: str) -> str:
        if v not in TelemetryNameMap.type_to_versioned_enum_dict:
            v = TelemetryNameMap.local_to_type(EnumTelemetryName.default())
        return v

    @property
    def TelemetryName(self) -> EnumTelemetryName:
        return TelemetryNameMap.type_to_local(
            self.TelemetryNameGtEnumSymbol,
        )

    def as_dict(self) -> Dict[str, Any]:
        return self.dict(exclude_unset=True)

    def as_type(self) -> str:
        return json.dumps(self.as_dict())

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))

    @classmethod
    def from_data_class(
        cls, component: FibaroTankTempSensorComponent
    ) -> "FibaroTankTempSensorComponentGt":
        return FibaroTankTempSensorComponentGt(
            ComponentId=component.component_id,
            ComponentAttributeClassId=component.component_attribute_class_id,
            Exponent=component.exponent,
            TelemetryNameGtEnumSymbol=TelemetryNameMap.local_to_type(
                component.telemetry_name
            ),
            DisplayName=component.display_name,
            HwUid=component.hw_uid,
            Rest=component.rest,
        )

    def to_data_class(self) -> FibaroTankTempSensorComponent:
        component = Component.by_id.get(self.ComponentId, None)
        if component is not None:
            return typing.cast(FibaroTankTempSensorComponent, component)
        return FibaroTankTempSensorComponent(
            component_id=self.ComponentId,
            component_attribute_class_id=self.ComponentAttributeClassId,
            exponent=self.Exponent,
            telemetry_name=self.TelemetryName,
            rest=self.Rest,
            display_name=self.DisplayName,
            hw_uid=self.HwUid,
        )


class FibaroTankTempSensorComponentGt_Maker:
    type_name: str = FibaroTankTempSensorComponentGt.__fields__["TypeName"].default
    version = "000"
    tuple: FibaroTankTempSensorComponentGt

    def __init__(self, component: FibaroTankTempSensorComponent):
        self.tuple = FibaroTankTempSensorComponentGt.from_data_class(component)

    @classmethod
    def tuple_to_type(cls, tpl: FibaroTankTempSensorComponentGt) -> str:
        return tpl.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> FibaroTankTempSensorComponentGt:
        return cls.dict_to_tuple(json.loads(t))

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> FibaroTankTempSensorComponentGt:
        return FibaroTankTempSensorComponentGt(**d)

    @classmethod
    def tuple_to_dc(
        cls, t: FibaroTankTempSensorComponentGt
    ) -> FibaroTankTempSensorComponent:
        return t.to_data_class()

    @classmethod
    def dc_to_tuple(
        cls, dc: FibaroTankTempSensorComponent
    ) -> FibaroTankTempSensorComponentGt:
        return FibaroTankTempSensorComponentGt.from_data_class(dc)

    @classmethod
    def type_to_dc(cls, t: str) -> FibaroTankTempSensorComponent:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: FibaroTankTempSensorComponent) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> RESTPollerComponent:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
