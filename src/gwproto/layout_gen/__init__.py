"""Temporary package for assisting generation of hardware_layout.json files"""

from gwproto.layout_gen.ads111x import AdsGenCfg, AdsSensorCfg, add_ads1115
from gwproto.layout_gen.house_0_egauge import (
    EGaugeGenCfg,
    EGaugeIOGenCfg,
    add_house0_egauge,
)
from gwproto.layout_gen.house_0_layout_db import House0LayoutDb, House0StubConfig
from gwproto.layout_gen.i2c_flow import (
    I2cFlowMeterGenCfg,
    I2cFlowSensorCfg,
    add_i2c_flow_totalizer,
)
from gwproto.layout_gen.i2c_relay import (
    I2cRelayBoardCfg,
    I2cRelayPinCfg,
    add_i2c_relay_board,
)
from gwproto.layout_gen.layout_db import LayoutDb, LayoutIDMap

__all__ = [
    "add_ads1115",
    "add_house0_egauge",
    "add_i2c_flow_totalizer",
    "add_i2c_relay_board",
    "AdsGenCfg",
    "AdsSensorCfg",
    "EGaugeGenCfg",
    "EGaugeIOGenCfg",
    "I2cFlowMeterGenCfg",
    "I2cFlowSensorCfg",
    "I2cRelayPinCfg",
    "I2cRelayBoardCfg",
    "House0StubConfig",
    "House0LayoutDb",
    "LayoutDb",
    "LayoutIDMap",
]
