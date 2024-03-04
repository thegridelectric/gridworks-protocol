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
    - Format: UuidCanonicalTextual

**AboutGNodeAlias**:
    - Description: 
    - Format: LeftRightDot

**SlotStartUnixS**:
    - Description: 
    - Format: ReasonableUnixTimeS

**BatchedTransmissionPeriodS**:
    - Description: 
    - Format: PositiveInteger

**ChannelReadingList**:
    - Description: 

**FsmActionList**:
    - Description: Finite State Machine Action List. FSM Actions (that is, side-effects of state machine transitions with real-world changes to the underlying TerminalAsset).

**FsmReportList**:
    - Description: Finite State Machine Report List. FSM Reports are the cacading events, actions and transitions caused by a single high-level event. There is duplication with the action list. 

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.batched_readings.check_is_reasonable_unix_time_s
    :members:


.. autoclass:: gwproto.types.batched_readings.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.batched_readings.check_is_left_right_dot
    :members:


.. autoclass:: gwproto.types.BatchedReadings_Maker
    :members:

