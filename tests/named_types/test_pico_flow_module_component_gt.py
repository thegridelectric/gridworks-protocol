"""Tests pico.flow.module.component.gt type, version 000"""

from gwproto.named_types import PicoFlowModuleComponentGt


def test_pico_flow_module_component_gt_generated() -> None:
    d = {
        "AsyncCaptureThresholdGpmTimes100": 20,
        "ComponentAttributeClassId": "9d045a8d-12ee-43e6-8d7b-11c77b19de2f",
        "ComponentId": "f69dc008-ae12-4081-8502-a5c3b2bc043d",
        "ConfigList": [
            {
                "AsyncCapture": True,
                "CapturePeriodS": 300,
                "ChannelName": "dist-flow",
                "Exponent": 2,
                "TypeName": "channel.config",
                "Unit": "Gpm",
                "Version": "000",
            },
            {
                "AsyncCapture": True,
                "CapturePeriodS": 300,
                "ChannelName": "dist-flow-hz",
                "Exponent": 6,
                "TypeName": "channel.config",
                "Unit": "VoltsRms",
                "Version": "000",
            },
        ],
        "ConstantGallonsPerTick": 0.0009,
        "DisplayName": "dist-flow HallFlowModule",
        "Enabled": True,
        "ExpAlpha": 0.2,
        "FlowMeterType": "SAIER__SENHZG1WA",
        "FlowNodeName": "dist-flow",
        "GpmFromHzMethod": "Constant",
        "HwUid": "pico_53102a",
        "HzCalcMethod": "BasicExpWeightedAvg",
        "NoFlowMs": 250,
        "PublishEmptyTicklistAfterS": 7,
        "PublishTicklistPeriodS": 10,
        "SendGallons": False,
        "SendHz": True,
        "SendTickLists": False,
        "SerialNumber": "NA",
        "TypeName": "pico.flow.module.component.gt",
        "Version": "000",
    }

    d2 = PicoFlowModuleComponentGt.from_dict(d).to_dict()
    assert d2 == d
