from typing import Optional

from gwproto.data_classes.component import Component
from gwproto.data_classes.sh_node import ShNode
from gwproto.types.hubitat_component_gt import HubitatComponentGt
from gwproto.types.hubitat_component_gt import HubitatRESTResolutionSettings
from gwproto.types.hubitat_tank_gt import DEFAULT_SENSOR_NODE_NAME_FORMAT
from gwproto.types.hubitat_tank_gt import FibaroTempSensorSettings
from gwproto.types.hubitat_tank_gt import FibaroTempSensorSettingsGt
from gwproto.types.hubitat_tank_gt import HubitatTankSettingsGt


class HubitatTankComponent(Component):
    hubitat: HubitatComponentGt
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
        self.hubitat = HubitatComponentGt(
            ComponentId=tank_gt.hubitat_component_id,
            ComponentAttributeClassId="",
            Host="",
            MakerApiId=0,
            AccessToken="",
        )
        self.devices_gt = list(tank_gt.devices)
        super().__init__(
            display_name=display_name,
            component_id=component_id,
            hw_uid=hw_uid,
            component_attribute_class_id=component_attribute_class_id,
        )

    def resolve(
        self,
        tank_node_name: str,
        components: dict[str, Component],
        nodes: dict[str, ShNode],
        node_name_format=DEFAULT_SENSOR_NODE_NAME_FORMAT,
    ):
        hubitat_component = components.get(self.hubitat.ComponentId, None)
        if hubitat_component is None:
            raise ValueError(
                "ERROR. No component found for "
                f"HubitatTankComponent.hubitat.CompnentId {self.hubitat.ComponentId}"
            )
        if not isinstance(hubitat_component, HubitatComponentGt):
            raise ValueError(
                "ERROR. Referenced hubitat component has type "
                f"{type(hubitat_component)}; "
                "must be instance of HubitatComponentGt. "
                f"Hubitat component id: {self.hubitat.ComponentId}"
            )
        hubitat_settings = HubitatRESTResolutionSettings(hubitat_component)
        devices = [
            FibaroTempSensorSettings.create(
                tank_name=tank_node_name,
                settings_gt=device_gt,
                hubitat=hubitat_settings,
                node_name_format=node_name_format,
            )
            for device_gt in self.devices_gt
        ]
        for device in devices:
            if device.node_name not in nodes:
                raise ValueError(
                    f"ERROR. Node not found for tank temp sensor <{device.node_name}>"
                )
        # replace proxy hubitat component, which only had component id.
        # with the actual hubitat component containing data.
        self.hubitat = hubitat_component
        self.devices = devices
