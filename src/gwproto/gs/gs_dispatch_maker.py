"""Makes GridWorksSerial protocol GsDispatch with MpAlias d"""
import struct

from gwproto.gs.gs_dispatch import GsDispatch


class GsDispatch_Maker:
    type_name = "d"

    def __init__(self, relay_state):
        tpl = GsDispatch(RelayState=relay_state)
        tpl.check_for_errors()
        self.tuple = tpl

    @classmethod
    def tuple_to_type(cls, tpl: GsDispatch) -> bytes:
        tpl.check_for_errors()
        return tpl.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> GsDispatch:
        (relay_state,) = struct.unpack("<h", b)
        tpl = GsDispatch(RelayState=relay_state)
        tpl.check_for_errors()
        return tpl
