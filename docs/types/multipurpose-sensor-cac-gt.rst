MultipurposeSensorCacGt
==========================
Python pydantic class corresponding to json type `multipurpose.sensor.cac.gt`, version `000`.

.. autoclass:: gwproto.types.MultipurposeSensorCacGt
    :members:

**ComponentAttributeClassId**:
    - Description: ComponentAttributeClassId. Unique identifier for the device class (aka 'cac' or Component Attribute Class). Authority is maintained by the World Registry.
    - Format: UuidCanonicalTextual

**MakeModel**:
    - Description: MakeModel. Meant to be enough to articulate any difference in how GridWorks code would interact with a device. Should be able to use this information to buy or build a device.

**PollPeriodMs**:
    - Description: Poll Period in Milliseconds. Poll Period refers to the period of time between two readings by the local actor. This is in contrast to Capture Period, which refers to the period between readings that are sent up to the cloud (or otherwise saved for the long-term).

**Exponent**:
    - Description: Exponent. Say the TelemetryName is WaterTempCTimes1000; this corresponds to units of Celsius.  To match the implication in the name, the Exponent should be 3, and a Value of 65300 would indicate 65.3 deg C

**TempUnit**:
    - Description: Temp Unit.

**TelemetryNameList**:
    - Description:

**MaxThermistors**:
    - Description: The maximum number of temperature sensors this multipurpose sensor can read.

**DisplayName**:
    - Description: Sample: GridWorks TSnap1.0 as 12-channel analog temp sensor

**CommsMethod**:
    - Description:

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.multipurpose_sensor_cac_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.MultipurposeSensorCacGt_Maker
    :members:
