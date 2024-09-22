from enum import auto

from gw.enums import GwStrEnum


class Role(GwStrEnum):
    """
    Categorizes SpaceheatNodes by their function within the heating system

    Enum sh.node.role version 000 in the GridWorks Type registry.

    Used by used by multiple Application Shared Languages (ASLs), including but not limited to
    gwproto. For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#shnoderole)
      - [More Info](https://gridworks-protocol.readthedocs.io/en/latest/spaceheat-node-role.html)

    Values (with symbols in parens):
      - Unknown (00000000): Unknown Role
      - Scada (d0afb424): Primary SCADA
      - HomeAlone (863e50d1): HomeAlone GNode
      - Atn (6ddff83b): AtomicTNode
      - PowerMeter (9ac68b6e): A SpaceheatNode representing the power meter that is used to settle
        financial transactions with the TerminalAsset. That is, this is the power meter whose
        accuracy is certified in the creation of the TerminalAsset GNode via creation of the
        TaDeed. [More Info](https://gridworks.readthedocs.io/en/latest/terminal-asset.html).
      - BoostElement (99c5f326): Resistive element used for providing heat to a thermal store.
      - BooleanActuator (57b788ee): A solid state or mechanical relay with two states (open, closed)
      - DedicatedThermalStore (3ecfe9b8): A dedicated thermal store within a thermal storage heating
        system - could be one or more water tanks, phase change material, etc.
      - TankWaterTempSensor (73308a1f): A temperature sensor used for measuring temperature inside
        or on the immediate outside of a water tank.
      - PipeTempSensor (c480f612): A temperature sensor used for measuring the temperature of a tank.
        Typically curved metal thermistor with thermal grease for good contact.
      - RoomTempSensor (fec74958): A temperature sensor used for measuring room temperature, or temp
        in a heated space more generally.
      - OutdoorTempSensor (5938bf1f): A temperature sensor used for measuring outdoor temperature.
      - PipeFlowMeter (ece3b600): A meter that measures flow of liquid through a pipe, in units of
        VOLUME/TIME
      - HeatedSpace (65725f44): A Heated Space.
      - HydronicPipe (fe3cbdd5): A pipe carrying techinical water or other fluid (e.g. glycol) in
        a heating system.
      - BaseboardRadiator (05fdd645): A baseboard radiator - one kind of emitter in a hydronic heating
        system.
      - RadiatorFan (6896109b): A fan that can amplify the power out of a radiator.
      - CirculatorPump (b0eaf2ba): Circulator pump for one or more of the hydronic pipe loops
      - MultiChannelAnalogTempSensor (661d7e73): An analog multi channel temperature sensor
      - Outdoors (dd975b31): The outdoors
    """

    Unknown = auto()
    Scada = auto()
    HomeAlone = auto()
    Atn = auto()
    PowerMeter = auto()
    BoostElement = auto()
    BooleanActuator = auto()
    DedicatedThermalStore = auto()
    TankWaterTempSensor = auto()
    PipeTempSensor = auto()
    RoomTempSensor = auto()
    OutdoorTempSensor = auto()
    PipeFlowMeter = auto()
    HeatedSpace = auto()
    HydronicPipe = auto()
    BaseboardRadiator = auto()
    RadiatorFan = auto()
    CirculatorPump = auto()
    MultiChannelAnalogTempSensor = auto()
    Outdoors = auto()

    @classmethod
    def default(cls) -> "Role":
        """
        Returns default value (in this case Unknown)
        """
        return cls.Unknown

    @classmethod
    def enum_name(cls) -> str:
        """
        The name in the GridWorks Type Registry (sh.node.role)
        """
        return "sh.node.role"
