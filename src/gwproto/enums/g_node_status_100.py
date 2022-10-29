"""Schema enum g.node.status.100 definition.

Look in enums/g_node_status_100 for:
    - the local python enum GNodeStatus
    - the SchemaEnum GNodeStatus100SchemaEnum

The SchemaEnum is a list of symbols sent in API/ABI messages. Its symbols
are not supposed to be human readable.

The LocalEnum are intended to be human readable."""

from abc import ABC
from enum import auto
from typing import Dict
from typing import List

from fastapi_utils.enums import StrEnum

from gwproto.errors import SchemaError


class GNodeStatus(StrEnum):
    """
    PermanentlyDeactivated,
    Pending,
    Active,
    Suspended,
    
    This is the enum intended for the local application. It is forwards and backwards
    compatible with GNodeStatus enums used in types.
    """

    @classmethod
    def values(cls):
        return [elt.value for elt in cls]

    PermanentlyDeactivated = auto()
    Pending = auto()
    Active = auto()
    Suspended = auto()
    


class GNodeStatusMap:
    """ Handles the bijection
        "839b38db" -  PermanentlyDeactivated,
        "153d3475" -  Pending,
        "8d92bebe" -  Active,
        "f5831e1d" -  Suspended,
    """
    type_name = "g.node.status.100"

    symbols: List[str] = [
        "839b38db",
        "153d3475",
        "8d92bebe",
        "f5831e1d",
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
                f"{symbol} must belong to key of {GNodeStatusMap.type_to_local_dict}"
            )
        return cls.type_to_local_dict[symbol]

    @classmethod
    def local_to_type(cls, g_node_status):
        if not isinstance(g_node_status, GNodeStatus):
            raise SchemaError(f"{g_node_status} must be of type {GNodeStatus}")
        return cls.local_to_type_dict[g_node_status]

    type_to_local_dict: Dict[str, GNodeStatus] = {
        "839b38db": GNodeStatus.PermanentlyDeactivated,
        "153d3475": GNodeStatus.Pending,
        "8d92bebe": GNodeStatus.Active,
        "f5831e1d": GNodeStatus.Suspended,
    }

    local_to_type_dict: Dict[GNodeStatus, str] = {
        GNodeStatus.PermanentlyDeactivated: "839b38db",
        GNodeStatus.Pending: "153d3475",
        GNodeStatus.Active: "8d92bebe",
        GNodeStatus.Suspended: "f5831e1d",
        #
    }
