import pytest
from gwproto.errors import SchemaError
from gwproto.messages import GsPwr_Maker as Maker


def test_gs_pwr() -> None:
    gw_tuple = Maker(power=3200).tuple

    assert Maker.tuple_to_type(gw_tuple) == b"\x80\x0c"  # type: ignore
    assert Maker.type_to_tuple(b"\x80\x0c") == gw_tuple

    with pytest.raises(SchemaError):
        Maker(power="hi")

    with pytest.raises(SchemaError):
        Maker(power=32768)
