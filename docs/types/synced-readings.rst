SyncedReadings
==========================
Python pydantic class corresponding to json type `synced.readings`, version `000`.

.. autoclass:: gwproto.types.SyncedReadings
    :members:

**ScadaReadTimeUnixMs**:
    - Description: ScadaReadTime in Unix MilliSeconds. The single time, in unix milliseconds, assigned to this list of readings.
    - Format: UTCMilliseconds

**ChannelNameList**:
    - Description: Channel Name List. List of the names of the  Data Channels getting measured. These names are immutable and locally unique for the Scada.
    - Format: SpaceheatName

**ValueList**:
    - Description: ValueList. List of the values read.

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.synced_readings.check_is_spaceheat_name
    :members:


.. autoclass:: gwproto.types.synced_readings.check_is_u_t_c_milliseconds
    :members:


.. autoclass:: gwproto.types.SyncedReadings_Maker
    :members:

