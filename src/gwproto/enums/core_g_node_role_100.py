"""Schema enum core.g.node.role.100 definition.

Look in enums/core_g_node_role_100 for:
    - the local python enum CoreGNodeRole
    - the SchemaEnum CoreGNodeRole100SchemaEnum

The SchemaEnum is a list of symbols sent in API/ABI messages. Its symbols
are not supposed to be human readable.

The LocalEnum are intended to be human readable."""

from abc import ABC
from enum import auto
from typing import Dict
from typing import List

from fastapi_utils.enums import StrEnum

from gwproto.errors import SchemaError


class CoreGNodeRole(StrEnum):
    """
    ConductorTopologyNode,
    AtomicTNode,
    TerminalAsset,
    InterconnectionComponent,
    Other,
    MarketMaker,
    AtomicMeteringNode,
    
    This is the enum intended for the local application. It is forwards and backwards
    compatible with CoreGNodeRole enums used in types.
    """

    @classmethod
    def values(cls):
        return [elt.value for elt in cls]

    ConductorTopologyNode = auto()
    AtomicTNode = auto()
    TerminalAsset = auto()
    InterconnectionComponent = auto()
    Other = auto()
    MarketMaker = auto()
    AtomicMeteringNode = auto()
    


class CoreGNodeRoleMap:
    """ Handles the bijection
        "4502e355" -  ConductorTopologyNode,
        "d9823442" -  AtomicTNode,
        "0f8872f7" -  TerminalAsset,
        "d67e564e" -  InterconnectionComponent,
        "6b58d301" -  Other,
        "86f21dd2" -  MarketMaker,
        "9521af06" -  AtomicMeteringNode,
    """
    type_name = "core.g.node.role.100"

    symbols: List[str] = [
        "4502e355",
        "d9823442",
        "0f8872f7",
        "d67e564e",
        "6b58d301",
        "86f21dd2",
        "9521af06",
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
                f"{symbol} must belong to key of {CoreGNodeRoleMap.type_to_local_dict}"
            )
        return cls.type_to_local_dict[symbol]

    @classmethod
    def local_to_type(cls, core_g_node_role):
        if not isinstance(core_g_node_role, CoreGNodeRole):
            raise SchemaError(f"{core_g_node_role} must be of type {CoreGNodeRole}")
        return cls.local_to_type_dict[core_g_node_role]

    type_to_local_dict: Dict[str, CoreGNodeRole] = {
        "4502e355": CoreGNodeRole.ConductorTopologyNode,
        "d9823442": CoreGNodeRole.AtomicTNode,
        "0f8872f7": CoreGNodeRole.TerminalAsset,
        "d67e564e": CoreGNodeRole.InterconnectionComponent,
        "6b58d301": CoreGNodeRole.Other,
        "86f21dd2": CoreGNodeRole.MarketMaker,
        "9521af06": CoreGNodeRole.AtomicMeteringNode,
    }

    local_to_type_dict: Dict[CoreGNodeRole, str] = {
        CoreGNodeRole.ConductorTopologyNode: "4502e355",
        CoreGNodeRole.AtomicTNode: "d9823442",
        CoreGNodeRole.TerminalAsset: "0f8872f7",
        CoreGNodeRole.InterconnectionComponent: "d67e564e",
        CoreGNodeRole.Other: "6b58d301",
        CoreGNodeRole.MarketMaker: "86f21dd2",
        CoreGNodeRole.AtomicMeteringNode: "9521af06",
        #
    }
