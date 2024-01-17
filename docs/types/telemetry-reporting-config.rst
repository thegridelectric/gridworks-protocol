TelemetryReportingConfig
==========================
Python pydantic class corresponding to json type `telemetry.reporting.config`, version `000`.

.. autoclass:: gwproto.types.TelemetryReportingConfig
    :members:

**TelemetryName**:
    - Description:

**AboutNodeName**:
    - Description: The name of the SpaceheatNode whose physical quantity is getting captured.
    - Format: LeftRightDot

**ReportOnChange**:
    - Description:

**SamplePeriodS**:
    - Description:

**Exponent**:
    - Description: Exponent. Say the TelemetryName is WaterTempCTimes1000; this corresponds to units of Celsius.  To match the implication in the name, the Exponent should be 3, and a Value of 65300 would indicate 65.3 deg C

**Unit**:
    - Description:

**AsyncReportThreshold**:
    - Description:

**NameplateMaxValue**:
    - Description:
    - Format: PositiveInteger

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.telemetry_reporting_config.check_is_positive_integer
    :members:


.. autoclass:: gwproto.types.telemetry_reporting_config.check_is_left_right_dot
    :members:


.. autoclass:: gwproto.types.TelemetryReportingConfig_Maker
    :members:
