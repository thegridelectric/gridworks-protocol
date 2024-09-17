SingleReading
==========================
Python pydantic class corresponding to json type `single.reading`, version `000`.

.. autoclass:: gwproto.types.SingleReading
    :members:

**ScadaReadTimeUnixMs**:
    - Description: Scada Read Time in Unix Milliseconds. 
    - Format: UTCMilliseconds

**ChannelName**:
    - Description: Data Channel Name. The name of the Channel getting reported
    - Format: SpaceheatName

**Value**:
    - Description: Value. The value of the reading. 

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.single_reading.check_is_spaceheat_name
    :members:


.. autoclass:: gwproto.types.single_reading.check_is_u_t_c_milliseconds
    :members:


.. autoclass:: gwproto.types.SingleReading_Maker
    :members:

