"""Tests async.btu.params type, version 000"""

from gwproto.named_types import AsyncBtuParams


def test_async_btu_params_generated() -> None:
    d = {
        "ActorNodeName": "primary-btu",
        "FlowNodeName": "primary-flow",
        "HotNodeName": "hp-lwt",
        "ColdNodeName": "hp-ewt",
        "CtNodeName": "primary-pump-pwr",
        "CapturePeriodS": 60,
        "GallonsPerPulse": 0.0009,
        "AsyncCaptureDeltaGpmX100": 10,
        "AsyncCaptureDeltaCelsiusX100": 20,
        "AsyncCaptureDeltaCtVoltsX100": 20,
        "TypeName": "async.btu.params",
        "Version": "000",
    }

    d2 = AsyncBtuParams.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
