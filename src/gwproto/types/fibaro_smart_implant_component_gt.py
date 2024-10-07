from typing import Literal

from gwproto.types import ComponentGt


class FibaroSmartImplantComponentGt(ComponentGt):
    ZWaveDSK: str = ""
    TypeName: Literal["fibaro.smart.implant.component.gt"] = (
        "fibaro.smart.implant.component.gt"
    )
