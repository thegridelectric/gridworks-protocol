"""Temporary package for assisting generation of hardware_layout.json files"""

import json
import subprocess
import uuid
from pathlib import Path
from typing import Optional

from gwproto.enums import MakeModel
from gwproto.type_helpers import CACS_BY_MAKE_MODEL
from gwproto.types import (
    ComponentAttributeClassGt,
    ComponentGt,
    DataChannelGt,
    SpaceheatNodeGt,
)


class LayoutIDMap:
    cacs_by_make_model: dict[MakeModel, str]
    unknown_cacs_by_display_name: dict[str, str]
    components_by_display_name: dict[str, str]
    nodes_by_name: dict[str, str]
    channels_by_name: dict[str, str]
    gnodes: dict[str, dict]

    def __init__(self, d: Optional[dict] = None):
        self.cacs_by_make_model = {}
        self.unknown_cacs_by_display_name = {}
        self.components_by_display_name = {}
        self.nodes_by_name = {}
        self.channels_by_name = {}
        self.gnodes = {}

        if not d:
            return
        for k, v in d.items():
            if isinstance(v, dict) and "GNodeId" in v:
                self.gnodes[k] = v
            if k == "ShNodes":
                for node in v:
                    try:
                        self.add_node(
                            node["ShNodeId"],
                            node["Name"],
                        )
                    except Exception as e:
                        raise Exception(
                            f"ERROR in LayoutIDMap() for {k}:{node}. Error: {type(e)}, <{e}>"
                        ) from e
            elif k == "DataChannels":
                for channel in v:
                    try:
                        self.add_channel(
                            channel["Id"],
                            channel["Name"],
                        )
                    except Exception as e:
                        raise Exception(
                            f"ERROR in LayoutIDMap() for {k}:{channel}. Error: {type(e)}, <{e}>"
                        ) from e
            elif k.lower().endswith("cacs"):
                for cac in v:
                    try:
                        if "DisplayName" in cac.keys():
                            display_name = cac["DisplayName"]
                        else:
                            display_name = None
                        self.add_cac(
                            cac["ComponentAttributeClassId"],
                            MakeModel(cac["MakeModel"]),
                            display_name,
                        )
                    except Exception as e:
                        raise Exception(
                            f"ERROR in LayoutIDMap() for {k}:{cac}. Error: {type(e)}, <{e}>"
                        ) from e

            elif k.lower().endswith("components"):
                for component in v:
                    try:
                        self.add_component(
                            component["ComponentId"],
                            component["DisplayName"],
                        )
                    except Exception as e:
                        raise Exception(
                            f"ERROR in LayoutIDMap() for {k}:{component}. Error: {type(e)}, <{e}>"
                        ) from e

    def add_cac(self, id_: str, make_model_: MakeModel, display_name_: Optional[str]):
        if make_model_ == MakeModel.UNKNOWNMAKE__UNKNOWNMODEL:
            if display_name_ is None:
                raise Exception(
                    "add_cacs requires a display name for Cacs w unknown MakeModel"
                )
            if id_ in self.unknown_cacs_by_display_name.values():
                # TODO: possibly allow instead to change display name here
                return
            if display_name_ in self.unknown_cacs_by_display_name:
                return
            if id_ in self.cacs_by_make_model.values():
                raise Exception(
                    f"id <{id}> already assigned to an existing cac. Not assigning to <{display_name_}>"
                )
            self.unknown_cacs_by_display_name[display_name_] = id_
        else:
            if CACS_BY_MAKE_MODEL[make_model_] != id_:
                raise Exception(
                    f"cac make model {make_model_} does not have id <{id_}>:\n"
                    "see from gwproto.type_helpers import CACS_BY_MAKE_MODEL"
                )
            if (
                id_ in self.cacs_by_make_model.values()
                or id_ in self.unknown_cacs_by_display_name.values()
            ):
                raise Exception(
                    f"id <{id_}> already assigned to an existing cac. Not assigning to <{make_model_}>"
                )
            self.cacs_by_make_model[make_model_] = id_

    def add_component(self, id_: str, display_name: str):
        self.components_by_display_name[display_name] = id_

    def add_node(self, id_: str, name: str):
        self.nodes_by_name[name] = id_

    def add_channel(self, id_: str, name: str):
        self.channels_by_name[name] = id_

    @classmethod
    def from_path(cls, path: Path) -> "LayoutIDMap":
        with path.open() as f:
            return LayoutIDMap(json.loads(f.read()))

    @classmethod
    def from_rclone(cls, rclone_name: str, upload_dir: Path) -> "LayoutIDMap":
        if not upload_dir.exists():
            upload_dir.mkdir(parents=True)
        dest_path = upload_dir / f"{rclone_name}.uploaded.json"
        upload = [
            "rclone",
            "copyto",
            f"{rclone_name}:/home/pi/.config/gridworks/scada/hardware-layout.json",
            f"{dest_path}",
        ]
        print(f"Running upload command:\n\n{' '.join(upload)}\n")
        result = subprocess.run(upload, capture_output=True, check=False)
        if result.returncode != 0:
            print(f"Command output:\n[\n{result.stderr.decode('utf-8')}\n]")
            raise RuntimeError(
                f"ERROR. Command <{' '.join(upload)}> failed with returncode:{result.returncode}"
            )
        return cls.from_path(dest_path)


class LayoutDb:
    lists: dict[str, list[ComponentAttributeClassGt | ComponentGt | SpaceheatNodeGt]]
    cacs_by_id: dict[str, ComponentAttributeClassGt]
    components_by_id: dict[str, ComponentGt]
    nodes_by_id: dict[str, SpaceheatNodeGt]
    channels_by_id: dict[str, DataChannelGt]
    loaded: LayoutIDMap
    maps: LayoutIDMap
    misc: dict

    def __init__(
        self,
        existing_layout: Optional[LayoutIDMap] = None,
        cacs: Optional[list[ComponentAttributeClassGt]] = None,
        components: Optional[list[ComponentGt]] = None,
        nodes: Optional[list[SpaceheatNodeGt]] = None,
        channels: Optional[list[DataChannelGt]] = None,
    ):
        self.lists = dict(OtherComponents=[])
        self.cacs_by_id = {}
        self.components_by_id = {}
        self.nodes_by_id = {}
        self.channels_by_id = {}
        self.misc = {}
        self.loaded = existing_layout or LayoutIDMap()
        self.maps = LayoutIDMap()
        if cacs is not None:
            self.add_cacs(cacs)
        if components is not None:
            self.add_components(components)
        if nodes is not None:
            self.add_nodes(nodes)
        if channels is not None:
            self.add_channels(channels)

    def cac_id_by_make_model(self, make_model: MakeModel) -> Optional[str]:
        return self.maps.cacs_by_make_model.get(make_model, None)

    def component_id_by_display_name(
        self, component_display_name: str
    ) -> Optional[str]:
        return self.maps.components_by_display_name.get(component_display_name, None)

    def node_id_by_name(self, node_name: str) -> Optional[str]:
        return self.maps.nodes_by_name.get(node_name, None)

    def make_cac_id(
        self, cac_make_model: MakeModel, display_name: Optional[str]
    ) -> str:
        if cac_make_model in self.loaded.cacs_by_make_model:
            return self.loaded.cacs_by_make_model[cac_make_model]
        elif cac_make_model is not MakeModel.UNKNOWNMAKE__UNKNOWNMODEL:
            return CACS_BY_MAKE_MODEL[cac_make_model]
        elif display_name is not None:
            if display_name in self.loaded.unknown_cacs_by_display_name:
                return self.loaded.unknown_cacs_by_display_name
            else:
                return str(uuid.uuid4())

    def make_component_id(self, component_display_name: str) -> str:
        return self.loaded.components_by_display_name.get(
            component_display_name, str(uuid.uuid4())
        )

    def make_node_id(self, node_name: str) -> str:
        return self.loaded.nodes_by_name.get(node_name, str(uuid.uuid4()))

    def make_channel_id(self, channel_name: str) -> str:
        return self.loaded.channels_by_name.get(channel_name, str(uuid.uuid4()))

    def add_cacs(
        self, cacs: list[ComponentAttributeClassGt], layout_list_name: str = "OtherCacs"
    ):
        for cac in cacs:
            if cac.component_attribute_class_id in self.cacs_by_id:
                print(
                    f"cac with id <{cac.component_attribute_class_id}> " "already present"
                )

            elif cac.make_model in self.maps.cacs_by_make_model:
                print(f"cac with MakeModel <{cac.make_model}> " "already present")
            else:
                self.cacs_by_id[cac.component_attribute_class_id] = cac
                self.maps.add_cac(
                    id_=cac.component_attribute_class_id,
                    make_model_=cac.make_model,
                    display_name_=cac.display_name,
                )
                if layout_list_name not in self.lists:
                    self.lists[layout_list_name] = []
                self.lists[layout_list_name].append(cac)

    def add_components(
        self, components: list[ComponentGt], layout_list_name: str = "OtherComponents"
    ):
        for component in components:
            self.components_by_id[component.component_id] = component
            self.maps.add_component(
                component.component_id,
                component.display_name,
            )
            if layout_list_name not in self.lists:
                self.lists[layout_list_name] = []
            self.lists[layout_list_name].append(component)

    def add_nodes(self, nodes: list[SpaceheatNodeGt]):
        for node in nodes:
            self.nodes_by_id[node.sh_node_id] = node
            self.maps.add_node(node.sh_node_id, node.name)
            layout_list_name = "ShNodes"
            if layout_list_name not in self.lists:
                self.lists[layout_list_name] = []
            self.lists[layout_list_name].append(node)

    def add_channels(self, channels: list[DataChannelGt]):
        for channel in channels:
            self.channels_by_id[channel.id] = channel
            self.maps.add_channel(channel.id, channel.name)
            layout_list_name = "DataChannels"
            if layout_list_name not in self.lists:
                self.lists[layout_list_name] = []
            self.lists[layout_list_name].append(channel)

    def dict(self) -> dict:
        d = dict(
            self.misc,
            **{
                list_name: [entry.as_dict() for entry in entries]
                for list_name, entries in self.lists.items()
            },
        )
        return d

    def write(self, path: str | Path) -> None:
        with Path(path).open("w") as f:
            f.write(json.dumps(self.dict(), sort_keys=True, indent=2))
