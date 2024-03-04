TaDataChannels
==========================
Python pydantic class corresponding to json type `ta.data.channels`, version `000`.

.. autoclass:: gwproto.types.TaDataChannels
    :members:

**TerminalAssetGNodeAlias**:
    - Description: GNodeAlias for the Terminal Asset. The Alias of the Terminal Asset about which the time series data is providing information. 
    - Format: LeftRightDot

**TerminalAssetGNodeId**:
    - Description: GNodeId for the Terminal Asset. The immutable unique identifier for the Terminal Asset.
    - Format: UuidCanonicalTextual

**TimeUnixS**:
    - Description: TimeUnixS. The time that this list of data channels was created
    - Format: ReasonableUnixTimeS

**Author**:
    - Description: Author of this list of data channels.

**Channels**:
    - Description: The list of data channels. 

**Identifier**:
    - Description: Identifier. Unique identifier for a specific instance of this type that can be used to establish how time series csv's were constructed.
    - Format: UuidCanonicalTextual

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.ta_data_channels.check_is_reasonable_unix_time_s
    :members:


.. autoclass:: gwproto.types.ta_data_channels.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.ta_data_channels.check_is_left_right_dot
    :members:


.. autoclass:: gwproto.types.TaDataChannels_Maker
    :members:

