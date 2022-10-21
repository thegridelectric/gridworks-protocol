import pytest

from gwproto.errors import MpSchemaError
from gwproto.messages import GsPwr_Maker as Maker


def test_gs_pwr():

    gw_tuple = Maker(power=3200).tuple

    assert Maker.tuple_to_type(gw_tuple) == b"\x80\x0c"  # type: ignore
    assert Maker.type_to_tuple(b"\x80\x0c") == gw_tuple

    with pytest.raises(MpSchemaError):
        Maker(power="hi")

    with pytest.raises(MpSchemaError):
        Maker(power=32768)
