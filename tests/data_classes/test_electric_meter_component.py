# import pytest
# from gwproto.data_classes.components.electric_meter_component import (
#     ElectricMeterComponent,
# )
# from gwproto.data_classes.component_attribute_class import ComponentAttributeClass
# from gwproto.types.electric_meter_component_gt import ElectricMeterComponentGt, ElectricMeterComponentGt_Maker
# from gwproto.data_classes.cacs.electric_meter_cac import ElectricMeterCac
# from gwproto.types import ChannelConfig
# from gwproto.types import ElectricMeterCacGt, ElectricMeterCacGt_Maker
# from gwproto.types import EgaugeIo
# from gwproto.types import EgaugeRegisterConfig

# from gwproto.enums import MakeModel, TelemetryName, Unit
# from gwproto.type_helpers import CACS_BY_MAKE_MODEL
# from gwproto.data_classes.component import Component
# from gwproto.errors import DcError
# # Running the below disrupts other tests. Need to set up the
# # test isolation as per scada


# def test_electric_meter_component():
#     cac_gt = ElectricMeterCacGt(
#         ComponentAttributeClassId=CACS_BY_MAKE_MODEL[MakeModel.EGAUGE__4030],
#         MakeModel=MakeModel.EGAUGE__4030,
#         DisplayName="eGauge 4030",
#         TelemetryNameList=[TelemetryName.PowerW, TelemetryName.VoltageRmsMilliVolts],
#         MinPollPeriodMs=1000,
#         DefaultBaud=9600,
#     )
    
#     comp_gt = ElectricMeterComponentGt(
#         ComponentId="04ceb282-d7e8-4293-80b5-72455e1a5db3",
#         ComponentAttributeClassId=CACS_BY_MAKE_MODEL[MakeModel.EGAUGE__4030],
#         DisplayName="eGauge4922.local",
#         ConfigList=[
#             ChannelConfig(
#                 ChannelName="hp-idu-pwr",
#                 PollPeriodMs=1000,
#                 CapturePeriodS=60,
#                 AsyncCapture=True,
#                 AsyncCaptureDelta=20,
#                 Exponent=1,
#                 Unit=Unit.W,
#             )
#         ],
#         HwUid="35941_308",
#         ModbusHost="eGauge4922.local",
#         ModbusPort=502,
#         EgaugeIoList=[
#             EgaugeIo(
#                 ChannelName="hp-idu-pwr",
#                 InputConfig=EgaugeRegisterConfig(
#                     Address=9000,
#                     Name="",
#                     Description="change in value",
#                     Denominator=1,
#                     Type="f32",
#                     Unit=Unit.W,
#                 ),
#             )
#         ],
#     )
    
#     # Need to load the Cac as a data class first
#     with pytest.raises(DcError):
#         ElectricMeterComponentGt_Maker.tuple_to_dc(comp_gt)

#     cac = ElectricMeterCacGt_Maker.tuple_to_dc(cac_gt)
    
#     comp = ElectricMeterComponentGt_Maker.tuple_to_dc(comp_gt)

#     assert comp_gt.ComponentId in ElectricMeterComponent.by_id.keys()
#     assert comp == ElectricMeterComponent.by_id[comp_gt.ComponentId]

#     assert comp.hw_uid == "35941_308"
#     comp_gt.HwUid = "999"

#     comp2 = ElectricMeterComponentGt_Maker.tuple_to_dc(comp_gt)

#     assert comp2.hw_uid == "35941_308"
#     # flush
#     Component.by_id = {}
#     ComponentAttributeClass.by_id = {}
#     ElectricMeterComponent.by_id = {}
#     ElectricMeterCac.by_id = {}


