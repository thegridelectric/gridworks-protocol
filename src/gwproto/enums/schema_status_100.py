"""Schema enum schema.status.100 definition.

Look in enums/schema_status_100 for:
    - the local python enum SchemaStatus
    - the SchemaEnum SchemaStatus100SchemaEnum

The SchemaEnum is a list of symbols sent in API/ABI messages. Its symbols
are not supposed to be human readable.

The LocalEnum are intended to be human readable."""

from abc import ABC
from enum import auto
from typing import Dict
from typing import List

from fastapi_utils.enums import StrEnum

from gwproto.errors import SchemaError


class SchemaStatus(StrEnum):
    """
    Deprecated,
    Active,
    Pending,
    
    This is the enum intended for the local application. It is forwards and backwards
    compatible with SchemaStatus enums used in types.
    """

    @classmethod
    def values(cls):
        return [elt.value for elt in cls]

    Deprecated = auto()
    Active = auto()
    Pending = auto()
    


class SchemaStatusMap:
    """ Handles the bijection
        "eec5f61c" -  Deprecated,
        "c88a914d" -  Active,
        "3661506b" -  Pending,
    """
    type_name = "schema.status.100"

    symbols: List[str] = [
        "eec5f61c",
        "c88a914d",
        "3661506b",
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
                f"{symbol} must belong to key of {SchemaStatusMap.type_to_local_dict}"
            )
        return cls.type_to_local_dict[symbol]

    @classmethod
    def local_to_type(cls, schema_status):
        if not isinstance(schema_status, SchemaStatus):
            raise SchemaError(f"{schema_status} must be of type {SchemaStatus}")
        return cls.local_to_type_dict[schema_status]

    type_to_local_dict: Dict[str, SchemaStatus] = {
        "eec5f61c": SchemaStatus.Deprecated,
        "c88a914d": SchemaStatus.Active,
        "3661506b": SchemaStatus.Pending,
    }

    local_to_type_dict: Dict[SchemaStatus, str] = {
        SchemaStatus.Deprecated: "eec5f61c",
        SchemaStatus.Active: "c88a914d",
        SchemaStatus.Pending: "3661506b",
        #
    }
