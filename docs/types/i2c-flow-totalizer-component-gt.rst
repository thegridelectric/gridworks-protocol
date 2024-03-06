I2cFlowTotalizerComponentGt
==========================
Python pydantic class corresponding to json type `i2c.flow.totalizer.component.gt`, version `000`.

.. autoclass:: gwproto.types.I2cFlowTotalizerComponentGt
    :members:

**ComponentId**:
    - Description: Component Id. Primary GridWorks identifier for a specific physical instance of a PipeFlowSensor, and also as a more generic Component.
    - Format: UuidCanonicalTextual

**ComponentAttributeClassId**:
    - Description: ComponentAttributeClass. Unique identifier for the device class. Authority for these, as well as the relationship between Components and ComponentAttributeClasses (Cacs) is maintained by the World Registry. 
    - Format: UuidCanonicalTextual

**I2cAddress**:
    - Description: I2cAddress. The I2cAddress that this component can be found at on the I2cBus.

**ConfigList**:
    - Description: Config List. A list of the ChannelConfigs for the data channels reported by this actor.

**PulseFlowMeterMakeModel**:
    - Description: Pulse Flow Meter MakeModel. The MakeModel of the pulse flow meter that this I2cFlowTotalizer is attached to.

**ConversionFactor**:
    - Description: ConversionFactor. The factor that the cumulative output must be multiplied by in order to read gallons.

**DisplayName**:
    - Description: Display Name. Sample: Pipe Flow Meter Component <dist-flow>

**HwUid**:
    - Description: Hardware Unique Id. 

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.i2c_flow_totalizer_component_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.I2cFlowTotalizerComponentGt_Maker
    :members:

