BatchedReadings
==========================
Python pydantic class corresponding to json type `batched.readings`, version `000`.

.. autoclass:: gwproto.types.BatchedReadings
    :members:

**FromGNodeAlias**:
    - Description: 
    - Format: LeftRightDot

**FromGNodeInstanceId**:
    - Description: 
    - Format: UUID4Str

**AboutGNodeAlias**:
    - Description: 
    - Format: LeftRightDot

**SlotStartUnixS**:
    - Description: 
    - Format: UTCSeconds

**BatchedTransmissionPeriodS**:
    - Description: 
    - Format: PositiveInteger

**MessageCreatedMs**:
    - Description: MessageCreatedMs. The SCADA timestamp for when this message was created. If the message is not acked by the AtomicTNode, the message is stored and sent again later - so the MessageCreatedMs may occur significantly before the timestamp for when the message is put into the persistent store.
    - Format: UTCMilliseconds

**DataChannelList**:
    - Description: DataChannel List. The list of data channels for which there is data getting reported in this batched reading. It is a subset of all the data channels for the SCADA - may not be all of them.

**ChannelReadingList**:
    - Description: 

**FsmActionList**:
    - Description: Finite State Machine Action List. FSM Actions (that is, side-effects of state machine transitions with real-world changes to the underlying TerminalAsset).

**FsmReportList**:
    - Description: Finite State Machine Report List. FSM Reports are the cacading events, actions and transitions caused by a single high-level event. There is duplication with the action list. 

**Id**:
    - Description: Batched Reading Id. Globally Unique identifier for a BatchedReadings message
    - Format: UUID4Str

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.batched_readings.check_is_u_t_c_seconds
    :members:


.. autoclass:: gwproto.types.batched_readings.check_is_u_u_i_d4_str
    :members:


.. autoclass:: gwproto.types.batched_readings.check_is_positive_integer
    :members:


.. autoclass:: gwproto.types.batched_readings.check_is_left_right_dot
    :members:


.. autoclass:: gwproto.types.batched_readings.check_is_u_t_c_milliseconds
    :members:


.. autoclass:: gwproto.types.BatchedReadings_Maker
    :members:

