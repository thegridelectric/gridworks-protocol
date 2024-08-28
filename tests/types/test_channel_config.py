"""Tests channel.config type, version 000"""

import json

import pytest
from gw.errors import GwTypeError
from pydantic import ValidationError

from gwproto.enums import Unit
from gwproto.types import ChannelConfig
from gwproto.types import ChannelConfigMaker as Maker


def test_channel_config_generated() -> None:
    t = ChannelConfig(
        channel_name="hp-idu-pwr",
        poll_period_ms=300,
        capture_period_s=60,
        async_capture=True,
        async_capture_delta=30,
        exponent=6,
        unit=Unit.W,
    )

    d = {
        "ChannelName": "hp-idu-pwr",
        "PollPeriodMs": 300,
        "CapturePeriodS": 60,
        "AsyncCapture": True,
        "AsyncCaptureDelta": 30,
        "Exponent": 6,
        "UnitGtEnumSymbol": "f459a9c3",
        "TypeName": "channel.config",
        "Version": "000",
    }

    assert t.as_dict() == d

    d2 = d.copy()

    del d2["UnitGtEnumSymbol"]
    d2["Unit"] = Unit.W.value
    assert t == Maker.dict_to_tuple(d2)

    with pytest.raises(GwTypeError):
        Maker.type_to_tuple(d)

    with pytest.raises(GwTypeError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gtype = json.dumps(d)
    gtuple = Maker.type_to_tuple(gtype)
    assert gtuple == t

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

    ######################################
    # GwTypeError raised if missing a required attribute
    ######################################

    d2 = d.copy()
    del d2["TypeName"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["ChannelName"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["PollPeriodMs"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["CapturePeriodS"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["AsyncCapture"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["Exponent"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["UnitGtEnumSymbol"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "AsyncCaptureDelta" in d2.keys():
        del d2["AsyncCaptureDelta"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, PollPeriodMs="300.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, CapturePeriodS="60.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AsyncCapture="this is not a boolean")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AsyncCaptureDelta="30.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Exponent="6.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, UnitGtEnumSymbol="unknown_symbol")
    assert Maker.dict_to_tuple(d2).unit == Unit.default()

    ######################################
    # ValidationError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # ValidationError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, ChannelName="A.hot-stuff")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, PollPeriodMs=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, CapturePeriodS=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AsyncCaptureDelta=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
