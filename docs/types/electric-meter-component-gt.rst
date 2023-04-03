ElectricMeterComponentGt
==========================
Python pydantic class corresponding to  json type ```electric.meter.component.gt```.

.. autoclass:: gwproto.types.ElectricMeterComponentGt
    :members:

**ComponentId**:
    - Description:
    - Format: UuidCanonicalTextual

**ComponentAttributeClassId**:
    - Description:
    - Format: UuidCanonicalTextual

**DisplayName**:
    - Description: Display Name for the Power Meter

**ConfigList**:
    - Description: List of Data Channel configs . This power meter will produce multiple data channels. Each data channel measures a certain quantities (like power, current) for certain ShNodes (like a boost element or heat pump).

**HwUid**:
    - Description: Unique Hardware Id for the Power Meter

**ModbusHost**:
    - Description: Host on LAN when power meter is modbus over Ethernet

**ModbusPort**:
    - Description:

**EgaugeIoList**:
    - Description: Bijecton from EGauge4030 input to ConfigList output. This should be empty unless the MakeModel of the corresponding component attribute class is EGauge 4030. The channels that can be read from an EGauge 4030 are configurable by the person who installs the device. The information is encapsulated in a modbus map provided by eGauge as a csv from a device-specific API. The EGaugeIoList maps the data from this map to the data that the SCADA expects to see.

.. autoclass:: gwproto.types.electric_meter_component_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.ElectricMeterComponentGt_Maker
    :members:
