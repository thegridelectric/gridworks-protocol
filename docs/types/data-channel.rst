DataChannel
==========================
Python pydantic class corresponding to json type `data.channel`, version `000`.

.. autoclass:: gwproto.types.DataChannel
    :members:

**Name**:
    - Description: Name. The Channel Name is meant to be the local unique identifier for the channel within the context of a specific TerminalAsset. In addition to local uniqueness, it is immutable. It is designed to be the key that time series data is sorted by in analysis, as well as a useful way of referencing a channel within Scada code.
    - Format: SpaceheatName

**DisplayName**:
    - Description: Display Name. This display name is the handle for the data channel. It is meant to be set by the person/people who will be analyzing time series data. It is only expected to be unique within the data channels associated to a specific Terminal Asset.  Mutable.

**AboutNodeName**:
    - Description: About Name. The name of the SpaceheatNode whose physical quantities are getting captured.
    - Format: SpaceheatName

**CapturedByNodeName**:
    - Description: Captured By Name. The name of the SpaceheatNode that is capturing the physical quantities (which can be AboutName but does not have to be).
    - Format: SpaceheatName

**TelemetryName**:
    - Description: Telemetry Name. The name of the physical quantity getting measured.

**Id**:
    - Description: Id. Meant to be an immutable identifier that is globally unique (i.e., across terminal assets).
    - Format: UuidCanonicalTextual

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.data_channel.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.data_channel.check_is_spaceheat_name
    :members:


.. autoclass:: gwproto.types.DataChannel_Maker
    :members:

