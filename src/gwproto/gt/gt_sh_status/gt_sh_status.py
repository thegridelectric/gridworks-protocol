"""gt.sh.status.110 type"""

from gwproto.errors import MpSchemaError
from gwproto.gt.gt_sh_status.gt_sh_status_base import GtShStatusBase


class GtShStatus(GtShStatusBase):
    def check_for_errors(self):
        errors = self.derived_errors() + self.hand_coded_errors()
        if len(errors) > 0:
            raise MpSchemaError(f" Errors making making gt.sh.status.110 for {self}: {errors}")

    def hand_coded_errors(self):
        return []
