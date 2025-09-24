"""Tests pico.btu.meter.component.gt type, version 000"""

from gwproto.enums import GpmFromHzMethod, HzCalcMethod, MakeModel, TempCalcMethod
from gwproto.named_types import PicoBtuMeterComponentGt


def test_pico_btu_meter_component_gt_generated() -> None:
    d = {
        "Enabled": True,
        "SerialNumber": "105",
        "FlowNodeName": "primary-flow",
        "HotNodeName": "hp-lwt",
        "ColdNodeName": "hp-ewt",
        "ReadCt": True,
        "CtNodeName": "primary-pump-pwr",
        "FlowMeterType": "SAIER__SENHZG1WA",
        "HzCalcMethod": "UniformWindow",
        "TempCalcMethod": "SimpleBeta",
        "ThermistorBeta": 3977,
        "GpmFromHzMethod": "Constant",
        "GallonsPerPulse": 0.0009,
        "AsyncCaptureDeltaGpmX100": 10,
        "AsyncCaptureDeltaCelsiusX100": 20,
        "AsyncCaptureDeltaCtVoltsX100": 20,
        "TypeName": "pico.btu.meter.component.gt",
        "Version": "000",
    }

    d2 = PicoBtuMeterComponentGt.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d

    ######################################
    # Enum related
    ######################################

    assert type(d2["FlowMeterType"]) is str

    d2 = dict(d, FlowMeterType="unknown_enum_thing")
    assert PicoBtuMeterComponentGt(**d2).FlowMeterType == MakeModel.default()

    assert type(d2["HzCalcMethod"]) is str

    d2 = dict(d, HzCalcMethod="unknown_enum_thing")
    assert PicoBtuMeterComponentGt(**d2).HzCalcMethod == HzCalcMethod.default()

    assert type(d2["TempCalcMethod"]) is str

    d2 = dict(d, TempCalcMethod="unknown_enum_thing")
    assert PicoBtuMeterComponentGt(**d2).TempCalcMethod == TempCalcMethod.default()

    assert type(d2["GpmFromHzMethod"]) is str

    d2 = dict(d, GpmFromHzMethod="unknown_enum_thing")
    assert PicoBtuMeterComponentGt(**d2).GpmFromHzMethod == GpmFromHzMethod.default()
