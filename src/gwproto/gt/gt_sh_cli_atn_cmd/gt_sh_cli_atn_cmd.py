"""gt.sh.cli.atn.cmd.110 type"""

from gwproto.errors import MpSchemaError
from gwproto.gt.gt_sh_cli_atn_cmd.gt_sh_cli_atn_cmd_base import GtShCliAtnCmdBase


class GtShCliAtnCmd(GtShCliAtnCmdBase):
    def check_for_errors(self):
        errors = self.derived_errors() + self.hand_coded_errors()
        if len(errors) > 0:
            raise MpSchemaError(f" Errors making making gt.sh.cli.atn.cmd.110 for {self}: {errors}")

    def hand_coded_errors(self):
        return []
