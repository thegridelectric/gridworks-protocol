import pytest
from gwproto.errors import SchemaError
from gwproto.messages import GsDispatch_Maker as Maker


def test_gs_dispatch():
    gw_tuple = Maker(relay_state=1).tuple

    assert Maker.tuple_to_type(gw_tuple) == b"\x01\x00"  # type: ignore
    assert Maker.type_to_tuple(b"\x01\x00") == gw_tuple

    with pytest.raises(SchemaError):
        Maker(relay_state="hi")

    with pytest.raises(SchemaError):
        Maker(relay_state=2)
