"""(Mostly) static functions describing ShNodes that were in Actor/ActorBase Scada/ScadaBase.

This will probably be refactored as we implement our local registry. Currently separated out here for clarity
because content is static (except for needing a path to the houses.json file, which we should be able to do
away with).
"""

import copy
import json
import typing
from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import Any, List, Optional, Type, TypeVar

import gwproto.data_classes.components
from gwproto.data_classes.components import Component
from gwproto.data_classes.components.component import ComponentOnly
from gwproto.data_classes.components.electric_meter_component import (
    ElectricMeterComponent,
)
from gwproto.data_classes.data_channel import DataChannel
from gwproto.data_classes.errors import DataClassLoadingError
from gwproto.data_classes.resolver import ComponentResolver
from gwproto.data_classes.sh_node import ShNode
from gwproto.data_classes.telemetry_tuple import TelemetryTuple
from gwproto.default_decoders import (
    CacDecoder,
    ComponentDecoder,
    default_cac_decoder,
    default_component_decoder,
)
from gwproto.enums import ActorClass, TelemetryName
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
            raise DataClassLoadingError(  # noqa: TRY301
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
            raise DataClassLoadingError(  # noqa: TRY301
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
            "ElectricMeterComponents",
            "I2cMultichannelDtRelayComponents",
            "ResistiveHeaterComponents",
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
                    f"for node <{node_dict.get('Name')}>"
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
                node_name = node_dict["Name"]
                if included_node_names is None or node_name in included_node_names:
                    nodes[node_name] = cls.make_node(node_dict, components)
            except Exception as e:  # noqa: PERF203
                if raise_errors:
                    raise
                errors.append(LoadError("ShNode", node_dict, e))
        return nodes

    @classmethod
    def make_channel(cls, dc_dict: dict, nodes: dict[str, ShNode]) -> DataChannel:
        about_node_name = dc_dict.get("AboutNodeName")
        captured_by_node_name = dc_dict.get("CapturedByNodeName")
        about_node = nodes.get(about_node_name)
        captured_by_node = nodes.get(captured_by_node_name)
        return DataChannel(
            about_node=about_node, captured_by_node=captured_by_node, **dc_dict
        )

    @classmethod
    def load_data_channels(
        cls,
        layout: dict[Any, Any],
        nodes: dict[str, ShNode],
        *,
        raise_errors: bool = True,
        errors: Optional[list[LoadError]] = None,
        included_channel_names: Optional[set[str]] = None,
    ) -> dict[str, DataChannel]:
        dcs = {}
        if errors is None:
            errors = []
        for dc_dict in layout.get("DataChannels", []):
            try:
                dc_name = dc_dict["Name"]
                if included_channel_names is None or dc_name in included_channel_names:
                    dcs[dc_name] = cls.make_channel(dc_dict, nodes)
            except Exception as e:  # noqa: PERF203
                if raise_errors:
                    raise
                errors.append(LoadError("DataChannel", dc_dict, e))
        return dcs

    @classmethod
    def resolve_links(
        cls,
        data_channels: dict[str, DataChannel],
        nodes: dict[str, ShNode],
        components: dict[str, Component],
        *,
        raise_errors: bool = True,
        errors: Optional[list[LoadError]] = None,
    ) -> None:
        if errors is None:
            errors = []
        for dc_name, dc in data_channels.items():
            d = {"data_channel": {"name": dc_name, "data_channel": dc}}
            try:
                nodes.get(dc.AboutNodeName)
                nodes.get(dc.CapturedByNodeName)
            except Exception as e:
                if raise_errors:
                    raise
                errors.append(LoadError("DataClass", d, e))
        for node_name, node in nodes.items():
            d = {"node": {"name": node_name, "node": node}}
            try:
                if node.component_id is not None:
                    component = components.get(node.component_id, None)
                    if component is None:
                        raise DataClassLoadingError(  # noqa: TRY301
                            f"{node.name} component {node.component_id} not loaded!"
                        )
                    if isinstance(component, ComponentResolver):
                        component.resolve(
                            node.name,
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
            node.component_id: node.Name for node in self.nodes.values()
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
        included_channel_names: Optional[set[str]] = None,
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
        load_args = {
            "cacs": cacs,
            "components": components,
            "nodes": nodes,
            "data_channels": cls.load_data_channels(
                layout=layout,
                nodes=nodes,
                raise_errors=raise_errors,
                errors=errors,
                included_channel_names=included_channel_names,
            ),
        }
        cls.resolve_links(
            load_args["data_channels"],
            load_args["nodes"],
            load_args["components"],
            raise_errors=raise_errors,
            errors=errors,
        )
        return HardwareLayout(layout, **load_args)

    def node(self, name: str, default: Any = None) -> ShNode:  # noqa: ANN401
        return self.nodes.get(name, default)

    def component(self, node_name: str) -> Optional[Component]:
        return self.component_from_node(self.node(node_name, None))

    def cac(self, node_name: str) -> Optional[ComponentAttributeClassGt]:
        return self.component(node_name).cac

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

    # @classmethod
    # def parent_alias(cls, alias: str) -> str:
    #     last_delimiter = alias.rfind(".")
    #     if last_delimiter == -1:
    #         return ""
    #     return alias[:last_delimiter]

    # def parent_node(self, alias: str) -> Optional[ShNode]:
    #     parent_alias = self.parent_alias(alias)
    #     if not parent_alias:
    #         return None
    #     if parent_alias not in self.nodes:
    #         raise DataClassLoadingError(f"{alias} is missing parent {parent_alias}!")
    #     return self.node(parent_alias)

    # def descendants(self, alias: str) -> List[ShNode]:
    #     return list(filter(lambda x: x.alias.startswith(alias), self.nodes.values()))

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
    def power_meter_node(self) -> ShNode:
        """Schema for input data enforces exactly one Spaceheat Node with role PowerMeter"""
        return next(
            filter(
                lambda x: x.actor_class == ActorClass.PowerMeter, self.nodes.values()
            )
        )

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
        return self.power_meter_node.component.cac  # type: ignore[union-attr, return-value]

    @cached_property
    def scada_node(self) -> ShNode:
        """Schema for input data enforces exactly one Spaceheat Node with role Scada"""
        nodes = list(
            filter(lambda x: x.actor_class == ActorClass.Scada, self.nodes.values())
        )
        return nodes[0]

    @cached_property
    def home_alone_node(self) -> ShNode:
        """Schema for input data enforces exactly one Spaceheat Node with role HomeAlone"""
        nodes = list(
            filter(lambda x: x.actor_class == ActorClass.HomeAlone, self.nodes.values())
        )
        return nodes[0]

    @cached_property
    def my_home_alone(self) -> ShNode:
        all_nodes = list(self.nodes.values())
        home_alone_nodes = list(
            filter(lambda x: (x.actor_class == ActorClass.HomeAlone), all_nodes)
        )
        if len(home_alone_nodes) != 1:
            raise ValueError(
                "there should be a single SpaceheatNode with role HomeAlone"
            )
        return home_alone_nodes[0]

    @cached_property
    def my_boolean_actuators(self) -> List[ShNode]:
        all_nodes = list(self.nodes.values())
        return list(filter(lambda x: (x.actor_class == ActorClass.Relay), all_nodes))

    @cached_property
    def my_telemetry_tuples(self) -> List[TelemetryTuple]:
        return [
            TelemetryTuple(
                AboutNode=dc.about_node,
                SensorNode=dc.captured_by_node,
                TelemetryName=dc.TelemetryName,
            )
            for dc in self.data_channels.values()
        ]
