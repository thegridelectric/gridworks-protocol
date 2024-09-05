from enum import StrEnum
from typing import Any


class BetterStrEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(
        name: str,
        start: int,  # noqa: ARG004
        count: int,  # noqa: ARG004
        last_values: list[Any],  # noqa: ARG004
    ) -> str:
        return name
