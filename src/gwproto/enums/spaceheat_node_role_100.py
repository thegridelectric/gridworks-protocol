"""Schema enum spaceheat.node.role.100 definition.

Look in enums/spaceheat_node_role_100 for:
    - the local python enum Role
    - the SchemaEnum SpaceheatNodeRole100SchemaEnum

The SchemaEnum is a list of symbols sent in API/ABI messages. Its symbols
are not supposed to be human readable.

The LocalEnum are intended to be human readable."""

from abc import ABC
from enum import auto
from typing import Dict
from typing import List

from fastapi_utils.enums import StrEnum

from gwproto.errors import SchemaError


class Role(StrEnum):
    """
    BooleanActuator,
    MultipurposeSensor,
    HydronicPipe,
    DedicatedThermalStore,
    Atn,
    RadiatorFan,
    PrimaryScada,
    Outdoors,
    Heatpump,
    HomeAlone,
    PipeFlowMeter,
    CurrentTransformer,
    BoostElement,
    CirculatorPump,
    HeatedSpace,
    RoomTempSensor,
    BaseboardRadiator,
    PipeTempSensor,
    OutdoorTempSensor,
    TankWaterTempSensor,
    PrimaryMeter,
    
    This is the enum intended for the local application. It is forwards and backwards
    compatible with Role enums used in types.
    """

    @classmethod
    def values(cls):
        return [elt.value for elt in cls]

    BooleanActuator = auto()
    MultipurposeSensor = auto()
    HydronicPipe = auto()
    DedicatedThermalStore = auto()
    Atn = auto()
    RadiatorFan = auto()
    PrimaryScada = auto()
    Outdoors = auto()
    Heatpump = auto()
    HomeAlone = auto()
    PipeFlowMeter = auto()
    CurrentTransformer = auto()
    BoostElement = auto()
    CirculatorPump = auto()
    HeatedSpace = auto()
    RoomTempSensor = auto()
    BaseboardRadiator = auto()
    PipeTempSensor = auto()
    OutdoorTempSensor = auto()
    TankWaterTempSensor = auto()
    PrimaryMeter = auto()
    


class RoleMap:
    """ Handles the bijection
        "7eabbec4" -  BooleanActuator,
        "41cfa90c" -  MultipurposeSensor,
        "75bea4fd" -  HydronicPipe,
        "2a6717f0" -  DedicatedThermalStore,
        "8baeafd0" -  Atn,
        "2e42e2ef" -  RadiatorFan,
        "e8d8e80f" -  PrimaryScada,
        "d3a986eb" -  Outdoors,
        "f4de2c48" -  Heatpump,
        "f4cee199" -  HomeAlone,
        "ceb28e59" -  PipeFlowMeter,
        "2f5edce8" -  CurrentTransformer,
        "5a28eb2e" -  BoostElement,
        "7abc3adc" -  CirculatorPump,
        "71410179" -  HeatedSpace,
        "433bc47b" -  RoomTempSensor,
        "fdca28dd" -  BaseboardRadiator,
        "e1578faa" -  PipeTempSensor,
        "b86977b9" -  OutdoorTempSensor,
        "758077ee" -  TankWaterTempSensor,
        "01888c51" -  PrimaryMeter,
    """
    type_name = "spaceheat.node.role.100"

    symbols: List[str] = [
        "7eabbec4",
        "41cfa90c",
        "75bea4fd",
        "2a6717f0",
        "8baeafd0",
        "2e42e2ef",
        "e8d8e80f",
        "d3a986eb",
        "f4de2c48",
        "f4cee199",
        "ceb28e59",
        "2f5edce8",
        "5a28eb2e",
        "7abc3adc",
        "71410179",
        "433bc47b",
        "fdca28dd",
        "e1578faa",
        "b86977b9",
        "758077ee",
        "01888c51",
        #
    ]

    @classmethod
    def is_symbol(cls, candidate) -> bool:
        if candidate in cls.symbols:
            return True
        return False

    @classmethod
    def type_to_local(cls, symbol):
        if not cls.is_symbol(symbol):
            raise SchemaError(
                f"{symbol} must belong to key of {RoleMap.type_to_local_dict}"
            )
        return cls.type_to_local_dict[symbol]

    @classmethod
    def local_to_type(cls, role):
        if not isinstance(role, Role):
            raise SchemaError(f"{role} must be of type {Role}")
        return cls.local_to_type_dict[role]

    type_to_local_dict: Dict[str, Role] = {
        "7eabbec4": Role.BooleanActuator,
        "41cfa90c": Role.MultipurposeSensor,
        "75bea4fd": Role.HydronicPipe,
        "2a6717f0": Role.DedicatedThermalStore,
        "8baeafd0": Role.Atn,
        "2e42e2ef": Role.RadiatorFan,
        "e8d8e80f": Role.PrimaryScada,
        "d3a986eb": Role.Outdoors,
        "f4de2c48": Role.Heatpump,
        "f4cee199": Role.HomeAlone,
        "ceb28e59": Role.PipeFlowMeter,
        "2f5edce8": Role.CurrentTransformer,
        "5a28eb2e": Role.BoostElement,
        "7abc3adc": Role.CirculatorPump,
        "71410179": Role.HeatedSpace,
        "433bc47b": Role.RoomTempSensor,
        "fdca28dd": Role.BaseboardRadiator,
        "e1578faa": Role.PipeTempSensor,
        "b86977b9": Role.OutdoorTempSensor,
        "758077ee": Role.TankWaterTempSensor,
        "01888c51": Role.PrimaryMeter,
    }

    local_to_type_dict: Dict[Role, str] = {
        Role.BooleanActuator: "7eabbec4",
        Role.MultipurposeSensor: "41cfa90c",
        Role.HydronicPipe: "75bea4fd",
        Role.DedicatedThermalStore: "2a6717f0",
        Role.Atn: "8baeafd0",
        Role.RadiatorFan: "2e42e2ef",
        Role.PrimaryScada: "e8d8e80f",
        Role.Outdoors: "d3a986eb",
        Role.Heatpump: "f4de2c48",
        Role.HomeAlone: "f4cee199",
        Role.PipeFlowMeter: "ceb28e59",
        Role.CurrentTransformer: "2f5edce8",
        Role.BoostElement: "5a28eb2e",
        Role.CirculatorPump: "7abc3adc",
        Role.HeatedSpace: "71410179",
        Role.RoomTempSensor: "433bc47b",
        Role.BaseboardRadiator: "fdca28dd",
        Role.PipeTempSensor: "e1578faa",
        Role.OutdoorTempSensor: "b86977b9",
        Role.TankWaterTempSensor: "758077ee",
        Role.PrimaryMeter: "01888c51",
        #
    }
