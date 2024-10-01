from typing import NamedTuple

from pydantic import BaseModel

from gwproto.data_classes.sh_node import ShNode
from gwproto.enums import TelemetryName
from gwproto.property_format import SpaceheatName


class TelemetryTuple(NamedTuple):
    AboutNode: ShNode
    SensorNode: ShNode
    TelemetryName: TelemetryName

    def __repr__(self) -> str:
        return f"TT({self.AboutNode.alias} {self.TelemetryName} read by {self.SensorNode.alias})"


class ChannelStub(BaseModel):
    Name: SpaceheatName
    AboutNodeName: SpaceheatName
    CapturedByNodeName: SpaceheatName
    TelemetryName: TelemetryName
    InPowerMetering: bool = False

    def __hash__(self) -> int:
        return hash(self.Name)
