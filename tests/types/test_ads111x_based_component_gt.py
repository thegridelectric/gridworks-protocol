"""Tests ads111x.based.component.gt type, version 000"""

from gwproto.types.ads111x_based_component_gt import Ads111xBasedComponentGt


def test_ads111x_based_component_gt_generated() -> None:
    d =     {
      "ComponentAttributeClassId": "432073b8-4d2b-4e36-9229-73893f33f846",
      "ComponentId": "dfbb257e-a851-437b-b9af-55f948f7d4af",
      "ConfigList": [
        {
          "AsyncCapture": True,
          "AsyncCaptureDelta": 250,
          "CapturePeriodS": 60,
          "ChannelName": "dist-swt",
          "Exponent": 3,
          "PollPeriodMs": 200,
          "TypeName": "channel.config",
          "Unit": "Celcius",
          "Version": "000"
        },
        {
          "AsyncCapture": True,
          "AsyncCaptureDelta": 250,
          "CapturePeriodS": 60,
          "ChannelName": "dist-rwt",
          "Exponent": 3,
          "PollPeriodMs": 200,
          "TypeName": "channel.config",
          "Unit": "Celcius",
          "Version": "000"
        },
        {
          "AsyncCapture": True,
          "AsyncCaptureDelta": 250,
          "CapturePeriodS": 60,
          "ChannelName": "hp-lwt",
          "Exponent": 3,
          "PollPeriodMs": 200,
          "TypeName": "channel.config",
          "Unit": "Celcius",
          "Version": "000"
        },
        {
          "AsyncCapture": True,
          "AsyncCaptureDelta": 250,
          "CapturePeriodS": 60,
          "ChannelName": "hp-ewt",
          "Exponent": 3,
          "PollPeriodMs": 200,
          "TypeName": "channel.config",
          "Unit": "Celcius",
          "Version": "000"
        },
        {
          "AsyncCapture": True,
          "AsyncCaptureDelta": 250,
          "CapturePeriodS": 60,
          "ChannelName": "store-hot-pipe",
          "Exponent": 3,
          "PollPeriodMs": 200,
          "TypeName": "channel.config",
          "Unit": "Celcius",
          "Version": "000"
        },
        {
          "AsyncCapture": True,
          "AsyncCaptureDelta": 250,
          "CapturePeriodS": 60,
          "ChannelName": "store-cold-pipe",
          "Exponent": 3,
          "PollPeriodMs": 200,
          "TypeName": "channel.config",
          "Unit": "Celcius",
          "Version": "000"
        },
        {
          "AsyncCapture": True,
          "AsyncCaptureDelta": 250,
          "CapturePeriodS": 60,
          "ChannelName": "buffer-hot-pipe",
          "Exponent": 3,
          "PollPeriodMs": 200,
          "TypeName": "channel.config",
          "Unit": "Celcius",
          "Version": "000"
        },
        {
          "AsyncCapture": True,
          "AsyncCaptureDelta": 250,
          "CapturePeriodS": 60,
          "ChannelName": "buffer-cold-pipe",
          "Exponent": 3,
          "PollPeriodMs": 200,
          "TypeName": "channel.config",
          "Unit": "Celcius",
          "Version": "000"
        },
        {
          "AsyncCapture": True,
          "AsyncCaptureDelta": 500,
          "CapturePeriodS": 60,
          "ChannelName": "oat",
          "Exponent": 3,
          "PollPeriodMs": 200,
          "TypeName": "channel.config",
          "Unit": "Celcius",
          "Version": "000"
        },
        {
          "AsyncCapture": False,
          "AsyncCaptureDelta": 250,
          "CapturePeriodS": 5,
          "ChannelName": "zone2-up-gw-temp",
          "Exponent": 3,
          "PollPeriodMs": 200,
          "TypeName": "channel.config",
          "Unit": "Celcius",
          "Version": "000"
        },
        {
          "AsyncCapture": False,
          "AsyncCaptureDelta": 250,
          "CapturePeriodS": 5,
          "ChannelName": "zone1-down-gw-temp",
          "Exponent": 3,
          "PollPeriodMs": 200,
          "TypeName": "channel.config",
          "Unit": "Celcius",
          "Version": "000"
        },
        {
          "AsyncCapture": True,
          "AsyncCaptureDelta": 250,
          "CapturePeriodS": 60,
          "ChannelName": "buffer-well",
          "Exponent": 3,
          "PollPeriodMs": 200,
          "TypeName": "channel.config",
          "Unit": "Celcius",
          "Version": "000"
        }
      ],
      "DisplayName": "GridWorks 12-Channel Ads-1115 based I2c Temp Sensor",
      "OpenVoltageByAds": [
        4.95,
        4.95,
        4.95
      ],
      "ThermistorConfigList": [
        {
          "ChannelName": "dist-swt",
          "DataProcessingDescription": "Using beta of 3977",
          "DataProcessingMethod": "SimpleBeta",
          "TerminalBlockIdx": 1,
          "ThermistorMakeModel": "Tewa__TT0P-10KC3-T105-1500",
          "TypeName": "thermistor.data.processing.config",
          "Version": "000"
        },
        {
          "ChannelName": "dist-rwt",
          "DataProcessingDescription": "Using beta of 3977",
          "DataProcessingMethod": "SimpleBeta",
          "TerminalBlockIdx": 2,
          "ThermistorMakeModel": "Tewa__TT0P-10KC3-T105-1500",
          "TypeName": "thermistor.data.processing.config",
          "Version": "000"
        },
        {
          "ChannelName": "hp-lwt",
          "DataProcessingDescription": "Using beta of 3977",
          "DataProcessingMethod": "SimpleBeta",
          "TerminalBlockIdx": 3,
          "ThermistorMakeModel": "Tewa__TT0P-10KC3-T105-1500",
          "TypeName": "thermistor.data.processing.config",
          "Version": "000"
        },
        {
          "ChannelName": "hp-ewt",
          "DataProcessingDescription": "Using beta of 3977",
          "DataProcessingMethod": "SimpleBeta",
          "TerminalBlockIdx": 4,
          "ThermistorMakeModel": "Tewa__TT0P-10KC3-T105-1500",
          "TypeName": "thermistor.data.processing.config",
          "Version": "000"
        },
        {
          "ChannelName": "store-hot-pipe",
          "DataProcessingDescription": "Using beta of 3977",
          "DataProcessingMethod": "SimpleBeta",
          "TerminalBlockIdx": 5,
          "ThermistorMakeModel": "Tewa__TT0P-10KC3-T105-1500",
          "TypeName": "thermistor.data.processing.config",
          "Version": "000"
        },
        {
          "ChannelName": "store-cold-pipe",
          "DataProcessingDescription": "Using beta of 3977",
          "DataProcessingMethod": "SimpleBeta",
          "TerminalBlockIdx": 6,
          "ThermistorMakeModel": "Tewa__TT0P-10KC3-T105-1500",
          "TypeName": "thermistor.data.processing.config",
          "Version": "000"
        },
        {
          "ChannelName": "buffer-hot-pipe",
          "DataProcessingDescription": "Using beta of 3977",
          "DataProcessingMethod": "SimpleBeta",
          "TerminalBlockIdx": 7,
          "ThermistorMakeModel": "Tewa__TT0P-10KC3-T105-1500",
          "TypeName": "thermistor.data.processing.config",
          "Version": "000"
        },
        {
          "ChannelName": "buffer-cold-pipe",
          "DataProcessingDescription": "Using beta of 3977",
          "DataProcessingMethod": "SimpleBeta",
          "TerminalBlockIdx": 8,
          "ThermistorMakeModel": "Tewa__TT0P-10KC3-T105-1500",
          "TypeName": "thermistor.data.processing.config",
          "Version": "000"
        },
        {
          "ChannelName": "oat",
          "DataProcessingDescription": "Using beta of 3977",
          "DataProcessingMethod": "SimpleBeta",
          "TerminalBlockIdx": 9,
          "ThermistorMakeModel": "Amphenol__NTC_10K_Thermistor_MA100GG103BN",
          "TypeName": "thermistor.data.processing.config",
          "Version": "000"
        },
        {
          "ChannelName": "zone2-up-gw-temp",
          "DataProcessingDescription": "Using beta of 3977",
          "DataProcessingMethod": "SimpleBeta",
          "TerminalBlockIdx": 10,
          "ThermistorMakeModel": "Amphenol__NTC_10K_Thermistor_MA100GG103BN",
          "TypeName": "thermistor.data.processing.config",
          "Version": "000"
        },
        {
          "ChannelName": "zone1-down-gw-temp",
          "DataProcessingDescription": "Using beta of 3977",
          "DataProcessingMethod": "SimpleBeta",
          "TerminalBlockIdx": 11,
          "ThermistorMakeModel": "Amphenol__NTC_10K_Thermistor_MA100GG103BN",
          "TypeName": "thermistor.data.processing.config",
          "Version": "000"
        },
        {
          "ChannelName": "buffer-well",
          "DataProcessingDescription": "Using beta of 3977",
          "DataProcessingMethod": "SimpleBeta",
          "TerminalBlockIdx": 12,
          "ThermistorMakeModel": "Tewa__TT0P-10KC3-T105-1500",
          "TypeName": "thermistor.data.processing.config",
          "Version": "000"
        }
      ],
      "TypeName": "ads111x.based.component.gt",
      "Version": "000"
    }

    t = Ads111xBasedComponentGt(**d)

    assert t.model_dump(exclude_none=True) == d
