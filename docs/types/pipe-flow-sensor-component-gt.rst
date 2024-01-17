PipeFlowSensorComponentGt
==========================
Python pydantic class corresponding to json type `pipe.flow.sensor.component.gt`, version `000`.

.. autoclass:: gwproto.types.PipeFlowSensorComponentGt
    :members:

**ComponentId**:
    - Description: Component Id. Primary GridWorks identifier for a specific physical instance of a PipeFlowSensor, and also as a more generic Component.
    - Format: UuidCanonicalTextual

**ComponentAttributeClassId**:
    - Description: ComponentAttributeClassId. Unique identifier for the device class. Authority for these, as well as the relationship between Components and ComponentAttributeClasses (Cacs) is maintained by the World Registry.
    - Format: UuidCanonicalTextual

**I2cAddress**:
    - Description:

**ConversionFactor**:
    - Description:

**DisplayName**:
    - Description: Sample: Pipe Flow Meter Component <dist-flow>

**HwUid**:
    - Description: Hardware Unique Id.

**ExpectedMaxGpmTimes100**:
    - Description: Expected Max Flow in Gallons per Minute, times 100.

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.pipe_flow_sensor_component_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.PipeFlowSensorComponentGt_Maker
    :members:
