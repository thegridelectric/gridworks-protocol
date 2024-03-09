ElectricMeterCacGt
==========================
Python pydantic class corresponding to json type `electric.meter.cac.gt`, version `001`.

.. autoclass:: gwproto.types.ElectricMeterCacGt
    :members:

**ComponentAttributeClassId**:
    - Description: ComponentAttributeClassId. Unique identifier for the device class (aka 'cac' or Component Attribute Class). Authority is maintained by the World Registry.
    - Format: UuidCanonicalTextual

**MakeModel**:
    - Description: MakeModel. The brand name identifier for the electric meter (what you would specify in order to buy one).

**DisplayName**:
    - Description: Sample: EGauge 4030

**TelemetryNameList**:
    - Description: TelemetryNames read by this power meter. 

**MinPollPeriodMs**:
    - Description: Poll Period in Milliseconds. Poll Period refers to the period of time between two readings by the local actor. This is in contrast to Capture Period, which refers to the period between readings that are sent up to the cloud (or otherwise saved for the long-term). 

**DefaultBaud**:
    - Description: To be used when the comms method requires a baud rate. 

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.electric_meter_cac_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.electric_meter_cac_gt.check_is_positive_integer
    :members:


.. autoclass:: gwproto.types.ElectricMeterCacGt_Maker
    :members:

