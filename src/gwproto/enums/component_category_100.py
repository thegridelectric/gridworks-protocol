"""Schema enum component.category.100 definition.

Look in enums/component_category_100 for:
    - the local python enum ComponentCategory
    - the SchemaEnum ComponentCategory100SchemaEnum

The SchemaEnum is a list of symbols sent in API/ABI messages. Its symbols
are not supposed to be human readable.

The LocalEnum are intended to be human readable."""

from abc import ABC
from enum import auto
from typing import Dict
from typing import List

from fastapi_utils.enums import StrEnum

from gwproto.errors import SchemaError


class ComponentCategory(StrEnum):
    """
    Generator,
    Load,
    Battery,
    Interconnector,
    
    This is the enum intended for the local application. It is forwards and backwards
    compatible with ComponentCategory enums used in types.
    """

    @classmethod
    def values(cls):
        return [elt.value for elt in cls]

    Generator = auto()
    Load = auto()
    Battery = auto()
    Interconnector = auto()
    


class ComponentCategoryMap:
    """ Handles the bijection
        "f8cf443b" -  Generator,
        "c8b4617d" -  Load,
        "f8b0cb6d" -  Battery,
        "b9e298b7" -  Interconnector,
    """
    type_name = "component.category.100"

    symbols: List[str] = [
        "f8cf443b",
        "c8b4617d",
        "f8b0cb6d",
        "b9e298b7",
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
                f"{symbol} must belong to key of {ComponentCategoryMap.type_to_local_dict}"
            )
        return cls.type_to_local_dict[symbol]

    @classmethod
    def local_to_type(cls, component_category):
        if not isinstance(component_category, ComponentCategory):
            raise SchemaError(f"{component_category} must be of type {ComponentCategory}")
        return cls.local_to_type_dict[component_category]

    type_to_local_dict: Dict[str, ComponentCategory] = {
        "f8cf443b": ComponentCategory.Generator,
        "c8b4617d": ComponentCategory.Load,
        "f8b0cb6d": ComponentCategory.Battery,
        "b9e298b7": ComponentCategory.Interconnector,
    }

    local_to_type_dict: Dict[ComponentCategory, str] = {
        ComponentCategory.Generator: "f8cf443b",
        ComponentCategory.Load: "c8b4617d",
        ComponentCategory.Battery: "f8b0cb6d",
        ComponentCategory.Interconnector: "b9e298b7",
        #
    }
