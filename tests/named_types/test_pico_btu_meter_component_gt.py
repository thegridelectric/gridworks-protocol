"""Tests pico.btu.meter.component.gt type, version 000"""

from gwproto.enums import GpmFromHzMethod, HzCalcMethod, MakeModel, TempCalcMethod
from gwproto.named_types import PicoBtuMeterComponentGt


def test_pico_btu_meter_component_gt_generated() -> None:
    d = {
        "ComponentId": "03796a77-bf88-4a4b-a96e-efeb1bc6336e",
        "ComponentAttributeClassId": "d020608d-d5ed-4b12-9592-7135db34e4ba",
        "DisplayName": "Pico BtuMeter",
        "ConfigList": [],
        "Enabled": True,
        "SerialNumber": "105",
        "FlowChannelName": "primary-flow",
        "HotChannelName": "hp-lwt",
        "ColdChannelName": "hp-ewt",
        "ReadCtVoltage": True,
        "SendHz": False,
        "CtChannelName": "primary-pump-pwr",
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
