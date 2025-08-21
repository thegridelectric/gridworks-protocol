from dataclasses import dataclass, field
from typing import Any, Optional

from gwproto import CacDecoder, HardwareLayout
from gwproto.default_decoders import _get_default_cac_decoder
from gwproto.named_types import ComponentAttributeClassGt


@dataclass
class CacCase:
    tag: str
    src_cac: ComponentAttributeClassGt | dict[str, Any]
    exp_cac_type: Optional[type[Any]] = ComponentAttributeClassGt
    exp_cac: Optional[ComponentAttributeClassGt | dict[str, Any]] = None
    exp_exceptions: list[type[Exception]] = field(default_factory=list)


@dataclass
class CacCaseError:
    case_idx: int
    case: CacCase

    def __str__(self) -> str:
        return f"{self.case.tag:30s}  {self.case_idx:2d}  {type(self)}"


@dataclass
class CacLoadError(CacCaseError):
    exception: Exception | None

    def __str__(self) -> str:
        return f"{super().__str__()}\n\t\t{type(self.exception)}\n\t\t{self.exception}"


@dataclass
class CacMatchError(CacCaseError):
    exp_cac: ComponentAttributeClassGt | dict[str, Any]
    loaded_cac: ComponentAttributeClassGt | None

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\n\t\texp: {type(self.exp_cac)}"
            f"\n\t\tgot: {type(self.loaded_cac)}"
        )


@dataclass
class CacLoadResult:
    ok: bool
    loaded: ComponentAttributeClassGt | None
    exception: Exception | None


def _decode_cac(case: CacCase, decoder: Optional[CacDecoder]) -> CacLoadResult:
    if decoder is None:
        decoder = _get_default_cac_decoder()
    cac_dict = (
        case.src_cac.model_dump()
        if isinstance(case.src_cac, ComponentAttributeClassGt)
        else case.src_cac
    )
    cac_id = cac_dict["ComponentAttributeClassId"]
    try:
        loaded_cac = HardwareLayout.load_cacs(
            layout={"OtherCacs": [cac_dict]},
            raise_errors=True,
            cac_decoder=decoder,
        )[cac_id]
        exception = None
    except Exception as e:  # noqa: BLE001
        loaded_cac = None
        exception = e
    if loaded_cac is None:
        ok = type(exception) in case.exp_exceptions
    else:
        ok = not case.exp_exceptions
    return CacLoadResult(ok, loaded_cac, exception)
