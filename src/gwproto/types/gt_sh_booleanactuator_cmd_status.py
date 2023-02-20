"""Type gt.sh.booleanactuator.cmd.status, version 100"""
import json
from typing import Any
from typing import Dict
from typing import List
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gwproto.errors import MpSchemaError


def check_is_left_right_dot(v: str) -> None:
    """
    LeftRightDot format: Lowercase alphanumeric words separated by periods,
    most significant word (on the left) starting with an alphabet character.

    Raises:
        ValueError: if not LeftRightDot format
    """
    from typing import List

    try:
        x: List[str] = v.split(".")
    except:
        raise ValueError(f"Failed to seperate {v} into words with split'.'")
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(f"Most significant word of {v} must start with alphabet char.")
    for word in x:
        if not word.isalnum():
            raise ValueError(f"words of {v} split by by '.' must be alphanumeric.")
    if not v.islower():
        raise ValueError(f"All characters of {v} must be lowercase.")


def check_is_reasonable_unix_time_ms(v: str) -> None:
    """
    ReasonableUnixTimeMs format: time in unix milliseconds between Jan 1 2000 and Jan 1 3000

    Raises:
        ValueError: if not ReasonableUnixTimeMs format
    """
    import pendulum

    if pendulum.parse("2000-01-01T00:00:00Z").int_timestamp * 1000 > v:  # type: ignore[attr-defined]
        raise ValueError(f"{v} must be after Jan 1 2000")
    if pendulum.parse("3000-01-01T00:00:00Z").int_timestamp * 1000 < v:  # type: ignore[attr-defined]
        raise ValueError(f"{v} must be before Jan 1 3000")


class GtShBooleanactuatorCmdStatus(BaseModel):
    """ """

    ShNodeAlias: str = Field(
        title="ShNodeAlias",
    )
    RelayStateCommandList: List[int] = Field(
        title="RelayStateCommandList",
    )
    CommandTimeUnixMsList: List[int] = Field(
        title="CommandTimeUnixMsList",
    )
    TypeName: Literal[
        "gt.sh.booleanactuator.cmd.status"
    ] = "gt.sh.booleanactuator.cmd.status"
    Version: str = "100"

    @validator("ShNodeAlias")
    def _check_sh_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(f"ShNodeAlias failed LeftRightDot format validation: {e}")
        return v

    @validator("CommandTimeUnixMsList")
    def _check_command_time_unix_ms_list(cls, v: List) -> List:
        for elt in v:
            try:
                check_is_reasonable_unix_time_ms(elt)
            except ValueError as e:
                raise ValueError(
                    f"CommandTimeUnixMsList element {elt} failed ReasonableUnixTimeMs format validation: {e}"
                )
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class GtShBooleanactuatorCmdStatus_Maker:
    type_name = "gt.sh.booleanactuator.cmd.status"
    version = "100"

    def __init__(
        self,
        sh_node_alias: str,
        relay_state_command_list: List[int],
        command_time_unix_ms_list: List[int],
    ):

        self.tuple = GtShBooleanactuatorCmdStatus(
            ShNodeAlias=sh_node_alias,
            RelayStateCommandList=relay_state_command_list,
            CommandTimeUnixMsList=command_time_unix_ms_list,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: GtShBooleanactuatorCmdStatus) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtShBooleanactuatorCmdStatus:
        """
        Given a serialized JSON type object, returns the Python class object
        """
        try:
            d = json.loads(t)
        except TypeError:
            raise MpSchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise MpSchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> GtShBooleanactuatorCmdStatus:
        d2 = dict(d)
        if "ShNodeAlias" not in d2.keys():
            raise MpSchemaError(f"dict {d2} missing ShNodeAlias")
        if "RelayStateCommandList" not in d2.keys():
            raise MpSchemaError(f"dict {d2} missing RelayStateCommandList")
        if "CommandTimeUnixMsList" not in d2.keys():
            raise MpSchemaError(f"dict {d2} missing CommandTimeUnixMsList")
        if "TypeName" not in d2.keys():
            raise MpSchemaError(f"dict {d2} missing TypeName")

        return GtShBooleanactuatorCmdStatus(
            ShNodeAlias=d2["ShNodeAlias"],
            RelayStateCommandList=d2["RelayStateCommandList"],
            CommandTimeUnixMsList=d2["CommandTimeUnixMsList"],
            TypeName=d2["TypeName"],
            Version="100",
        )
