import re
import uuid
from typing import Annotated

from pydantic import BeforeValidator

snake_add_underscore_to_camel_pattern = re.compile(r"(?<!^)(?=[A-Z])")


def camel_to_snake(name: str) -> str:
    return snake_add_underscore_to_camel_pattern.sub("_", name).lower()


def snake_to_camel(word: str) -> str:
    return "".join(x.capitalize() or "_" for x in word.split("_"))


def rld_alias(alias: str) -> str:
    return ".".join(reversed(alias.split(".")))


MAC_REGEX = re.compile("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$")


def has_mac_address_format(mac_str: str) -> bool:
    return bool(MAC_REGEX.match(mac_str.lower()))


def str_is_valid_uuid4(v: str) -> str:
    v = str(v)
    try:
        u = uuid.UUID(v)
    except Exception as e:
        raise ValueError(f"Invalid UUID4: {v}  <{e}>") from e
    if u.version != 4:
        raise ValueError(f"{v} is valid uid, but of version {u.version}, not 4")
    return str(u)


UUID4Str = Annotated[str, BeforeValidator(str_is_valid_uuid4)]
