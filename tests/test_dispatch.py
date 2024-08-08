import pytest
from gw.errors import GwTypeError
from gwproto.messages import Dispatch, DispatchMaker
from pydantic import ValidationError


def test_dispatch():
    gw_tuple = Dispatch(turn_on_or_off=1)

    assert DispatchMaker.tuple_to_type(gw_tuple) == b"\x01\x00"  # type: ignore
    assert DispatchMaker.type_to_tuple(b"\x01\x00") == gw_tuple

    with pytest.raises(ValidationError):
        Dispatch(turn_on_or_off=3)

    with pytest.raises(ValidationError):
        Dispatch(turn_on_or_off=1, other_field="hi")

    with pytest.raises(GwTypeError):
        DispatchMaker.type_to_tuple("some string")
