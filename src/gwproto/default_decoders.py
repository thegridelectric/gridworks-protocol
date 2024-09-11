# ruff: noqa: ANN401, RUF100,
import re
from typing import Any, TypeVar

from pydantic import ValidationError

import gwproto.types.cacs
import gwproto.types.components
from gwproto.decoders import PydanticTypeNameDecoder
from gwproto.types import ComponentAttributeClassGt, ComponentGt

T = TypeVar("T")


class CacDecoder(PydanticTypeNameDecoder):
    TYPE_NAME_REGEX = re.compile(r".*\.cac\.gt")

    def __init__(self, model_name: str, **kwargs: Any) -> None:
        if "type_name_regex" not in kwargs:
            kwargs["type_name_regex"] = CacDecoder.TYPE_NAME_REGEX
        super().__init__(model_name, **kwargs)

    def decode(
        self, d: dict, *, allow_missing: bool = True
    ) -> ComponentAttributeClassGt:
        try:
            decoded = self.loader.model_validate({self.payload_field_name: d}).Payload
            if not isinstance(decoded, ComponentAttributeClassGt):
                raise TypeError(
                    f"ERROR. CacDecoder decoded type {type(decoded)}, "
                    "not ComponentAttributeClassGt"
                )
        except ValidationError as e:
            if allow_missing and any(
                error.get("type") == "union_tag_invalid" for error in e.errors()
            ):
                decoded = ComponentAttributeClassGt(**d)
            else:
                raise
        return decoded


class ComponentDecoder(PydanticTypeNameDecoder):
    TYPE_NAME_REGEX = re.compile(r".*\.?component\.gt")

    def __init__(self, model_name: str, **kwargs: Any) -> None:
        if "type_name_regex" not in kwargs:
            kwargs["type_name_regex"] = ComponentDecoder.TYPE_NAME_REGEX
        super().__init__(model_name, **kwargs)

    def decode(self, d: dict, *, allow_missing: bool = True) -> ComponentGt:
        try:
            decoded = self.loader.model_validate({self.payload_field_name: d}).Payload
            if not isinstance(decoded, ComponentGt):
                raise TypeError(
                    f"ERROR. ComponentDecoder decoded type {type(decoded)}, "
                    "not ComponentGt"
                )
        except ValidationError as e:
            if allow_missing and any(
                error.get("type") == "union_tag_invalid" for error in e.errors()
            ):
                decoded = ComponentGt(**d)
            else:
                raise
        return decoded


default_cac_decoder = CacDecoder(
    model_name="DefaultCacDecoder",
    modules=[gwproto.types.cacs],
)

default_component_decoder = ComponentDecoder(
    model_name="DefaultComponentDecoder",
    modules=[gwproto.types.components],
)
