import os
from typing import Type

from gwproto.enums.better_str_enum import BetterStrEnum


class SymbolizedEnum(BetterStrEnum):
    @classmethod
    def symbol_to_value(cls, symbol: str) -> str:
        raise NotImplementedError

    @classmethod
    def value_to_symbol(cls, value: str) -> str:
        raise NotImplementedError


DEFAULT_SYMBOLIZED_TAG = "GtEnumSymbol"
SYMBOLIZE_ENV_VAR = "SYMBOLIZE_GRIDWORKS_ENUMS"


def symbolizing() -> bool:
    return os.getenv(SYMBOLIZE_ENV_VAR, "1").lower() not in ("0", "false")


def default_enum_name(symbolized_name: str) -> str:
    return symbolized_name[: -len(DEFAULT_SYMBOLIZED_TAG)]


def default_symbolized_name(enum_name: str) -> str:
    return enum_name + DEFAULT_SYMBOLIZED_TAG


def symbolize(
    d: dict,
    *,
    enum_class: Type[SymbolizedEnum],
    enum_name: str = "",
    symbolized_name: str = "",
) -> None:
    if not enum_name:
        enum_name = enum_class.__name__
    if not symbolized_name:
        symbolized_name = default_symbolized_name(enum_name)
    if enum_name in d:
        d[symbolized_name] = enum_class.value_to_symbol(d[enum_name])
        del d[enum_name]


def desymbolize(
    d: dict,
    *,
    symbolized_name: str,
    enum_class: Type[SymbolizedEnum],
    enum_name: str = "",
) -> None:
    if not enum_name:
        enum_name = default_enum_name(symbolized_name)
    if symbolized_name in d:
        if not enum_name:
            enum_name = symbolized_name[: -len("GtEnumSymbol")]
        d[enum_name] = enum_class.symbol_to_value(d[symbolized_name])
        del d[symbolized_name]
