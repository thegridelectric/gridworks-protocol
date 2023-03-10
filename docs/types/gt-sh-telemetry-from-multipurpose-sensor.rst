GtShTelemetryFromMultipurposeSensor
==========================
Python pydantic class corresponding to  json type ```gt.sh.telemetry.from.multipurpose.sensor```.

.. autoclass:: gwproto.types.GtShTelemetryFromMultipurposeSensor
    :members:

**ScadaReadTimeUnixMs**:
    - Description: ScadaReadTime in Unix MilliSeconds
    - Format: ReasonableUnixTimeMs

**AboutNodeAliasList**:
    - Description: AboutNodeAliasList. List of aliases of the SpaceHeat Nodes getting measured
    - Format: LeftRightDot

**TelemetryNameList**:
    - Description: TelemetryNameList. List of the TelemetryNames. The nth name in this list indicates the TelemetryName of the nth alias in the AboutNodeAliasList.

**ValueList**:
    - Description: ValueList

.. autoclass:: gwproto.types.gt_sh_telemetry_from_multipurpose_sensor.check_is_left_right_dot
    :members:


.. autoclass:: gwproto.types.gt_sh_telemetry_from_multipurpose_sensor.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwproto.types.GtShTelemetryFromMultipurposeSensor_Maker
    :members:
