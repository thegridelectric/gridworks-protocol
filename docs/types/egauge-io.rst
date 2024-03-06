EgaugeIo
==========================
Python pydantic class corresponding to json type `egauge.io`, version `001`.

.. autoclass:: gwproto.types.EgaugeIo
    :members:

**ChannelName**:
    - Description: Name of the Data Channel. Each input on the egauge is associated with a unique Data Channel (for example, TelemetryName PowerW, AboutNodeName hp-idu-pwr, CapturedByNodeName pwr-meter). The Data Channel's name is meant to be an easy-to-read immutable and (locally to the SCADA) unique identifier.  Stylistically, when there is no ambiguity about what node is capturing the data or what the telemetry name is, choose the data channel's name as the AboutNodeName (e.g. hp-idu-pwr).
    - Format: SpaceheatName

**InputConfig**:
    - Description: Input config for one channel of data for a specific eGauge meter. This is the data available from the modbus csv map provided by eGauge for this component, for example http://egauge14875.egaug.es/6001C/settings.html for a eGauge device with ID 14875

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.egauge_io.check_is_spaceheat_name
    :members:


.. autoclass:: gwproto.types.EgaugeIo_Maker
    :members:

