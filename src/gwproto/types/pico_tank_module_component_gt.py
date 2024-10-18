"""Type pico.tank.reader.component.gt, version 000"""

import re
from typing import List, Literal

from pydantic import ConfigDict, model_validator
from typing_extensions import Self

from gwproto.types.component_gt import ComponentGt


class PicoTankModuleComponentGt(ComponentGt):
    PicoHwUidList: List[str]
    Enabled: bool
    SendMicroVolts: bool
    Samples: int
    NumSampleAverages: int
    TypeName: Literal["pico.tank.module.component.gt"] = "pico.tank.module.component.gt"
    Version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        if len(self.PicoHwUidList) != 2:
            raise ValueError("Check Axiom 1: Tank Modules have two picos!")
        if len(self.ConfigList) != 4:
            raise ValueError("Check Axiom 1: tank modules have 4 configs")
        channel_names = [cfg.ChannelName for cfg in self.ConfigList]
        actor_names = {n.split("-")[0] for n in channel_names}
        if len(actor_names) > 1:
            raise ValueError(
                "Channel names need to have the pattern '{actor_name}-depth{i}'"
            )
        for n in channel_names:
            try:
                n.split("-")[1]
            except IndexError:
                raise ValueError(
                    "Channel names need to have the pattern '{actor_name}-depth{i}'"
                )
            if not re.match(r"depth[1-4]$", n.split("-")[1]):
                raise ValueError(
                    "Channel names need to have the pattern '{actor_name}-depth{i}'"
                )
        return self

    @model_validator(mode="after")
    def check_axiom_2(self) -> Self:
        """
        Axiom 2: PollPeriod, CapturePeriod, AsyncCapture etc all match between 0/1
        and 2/3
        """
        return self
