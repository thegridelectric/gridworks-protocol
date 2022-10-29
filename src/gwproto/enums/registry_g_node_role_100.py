"""Schema enum registry.g.node.role.100 definition.

Look in enums/registry_g_node_role_100 for:
    - the local python enum RegistryGNodeRole
    - the SchemaEnum RegistryGNodeRole100SchemaEnum

The SchemaEnum is a list of symbols sent in API/ABI messages. Its symbols
are not supposed to be human readable.

The LocalEnum are intended to be human readable."""

from abc import ABC
from enum import auto
from typing import Dict
from typing import List

from fastapi_utils.enums import StrEnum

from gwproto.errors import SchemaError


class RegistryGNodeRole(StrEnum):
    """
    GNodeFactory,
    WorldInstanceRegistry,
    WorldCoordinator,
    GNodeRegistry,
    GridWorks,
    
    This is the enum intended for the local application. It is forwards and backwards
    compatible with RegistryGNodeRole enums used in types.
    """

    @classmethod
    def values(cls):
        return [elt.value for elt in cls]

    GNodeFactory = auto()
    WorldInstanceRegistry = auto()
    WorldCoordinator = auto()
    GNodeRegistry = auto()
    GridWorks = auto()
    


class RegistryGNodeRoleMap:
    """ Handles the bijection
        "79503448" -  GNodeFactory,
        "baa537f6" -  WorldInstanceRegistry,
        "06469a3c" -  WorldCoordinator,
        "63a78529" -  GNodeRegistry,
        "f0f14c88" -  GridWorks,
    """
    type_name = "registry.g.node.role.100"

    symbols: List[str] = [
        "79503448",
        "baa537f6",
        "06469a3c",
        "63a78529",
        "f0f14c88",
        #
    ]

    @classmethod
    def is_symbol(cls, candidate) -> bool:
        if candidate in cls.symbols:
            return True
        return False

    @classmethod
    def type_to_local(cls, symbol):
        if not cls.is_symbol(symbol):
            raise SchemaError(
                f"{symbol} must belong to key of {RegistryGNodeRoleMap.type_to_local_dict}"
            )
        return cls.type_to_local_dict[symbol]

    @classmethod
    def local_to_type(cls, registry_g_node_role):
        if not isinstance(registry_g_node_role, RegistryGNodeRole):
            raise SchemaError(f"{registry_g_node_role} must be of type {RegistryGNodeRole}")
        return cls.local_to_type_dict[registry_g_node_role]

    type_to_local_dict: Dict[str, RegistryGNodeRole] = {
        "79503448": RegistryGNodeRole.GNodeFactory,
        "baa537f6": RegistryGNodeRole.WorldInstanceRegistry,
        "06469a3c": RegistryGNodeRole.WorldCoordinator,
        "63a78529": RegistryGNodeRole.GNodeRegistry,
        "f0f14c88": RegistryGNodeRole.GridWorks,
    }

    local_to_type_dict: Dict[RegistryGNodeRole, str] = {
        RegistryGNodeRole.GNodeFactory: "79503448",
        RegistryGNodeRole.WorldInstanceRegistry: "baa537f6",
        RegistryGNodeRole.WorldCoordinator: "06469a3c",
        RegistryGNodeRole.GNodeRegistry: "63a78529",
        RegistryGNodeRole.GridWorks: "f0f14c88",
        #
    }
