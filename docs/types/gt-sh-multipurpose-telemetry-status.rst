GtShMultipurposeTelemetryStatus
==========================
Python pydantic class corresponding to  json type ```gt.sh.multipurpose.telemetry.status```.

.. autoclass:: gwproto.types.GtShMultipurposeTelemetryStatus
    :members:

**AboutNodeAlias**:
    - Description: AboutNodeAlias. The SpaceheatNode representing the physical object that the sensor reading is
        collecting data about. For example, a multipurpose temp sensor that reads
        12 temperatures would have data for 12 different AboutNodeAliases,
        including say `a.tank1.temp1` for a temp sensor at the top of a water tank.
    - Format: LeftRightDot

**SensorNodeAlias**:
    - Description: SensorNodeAlias. The alias of the SpaceheatNode representing the telemetry device

**TelemetryName**:
    - Description: TelemetryName. The TelemetryName of the readings. This is used to interpet the meaning of the
        reading values. For example, WaterTempCTimes1000 means the reading is measuring
        the temperature of water, in Celsius multiplied by 1000. So a value of 37000 would be
        a reading of 37 deg C.

**ValueList**:
    - Description: List of Values. The values of the readings.

**ReadTimeUnixMsList**:
    - Description: List of Read Times. The times that the MultipurposeSensor took the readings, in unix milliseconds
    - Format: ReasonableUnixTimeMs

.. autoclass:: gwproto.types.gt_sh_multipurpose_telemetry_status.check_is_left_right_dot
    :members:


.. autoclass:: gwproto.types.gt_sh_multipurpose_telemetry_status.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwproto.types.GtShMultipurposeTelemetryStatus_Maker
    :members: