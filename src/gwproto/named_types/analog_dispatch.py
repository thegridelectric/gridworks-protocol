"""Type analog.dispatch, version 000"""

from typing import Literal, Optional

from gw.named_types import GwBase
from pydantic import StrictInt, model_validator
from typing_extensions import Self

from gwproto.property_format import (
    HandleName,
    LeftRightDotStr,
    SpaceheatName,
    UTCMilliseconds,
    UUID4Str,
)


class AnalogDispatch(GwBase):
    """ASL schema of record [analog.dispatch v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/analog.dispatch.000.yaml)"""

    from_g_node_alias: Optional[LeftRightDotStr] = None
    from_handle: HandleName
    to_handle: HandleName
    about_name: SpaceheatName
    value: StrictInt
    trigger_id: UUID4Str
    unix_time_ms: UTCMilliseconds
    type_name: Literal["analog.dispatch"] = "analog.dispatch"
    version: Literal["000"] = "000"

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: FromHandle must be the immediate boss of ToHandle, unless ToHandle contains 'multiplexer'.

        """
        # Implement check for axiom 1"
        return self
