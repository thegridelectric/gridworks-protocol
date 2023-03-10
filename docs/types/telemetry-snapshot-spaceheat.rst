TelemetrySnapshotSpaceheat
==========================
Python pydantic class corresponding to  json type ```telemetry.snapshot.spaceheat```.

.. autoclass:: gwproto.types.TelemetrySnapshotSpaceheat
    :members:

**ReportTimeUnixMs**:
    - Description: ReportTimeUnixMs. The time, in unix ms, that the SCADA creates this type. It may not be when the SCADA sends the type to the atn (for example if Internet is down).
    - Format: ReasonableUnixTimeMs

**AboutNodeAliasList**:
    - Description: AboutNodeAliases. The list of Spaceheat nodes in the snapshot.
    - Format: LeftRightDot

**ValueList**:
    - Description: ValueList

**TelemetryNameList**:
    - Description:

.. autoclass:: gwproto.types.telemetry_snapshot_spaceheat.check_is_left_right_dot
    :members:


.. autoclass:: gwproto.types.telemetry_snapshot_spaceheat.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwproto.types.TelemetrySnapshotSpaceheat_Maker
    :members:
