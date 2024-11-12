import json
from pathlib import Path
from typing import Any, List, Literal, Optional

from gw.errors import DcError

from gwproto.data_classes.components import Component
from gwproto.data_classes.data_channel import DataChannel
from gwproto.data_classes.hardware_layout import (
    HardwareLayout,
    LoadArgs,
    LoadError,
)
from gwproto.data_classes.house_0_names import H0N
from gwproto.data_classes.sh_node import ShNode
from gwproto.decoders import (
    CacDecoder,
    ComponentDecoder,
)
from gwproto.named_types import ComponentAttributeClassGt


class House0Layout(HardwareLayout):
    zone_list: List[str]
    total_store_tanks: int
    strategy: Literal["House0"] = "House0"

    def __init__(
        self,
        layout: dict[Any, Any],
        cacs: dict[str, ComponentAttributeClassGt],
        components: dict[str, Component[Any, Any]],
        nodes: dict[str, ShNode],
        data_channels: dict[str, DataChannel],
    ) -> None:
        super().__init__(
            layout=layout,
            cacs=cacs,
            components=components,
            nodes=nodes,
            data_channels=data_channels,
        )
        if "ZoneList" not in layout:
            raise DcError(
                "House0 requires ZoneList, a list of the thermostat zone names!"
            )
        if "TotalStoreTanks" not in layout:
            raise DcError("House0 requires TotalStoreTanks")
        if "Strategy" not in layout:
            raise DcError("House0 requires strategy")
        if not self.layout["Strategy"] == "House0":
            raise DcError("House0 requires House0 strategy!")
        self.zone_list = layout["ZoneList"]
        self.total_store_tanks = layout["TotalStoreTanks"]
        if not isinstance(self.total_store_tanks, int):
            raise TypeError("TotalStoreTanks must be an integer")
        if not 1 <= self.total_store_tanks <= 6:
            raise ValueError("Must have between 1 and 6 store tanks")
        if not isinstance(self.zone_list, List):
            raise TypeError("ZoneList must be a list")
        if not 1 <= len(self.zone_list) <= 6:
            raise ValueError("Must have between 1 and 6 store zones")
        self.short_names = H0N(self.total_store_tanks, self.zone_list)

    # overwrites base class to return correct object
    @classmethod
    def load(  # noqa: PLR0913
        cls,
        layout_path: Path | str,
        *,
        included_node_names: Optional[set[str]] = None,
        raise_errors: bool = True,
        errors: Optional[list[LoadError]] = None,
        cac_decoder: Optional[CacDecoder] = None,
        component_decoder: Optional[ComponentDecoder] = None,
    ) -> "House0Layout":
        with Path(layout_path).open() as f:
            layout = json.loads(f.read())
        return cls.load_dict(
            layout,
            included_node_names=included_node_names,
            raise_errors=raise_errors,
            errors=errors,
            cac_decoder=cac_decoder,
            component_decoder=component_decoder,
        )

    # overwrites base class to return correct object
    @classmethod
    def load_dict(  # noqa: PLR0913
        cls,
        layout: dict[Any, Any],
        *,
        included_node_names: Optional[set[str]] = None,
        raise_errors: bool = True,
        errors: Optional[list[LoadError]] = None,
        cac_decoder: Optional[CacDecoder] = None,
        component_decoder: Optional[ComponentDecoder] = None,
    ) -> "House0Layout":
        if errors is None:
            errors = []
        cacs = cls.load_cacs(
            layout=layout,
            raise_errors=raise_errors,
            errors=errors,
            cac_decoder=cac_decoder,
        )
        components = cls.load_components(
            layout=layout,
            cacs=cacs,
            raise_errors=raise_errors,
            errors=errors,
            component_decoder=component_decoder,
        )
        nodes = cls.load_nodes(
            layout=layout,
            components=components,
            raise_errors=raise_errors,
            errors=errors,
            included_node_names=included_node_names,
        )
        data_channels = cls.load_data_channels(
            layout=layout,
            nodes=nodes,
            raise_errors=raise_errors,
            errors=errors,
        )
        load_args: LoadArgs = {
            "cacs": cacs,
            "components": components,
            "nodes": nodes,
            "data_channels": data_channels,
        }
        cls.resolve_links(
            load_args["nodes"],
            load_args["components"],
            raise_errors=raise_errors,
            errors=errors,
        )
        cls.validate_layout(load_args, raise_errors=raise_errors, errors=errors)
        return House0Layout(layout, **load_args)

    @property
    def chg_dschg_relay(self) -> ShNode:
        return next(
            (
                node
                for name, node in self.nodes.items()
                if name.split(".")[-1] == self.short_names.store_charge_discharge_relay
            )
        )

    @property
    def tstat_common_relay(self) -> ShNode:
        return next(
            (
                node
                for name, node in self.nodes.items()
                if name.split(".")[-1] == self.short_names.tstat_common_relay
            )
        )

    @property
    def store_charge_discharge_relay(self) -> ShNode:
        return next(
            (
                node
                for name, node in self.nodes.items()
                if name.split(".")[-1] == self.short_names.store_charge_discharge_relay
            )
        )
