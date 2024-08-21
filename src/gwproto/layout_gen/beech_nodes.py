from gwproto.data_classes.house_0_names import House0RequiredNames


class BeechNames(House0RequiredNames):
    """
    This class provides the names of the Beech Spaceheat Nodes.
    These are immutable identifiers of the Spaceheat Nodes associated
    to the Beech SCADA GNode ("hw1.isone.me.versant.keene.beech.scada")
    """

    # zone names
    ZONE1_DOWN = "zone1-down"
    ZONE2_UP = "zone2-up"
    # important but not in all House0 tempaltes
    ELT1_PWR = "elt1-pwr"
    DIST_PUMP = "dist-pump"
    OIL_BOILER = "oil-boiler"
    # Less important, for experiments or observation only
    BUFFER_WELL = "buffer-well"
    OIL_BOILER_FLOW = "oil-boiler-flow"
    HP_FOSSIL_LWT = "hp-fossil-lwt"
    AMPHA_DIST_SWT = "ampha-dist-swt"
    AMPHB_DIST_SWT = "amphb-dist-swt"
    # readers
    ANALOG_TEMP = "analog-temp"
    BUFFER_READER = "buffer-reader"
    TANK1_READER = "tank1-reader"
    TANK2_READER = "tank2-reader"
    TANK3_READER = "tank3-reader"
    PRIMARY_POWER_METER = "primary-pwr-meter"

    def __init__(self):
        super().__init__(total_store_tanks=3, zone_list=["down", "up"])
