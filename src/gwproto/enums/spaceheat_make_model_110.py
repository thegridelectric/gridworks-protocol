"""Schema enum spaceheat.make.model.110 definition.

Look in enums/spaceheat_make_model_110 for:
    - the local python enum MakeModel
    - the SchemaEnum SpaceheatMakeModel110SchemaEnum

The SchemaEnum is a list of symbols sent in API/ABI messages. Its symbols
are not supposed to be human readable.

The LocalEnum are intended to be human readable."""

from abc import ABC
from enum import auto
from typing import Dict
from typing import List

from fastapi_utils.enums import StrEnum

from gwproto.errors import SchemaError


class MakeModel(StrEnum):
    """
    Magnelab__SCT-0300-050,
    UnknownMake__UnknownModel,
    OpenEnergy__EmonPi,
    NCD__PR8-14-SPST,
    YMDC__SCT013-100,
    GridWorks__WaterTempHighPrecision,
    Gridworks__SimPm1,
    Gridworks__SimCurrentTransformer,
    SchneiderElectric__Iem3455,
    Egauge__3010,
    GridWorks__SimBool30AmpRelay,
    Adafruit__642,
    Rheem__XE50T10H45U0,
    
    This is the enum intended for the local application. It is forwards and backwards
    compatible with MakeModel enums used in types.
    """

    @classmethod
    def values(cls):
        return [elt.value for elt in cls]

    Magnelab__SCT-0300-050 = auto()
    UnknownMake__UnknownModel = auto()
    OpenEnergy__EmonPi = auto()
    NCD__PR8-14-SPST = auto()
    YMDC__SCT013-100 = auto()
    GridWorks__WaterTempHighPrecision = auto()
    Gridworks__SimPm1 = auto()
    Gridworks__SimCurrentTransformer = auto()
    SchneiderElectric__Iem3455 = auto()
    Egauge__3010 = auto()
    GridWorks__SimBool30AmpRelay = auto()
    Adafruit__642 = auto()
    Rheem__XE50T10H45U0 = auto()
    


class MakeModelMap:
    """ Handles the bijection
        "a8d9a70d" -  Magnelab__SCT-0300-050,
        "fe60719b" -  UnknownMake__UnknownModel,
        "c75d269f" -  OpenEnergy__EmonPi,
        "e9e93e86" -  NCD__PR8-14-SPST,
        "08da3f7d" -  YMDC__SCT013-100,
        "09185ae3" -  GridWorks__WaterTempHighPrecision,
        "b2197e5a" -  Gridworks__SimPm1,
        "d5cb9217" -  Gridworks__SimCurrentTransformer,
        "53129448" -  SchneiderElectric__Iem3455,
        "4bb099ce" -  Egauge__3010,
        "9cc57878" -  GridWorks__SimBool30AmpRelay,
        "771bd405" -  Adafruit__642,
        "899778cd" -  Rheem__XE50T10H45U0,
    """
    type_name = "spaceheat.make.model.110"

    symbols: List[str] = [
        "a8d9a70d",
        "fe60719b",
        "c75d269f",
        "e9e93e86",
        "08da3f7d",
        "09185ae3",
        "b2197e5a",
        "d5cb9217",
        "53129448",
        "4bb099ce",
        "9cc57878",
        "771bd405",
        "899778cd",
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
                f"{symbol} must belong to key of {MakeModelMap.type_to_local_dict}"
            )
        return cls.type_to_local_dict[symbol]

    @classmethod
    def local_to_type(cls, make_model):
        if not isinstance(make_model, MakeModel):
            raise SchemaError(f"{make_model} must be of type {MakeModel}")
        return cls.local_to_type_dict[make_model]

    type_to_local_dict: Dict[str, MakeModel] = {
        "a8d9a70d": MakeModel.Magnelab__SCT-0300-050,
        "fe60719b": MakeModel.UnknownMake__UnknownModel,
        "c75d269f": MakeModel.OpenEnergy__EmonPi,
        "e9e93e86": MakeModel.NCD__PR8-14-SPST,
        "08da3f7d": MakeModel.YMDC__SCT013-100,
        "09185ae3": MakeModel.GridWorks__WaterTempHighPrecision,
        "b2197e5a": MakeModel.Gridworks__SimPm1,
        "d5cb9217": MakeModel.Gridworks__SimCurrentTransformer,
        "53129448": MakeModel.SchneiderElectric__Iem3455,
        "4bb099ce": MakeModel.Egauge__3010,
        "9cc57878": MakeModel.GridWorks__SimBool30AmpRelay,
        "771bd405": MakeModel.Adafruit__642,
        "899778cd": MakeModel.Rheem__XE50T10H45U0,
    }

    local_to_type_dict: Dict[MakeModel, str] = {
        MakeModel.Magnelab__SCT-0300-050: "a8d9a70d",
        MakeModel.UnknownMake__UnknownModel: "fe60719b",
        MakeModel.OpenEnergy__EmonPi: "c75d269f",
        MakeModel.NCD__PR8-14-SPST: "e9e93e86",
        MakeModel.YMDC__SCT013-100: "08da3f7d",
        MakeModel.GridWorks__WaterTempHighPrecision: "09185ae3",
        MakeModel.Gridworks__SimPm1: "b2197e5a",
        MakeModel.Gridworks__SimCurrentTransformer: "d5cb9217",
        MakeModel.SchneiderElectric__Iem3455: "53129448",
        MakeModel.Egauge__3010: "4bb099ce",
        MakeModel.GridWorks__SimBool30AmpRelay: "9cc57878",
        MakeModel.Adafruit__642: "771bd405",
        MakeModel.Rheem__XE50T10H45U0: "899778cd",
        #
    }
