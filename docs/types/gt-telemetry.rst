GtTelemetry
==========================
Python pydantic class corresponding to json type `gt.telemetry`, version `110`.

.. autoclass:: gwproto.types.GtTelemetry
    :members:

**ScadaReadTimeUnixMs**:
    - Description: Scada Read Time in Unix Milliseconds.
    - Format: ReasonableUnixTimeMs

**Value**:
    - Description: Value. The value of the reading.

**Name**:
    - Description: Name. The name of the Simple Sensing Spaceheat Node. This is both the AboutNodeName and FromNodeName for a data channel. The TelemetryName (and thus Units) are expected to be inferred by the Spaceheat Node. For example this is done initially in SCADA code according to whether the component of the Node is a PipeFlowSensorComponent, SimpleTempSensorComponent etc.

**Exponent**:
    - Description: Exponent. Say the TelemetryName is WaterTempCTimes1000; this corresponds to units of Celsius.  To match the implication in the name, the Exponent should be 3, and a Value of 65300 would indicate 65.3 deg C

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.gt_telemetry.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwproto.types.GtTelemetry_Maker
    :members:
