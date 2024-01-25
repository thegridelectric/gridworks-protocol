SimpleSensorTelemetry
==========================
Python pydantic class corresponding to json type `simple.sensor.telemetry`, version `000`.

.. autoclass:: gwproto.types.SimpleSensorTelemetry
    :members:

**Name**:
    - Description: Name. The name of the Simple Sensing Spaceheat Node. This is both the AboutNodeName and FromNodeName for a data channel. The TelemetryName (and thus Units) are expected to be inferred by the Spaceheat Node. For example this is done initially in SCADA code according to whether the component of the Node is a PipeFlowSensorComponent, SimpleTempSensorComponent etc.

**Value**:
    - Description: Value. The value of the reading. 

**ScadaReadTimeUnixMs**:
    - Description: Scada Read Time in Unix Milliseconds. 
    - Format: ReasonableUnixTimeMs

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.SimpleSensorTelemetry_Maker
    :members:

