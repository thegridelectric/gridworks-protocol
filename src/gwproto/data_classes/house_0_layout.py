from typing import Any, List, Optional

from gwproto.data_classes.components import Component
from gwproto.data_classes.data_channel import DataChannel
from gwproto.data_classes.hardware_layout import (
    HardwareLayout,
)
from gwproto.data_classes.house_0_names import H0N
from gwproto.data_classes.sh_node import ShNode
from gwproto.named_types import ComponentAttributeClassGt


class House0StartHandles:
    scada = "h.s"
    admin = "admin"
    home_alone = "h"
    i2c_multiplexer = "admin.relay-multiplexer"


class House0Layout(HardwareLayout):
    total_zones: int
    total_store_tanks: int

    def __init__(
        self,
        layout: dict[Any, Any],
        cacs: Optional[dict[str, ComponentAttributeClassGt]] = None,  # by id
        components: Optional[dict[str, Component]] = None,  # by id
        nodes: Optional[dict[str, ShNode]] = None,  # by name
        channels: Optional[dict[str, DataChannel]] = None,  # by name
    ) -> None:
        super().__init__(
            layout=layout,
            cacs=cacs,
            components=components,
            nodes=nodes,
            data_channels=channels,
        )

        scada_dict = next((x for x in self.layout["ShNodes"] if x["Name"] == "s"), None)
        if not {"Strategy", "TotalStoreTanks", "ZoneList"} <= set(scada_dict.keys()):
            raise ValueError("Scada ShNode s needs Strategy, TotalStoreTanks, ZoneList")

        if not scada_dict["Strategy"] == "House0":
            raise ValueError("Scada node (name s) must have Strategy House0")
        self.total_store_tanks = scada_dict["TotalStoreTanks"]
        if not isinstance(self.total_store_tanks, int):
            raise TypeError("TotalStoreTanks must be an integer")
        if not 1 <= self.total_store_tanks <= 6:
            raise ValueError("Must have between 1 and 6 store tanks")
        self.zone_list = scada_dict["ZoneList"]
        if not isinstance(self.zone_list, List):
            raise TypeError("ZoneList must be a list")
        if not 1 <= len(self.zone_list) <= 6:
            raise ValueError("Must have between 1 and 6 store zones")
        self.short_names = H0N(self.total_store_tanks, self.zone_list)

    @property
    def chg_dschg_relay(self) -> ShNode:
        return next(
            (
                node
                for name, node in self.nodes.items()
                if name.split(".")[-1] == self.short_names.store_charge_discharge_relay
            )
        )
