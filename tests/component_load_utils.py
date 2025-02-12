from dataclasses import dataclass, field
from typing import Any, Optional

from gwproto import (
    ComponentDecoder,
    HardwareLayout,
    default_component_decoder,
)
from gwproto.data_classes.components import Component
from gwproto.named_types import ComponentAttributeClassGt, ComponentGt


@dataclass
class ComponentCase:
    tag: str
    src_component_gt: ComponentGt | dict[str, Any]
    exp_component_gt_type: type[Any] = ComponentGt
    exp_component_type: type[Any] = Component
    exp_component: Optional[Component[Any, Any]] = None
    exp_exceptions: list[type[Exception]] = field(default_factory=list)


@dataclass
class ComponentCaseError:
    case_idx: int
    case: ComponentCase

    def __str__(self) -> str:
        return f"{self.case.tag:30s}  {self.case_idx:2d}  {type(self)}"


@dataclass
class ComponentLoadError(ComponentCaseError):
    exception: Exception

    def __str__(self) -> str:
        return f"{super().__str__()}\n\t\t{type(self.exception)}\n\t\t{self.exception}"


@dataclass
class ComponentMatchError(ComponentCaseError):
    exp_component: Component[Any, Any] | dict[str, Any]
    loaded_component: Component[Any, Any]

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\n\t\texp: {type(self.exp_component)}"
            f"\n\t\tgot: {type(self.loaded_component)}"
        )


@dataclass
class ComponentLoadResult:
    ok: bool
    loaded: Component[Any, Any] | None
    exception: Exception | None


def _decode_component(
    case: ComponentCase,
    decoder: Optional[ComponentDecoder],
    cacs: dict[str, ComponentAttributeClassGt],
) -> ComponentLoadResult:
    if decoder is None:
        decoder = default_component_decoder
    component_dict = (
        case.src_component_gt.model_dump()
        if isinstance(case.src_component_gt, ComponentGt)
        else case.src_component_gt
    )
    component_id = component_dict["ComponentId"]
    try:
        loaded_component = HardwareLayout.load_components(
            layout={"OtherComponents": [component_dict]},
            cacs=cacs,
            raise_errors=True,
            component_decoder=decoder,
        )[component_id]
        exception = None
    except Exception as e:  # noqa: BLE001
        loaded_component = None
        exception = e
    if loaded_component is None:
        ok = type(exception) in case.exp_exceptions
    else:
        ok = not case.exp_exceptions
    return ComponentLoadResult(ok, loaded_component, exception)


def assert_component_load(
    cases: list[ComponentCase],
    decoder: Optional[ComponentDecoder] = None,
    cacs: Optional[dict[str, ComponentAttributeClassGt]] = None,
) -> None:
    errors: list[ComponentCaseError] = []
    if cacs is None:
        cacs = HardwareLayout.load("tests/config/hardware-layout.json").cacs
    for case_idx, case in enumerate(cases):
        load_result = _decode_component(case, decoder, cacs)
        if not load_result.ok:
            assert isinstance(load_result.exception, Exception)
            errors.append(ComponentLoadError(case_idx, case, load_result.exception))
        elif not case.exp_exceptions:
            exp_component_gt = (
                case.src_component_gt
                if case.exp_component is None
                else case.exp_component
            )
            if isinstance(exp_component_gt, dict):
                exp_component_gt = case.exp_component_gt_type(**exp_component_gt)
            if case.exp_component is None:
                assert isinstance(exp_component_gt, ComponentGt)
                cac = cacs[exp_component_gt.ComponentAttributeClassId]
                exp_component = case.exp_component_type(exp_component_gt, cac)
            else:
                exp_component = case.exp_component
            if load_result.loaded.__dict__ != exp_component.__dict__:
                assert isinstance(load_result.loaded, Component)
                errors.append(
                    ComponentMatchError(
                        case_idx=case_idx,
                        case=case,
                        exp_component=exp_component,
                        loaded_component=load_result.loaded,
                    )
                )
    if errors:
        err_str = "ERROR. Got component load/matching errors:"
        first_exception = None
        for error in errors:
            err_str += f"\n\t{error}"
            if first_exception is None and hasattr(error, "exception"):
                first_exception = error.exception
        if first_exception is not None:
            raise ValueError(err_str) from first_exception
        raise ValueError(err_str)
