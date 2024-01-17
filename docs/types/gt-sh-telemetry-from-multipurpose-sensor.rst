GtShTelemetryFromMultipurposeSensor
==========================
Python pydantic class corresponding to json type `gt.sh.telemetry.from.multipurpose.sensor`, version `100`.

.. autoclass:: gwproto.types.GtShTelemetryFromMultipurposeSensor
    :members:

**ScadaReadTimeUnixMs**:
    - Description: ScadaReadTime in Unix MilliSeconds. 
    - Format: ReasonableUnixTimeMs

**AboutNodeAliasList**:
    - Description: AboutNodeAliasList. List of aliases of the SpaceHeat Nodes getting measured
    - Format: LeftRightDot

**TelemetryNameList**:
    - Description: TelemetryNameList. List of the TelemetryNames. The nth name in this list indicates the TelemetryName of the nth alias in the AboutNodeAliasList.

**ValueList**:
    - Description: ValueList. 

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.gt_sh_telemetry_from_multipurpose_sensor.check_is_left_right_dot
    :members:


.. autoclass:: gwproto.types.gt_sh_telemetry_from_multipurpose_sensor.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwproto.types.GtShTelemetryFromMultipurposeSensor_Maker
    :members:

