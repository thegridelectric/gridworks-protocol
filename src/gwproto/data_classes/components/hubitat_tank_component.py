from typing import Optional

import yarl

from gwproto.data_classes.component import Component
from gwproto.data_classes.component_attribute_class import ComponentAttributeClass as Cac

from gwproto.data_classes.resolver import ComponentResolver
from gwproto.data_classes.sh_node import ShNode
from gwproto.types.hubitat_component_gt import HubitatComponentGt
from gwproto.types.hubitat_component_gt import HubitatRESTResolutionSettings
from gwproto.types.hubitat_tank_gt import FibaroTempSensorSettings
from gwproto.types.hubitat_tank_gt import FibaroTempSensorSettingsGt
from gwproto.types.hubitat_tank_gt import HubitatTankSettingsGt
from gwproto.types.channel_config import ChannelConfig_Maker, ChannelConfig
from gwproto.types.data_channel_gt import DataChannelGt_Maker


class HubitatTankComponent(Component, ComponentResolver):
    hubitat: HubitatComponentGt
    sensor_supply_voltage: float
    devices_gt: list[FibaroTempSensorSettingsGt]
    devices: list[FibaroTempSensorSettings] = []

    def __init__(
        self,
        component_id: str,
        component_attribute_class_id: str,
        tank_gt: HubitatTankSettingsGt,
        display_name: Optional[str] = None,
        hw_uid: Optional[str] = None,
    ):
        # Create self.hubitat as a proxy containing only the id
        # of the hubitat; the actual component data will be resolved
        # when resolve() is called; Here in the constructor we cannot
        # rely on the actual HubitatComponentGt existing yet.
        self.hubitat = HubitatComponentGt.make_stub(tank_gt.hubitat_component_id)
        self.sensor_supply_voltage = tank_gt.sensor_supply_voltage
        self.devices_gt = list(tank_gt.devices)
        self.my_node_name = tank_gt.my_node_name
        super().__init__(
            display_name=display_name,
            component_id=component_id,
            hw_uid=hw_uid,
            config_list=self.make_config_list(),
            component_attribute_class_id=component_attribute_class_id,
        )
    
    @property
    def cac(self) -> Cac:
        return Cac.by_id[self.component_attribute_class_id]

    def resolve(
        self,
        nodes: dict[str, ShNode],
        components: dict[str, Component],
    ):
        hubitat_component_gt = HubitatComponentGt.from_component_id(
            self.hubitat.ComponentId, components
        )
        hubitat_settings = HubitatRESTResolutionSettings(hubitat_component_gt)
        devices = [
            FibaroTempSensorSettings.create(
                settings_gt=device_gt,
                hubitat=hubitat_settings,
            )
            for device_gt in self.devices_gt
            if device_gt.enabled
        ]
        for device in devices:
            if device.about_node_name not in nodes:
                raise ValueError(
                    f"ERROR. Node <{device.about_node_name}> not found for <{self.my_node_name}> (thermistor <{device.stack_depth}>)"
                )
        # replace proxy hubitat component, which only had component id.
        # with the actual hubitat component containing data.
        self.hubitat = hubitat_component_gt
        self.devices = devices

    def urls(self) -> dict[str, Optional[yarl.URL]]:
        urls = self.hubitat.urls()
        for device in self.devices:
            urls[device.about_node_name] = device.url
        return urls

    def make_config_list(self) -> list[ChannelConfig]:
        return [
            ChannelConfig_Maker(
                channel_name=device.channel_name,
                poll_period_ms = int(device.rest.poll_period_seconds * 1000),
                async_capture=False,
                capture_period_s = int(device.rest.poll_period_seconds * 1000),
                exponent=device.exponent,
                unit=device.unit,
            )
            for device in self.devices
        ]
