"""(Mostly) static functions describing ShNodes that were in Actor/ActorBase Scada/ScadaBase.

This will probably be refactored as we implement our local registry. Currently separated out here for clarity
because content is static (except for needing a path to the houses.json file, which we should be able to do
away with).
"""

import copy
import json
import typing
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import Any, List, Optional, Type, TypeVar

from gw.errors import DcError

import gwproto.data_classes.components
from gwproto.data_classes.components import Ads111xBasedComponent, Component
from gwproto.data_classes.components.component import ComponentOnly
from gwproto.data_classes.components.electric_meter_component import (
    ElectricMeterComponent,
)
from gwproto.types import ElectricMeterComponentGt
from gwproto.data_classes.data_channel import DataChannel
from gwproto.data_classes.resolver import ComponentResolver
from gwproto.data_classes.sh_node import ShNode
from gwproto.data_classes.telemetry_tuple import TelemetryTuple
from gwproto.default_decoders import (
    CacDecoder,
    ComponentDecoder,
    default_cac_decoder,
    default_component_decoder,
)
from gwproto.enums import ActorClass, Role, TelemetryName
from gwproto.types import (
    ComponentAttributeClassGt,
    ComponentGt,
    ElectricMeterCacGt,
)

T = TypeVar("T")


@dataclass
class LoadError:
    type_name: str
    src_dict: dict[Any, Any]
    exception: Exception


class HardwareLayout:
    layout: dict[Any, Any]
    cacs: dict[str, ComponentAttributeClassGt]
    components: dict[str, Component]
    components_by_type: dict[Type, list[Component]]
    nodes: dict[str, ShNode]
    nodes_by_component: dict[str, str]
    data_channels: dict[str, DataChannel]

    GT_SUFFIX = "Gt"

    @classmethod
    def load_cacs(
        cls,
        layout: dict[str, Any],
        *,
        raise_errors: bool = True,
        errors: Optional[list[LoadError]] = None,
        cac_decoder: Optional[CacDecoder] = None,
    ) -> dict[str, ComponentAttributeClassGt]:
        if errors is None:
            errors = []
        if cac_decoder is None:
            cac_decoder = default_cac_decoder
        cacs: dict[str, ComponentAttributeClassGt] = {}
        for type_name in [
            "Ads111xBasedCacs",
            "ResistiveHeaterCacs",
            "ElectricMeterCacs",
            "OtherCacs",
        ]:
            for cac_dict in layout.get(type_name, ()):
                try:
                    cac = cac_decoder.decode(cac_dict)
                    cacs[cac.ComponentAttributeClassId] = cac
                except Exception as e:  # noqa: PERF203
                    if raise_errors:
                        raise
                    errors.append(LoadError(type_name, cac_dict, e))
        return cacs

    @classmethod
    def get_data_class_name(cls, component_gt: ComponentGt) -> str:
        gt_class_name = component_gt.__class__.__name__
        if not gt_class_name.endswith(cls.GT_SUFFIX) or len(gt_class_name) <= len(
            cls.GT_SUFFIX
        ):
            raise DcError(  # noqa: TRY301
                f"Name of decoded component class ({gt_class_name}) "
                f"must end with <{cls.GT_SUFFIX}> "
                f"and be longer than {len(cls.GT_SUFFIX)} chars"
            )
        return gt_class_name[: -len(cls.GT_SUFFIX)]

    @classmethod
    def get_data_class_class(cls, component_gt: ComponentGt) -> Type[Component]:
        return getattr(
            gwproto.data_classes.components,
            cls.get_data_class_name(component_gt),
            ComponentOnly,
        )

    @classmethod
    def make_component(
        cls, component_gt: ComponentGt, cac: ComponentAttributeClassGt
    ) -> Component:
        if cac is None:
            raise DcError(  # noqa: TRY301
                f"cac {component_gt.ComponentAttributeClassId} not loaded for component "
                f"<{component_gt.ComponentId}/<{component_gt.DisplayName}>\n"
            )
        return cls.get_data_class_class(component_gt)(gt=component_gt, cac=cac)

    @classmethod
    def load_components(
        cls,
        layout: dict[Any, Any],
        cacs: dict[str, ComponentAttributeClassGt],
        *,
        raise_errors: bool = True,
        errors: Optional[list[LoadError]] = None,
        component_decoder: Optional[ComponentDecoder] = None,
    ) -> dict[str, Component]:
        if errors is None:
            errors = []
        if component_decoder is None:
            component_decoder = default_component_decoder
        components = {}
        for type_name in [
            "Ads111xBasedComponents",
            "ResistiveHeaterComponents",
            "ElectricMeterComponents",
            "OtherComponents",
        ]:
            for component_dict in layout.get(type_name, ()):
                try:
                    component_gt = component_decoder.decode(component_dict)
                    components[component_gt.ComponentId] = cls.make_component(
                        component_gt,
                        cacs.get(component_gt.ComponentAttributeClassId, None),
                    )
                except Exception as e:  # noqa: PERF203
                    if raise_errors:
                        raise
                    errors.append(LoadError(type_name, component_dict, e))
        return components

    @classmethod
    def make_node(cls, node_dict: dict, components: dict[str, Component]) -> ShNode:
        component_id = node_dict.get("ComponentId")
        if component_id:
            component = components.get(component_id)
            if component is None:
                raise ValueError(
                    f"ERROR. Component <{component_id}> not loaded "
                    f"for node <{node_dict.get('Alias')}>"
                )
        else:
            component = None
        return ShNode(component=component, **node_dict)

    @classmethod
    def load_nodes(
        cls,
        layout: dict[Any, Any],
        components: dict[str, Component],
        *,
        raise_errors: bool = True,
        errors: Optional[list[LoadError]] = None,
        included_node_names: Optional[set[str]] = None,
    ) -> dict[str, ShNode]:
        nodes = {}
        if errors is None:
            errors = []
        for node_dict in layout.get("ShNodes", []):
            try:
                node_name = node_dict["Alias"]
                if included_node_names is None or node_name in included_node_names:
                    nodes[node_name] = cls.make_node(node_dict, components)
            except Exception as e:  # noqa: PERF203
                if raise_errors:
                    raise
                errors.append(LoadError("ShNode", node_dict, e))
        return nodes

    @classmethod
    def make_channel(cls, dc_dict: dict, nodes: dict[str, ShNode]) -> DataChannel:
        about_node = nodes.get(dc_dict.get("AboutNodeName"))
        captured_by_node = nodes.get(dc_dict.get("CapturedByNodeName"))
        if about_node is None or captured_by_node is None:
            raise ValueError(
                f"ERROR. DataChannel related nodes must exist for {dc_dict.get('Name')}!\n"
                f"  For AboutNodeName <{dc_dict.get('AboutNodeName')}> "
                f"got {about_node}\n"
                f"  for CapturedByNodeName <{dc_dict.get('CapturedByNodeName')}>"
                f"got {captured_by_node}"
            )
        return DataChannel(
            about_node=about_node, captured_by_node=captured_by_node, **dc_dict
        )

    @classmethod
    def check_dc_id_uniqueness(
        cls,
        data_channels: dict[str, DataChannel],
    ) -> None:
        id_counter = Counter(dc.Id for dc in data_channels.values())
        dupes = [node_id for node_id, count in id_counter.items() if count > 1]
        if dupes:
            raise DcError(f"Duplicate dc.Id(s) found: {dupes}")

    @classmethod
    def check_node_channel_consistency(
        cls,
        nodes: dict[str, ShNode],
        data_channels: dict[str, DataChannel]
    ) -> None:
        capturing_classes = [
            ActorClass.PowerMeter,
            ActorClass.MultipurposeSensor,
        ]
        active_nodes = [node for node in nodes.values() if node.ActorClass in capturing_classes]
        for node in active_nodes:
            c: ComponentGt = node.component.gt
            my_channel_names = [config.ChannelName for config in c.ConfigList]
            my_channels = [dc for dc in data_channels.values() if dc.Name in my_channel_names]
            for channel in my_channels:
                if channel.CapturedByNodeName != node.Alias:
                    raise DcError(f"Channel {channel} should have CapturedByNodeName {node.Alias}")
        

    @classmethod
    def check_data_channel_consistency(
        cls,
        nodes: dict[str, ShNode],
        components: dict[str, Component],
        data_channels: dict[str, DataChannel],
    ) -> None:
        cls.check_dc_id_uniqueness(data_channels)
        dc_names_by_component = set()
        for c in components.values():
            channel_names = {config.ChannelName for config in c.gt.ConfigList}
            if dc_names_by_component & channel_names:
                raise DcError(
                    f"Channel name overlap!: {dc_names_by_component & channel_names}"
                )
            dc_names_by_component.update(channel_names)
        actual_dc_names = {dc.Name for dc in data_channels.values()}
        if dc_names_by_component != actual_dc_names:
            by_comp = list(dc_names_by_component)
            by_comp.sort()
            actual = list(actual_dc_names)
            actual.sort()
            raise DcError(
                "Channel inconsistency! \n"
                f"From Components:{by_comp}\n"
                f"From DataChannel list:{actual}\n"
            )
        cls.check_node_channel_consistency(nodes, data_channels)
    
    @classmethod
    def check_actor_component_consistency(cls, nodes: dict[str,ShNode]) -> None:
        pm_nodes = [node for node in nodes.values() if node.ActorClass == ActorClass.PowerMeter]
        for node in pm_nodes:
            if node.component.gt.TypeName != "electric.meter.component.gt":
                raise DcError(f"Power Meter node {node} needs ElectricMeterComponent."
                              f"Got {node.component.gt}")
        em_nodes = [node for node in nodes.values() if node.ActorClass == ActorClass.MultipurposeSensor]
        for node in em_nodes:
            multi_comp_type_names = ["ads111x.based.component.gt"]
            if node.component.gt.TypeName not in multi_comp_type_names:
                raise DcError(f"Power Meter node {node} needs Compeont "
                              f"in {multi_comp_type_names}. Got "
                              f"{node.component.gt}")

    @classmethod
    def check_node_unique_ids(cls, nodes: dict[str, ShNode]) -> None:
        id_counter = Counter(node.ShNodeId for node in nodes.values())
        dupes = [node_id for node_id, count in id_counter.items() if count > 1]
        if dupes:
            raise DcError(f"Duplicate ShNodeId(s) found: {dupes}")

    @classmethod
    def check_transactive_metering_consistency(
        cls, nodes: dict[str, ShNode], data_channels: dict[str, DataChannel]
    ) -> None:
        transactive_nodes = {node for node in nodes.values() if node.InPowerMetering}
        transactive_channels = {
            dc for dc in data_channels.values() if dc.InPowerMetering
        }
        # Part 1: If a data channel is in transactive_channels, its about_node must be in transactive_nodes
        for tc in transactive_channels:
            if tc.about_node not in transactive_nodes:
                raise DcError(
                    f"Data channel {tc} has about_node {tc.about_node}, which does not have InPowerMetering!"
                )
        # Check condition 2: If a node is in transactive_nodes, there must be a data channel with that node as about_node
        for node in transactive_nodes:
            if not any(tc for tc in transactive_channels if tc.about_node == node):
                raise DcError(
                    f"Node {node} is in transactive_nodes but no data channel with InPowerMetering has this node as about_node"
                )

    @classmethod
    def check_ads_terminal_block_consistency(cls, c: Ads111xBasedComponent) -> None:
        possible_indices = set(
            range(1, c.cac.TotalTerminalBlocks + 1)
        )  # e,g {1, .., 12}
        actual_indices = {tc.TerminalBlockIdx for tc in c.gt.ConfigList}
        if not actual_indices.issubset(possible_indices):
            raise DcError(
                f"Terminal Block indices {actual_indices}"
                f"When Ads only has {c.cac.TotalTerminalBlocks} terminal blocks!"
            )

    @classmethod
    def load_data_channels(
        cls,
        layout: dict[Any, Any],
        nodes: dict[str, ShNode],
        *,
        raise_errors: bool = True,
        errors: Optional[list[LoadError]] = None,
    ) -> dict[str, DataChannel]:
        dcs = {}
        if errors is None:
            errors = []
        for dc_dict in layout.get("DataChannels", []):
            try:
                dc_name = dc_dict["Name"]
                dcs[dc_name] = cls.make_channel(dc_dict, nodes)
            except Exception as e:  # noqa: PERF203
                if raise_errors:
                    raise
                errors.append(LoadError("DataChannel", dc_dict, e))
        return dcs

    @classmethod
    def resolve_links(
        cls,
        nodes: dict[str, ShNode],
        components: dict[str, Component],
        *,
        raise_errors: bool = True,
        errors: Optional[list[LoadError]] = None,
    ) -> None:
        if errors is None:
            errors = []
        for node_name, node in nodes.items():
            d = {"node": {"name": node_name, "node": node}}
            try:
                if node.component_id is not None:
                    component = components.get(node.component_id, None)
                    if component is None:
                        raise DcError(  # noqa: TRY301
                            f"{node.alias} component {node.component_id} not loaded!"
                        )
                    if isinstance(component, ComponentResolver):
                        component.resolve(
                            node.alias,
                            nodes,
                            components,
                        )
            except Exception as e:
                if raise_errors:
                    raise
                errors.append(LoadError("ShNode", d, e))

    def __init__(
        self,
        layout: dict[Any, Any],
        *,
        cacs: dict[str, ComponentAttributeClassGt],
        components: dict[str, Component],
        nodes: dict[str, ShNode],
        data_channels: dict[str, DataChannel],
    ) -> None:
        self.layout = copy.deepcopy(layout)
        self.cacs = dict(cacs)
        self.components = dict(components)
        self.components_by_type = defaultdict(list)
        for component in self.components.values():
            self.components_by_type[type(component)].append(component)
        self.nodes = dict(nodes)
        self.nodes_by_component = {
            node.component_id: node.alias for node in self.nodes.values()
        }
        self.data_channels = dict(data_channels)

    def clear_property_cache(self) -> None:
        for cached_prop_name in [
            prop_name
            for prop_name in type(self).__dict__
            if isinstance(type(self).__dict__[prop_name], cached_property)
        ]:
            self.__dict__.pop(cached_prop_name, None)

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
    ) -> "HardwareLayout":
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
    ) -> "HardwareLayout":
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
        load_args = {
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
        try:
            cls.check_node_unique_ids(nodes)
        except Exception as e:  # noqa: PERF203
            if raise_errors:
                raise
            errors.append(LoadError("hardware.layout", nodes, e))
        try: 
            cls.check_actor_component_consistency(nodes)
        except Exception as e:  # noqa: PERF203
            if raise_errors:
                raise
            errors.append(LoadError("hardware.layout", nodes, e))
        try:
            cls.check_data_channel_consistency(
                nodes,
                components,
                data_channels,
            )
            cls.check_transactive_metering_consistency(
                nodes,
                data_channels,
            )
        except Exception as e:  # noqa: PERF203
            if raise_errors:
                raise
            errors.append(LoadError("data.channel.gt", layout, e))
        ads111x_components = [
            comp
            for comp in components.values()
            if isinstance(comp, Ads111xBasedComponent)
        ]
        for c in ads111x_components:
            try:
                cls.check_ads_terminal_block_consistency(c)
            except Exception as e:  # noqa: PERF203
                if raise_errors:
                    raise
                errors.append(
                    LoadError("ads111x.based.component.gt", c.gt.model_dump(), e)
                )
        return HardwareLayout(layout, **load_args)

    def channel(self, name: str, default: Any = None) -> DataChannel:  # noqa: ANN401
        return self.data_channels.get(name, default)

    def node(self, alias: str, default: Any = None) -> ShNode:  # noqa: ANN401
        return self.nodes.get(alias, default)

    def component(self, node_alias: str) -> Optional[Component]:
        return self.component_from_node(self.node(node_alias, None))

    def cac(self, node_alias: str) -> Optional[ComponentAttributeClassGt]:
        return self.component(node_alias).cac

    def get_component_as_type(self, component_id: str, type_: Type[T]) -> Optional[T]:
        component = self.components.get(component_id, None)
        if component is not None and not isinstance(component, type_):
            raise ValueError(
                f"ERROR. Component <{component_id}> has type {type(component)} not {type_}"
            )
        return component

    def get_components_by_type(self, type_: Type[T]) -> list[T]:
        entries = self.components_by_type.get(type_, [])
        for i, entry in enumerate(entries):
            if not isinstance(entry, type_):
                raise TypeError(
                    f"ERROR. Entry {i + 1} in "
                    f"HardwareLayout.components_by_typ[{type_}] "
                    f"has the wrong type {type(entry)}"
                )
        return entries

    def node_from_component(self, component_id: str) -> Optional[ShNode]:
        return self.nodes.get(self.nodes_by_component.get(component_id, ""), None)

    def component_from_node(self, node: Optional[ShNode]) -> Optional[Component]:
        return (
            self.components.get(
                node.component_id if node.component_id is not None else "", None
            )
            if node is not None
            else None
        )

    @classmethod
    def parent_alias(cls, alias: str) -> str:
        last_delimiter = alias.rfind(".")
        if last_delimiter == -1:
            return ""
        return alias[:last_delimiter]

    def parent_node(self, alias: str) -> Optional[ShNode]:
        parent_alias = self.parent_alias(alias)
        if not parent_alias:
            return None
        if parent_alias not in self.nodes:
            raise DcError(f"{alias} is missing parent {parent_alias}!")
        return self.node(parent_alias)

    def descendants(self, alias: str) -> List[ShNode]:
        return list(filter(lambda x: x.alias.startswith(alias), self.nodes.values()))

    @cached_property
    def atn_g_node_alias(self) -> str:
        return self.layout["MyAtomicTNodeGNode"]["Alias"]  # type: ignore[no-any-return]

    @cached_property
    def atn_g_node_instance_id(self) -> str:
        return self.layout["MyAtomicTNodeGNode"]["GNodeId"]  # type: ignore[no-any-return]

    @cached_property
    def atn_g_node_id(self) -> str:
        return self.layout["MyAtomicTNodeGNode"]["GNodeId"]  # type: ignore[no-any-return]

    @cached_property
    def terminal_asset_g_node_alias(self) -> str:
        my_atn_as_dict = self.layout["MyTerminalAssetGNode"]
        return my_atn_as_dict["Alias"]  # type: ignore[no-any-return]

    @cached_property
    def terminal_asset_g_node_id(self) -> str:
        my_atn_as_dict = self.layout["MyTerminalAssetGNode"]
        return my_atn_as_dict["GNodeId"]  # type: ignore[no-any-return]

    @cached_property
    def scada_g_node_alias(self) -> str:
        my_scada_as_dict = self.layout["MyScadaGNode"]
        return my_scada_as_dict["Alias"]  # type: ignore[no-any-return]

    @cached_property
    def scada_g_node_id(self) -> str:
        my_scada_as_dict = self.layout["MyScadaGNode"]
        return my_scada_as_dict["GNodeId"]  # type: ignore[no-any-return]

    @cached_property
    def all_telemetry_tuples_for_agg_power_metering(self) -> List[TelemetryTuple]:
        telemetry_tuples = []
        for node in self.all_nodes_in_agg_power_metering:
            telemetry_tuples += [
                TelemetryTuple(
                    AboutNode=node,
                    SensorNode=self.power_meter_node,
                    TelemetryName=TelemetryName.PowerW,
                )
            ]
        return telemetry_tuples

    @cached_property
    def all_nodes_in_agg_power_metering(self) -> List[ShNode]:
        """All nodes whose power level is metered and included in power reporting by the Scada"""
        all_nodes = list(self.nodes.values())
        return list(filter(lambda x: x.in_power_metering, all_nodes))

    @cached_property
    def all_power_meter_telemetry_tuples(self) -> List[TelemetryTuple]:
        return [
            TelemetryTuple(
                AboutNode=self.node(config.AboutNodeName),
                SensorNode=self.power_meter_node,
                TelemetryName=config.TelemetryName,
            )
            for config in self.power_meter_component.gt.ConfigList
        ]

    @cached_property
    def power_meter_node(self) -> ShNode:
        """Schema for input data enforces exactly one Spaceheat Node with role PowerMeter"""
        return next(filter(lambda x: x.role == Role.PowerMeter, self.nodes.values()))

    @cached_property
    def power_meter_component(self) -> ElectricMeterComponent:
        if self.power_meter_node.component is None:
            raise ValueError(
                f"ERROR. power_meter_node {self.power_meter_node} has no component."
            )
        return typing.cast(ElectricMeterComponent, self.power_meter_node.component)

    @cached_property
    def power_meter_cac(self) -> ElectricMeterCacGt:
        if not isinstance(self.power_meter_component.cac, ElectricMeterCacGt):
            raise TypeError(
                f"ERROR. power_meter_component cac {self.power_meter_component.cac}"
                f" / {type(self.power_meter_component.cac)} is not an ElectricMeterCac"
            )
        return self.power_meter_node.component.component_attribute_class  # type: ignore[union-attr, return-value]

    @cached_property
    def all_resistive_heaters(self) -> List[ShNode]:
        all_nodes = list(self.nodes.values())
        return list(filter(lambda x: (x.role == Role.BoostElement), all_nodes))

    @cached_property
    def scada_node(self) -> ShNode:
        """Schema for input data enforces exactly one Spaceheat Node with role Scada"""
        nodes = list(filter(lambda x: x.role == Role.Scada, self.nodes.values()))
        return nodes[0]

    @cached_property
    def home_alone_node(self) -> ShNode:
        """Schema for input data enforces exactly one Spaceheat Node with role HomeAlone"""
        nodes = list(filter(lambda x: x.role == Role.HomeAlone, self.nodes.values()))
        return nodes[0]

    @cached_property
    def my_home_alone(self) -> ShNode:
        all_nodes = list(self.nodes.values())
        home_alone_nodes = list(filter(lambda x: (x.role == Role.HomeAlone), all_nodes))
        if len(home_alone_nodes) != 1:
            raise ValueError(
                "there should be a single SpaceheatNode with role HomeAlone"
            )
        return home_alone_nodes[0]

    @cached_property
    def my_boolean_actuators(self) -> List[ShNode]:
        all_nodes = list(self.nodes.values())
        return list(filter(lambda x: (x.role == Role.BooleanActuator), all_nodes))

    @cached_property
    def my_simple_sensors(self) -> List[ShNode]:
        all_nodes = list(self.nodes.values())
        return list(
            filter(
                lambda x: (
                    x.actor_class
                    in {ActorClass.SimpleSensor, ActorClass.BooleanActuator}
                ),
                all_nodes,
            )
        )

    @cached_property
    def all_multipurpose_telemetry_tuples(self) -> List[TelemetryTuple]:
        multi_nodes = list(
            filter(
                lambda x: (
                    (
                        x.actor_class
                        in {
                            ActorClass.MultipurposeSensor,
                            ActorClass.HubitatTankModule,
                            ActorClass.HubitatPoller,
                            ActorClass.HoneywellThermostat,
                        }
                    )
                    and hasattr(x.component, "config_list")
                ),
                self.nodes.values(),
            )
        )
        telemetry_tuples = []
        for node in multi_nodes:
            telemetry_tuples.extend(
                [
                    TelemetryTuple(
                        AboutNode=self.node(config.AboutNodeName),
                        SensorNode=node,
                        TelemetryName=config.TelemetryName,
                    )
                    for config in node.component.config_list
                ]
            )
        return telemetry_tuples

    @cached_property
    def my_multipurpose_sensors(self) -> List[ShNode]:
        """This will be a list of all sensing devices that either measure more
        than one ShNode or measure more than one physical quantity type (or both).
        This includes the (unique) power meter, but may also include other roles like thermostats
        and heat pumps."""
        all_nodes = list(self.nodes.values())
        multi_purpose_roles = [Role.PowerMeter, Role.MultiChannelAnalogTempSensor]
        return list(filter(lambda x: (x.role in multi_purpose_roles), all_nodes))

    @cached_property
    def my_telemetry_tuples(self) -> List[TelemetryTuple]:
        """This will include telemetry tuples from all the multipurpose sensors, the most
        important of which is the power meter."""
        return (
            self.all_power_meter_telemetry_tuples
            + self.all_multipurpose_telemetry_tuples
        )
