I2cMultichannelDtRelayComponentGt
==========================
Python pydantic class corresponding to json type `i2c.multichannel.dt.relay.component.gt`, version `000`.

.. autoclass:: gwproto.types.I2cMultichannelDtRelayComponentGt
    :members:

**ComponentId**:
    - Description: Component Id. Primary GridWorks identifier for a specific physical instance of a Relay, and also as a more generic Component. 
    - Format: UUID4Str

**ComponentAttributeClassId**:
    - Description: ComponentAttributeClassId. Unique identifier for the device class. Authority for these, as well as the relationship between Components and ComponentAttributeClasses (Cacs) is maintained by the World Registry. 
    - Format: UuidCanonicalTextual

**I2cAddressList**:
    - Description: I2c Address List. An ordered list of the I2c Addresses for the boards.

**ConfigList**:
    - Description: Channel Config List. A list of the ChannelConfigs for the data channels reported by the actors associated to this component's relays (actors specified in the RelayConfigLlist)

**RelayConfigList**:
    - Description: Relay Config List. Information about which actors control each relay, and the relay wiring state: (normally open, normally closed, double throw).

**DisplayName**:
    - Description: 

**HwUid**:
    - Description: Hardware Unique Id. 

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.i2c_multichannel_dt_relay_component_gt.check_is_u_u_i_d4_str
    :members:


.. autoclass:: gwproto.types.I2cMultichannelDtRelayComponentGt_Maker
    :members:

