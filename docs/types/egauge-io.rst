EgaugeIo
==========================
Python pydantic class corresponding to json type `egauge.io`, version `001`.

.. autoclass:: gwproto.types.EgaugeIo
    :members:

**InputConfig**:
    - Description: Input config for one channel of data for a specific eGauge meter. This is the data available from the modbus csv map provided by eGauge for this component, for example http://egauge14875.egaug.es/6001C/settings.html for a eGauge device with ID 14875

**OutputConfig**:
    - Description: Output config for the same channel . This is the data as the Scada proactor expects to consume it from the power meter driver proactor.

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.EgaugeIo_Maker
    :members:
