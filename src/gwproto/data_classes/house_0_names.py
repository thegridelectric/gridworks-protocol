from typing import ClassVar, Dict, List, Literal

from gwproto.data_classes.telemetry_tuple import ChannelStub
from gwproto.enums import TelemetryName

DEFAULT_ANALOG_READER = "analog-temp"


class ZoneNodes:
    def __init__(self, zone: str, idx: int) -> None:
        zone_name = f"zone{idx + 1}-{zone}".lower()
        self.zone_name = zone_name
        self.stat = f"{zone_name}-stat"

    def __repr__(self) -> str:
        return f"Zone {self.zone_name} and stat {self.stat}"


class TankNodes:
    def __init__(self, tank_name: str) -> None:
        self.reader = tank_name
        self.depth1 = f"{tank_name}-depth1"
        self.depth2 = f"{tank_name}-depth2"
        self.depth3 = f"{tank_name}-depth3"
        self.depth4 = f"{tank_name}-depth4"

    def __repr__(self) -> str:
        return f"{self.reader} reads {self.depth1}, {self.depth2}, {self.depth3}, {self.depth4}"


class ZoneChannelNames:
    def __init__(self, zone: str, idx: int) -> None:
        self.zone_name = f"zone{idx}-{zone}".lower()
        self.stat_name = f"{self.zone_name}-stat"
        self.temp = f"{self.zone_name}-temp"
        self.set = f"{self.zone_name}-set"
        self.state = f"{self.zone_name}-state"

    def __repr__(self) -> str:
        return f"Channels: .temp: {self.temp}, .set: {self.set}, .state: {self.state}"


class TankChannelNames:
    def __init__(self, tank_name: str) -> None:
        self.depth1 = f"{tank_name}-depth1"
        self.depth2 = f"{tank_name}-depth2"
        self.depth3 = f"{tank_name}-depth3"
        self.depth4 = f"{tank_name}-depth4"


class House0RelayIdx:
    vdc: Literal[1] = 1
    tstat_common: Literal[2] = 2
    store_charge_disharge: Literal[3] = 3
    hp_failsafe: Literal[5] = 5
    hp_scada_ops: Literal[6] = 6
    aquastat_ctrl: Literal[8] = 8
    store_pump_failsafe: Literal[9] = 9
    boiler_scada_ops: Literal[10] = 10
    primary_pump_ops: Literal[11] = 11
    primary_pump_failsafe: Literal[12] = 12


class H0N:
    # core actors
    atn = "a"
    atomic_ally = "aa"
    fake_atn = "fake-atn"
    primary_scada = "s"
    secondary_scada = "s2"
    home_alone = "h"
    primary_power_meter = "power-meter"
    admin = "admin"  # used when starter scripts take control
    auto = "auto"  # Finite State Machine responsible for homealone <-> atn transition
    analog_temp = "analog-temp"
    relay_multiplexer = "relay-multiplexer"
    synth_generator = "synth-generator"
    zero_ten_out_multiplexer = "dfr-multiplexer"

    # core power-metered nodes
    hp_odu = "hp-odu"
    hp_idu = "hp-idu"
    dist_pump = "dist-pump"
    primary_pump = "primary-pump"
    store_pump = "store-pump"

    # core temperatures
    dist_swt = "dist-swt"
    dist_rwt = "dist-rwt"
    hp_lwt = "hp-lwt"
    hp_ewt = "hp-ewt"
    buffer_hot_pipe = "buffer-hot-pipe"
    buffer_cold_pipe = "buffer-cold-pipe"
    store_hot_pipe = "store-hot-pipe"
    store_cold_pipe = "store-cold-pipe"
    oat = "oat"
    buffer = TankNodes("buffer")
    tank: ClassVar[Dict[int, TankNodes]] = {}
    zone: ClassVar[Dict[str, ZoneNodes]] = {}

    # core flow-metered nodes
    dist_flow = "dist-flow"
    primary_flow = "primary-flow"
    store_flow = "store-flow"

    # relay nodes
    vdc_relay: Literal["relay1"] = f"relay{House0RelayIdx.vdc}"
    tstat_common_relay: Literal["relay2"] = f"relay{House0RelayIdx.tstat_common}"
    store_charge_discharge_relay: Literal["relay3"] = (
        f"relay{House0RelayIdx.store_charge_disharge}"
    )
    hp_failsafe_relay: Literal["relay5"] = f"relay{House0RelayIdx.hp_failsafe}"
    hp_scada_ops_relay: Literal["relay6"] = f"relay{House0RelayIdx.hp_scada_ops}"
    aquastat_ctrl_relay: Literal["relay8"] = f"relay{House0RelayIdx.aquastat_ctrl}"
    store_pump_failsafe: Literal["relay9"] = (
        f"relay{House0RelayIdx.store_pump_failsafe}"
    )
    boiler_scada_ops: Literal["relay10"] = f"relay{House0RelayIdx.boiler_scada_ops}"
    primary_pump_scada_ops: Literal["relay11"] = (
        f"relay{House0RelayIdx.primary_pump_ops}"
    )
    primary_pump_failsafe: Literal["relay12"] = (
        f"relay{House0RelayIdx.primary_pump_failsafe}"
    )

    # zero ten output
    dist_010v = "dist-010v"
    primary_010v = "primary-010v"
    store_010v = "store-010v"
    hubitat = "hubitat"

    # finite state machines
    pico_cycler = "pico-cycler"

    def __init__(self, total_store_tanks: int, zone_list: List[str]) -> None:
        for i in range(total_store_tanks):
            self.tank[i + 1] = TankNodes(f"tank{i + 1}")
        for i in range(len(zone_list)):
            self.zone[zone_list[i]] = ZoneNodes(zone=zone_list[i], idx=i)


class House0StartHandles:
    scada = "h.s"
    admin = "admin"
    home_alone = "h"
    relay_multiplexer = "admin.relay-multiplexer"


class H0CN:
    # Power Channels
    hp_odu_pwr = f"{H0N.hp_odu}-pwr"
    hp_idu_pwr = f"{H0N.hp_idu}-pwr"
    dist_pump_pwr = f"{H0N.dist_pump}-pwr"
    primary_pump_pwr = f"{H0N.primary_pump}-pwr"
    store_pump_pwr = f"{H0N.store_pump}-pwr"

    # Temperature Channels
    dist_swt = H0N.dist_swt
    dist_rwt = H0N.dist_rwt
    hp_lwt = H0N.hp_lwt
    hp_ewt = H0N.hp_ewt
    store_hot_pipe = H0N.store_hot_pipe
    store_cold_pipe = H0N.store_cold_pipe
    buffer_hot_pipe = H0N.buffer_hot_pipe
    buffer_cold_pipe = H0N.buffer_cold_pipe
    oat = H0N.oat
    buffer = TankChannelNames("buffer")
    tank: ClassVar[Dict[int, TankChannelNames]] = {}
    zone: ClassVar[Dict[int, ZoneChannelNames]] = {}

    # Flow Channels
    dist_flow = H0N.dist_flow
    primary_flow = H0N.primary_flow
    store_flow = H0N.store_flow
    dist_flow_hz = f"{H0N.dist_flow}-hz"
    primary_flow_hz = f"{H0N.primary_flow}-hz"
    store_flow_hz = f"{H0N.store_flow}-hz"

    # relay state channels
    vdc_relay_state: Literal["vdc-relay1"] = f"vdc-{H0N.vdc_relay}"
    tstat_common_relay_state: Literal["tstat-common-relay2"] = (
        f"tstat-common-{H0N.tstat_common_relay}"
    )
    charge_discharge_relay_state: Literal["charge-discharge-relay3"] = (
        f"charge-discharge-{H0N.store_charge_discharge_relay}"
    )
    hp_failsafe_relay_state = f"hp-failsafe-{H0N.hp_failsafe_relay}"
    hp_scada_ops_relay_state = f"hp-scada-ops-{H0N.hp_scada_ops_relay}"
    aquastat_ctrl_relay_state = f"aquastat-ctrl-{H0N.aquastat_ctrl_relay}"
    store_pump_failsafe_relay_state = f"store-pump-failsafe-{H0N.store_pump_failsafe}"
    boiler_scada_ops_relay_state = f"boiler-scada_ops-{H0N.boiler_scada_ops}"
    primary_pump_scada_ops_relay_state = (
        f"primary-pump-scada-ops-{H0N.primary_pump_scada_ops}"
    )
    primary_pump_failsafe_relay_state = (
        f"primary-pump-failsafe-{H0N.primary_pump_failsafe}"
    )

    # 010V output state (as declared by entity sending, not reading)
    dist_010v = "dist-010v"
    primary_010v = "primary-010v"
    store_010v = "store-010v"

    def __init__(self, total_store_tanks: int, zone_list: List[str]) -> None:
        for i in range(total_store_tanks):
            self.tank[i + 1] = TankChannelNames(f"tank{i + 1}")
        for i in range(len(zone_list)):
            self.zone[i + 1] = ZoneChannelNames(zone=zone_list[i], idx=i + 1)

    def channel_stubs(self) -> Dict[str, ChannelStub]:
        d = {
            self.hp_odu_pwr: ChannelStub(
                Name=self.hp_odu_pwr,
                AboutNodeName=H0N.hp_odu,
                TelemetryName=TelemetryName.PowerW,
                InPowerMetering=True,
            ),
            self.hp_idu_pwr: ChannelStub(
                Name=self.hp_idu_pwr,
                AboutNodeName=H0N.hp_idu,
                TelemetryName=TelemetryName.PowerW,
                InPowerMetering=True,
            ),
            self.dist_pump_pwr: ChannelStub(
                Name=self.dist_pump_pwr,
                AboutNodeName=H0N.dist_pump,
                TelemetryName=TelemetryName.PowerW,
            ),
            self.primary_pump_pwr: ChannelStub(
                Name=self.primary_pump_pwr,
                AboutNodeName=H0N.primary_pump,
                TelemetryName=TelemetryName.PowerW,
            ),
            self.store_pump_pwr: ChannelStub(
                Name=self.store_pump_pwr,
                AboutNodeName=H0N.store_pump,
                TelemetryName=TelemetryName.PowerW,
            ),
            self.dist_swt: ChannelStub(
                Name=self.dist_swt,
                AboutNodeName=H0N.dist_swt,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            ),
            self.dist_rwt: ChannelStub(
                Name=self.dist_rwt,
                AboutNodeName=H0N.dist_rwt,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            ),
            self.hp_lwt: ChannelStub(
                Name=self.hp_lwt,
                AboutNodeName=H0N.hp_lwt,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            ),
            self.hp_ewt: ChannelStub(
                Name=self.hp_ewt,
                AboutNodeName=H0N.hp_ewt,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            ),
            self.store_hot_pipe: ChannelStub(
                Name=self.store_hot_pipe,
                AboutNodeName=H0N.store_hot_pipe,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            ),
            self.store_cold_pipe: ChannelStub(
                Name=self.store_cold_pipe,
                AboutNodeName=H0N.store_cold_pipe,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            ),
            self.buffer_hot_pipe: ChannelStub(
                Name=self.buffer_hot_pipe,
                AboutNodeName=H0N.buffer_hot_pipe,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            ),
            self.buffer_cold_pipe: ChannelStub(
                Name=self.buffer_cold_pipe,
                AboutNodeName=H0N.buffer_cold_pipe,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            ),
            self.oat: ChannelStub(
                Name=self.oat,
                AboutNodeName=H0N.oat,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            ),
            self.dist_flow: ChannelStub(
                Name=self.dist_flow,
                AboutNodeName=H0N.dist_flow,
                TelemetryName=TelemetryName.GpmTimes100,
            ),
            self.primary_flow: ChannelStub(
                Name=self.primary_flow,
                AboutNodeName=H0N.primary_flow,
                TelemetryName=TelemetryName.GpmTimes100,
            ),
            self.store_flow: ChannelStub(
                Name=self.store_flow,
                AboutNodeName=H0N.store_flow,
                TelemetryName=TelemetryName.GpmTimes100,
            ),
            self.buffer.depth1: ChannelStub(
                Name=self.buffer.depth1,
                AboutNodeName=H0N.buffer.depth1,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            ),
            self.buffer.depth2: ChannelStub(
                Name=self.buffer.depth2,
                AboutNodeName=H0N.buffer.depth2,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            ),
            self.buffer.depth3: ChannelStub(
                Name=self.buffer.depth3,
                AboutNodeName=H0N.buffer.depth3,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            ),
            self.buffer.depth4: ChannelStub(
                Name=self.buffer.depth4,
                AboutNodeName=H0N.buffer.depth4,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            ),
        }
        for i in self.tank:
            d[self.tank[i].depth1] = ChannelStub(
                Name=self.tank[i].depth1,
                AboutNodeName=self.tank[i].depth1,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            )
            d[self.tank[i].depth2] = ChannelStub(
                Name=self.tank[i].depth2,
                AboutNodeName=self.tank[i].depth2,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            )
            d[self.tank[i].depth3] = ChannelStub(
                Name=self.tank[i].depth3,
                AboutNodeName=self.tank[i].depth3,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            )
            d[self.tank[i].depth4] = ChannelStub(
                Name=self.tank[i].depth4,
                AboutNodeName=self.tank[i].depth4,
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            )
        for i in self.zone:
            d[self.zone[i].temp] = (
                ChannelStub(
                    Name=self.zone[i].temp,
                    AboutNodeName=self.zone[i].zone_name,
                    TelemetryName=TelemetryName.AirTempFTimes1000,
                ),
            )
            d[self.zone[i].set] = (
                ChannelStub(
                    Name=self.zone[i].temp,
                    AboutNodeName=self.zone[i].stat_name,
                    TelemetryName=TelemetryName.AirTempFTimes1000,
                ),
            )
            d[self.zone[i].set] = (
                ChannelStub(
                    Name=self.zone[i].state,
                    AboutNodeName=self.zone[i].stat_name,
                    TelemetryName=TelemetryName.ThermostatState,
                ),
            )
        return d
