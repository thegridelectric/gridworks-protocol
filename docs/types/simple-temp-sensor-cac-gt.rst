SimpleTempSensorCacGt
==========================
Python pydantic class corresponding to json type `simple.temp.sensor.cac.gt`, version `000`.

.. autoclass:: gwproto.types.SimpleTempSensorCacGt
    :members:

**ComponentAttributeClassId**:
    - Description: ComponentAttributeClassId. Unique identifier for the device class (aka 'cac' or Component Attribute Class). Authority is maintained by the World Registry.
    - Format: UuidCanonicalTextual

**MakeModel**:
    - Description: 

**TypicalResponseTimeMs**:
    - Description: 

**Exponent**:
    - Description: Exponent. Say the TelemetryName is WaterTempCTimes1000; this corresponds to units of Celsius.  To match the implication in the name, the Exponent should be 3, and a Value of 65300 would indicate 65.3 deg C

**TempUnit**:
    - Description: 

**TelemetryName**:
    - Description: 

**DisplayName**:
    - Description: 

**CommsMethod**:
    - Description: 

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.simple_temp_sensor_cac_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.SimpleTempSensorCacGt_Maker
    :members:

