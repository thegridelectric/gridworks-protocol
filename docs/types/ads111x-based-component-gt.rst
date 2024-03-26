Ads111xBasedComponentGt
==========================
Python pydantic class corresponding to json type `ads111x.based.component.gt`, version `000`.

.. autoclass:: gwproto.types.Ads111xBasedComponentGt
    :members:

**ComponentId**:
    - Description: Component Id. Primary GridWorks identifier for a specific physical instance of a MultipurposeSensor (perhaps only the 12-channel analog temp sensor), and also as a more generic Component.
    - Format: UuidCanonicalTextual

**ComponentAttributeClassId**:
    - Description: ComponentAttributeClassId. Unique identifier for the device class. Authority for these, as well as the relationship between Components and ComponentAttributeClasses (Cacs) is maintained by the World Registry.
    - Format: UuidCanonicalTextual

**DisplayName**:
    - Description: Display Name. Sample: Oak 16-channel AdsTemp Sensor <100>

**OpenVoltageByAds**:
    - Description: Open Voltage By Ads. The voltage reading with no thermistor attached is called the 'open voltage.'  It is close to the power supply voltage (e.g. 5V) , but we have found that there is non-trivial variation (~0.2 V), and there can even be variation in the average open voltage in the same installation across different ADS chips (~0.01 or 0.02V). This list follows the same order as the self.cac.AdsI2cAddressList.
    - Format: Near5

**ConfigList**:
    - Description: Config List.  The information re timing of data polling and capture for the channels read by the node.

**ThermistorConfigList**:
    - Description: Thermistor Config List. This includes the list of configuration information needed for data processing and reporting for the data collected by thermistors - both voltage and (derived) temperature. It also includes the information about what TYPE of thermistor is used.

**HwUid**:
    - Description: Hardware Unique Id.

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.ads111x_based_component_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.ads111x_based_component_gt.check_is_ads1115_i2c_address
    :members:


.. autoclass:: gwproto.types.ads111x_based_component_gt.check_is_near5
    :members:


.. autoclass:: gwproto.types.Ads111xBasedComponentGt_Maker
    :members:

