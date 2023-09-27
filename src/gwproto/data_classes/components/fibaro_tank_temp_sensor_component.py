from typing import Optional

from gwproto.data_classes.components.rest_poller_component import RESTPollerComponent
from gwproto.enums import TelemetryName
from gwproto.types.rest_poller_gt import RESTPollerSettings


class FibaroTankTempSensorComponent(RESTPollerComponent):
    exponent: int
    telemetry_name: TelemetryName

    def __init__(
        self,
        component_id: str,
        component_attribute_class_id: str,
        exponent: int,
        telemetry_name: TelemetryName,
        rest: RESTPollerSettings,
        display_name: Optional[str] = None,
        hw_uid: Optional[str] = None,
    ):
        self.exponent = exponent
        self.telemetry_name = telemetry_name
        super().__init__(
            component_id=component_id,
            component_attribute_class_id=component_attribute_class_id,
            rest=rest,
            display_name=display_name,
            hw_uid=hw_uid,
        )
