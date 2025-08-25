"""Tests analog.dispatch type, version 000"""

from gwproto.named_types import AnalogDispatch


def test_analog_dispatch_generated() -> None:
    d = {
        "FromGNodeAlias": "d1.isone.ct.orange",
        "FromHandle": "auto.h",
        "ToHandle": "auto.h.dist-010v",
        "AboutName": "dist-010v",
        "Value": 40,
        "TriggerId": "aa7899a6-d44a-4e56-b393-8ea9039235ca",
        "UnixTimeMs": 1732651420193,
        "TypeName": "analog.dispatch",
        "Version": "000",
    }

    d2 = AnalogDispatch.from_dict(d).to_dict()

    assert d2 == d
