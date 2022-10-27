"""Tests gt.dispatch.boolean.100 type"""

import pydantic
import pytest

from gwproto.messages import GtDispatchBoolean


def test_gt_dispatch_boolean():

    gw_dict = {
        "AboutNodeAlias": "a.elt1.relay",
        "ToGNodeAlias": "dw1.isone.ct.newhaven.orange1.ta.scada",
        "FromGNodeAlias": "dw1.isone.ct.newhaven.orange1",
        "FromGNodeId": "e7f7d6cc-08b0-4b36-bbbb-0a1f8447fd32",
        "RelayState": 0,
        "SendTimeUnixMs": 1657024737661,
        "TypeAlias": "gt.dispatch.boolean",
    }

    parsed = GtDispatchBoolean.parse_obj(gw_dict)
    assert parsed.dict() == gw_dict

    # test Maker init
    constructed = GtDispatchBoolean(
        AboutNodeAlias=parsed.AboutNodeAlias,
        ToGNodeAlias=parsed.ToGNodeAlias,
        FromGNodeAlias=parsed.FromGNodeAlias,
        FromGNodeId=parsed.FromGNodeId,
        RelayState=parsed.RelayState,
        SendTimeUnixMs=parsed.SendTimeUnixMs,
    )
    assert parsed == constructed
    assert parsed.dict() == constructed.dict()

    # Bad TypeAlias
    gw_dict["TypeAlias"] = "foo"
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)

    # No type alias ok
    del gw_dict["TypeAlias"]
    GtDispatchBoolean.parse_obj(gw_dict)

    # ######################################
    # # Missing values
    # ######################################
    orig_value = gw_dict["AboutNodeAlias"]
    del gw_dict["AboutNodeAlias"]
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["AboutNodeAlias"] = orig_value

    orig_value = gw_dict["ToGNodeAlias"]
    del gw_dict["ToGNodeAlias"]
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["ToGNodeAlias"] = orig_value

    orig_value = gw_dict["FromGNodeAlias"]
    del gw_dict["FromGNodeAlias"]
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["FromGNodeAlias"] = orig_value

    orig_value = gw_dict["FromGNodeId"]
    del gw_dict["FromGNodeId"]
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["FromGNodeId"] = orig_value

    orig_value = gw_dict["RelayState"]
    del gw_dict["RelayState"]
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["RelayState"] = orig_value

    orig_value = gw_dict["SendTimeUnixMs"]
    del gw_dict["SendTimeUnixMs"]
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["SendTimeUnixMs"] = orig_value

    # ######################################
    # # Invalid type
    # ######################################

    orig_value = gw_dict["AboutNodeAlias"]
    gw_dict["AboutNodeAlias"] = 42  # type: ignore
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["AboutNodeAlias"] = orig_value

    orig_value = gw_dict["ToGNodeAlias"]
    gw_dict["ToGNodeAlias"] = 42  # type: ignore
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["ToGNodeAlias"] = orig_value

    orig_value = gw_dict["FromGNodeAlias"]
    gw_dict["FromGNodeAlias"] = 42  # type: ignore
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["FromGNodeAlias"] = orig_value

    orig_value = gw_dict["FromGNodeId"]
    gw_dict["FromGNodeId"] = 42  # type: ignore
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["FromGNodeId"] = orig_value

    orig_value = gw_dict["RelayState"]
    gw_dict["RelayState"] = 1.1  # type: ignore
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["RelayState"] = orig_value

    orig_value = gw_dict["SendTimeUnixMs"]
    gw_dict["SendTimeUnixMs"] = 1.1  # type: ignore
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["SendTimeUnixMs"] = orig_value

    ######################################
    # MpSchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    gw_dict["AboutNodeAlias"] = "a.b-h"
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["AboutNodeAlias"] = "a.elt1.relay"

    gw_dict["ToGNodeAlias"] = "a.b-h"
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["ToGNodeAlias"] = "dw1.isone.ct.newhaven.orange1.ta.scada"

    gw_dict["FromGNodeAlias"] = "a.b-h"
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["FromGNodeAlias"] = "dw1.isone.ct.newhaven.orange1"

    gw_dict["FromGNodeId"] = "d4be12d5-33ba-4f1f-b9e5"
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["FromGNodeId"] = "e7f7d6cc-08b0-4b36-bbbb-0a1f8447fd32"

    gw_dict["RelayState"] = 2
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["RelayState"] = 0

    gw_dict["SendTimeUnixMs"] = 1656245000
    with pytest.raises(pydantic.ValidationError):
        GtDispatchBoolean.parse_obj(gw_dict)
    gw_dict["SendTimeUnixMs"] = 1657024737661

    # End of Test
