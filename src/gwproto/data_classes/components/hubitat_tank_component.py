from typing import Optional

import yarl

from gwproto.data_classes.components import HubitatComponent
from gwproto.data_classes.components.component import Component
from gwproto.data_classes.resolver import ComponentResolver
from gwproto.data_classes.sh_node import ShNode
from gwproto.types.component_attribute_class_gt import ComponentAttributeClassGt
from gwproto.types.hubitat_component_gt import (
    HubitatComponentGt,
    HubitatRESTResolutionSettings,
)
from gwproto.types.hubitat_tank_component_gt import HubitatTankComponentGt
from gwproto.types.hubitat_tank_gt import (
    FibaroTempSensorSettings,
    FibaroTempSensorSettingsGt,
)


class HubitatTankComponent(
    Component[HubitatTankComponentGt, ComponentAttributeClassGt], ComponentResolver
):
    hubitat: HubitatComponentGt
    devices_gt: list[FibaroTempSensorSettingsGt]
    devices: list[FibaroTempSensorSettings]

    def __init__(
        self, gt: HubitatTankComponentGt, cac: ComponentAttributeClassGt
    ) -> None:
        super().__init__(gt, cac)
        # Create self.hubitat as a proxy containing only the id
        # of the hubitat; the actual component data will be resolved
        # when resolve() is called; Here in the constructor we cannot
        # rely on the actual HubitatComponentGt existing yet.
        self.hubitat = HubitatComponentGt.make_stub(self.gt.Tank.hubitat_component_id)
        self.devices_gt = list(self.gt.Tank.devices)
        self.devices = []

    @property
    def sensor_supply_voltage(self) -> float:
        return self.gt.Tank.sensor_supply_voltage

    @property
    def default_poll_period_seconds(self) -> Optional[float]:
        return self.gt.Tank.default_poll_period_seconds

    @property
    def web_listen_enabled(self) -> bool:
        return self.gt.Tank.web_listen_enabled

    def resolve(
        self,
        tank_node_name: str,
        nodes: dict[str, ShNode],
        components: dict[str, Component],
    ) -> None:
        hubitat_component = components.get(self.hubitat.ComponentId, None)
        if hubitat_component is None or not isinstance(
            hubitat_component, HubitatComponent
        ):
            raise ValueError(
                f"ERROR. Component for {self.hubitat.ComponentId} "
                f"has type <{type(hubitat_component)}>. Expected <HubitatComponent>"
            )
        hubitat_settings = HubitatRESTResolutionSettings(hubitat_component.gt)
        devices = [
            FibaroTempSensorSettings.create(
                tank_name=tank_node_name,
                settings_gt=device_gt,
                hubitat=hubitat_settings,
                default_poll_period_seconds=self.default_poll_period_seconds,
            )
            for device_gt in self.devices_gt
            if device_gt.enabled
        ]
        for device in devices:
            if device.node_name not in nodes:
                raise ValueError(
                    f"ERROR. Node not found for tank temp sensor <{device.node_name}>"
                )
        # replace proxy hubitat component, which only had component id.
        # with the actual hubitat component containing data.
        self.hubitat = hubitat_component.gt
        self.devices = devices

        # register voltage attribute for fibaros which accept web posts
        if self.web_listen_enabled and hubitat_component.gt.Hubitat.WebListenEnabled:
            for device in self.devices:
                if device.web_listen_enabled:
                    hubitat_component.add_web_listener(tank_node_name)

    def urls(self) -> dict[str, Optional[yarl.URL]]:
        urls = self.hubitat.urls()
        for device in self.devices:
            urls[device.node_name] = device.url
        return urls
