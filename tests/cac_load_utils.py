from dataclasses import dataclass, field
from typing import Any, Optional, Type

from gwproto import CacDecoder, HardwareLayout, default_cac_decoder
from gwproto.named_types import ComponentAttributeClassGt


@dataclass
class CacCase:
    tag: str
    src_cac: ComponentAttributeClassGt | dict[str, Any]
    exp_cac_type: Optional[Type[Any]] = ComponentAttributeClassGt
    exp_cac: Optional[ComponentAttributeClassGt | dict[str, Any]] = None
    exp_exceptions: list[Type[Exception]] = field(default_factory=list)


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
        return (
            f"{super().__str__()}"
            f"\n\t\t{type(self.exception)}"
            f"\n\t\t{self.exception}"
        )


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
        decoder = default_cac_decoder
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


def assert_cac_load(cases: list[CacCase], decoder: Optional[CacDecoder] = None) -> None:
    errors: list[CacCaseError] = []
    for case_idx, case in enumerate(cases):
        load_result = _decode_cac(case, decoder)
        if not load_result.ok:
            errors.append(CacLoadError(case_idx, case, load_result.exception))
        elif not case.exp_exceptions:
            exp_cac = case.src_cac if case.exp_cac is None else case.exp_cac
            if isinstance(exp_cac, dict):
                if case.exp_cac_type is None:
                    raise ValueError(
                        "When exp_cac is a dict, exp_cac_type must not be None"
                    )
                exp_cac = case.exp_cac_type(**exp_cac)
            if load_result.loaded != exp_cac:
                errors.append(
                    CacMatchError(
                        case_idx=case_idx,
                        case=case,
                        exp_cac=exp_cac,
                        loaded_cac=load_result.loaded,
                    )
                )
    if errors:
        err_str = "ERROR. Got cac load/matching errors:"
        first_exception = None
        for error in errors:
            err_str += f"\n\t{error}"
            if first_exception is None and hasattr(error, "exception"):
                first_exception = error.exception
        if first_exception is not None:
            raise ValueError(err_str) from first_exception
        raise ValueError(err_str)
