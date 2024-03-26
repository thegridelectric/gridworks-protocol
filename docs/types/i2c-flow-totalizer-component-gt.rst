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

**I2cAddressList**:
    - Description: I2cAddress. The  list of I2cAddresses on the I2cBus. The assumption is each i2c address is reading from one Pulse Flow Meter.

**ConfigList**:
    - Description: Config List. A list of the ChannelConfigs for the data channels reported by this actor.

**PulseFlowMeterMakeModelList**:
    - Description: Pulse Flow Meter MakeModel. The list of MakeModels of the pulse flow meters getting read.

**ConversionFactorList**:
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

