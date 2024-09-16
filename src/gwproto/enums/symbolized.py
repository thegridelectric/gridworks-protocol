from gwproto.enums.better_str_enum import BetterStrEnum


class SymbolizedEnum(BetterStrEnum):
    @classmethod
    def symbol_to_value(cls, symbol: str) -> str:
        raise NotImplementedError

    @classmethod
    def value_to_symbol(cls, value: str) -> str:
        raise NotImplementedError
