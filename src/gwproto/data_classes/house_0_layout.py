import json
from pathlib import Path
from typing import Any, List, Optional

from pydantic import BaseModel

from gwproto.data_classes.component import Component
from gwproto.data_classes.component_attribute_class import ComponentAttributeClass
from gwproto.data_classes.data_channel import DataChannel
from gwproto.data_classes.hardware_layout import (
    HardwareLayout,
    LoadError,
    load_cacs,
    load_channels,
    load_components,
    load_nodes,
    resolve_links,
)
from gwproto.data_classes.house_0_names import House0RequiredNames
from gwproto.data_classes.sh_node import ShNode
from gwproto.default_decoders import ComponentDecoder
from gwproto.enums import (
    ChangeAquastatControl,
    ChangeHeatcallSource,
    ChangeHeatPumpControl,
    ChangeLgOperatingMode,
    ChangePrimaryPumpControl,
    ChangePrimaryPumpState,
    ChangeRelayPin,
    ChangeRelayState,
    ChangeStoreFlowDirection,
    ChangeValveState,
    FsmEventType,
    RelayWiringConfig,
)

#####################################################
# Relay related
#####################################################


class House0RelayIdx:
    VDC_RELAY = 1
    TSTAT_COMMON = 2
    ISO_VALVE = 3  # 16 seconds to open, 62 seconds to close
    CHARGE_DISCHARGE_VALVE = (
        4  # 16 seconds to go to discharge, 62 seconds to go to charge
    )
    HP_FAILSAFE = 5
    HP_SCADA_OPS = 6
    HP_DHW_VS_HEAT = 7
    AQUASTAT_CTRL = 8
    STORE_PUMP_FAILSAFE = 9
    BOILER_SCADA_OPS = 10
    PICOS = 13
    EMPTY = 15
    OPEN_ALL_THERMS = 16


class RelayAction:
    def __init__(self, relay_config: RelayWiringConfig, action: Any):
        self.relay_config = relay_config
        self.action = action

    def __eq__(self, other):
        return isinstance(other, RelayAction) and self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    def __str__(self):
        return f"{self.relay_config}, {self.action}"

    def __repr__(self):
        return f"{self.relay_config}, {self.action}"


RELAY_INSTRUCTION = {
    RelayAction(
        RelayWiringConfig.NormallyClosed, ChangeRelayState.CloseRelay
    ): ChangeRelayPin.DeEnergize,
    RelayAction(
        RelayWiringConfig.NormallyClosed, ChangeRelayState.OpenRelay
    ): ChangeRelayPin.Energize,
    RelayAction(
        RelayWiringConfig.NormallyOpen, ChangeRelayState.CloseRelay
    ): ChangeRelayPin.Energize,
    RelayAction(
        RelayWiringConfig.NormallyOpen, ChangeRelayState.OpenRelay
    ): ChangeRelayPin.DeEnergize,
    RelayAction(
        RelayWiringConfig.DoubleThrow, ChangeAquastatControl.SwitchToBoiler
    ): ChangeRelayPin.DeEnergize,
    RelayAction(
        RelayWiringConfig.DoubleThrow, ChangeAquastatControl.SwitchToScada
    ): ChangeRelayPin.Energize,
    RelayAction(
        RelayWiringConfig.DoubleThrow, ChangeHeatcallSource.SwitchToWallThermostat
    ): ChangeRelayPin.DeEnergize,
    RelayAction(
        RelayWiringConfig.DoubleThrow, ChangeHeatcallSource.SwitchToScada
    ): ChangeRelayPin.Energize,
    RelayAction(
        RelayWiringConfig.DoubleThrow, ChangeHeatPumpControl.SwitchToTankAquastat
    ): ChangeRelayPin.DeEnergize,
    RelayAction(
        RelayWiringConfig.DoubleThrow, ChangeHeatPumpControl.SwitchToScada
    ): ChangeRelayPin.Energize,
    RelayAction(
        RelayWiringConfig.DoubleThrow, ChangeLgOperatingMode.SwitchToHeat
    ): ChangeRelayPin.DeEnergize,
    RelayAction(
        RelayWiringConfig.DoubleThrow, ChangeLgOperatingMode.SwitchToDhw
    ): ChangeRelayPin.Energize,
    RelayAction(
        RelayWiringConfig.NormallyOpen, ChangeStoreFlowDirection.Discharge
    ): ChangeRelayPin.DeEnergize,
    RelayAction(
        RelayWiringConfig.NormallyOpen, ChangeStoreFlowDirection.Charge
    ): ChangeRelayPin.Energize,
    RelayAction(
        RelayWiringConfig.NormallyOpen, ChangeValveState.OpenValve
    ): ChangeRelayPin.DeEnergize,
    RelayAction(
        RelayWiringConfig.NormallyOpen, ChangeValveState.CloseValve
    ): ChangeRelayPin.Energize,
    RelayAction(
        RelayWiringConfig.DoubleThrow, ChangePrimaryPumpControl.SwitchToHeatPump
    ): ChangeRelayPin.DeEnergize,
    RelayAction(
        RelayWiringConfig.DoubleThrow, ChangePrimaryPumpControl.SwitchToScada
    ): ChangeRelayPin.Energize,
    RelayAction(
        RelayWiringConfig.NormallyClosed, ChangePrimaryPumpState.TurnPumpOff
    ): ChangeRelayPin.DeEnergize,
    RelayAction(
        RelayWiringConfig.NormallyClosed, ChangePrimaryPumpState.AllowPumpToRun
    ): ChangeRelayPin.Energize,
}


class RelayActionChoice(BaseModel):
    display_name: str
    idx: int
    config: RelayWiringConfig
    control_type: FsmEventType
    de_energize_option: Any
    energize_option: Any
    current_state: Optional[Any]


####################################################
# Temp Sensor Related
###################################################


class House0Layout(HardwareLayout):
    total_zones: int
    total_store_tanks: int

    def __init__(
        self,
        layout: dict[Any, Any],
        cacs: Optional[dict[str, ComponentAttributeClass]] = None,  # by id
        components: Optional[dict[str, Component]] = None,  # by id
        nodes: Optional[dict[str, ShNode]] = None,  # by name
        channels: Optional[dict[str, DataChannel]] = None,  # by name
    ):
        super().__init__(
            layout=layout,
            cacs=cacs,
            components=components,
            nodes=nodes,
            channels=channels,
        )

        scada_dict = next((x for x in self.layout["ShNodes"] if x["Name"] == "s"), None)
        if not {"Strategy", "TotalStoreTanks", "ZoneList"} <= set(scada_dict.keys()):
            raise Exception("Scada ShNode s needs Strategy, TotalStoreTanks, ZoneList")

        if not scada_dict["Strategy"] == "House0":
            raise Exception("Scada node (name s) must have Strategy House0")
        print("Scada Strategy is House0")
        self.total_store_tanks = scada_dict["TotalStoreTanks"]
        if not isinstance(self.total_store_tanks, int):
            raise Exception("TotalStoreTanks must be an integer")
        if not 1 <= self.total_store_tanks <= 6:
            raise Exception("Must have between 1 and 6 store tanks")
        self.zone_list = scada_dict["ZoneList"]
        if not isinstance(self.zone_list, List):
            raise Exception("ZoneList must be a list")
        if not 1 <= len(self.zone_list) <= 6:
            raise Exception("Must have between 1 and 6 store zones")
        self.short_names = House0RequiredNames(self.total_store_tanks, self.zone_list)

    @classmethod
    def load(
        cls,
        layout_path: Path | str,
        included_node_names: Optional[set[str]] = None,
        raise_errors: bool = True,
        errors: Optional[list[LoadError]] = None,
        component_decoder: Optional[ComponentDecoder] = None,
    ) -> "House0Layout":
        with Path(layout_path).open() as f:
            layout = json.loads(f.read())
        return cls.load_dict(
            layout,
            included_node_names=included_node_names,
            raise_errors=raise_errors,
            errors=errors,
            component_decoder=component_decoder,
        )

    @classmethod
    def load_dict(
        cls,
        layout: dict[Any, Any],
        included_node_names: Optional[set[str]] = None,
        included_channel_names: Optional[set[str]] = None,
        raise_errors: bool = True,
        errors: Optional[list[LoadError]] = None,
        component_decoder: Optional[ComponentDecoder] = None,
    ) -> "House0Layout":
        if errors is None:
            errors = []
        load_args = dict(
            cacs=load_cacs(
                layout=layout,
                raise_errors=raise_errors,
                errors=errors,
            ),
            components=load_components(
                layout=layout,
                raise_errors=raise_errors,
                errors=errors,
                component_decoder=component_decoder,
            ),
            nodes=load_nodes(
                layout=layout,
                raise_errors=raise_errors,
                errors=errors,
                included_node_names=included_node_names,
            ),
            channels=load_channels(
                layout=layout,
                raise_errors=raise_errors,
                errors=errors,
                included_channel_names=included_channel_names,
            ),
        )
        resolve_links(
            load_args["nodes"],
            load_args["components"],
            raise_errors=raise_errors,
            errors=errors,
        )
        return House0Layout(layout, **load_args)

    # TODO: house 0 layout axioms that all these relay nodes exist
    @property
    def iso_valve_relay(self) -> ShNode:
        return next(
            (
                node
                for name, node in self.nodes.items()
                if name.split(".")[-1] == self.short_names.ISO_VALVE_RELAY
            )
        )
