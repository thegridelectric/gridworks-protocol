ChannelConfig
==========================
Python pydantic class corresponding to json type `channel.config`, version `000`.

.. autoclass:: gwproto.types.ChannelConfig
    :members:

**ChannelName**:
    - Description: Data Channel Name. The (locally unique, immutable) name of the  Data Channel to which the configuration applies (What node is getting read, what telemetry name is getting read, and what node is doing the reading).
    - Format: SpaceheatName

**PollPeriodMs**:
    - Description: Poll Period in Milliseconds. Poll Period refers to the period of time between two readings by the local actor. This is in contrast to Capture Period, which refers to the period between readings that are sent up to the cloud (or otherwise saved for the long-term). 
    - Format: PositiveInteger

**CapturePeriodS**:
    - Description: Capture Period Seconds. This telemetry data channel will capture data periodically, at this rate.  It will be shared (although not necessarily immediately) with the AtomicTNode. The capture period must be longer than the poll period. If the channel is also capturing on change, those asynchronous reports do not reset this period.
    - Format: PositiveInteger

**AsyncCapture**:
    - Description: Asynchronous Capture. Set CaptureOnChange to true for asynchronous reporting of captured data, in addition to the synchronous periodic capture reflected by the CapturePeriodS.

**AsyncCaptureDelta**:
    - Description: Asynchronous Capture Delta. Represents the threshold or minimum change in value required for asynchronous reporting of telemetry data, assuming CaptureOnChange. For example, if TelemetryName is WaterTempCTimes1000 and one wants 0.25 deg C to trigger a new capture, then this would be set to 250.
    - Format: PositiveInteger

**Exponent**:
    - Description: Exponent. Say the TelemetryName is WaterTempCTimes1000; this corresponds to units of Celsius.  To match the implication in the name, the Exponent should be 3, and a Value of 65300 would indicate 65.3 deg C

**Unit**:
    - Description: Unit. Say TelemetryName is WaterTempCTimes1000. The unit would be Celcius.

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.channel_config.check_is_spaceheat_name
    :members:


.. autoclass:: gwproto.types.channel_config.check_is_positive_integer
    :members:


.. autoclass:: gwproto.types.ChannelConfig_Maker
    :members:

