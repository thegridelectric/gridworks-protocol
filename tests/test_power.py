import pytest
from gw.errors import GwTypeError
from pydantic import ValidationError

from gwproto.messages import Power, PowerMaker


def test_power():
    gw_tuple = Power(value=3200)

    assert PowerMaker.tuple_to_type(gw_tuple) == b"\x80\x0c"  # type: ignore
    assert PowerMaker.type_to_tuple(b"\x80\x0c") == gw_tuple

    with pytest.raises(ValidationError):
        Power(value=33000)

    with pytest.raises(ValidationError):
        Power(value=2000, other_field="hi")

    with pytest.raises(GwTypeError):
        PowerMaker.type_to_tuple("some string")
