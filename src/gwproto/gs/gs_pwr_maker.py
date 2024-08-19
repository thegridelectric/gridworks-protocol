"""Makes GridWorksSerial protocol gs.pwr.100 with MpAlias p"""

import struct

from gwproto.gs.gs_pwr import GsPwr


class GsPwr_Maker:
    type_name = "p"

    def __init__(self, power) -> None:
        tpl = GsPwr(Power=power)
        tpl.check_for_errors()
        self.tuple = tpl

    @classmethod
    def tuple_to_type(cls, tpl: GsPwr) -> bytes:
        tpl.check_for_errors()
        return tpl.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> GsPwr:
        (power,) = struct.unpack("<h", b)
        tpl = GsPwr(Power=power)
        tpl.check_for_errors()
        return tpl
