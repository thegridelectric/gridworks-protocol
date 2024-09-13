# ruff: noqa: ANN401
import re
import struct
import uuid
from datetime import datetime, timezone
from typing import Annotated, Any, Callable, List

import pydantic
from pydantic import BeforeValidator, Field

UTC_2000_01_01_TIMESTAMP = datetime(2000, 1, 1, tzinfo=timezone.utc).timestamp()
UTC_3000_01_01_TIMESTAMP = datetime(3000, 1, 1, tzinfo=timezone.utc).timestamp()


def predicate_validator(
    field_name: str,
    predicate: Callable[[Any], bool],
    error_format: str = "",
    **kwargs: dict[str, Any],
) -> classmethod:
    """
    Produce a pydantic validator from a function returning a bool.

    Example:

        from typing import Any
        from pydantic import BaseModel, ValidationError
        from gwproto.property_format import predicate_validator

        def is_truthy(v: Any) -> bool:
            return bool(v)

        class Foo(BaseModel):
            an_int: int

            _validate_an_int = predicate_validator("an_int", is_truthy)

        print(Foo(an_int=1))

        try:
            print(Foo(an_int=0))
        except ValidationError as e:
            print(e)

    Args:
        field_name: the name of the field to validate.
        predicate: the validation function. A truthy return value indicates success.
        error_format: Optional format string for use in exception raised by validation failure. Takes one parameter, 'v'.
        **kwargs: Passed to pydantic.validator()

    Returns:
        The passed in object v.
    """

    def _validator(v: Any) -> Any:
        if not predicate(v):
            if error_format:
                err_str = error_format.format(value=v)
            else:
                err_str = f"Failure of predicate on [{v}] with predicate {predicate}"
            raise ValueError(err_str)
        return v

    return pydantic.field_validator(field_name, **kwargs)(_validator)


MAC_REGEX = re.compile("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$")


def has_mac_address_format(mac_str: str) -> bool:
    return bool(MAC_REGEX.match(mac_str.lower()))


def is_short_integer(candidate: int) -> bool:
    try:
        struct.pack("h", candidate)
    except:  # noqa
        return False
    return True


def is_bit(candidate: int) -> bool:
    return not candidate not in {0, 1}


def check_is_hex_char(v: str) -> str:
    """Checks HexChar format

    HexChar format: single-char string in '0123456789abcdefABCDEF'

    Args:
        v (str): the candidate

    Raises:
        ValueError: if v is not HexChar format
    """
    if not isinstance(v, str):
        raise ValueError(f"<{v}> must be string. Got type <{type(v)}")  # noqa: TRY004
    if len(v) > 1:
        raise ValueError(f"<{v}> must be a hex char, but not of len 1")
    if v not in "0123456789abcdefABCDEF":
        raise ValueError(f"<{v}> must be one of '0123456789abcdefABCDEF'")
    return v


def check_is_left_right_dot(candidate: str) -> str:
    """Lowercase AlphanumericStrings separated by dots (i.e. periods), with most
    significant word to the left.  I.e. `d1.ne` is the child of `d1`.
    Checking the format cannot verify the significance of words. All
    words must be alphanumeric. Most significant word must start with
    an alphabet charecter


    Raises:
        ValueError: if candidate is not of lrd format (e.g. d1.iso.me.apple)
    """
    try:
        x: List[str] = candidate.split(".")
    except Exception as e:
        raise ValueError("Failed to seperate into words with split'.'") from e
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(
            f"Most significant word must start with alphabet char. Got '{first_word}'"
        )
    for word in x:
        if not word.isalnum():
            raise ValueError(
                f"words seperated by dots must be alphanumeric. Got '{word}'"
            )
    if not candidate.islower():
        raise ValueError(f"alias must be lowercase. Got '{candidate}'")
    return candidate


def str_is_valid_uuid4(v: str) -> str:
    v = str(v)
    try:
        u = uuid.UUID(v)
    except Exception as e:
        raise ValueError(f"Invalid UUID4: {v}  <{e}>") from e
    if u.version != 4:
        raise ValueError(f"{v} is valid uid, but of version {u.version}, not 4")
    return str(u)


HexChar = Annotated[str, BeforeValidator(check_is_hex_char)]

LeftRightDotStr = Annotated[str, BeforeValidator(check_is_left_right_dot)]

UUID4Str = Annotated[str, BeforeValidator(str_is_valid_uuid4)]

UTCSeconds = Annotated[
    int, Field(ge=UTC_2000_01_01_TIMESTAMP, le=UTC_3000_01_01_TIMESTAMP)
]

UTCMilliseconds = Annotated[
    int, Field(ge=UTC_2000_01_01_TIMESTAMP * 1000, le=UTC_3000_01_01_TIMESTAMP * 1000)
]
