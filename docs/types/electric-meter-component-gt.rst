ElectricMeterComponentGt
==========================
Python pydantic class corresponding to json type `electric.meter.component.gt`, version `001`.

.. autoclass:: gwproto.types.ElectricMeterComponentGt
    :members:

**ComponentId**:
    - Description: Component Id. Primary GridWorks identifier for a specific physical instance of an  ElectricMeter, and also as a more generic Component. 
    - Format: UuidCanonicalTextual

**ComponentAttributeClassId**:
    - Description: ComponentAttributeClassId. Unique identifier for the device class. Authority for these, as well as the relationship between Components and ComponentAttributeClasses (Cacs) is maintained by the World Registry. 
    - Format: UuidCanonicalTextual

**DisplayName**:
    - Description: Display Name for the Power Meter. Sample: Oak EGauge6074

**ConfigList**:
    - Description: List of Data Channel configs . Information re timing of data polling and capture for the channels read by the node (i.e. channels that convey power, current, voltage, frequency for various power consuming elements of the system).

**HwUid**:
    - Description: Unique Hardware Id for the Power Meter. For eGauge, use what comes back over modbus address 100.

**ModbusHost**:
    - Description: Host on LAN when power meter is modbus over Ethernet. 

**ModbusPort**:
    - Description: 
    - Format: NonNegativeInteger

**EgaugeIoList**:
    - Description: Bijecton from EGauge4030 input to ConfigList output. This should be empty unless the MakeModel of the corresponding component attribute class is EGauge 4030. The channels that can be read from an EGauge 4030 are configurable by the person who installs the device. The information is encapsulated in a modbus map provided by eGauge as a csv from a device-specific API. The EGaugeIoList maps the data from this map to the data that the SCADA expects to see.

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.electric_meter_component_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.ElectricMeterComponentGt_Maker
    :members:

