# ruff: noqa: ANN401, RUF100

import re
import typing
from typing import Any, Type, TypeVar

from pydantic import ValidationError

import gwproto.types.cacs
import gwproto.types.fibaro_smart_implant_component_gt  # noqa: F401
import gwproto.types.hubitat_component_gt  # noqa: F401
import gwproto.types.hubitat_poller_component_gt  # noqa: F401
import gwproto.types.hubitat_tank_component_gt  # noqa: F401
import gwproto.types.rest_poller_component_gt  # noqa: F401
import gwproto.types.web_server_component_gt  # noqa: F401
from gwproto.data_classes.component import Component
from gwproto.decoders import PydanticTypeNameDecoder
from gwproto.types import ComponentAttributeClassGt

T = TypeVar("T")


def decode_to_data_class(
    decoded_gt: typing.Any,
    return_type: Type[T],
    *,
    allow_missing_func: bool = True,
    allow_non_instance: bool = False,
) -> T:
    if hasattr(decoded_gt, "to_data_class"):
        data_class = decoded_gt.to_data_class()
        if not allow_non_instance and not isinstance(data_class, return_type):
            raise ValueError(
                f"ERROR. Returned data class {type(data_class)} is not"
                f" instance of {return_type}"
            )
        return typing.cast(T, decoded_gt.to_data_class())
    if allow_missing_func:
        raise ValueError(
            f"ERROR. Decoded type {type(decoded_gt)} has no" f" to_data_class() method."
        )
    return Component(**decoded_gt.dict())


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
    TYPE_NAME_REGEX = re.compile(r".*\.component\.gt")

    def __init__(self, model_name: str, **kwargs: Any) -> None:
        if "type_name_regex" not in kwargs:
            kwargs["type_name_regex"] = ComponentDecoder.TYPE_NAME_REGEX
        super().__init__(model_name, **kwargs)

    def decode_to_data_class(
        self,
        data: dict,
        *,
        allow_missing_func: bool = True,
    ) -> Component:
        return decode_to_data_class(
            decoded_gt=self.decode_obj(data),
            return_type=Component,
            allow_missing_func=allow_missing_func,
        )


default_cac_decoder = CacDecoder(
    model_name="DefaultCacDecoder",
    modules=[gwproto.types.cacs],
)

default_component_decoder = ComponentDecoder(
    model_name="DefaultComponentDecoder",
    module_names=[
        "gwproto.types.fibaro_smart_implant_component_gt",
        "gwproto.types.hubitat_component_gt",
        "gwproto.types.hubitat_poller_component_gt",
        "gwproto.types.hubitat_tank_component_gt",
        "gwproto.types.rest_poller_component_gt",
        "gwproto.types.web_server_component_gt",
    ],
)
