from typing import Literal

from pydantic import ConfigDict

from gwproto.types import ComponentAttributeClassGt


class FibaroSmartImplantCacGt(ComponentAttributeClassGt):
    Model: str = ""
    TypeName: Literal["fibaro.smart.implant.cac.gt"] = "fibaro.smart.implant.cac.gt"
    model_config = ConfigDict(extra="allow")
