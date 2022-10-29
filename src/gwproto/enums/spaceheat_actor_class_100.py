"""Schema enum spaceheat.actor.class.100 definition.

Look in enums/spaceheat_actor_class_100 for:
    - the local python enum ActorClass
    - the SchemaEnum SpaceheatActorClass100SchemaEnum

The SchemaEnum is a list of symbols sent in API/ABI messages. Its symbols
are not supposed to be human readable.

The LocalEnum are intended to be human readable."""

from abc import ABC
from enum import auto
from typing import Dict
from typing import List

from fastapi_utils.enums import StrEnum

from gwproto.errors import SchemaError


class ActorClass(StrEnum):
    """
    Atn,
    MultipurposeSensor,
    Thermostat,
    BooleanActuator,
    SimpleSensor,
    None,
    HomeAlone,
    PrimaryScada,
    PrimaryMeter,
    
    This is the enum intended for the local application. It is forwards and backwards
    compatible with ActorClass enums used in types.
    """

    @classmethod
    def values(cls):
        return [elt.value for elt in cls]

    Atn = auto()
    MultipurposeSensor = auto()
    Thermostat = auto()
    BooleanActuator = auto()
    SimpleSensor = auto()
    None = auto()
    HomeAlone = auto()
    PrimaryScada = auto()
    PrimaryMeter = auto()
    


class ActorClassMap:
    """ Handles the bijection
        "12722be0" -  Atn,
        "d9ab8f4a" -  MultipurposeSensor,
        "4a9c1785" -  Thermostat,
        "d90c6ef7" -  BooleanActuator,
        "378893c5" -  SimpleSensor,
        "638bf97b" -  None,
        "32a794c9" -  HomeAlone,
        "889ed9b7" -  PrimaryScada,
        "c24a6c5f" -  PrimaryMeter,
    """
    type_name = "spaceheat.actor.class.100"

    symbols: List[str] = [
        "12722be0",
        "d9ab8f4a",
        "4a9c1785",
        "d90c6ef7",
        "378893c5",
        "638bf97b",
        "32a794c9",
        "889ed9b7",
        "c24a6c5f",
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
                f"{symbol} must belong to key of {ActorClassMap.type_to_local_dict}"
            )
        return cls.type_to_local_dict[symbol]

    @classmethod
    def local_to_type(cls, actor_class):
        if not isinstance(actor_class, ActorClass):
            raise SchemaError(f"{actor_class} must be of type {ActorClass}")
        return cls.local_to_type_dict[actor_class]

    type_to_local_dict: Dict[str, ActorClass] = {
        "12722be0": ActorClass.Atn,
        "d9ab8f4a": ActorClass.MultipurposeSensor,
        "4a9c1785": ActorClass.Thermostat,
        "d90c6ef7": ActorClass.BooleanActuator,
        "378893c5": ActorClass.SimpleSensor,
        "638bf97b": ActorClass.None,
        "32a794c9": ActorClass.HomeAlone,
        "889ed9b7": ActorClass.PrimaryScada,
        "c24a6c5f": ActorClass.PrimaryMeter,
    }

    local_to_type_dict: Dict[ActorClass, str] = {
        ActorClass.Atn: "12722be0",
        ActorClass.MultipurposeSensor: "d9ab8f4a",
        ActorClass.Thermostat: "4a9c1785",
        ActorClass.BooleanActuator: "d90c6ef7",
        ActorClass.SimpleSensor: "378893c5",
        ActorClass.None: "638bf97b",
        ActorClass.HomeAlone: "32a794c9",
        ActorClass.PrimaryScada: "889ed9b7",
        ActorClass.PrimaryMeter: "c24a6c5f",
        #
    }
