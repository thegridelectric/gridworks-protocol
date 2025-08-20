# ruff: noqa: ANN401, RUF100, ANN202

from functools import lru_cache

__all__ = [
    "_get_default_cac_decoder",
    "_get_default_component_decoder",
]


@lru_cache(maxsize=1)
def _get_default_cac_decoder():
    from gwproto.decoders import CacDecoder
    from gwproto.named_types import cacs

    return CacDecoder(
        model_name="DefaultCacDecoder",
        modules=[cacs],
    )


@lru_cache(maxsize=1)
def _get_default_component_decoder():
    from gwproto.decoders import ComponentDecoder
    from gwproto.named_types import components

    return ComponentDecoder(
        model_name="DefaultComponentDecoder",
        modules=[components],
    )
