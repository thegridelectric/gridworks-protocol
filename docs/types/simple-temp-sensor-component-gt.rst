SimpleTempSensorComponentGt
==========================
Python pydantic class corresponding to json type `simple.temp.sensor.component.gt`, version `000`.

.. autoclass:: gwproto.types.SimpleTempSensorComponentGt
    :members:

**ComponentId**:
    - Description: Component Id. Primary GridWorks identifier for a specific physical instance of a SimpleTempSensor, and also as a more generic Component.
    - Format: UuidCanonicalTextual

**ComponentAttributeClassId**:
    - Description: ComponentAttributeClassId. Unique identifier for the device class. Authority for these, as well as the relationship between Components and ComponentAttributeClasses (Cacs) is maintained by the World Registry.
    - Format: UuidCanonicalTextual

**DisplayName**:
    - Description:

**HwUid**:
    - Description: Hardware Unique Id.

**Channel**:
    - Description:

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.simple_temp_sensor_component_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.SimpleTempSensorComponentGt_Maker
    :members:
