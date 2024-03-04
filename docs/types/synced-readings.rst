SyncedReadings
==========================
Python pydantic class corresponding to json type `synced.readings`, version `000`.

.. autoclass:: gwproto.types.SyncedReadings
    :members:

**ScadaReadTimeUnixMs**:
    - Description: ScadaReadTime in Unix MilliSeconds. The single time, in unix milliseconds, assigned to this list of readings.
    - Format: ReasonableUnixTimeMs

**AboutNodeNameList**:
    - Description: AboutNodeNameList. List of names of the SpaceHeat Nodes getting measured.
    - Format: SpaceheatName

**TelemetryNameList**:
    - Description: TelemetryNameList. List of the TelemetryNames. The nth name in this list indicates the TelemetryName of the nth alias in the AboutNodeAliasList.

**ValueList**:
    - Description: ValueList. List of the values read.

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.synced_readings.check_is_spaceheat_name
    :members:


.. autoclass:: gwproto.types.synced_readings.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwproto.types.SyncedReadings_Maker
    :members:

