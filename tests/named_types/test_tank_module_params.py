"""Tests tank.module.params type, version 100"""

from gwproto.named_types import TankModuleParams


def test_tank_module_params_generated() -> None:
    d = {
        "HwUid": "pico_4c1a21",
        "ActorNodeName": "buffer",
        "PicoAB": "a",
        "CapturePeriodS": 300,
        "Samples": 1000,
        "NumSampleAverages": 10,
        "AsyncCaptureDeltaMicroVolts": 2000,
        "CaptureOffsetS": 0,
        "TypeName": "tank.module.params",
        "Version": "100",
    }

    d2 = TankModuleParams.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
