"""Tests electric.meter.component.gt type, version 001"""

from gwproto.types.electric_meter_component_gt import ElectricMeterComponentGt


def test_electric_meter_component_gt_generated() -> None:
    d =  {
      "ComponentAttributeClassId": "739a6e32-bb9c-43bc-a28d-fb61be665522",
      "ComponentId": "dce5c63d-8a38-439e-88ac-dd5ad845e9ca",
      "ConfigList": [
        {
          "AsyncCapture": True,
          "AsyncCaptureDelta": 200,
          "CapturePeriodS": 300,
          "ChannelName": "hp-odu-pwr",
          "Exponent": 0,
          "PollPeriodMs": 1000,
          "TypeName": "channel.config",
          "Unit": "W",
          "Version": "000"
        },
        {
          "AsyncCapture": True,
          "AsyncCaptureDelta": 50,
          "CapturePeriodS": 300,
          "ChannelName": "hp-idu-pwr",
          "Exponent": 0,
          "PollPeriodMs": 1000,
          "TypeName": "channel.config",
          "Unit": "W",
          "Version": "000"
        },
        {
          "AsyncCapture": True,
          "AsyncCaptureDelta": 10,
          "CapturePeriodS": 300,
          "ChannelName": "primary-pump-pwr",
          "Exponent": 0,
          "PollPeriodMs": 1000,
          "TypeName": "channel.config",
          "Unit": "W",
          "Version": "000"
        },
        {
          "AsyncCapture": True,
          "AsyncCaptureDelta": 10,
          "CapturePeriodS": 300,
          "ChannelName": "dist-pump-pwr",
          "Exponent": 0,
          "PollPeriodMs": 1000,
          "TypeName": "channel.config",
          "Unit": "W",
          "Version": "000"
        },
        {
          "AsyncCapture": True,
          "AsyncCaptureDelta": 10,
          "CapturePeriodS": 300,
          "ChannelName": "store-pump-pwr",
          "Exponent": 0,
          "PollPeriodMs": 1000,
          "TypeName": "channel.config",
          "Unit": "W",
          "Version": "000"
        },
        {
          "AsyncCapture": True,
          "AsyncCaptureDelta": 10,
          "CapturePeriodS": 300,
          "ChannelName": "oil-boiler-pwr",
          "Exponent": 0,
          "PollPeriodMs": 1000,
          "TypeName": "channel.config",
          "Unit": "W",
          "Version": "000"
        }
      ],
      "DisplayName": "eGauge6069.local",
      "EgaugeIoList": [
        {
          "ChannelName": "hp-odu-pwr",
          "InputConfig": {
            "Address": 9006,
            "Denominator": 1,
            "Description": "change in value",
            "Name": "",
            "Type": "f32",
            "TypeName": "egauge.register.config",
            "Unit": "W",
            "Version": "000"
          },
          "TypeName": "egauge.io",
          "Version": "001"
        },
        {
          "ChannelName": "hp-idu-pwr",
          "InputConfig": {
            "Address": 9000,
            "Denominator": 1,
            "Description": "change in value",
            "Name": "",
            "Type": "f32",
            "TypeName": "egauge.register.config",
            "Unit": "W",
            "Version": "000"
          },
          "TypeName": "egauge.io",
          "Version": "001"
        },
        {
          "ChannelName": "primary-pump-pwr",
          "InputConfig": {
            "Address": 9012,
            "Denominator": 1,
            "Description": "change in value",
            "Name": "",
            "Type": "f32",
            "TypeName": "egauge.register.config",
            "Unit": "W",
            "Version": "000"
          },
          "TypeName": "egauge.io",
          "Version": "001"
        },
        {
          "ChannelName": "dist-pump-pwr",
          "InputConfig": {
            "Address": 9010,
            "Denominator": 1,
            "Description": "change in value",
            "Name": "",
            "Type": "f32",
            "TypeName": "egauge.register.config",
            "Unit": "W",
            "Version": "000"
          },
          "TypeName": "egauge.io",
          "Version": "001"
        },
        {
          "ChannelName": "store-pump-pwr",
          "InputConfig": {
            "Address": 9014,
            "Denominator": 1,
            "Description": "change in value",
            "Name": "",
            "Type": "f32",
            "TypeName": "egauge.register.config",
            "Unit": "W",
            "Version": "000"
          },
          "TypeName": "egauge.io",
          "Version": "001"
        },
        {
          "ChannelName": "oil-boiler-pwr",
          "InputConfig": {
            "Address": 9016,
            "Denominator": 1,
            "Description": "change in value",
            "Name": "",
            "Type": "f32",
            "TypeName": "egauge.register.config",
            "Unit": "W",
            "Version": "000"
          },
          "TypeName": "egauge.io",
          "Version": "001"
        }
      ],
      "HwUid": "BP01349",
      "ModbusHost": "eGauge6069.local",
      "ModbusPort": 502,
      "TypeName": "electric.meter.component.gt",
      "Version": "001"
    }

    t = ElectricMeterComponentGt(**d)

    assert t.model_dump() == d
