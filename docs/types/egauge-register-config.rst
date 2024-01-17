EgaugeRegisterConfig
==========================
Python pydantic class corresponding to json type `egauge.register.config`, version `000`.

.. autoclass:: gwproto.types.EgaugeRegisterConfig
    :members:

**Address**:
    - Description: Address. EGauge's modbus holding address. Note that the EGauge modbus map for holding address 100 will be 30100 - the '+30000' indicates it is a holding address. We use the 4-digit address after the '3'.

**Name**:
    - Description: Name. The name assigned in the EGauge's modbus map. This is configured by the user (see URL)

**Description**:
    - Description: Description. Again, assigned by the EGauge modbus map. Is usually 'change in value'

**Type**:
    - Description: Type. EGauge's numerical data type. Typically our power measurements are  f32 ( 32-bit floating-point number). The serial number & firmware are t16 (which work to treat as 16-bit unsigned integer)  and timestamps are u32 (32-bit unsigned integer).

**Denominator**:
    - Description: Denominator. Some of the modbus registers divide by 3.60E+06 (cumulative energy registers typically). For the power, current, voltage and phase angle the denominator is 1.

**Unit**:
    - Description: Unit. The EGauge unit - typically A, Hz, or W.

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.EgaugeRegisterConfig_Maker
    :members:
