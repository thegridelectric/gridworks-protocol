"""gt.sh.simple.telemetry.status.100 type"""

from gwproto.errors import MpSchemaError
from gwproto.gt.gt_sh_simple_telemetry_status.gt_sh_simple_telemetry_status_base import (
    GtShSimpleTelemetryStatusBase,
)


class GtShSimpleTelemetryStatus(GtShSimpleTelemetryStatusBase):
    def check_for_errors(self):
        errors = self.derived_errors() + self.hand_coded_errors()
        if len(errors) > 0:
            raise MpSchemaError(
                f" Errors making making gt.sh.simple.telemetry.status.100 for {self}: {errors}"
            )

    def hand_coded_errors(self):
        return []
