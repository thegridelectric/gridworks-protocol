GtDispatchBoolean
==========================
Python pydantic class corresponding to json type `gt.dispatch.boolean`, version `110`.

.. autoclass:: gwproto.types.GtDispatchBoolean
    :members:

**AboutNodeName**:
    - Description: The Spaceheat Node getting dispatched.
    - Format: LeftRightDot

**ToGNodeAlias**:
    - Description: GNodeAlias of the SCADA.
    - Format: LeftRightDot

**FromGNodeAlias**:
    - Description: GNodeAlias of AtomicTNode.
    - Format: LeftRightDot

**FromGNodeInstanceId**:
    - Description: GNodeInstance of the AtomicTNode.
    - Format: UuidCanonicalTextual

**RelayState**:
    - Description: Relay State (0 or 1). A Relay State of `0` indicates the relay is OPEN (off). A Relay State of `1` indicates the relay is CLOSED (on). Note that `0` means the relay is open whether or not the relay is normally open or normally closed (For a normally open relay, the relay is ENERGIZED when it is in state `0` and DE-ENERGIZED when it is in state `1`.)
    - Format: Bit

**SendTimeUnixMs**:
    - Description: Time the AtomicTNode sends the dispatch, by its clock.
    - Format: ReasonableUnixTimeMs

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.gt_dispatch_boolean.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.gt_dispatch_boolean.check_is_bit
    :members:


.. autoclass:: gwproto.types.gt_dispatch_boolean.check_is_left_right_dot
    :members:


.. autoclass:: gwproto.types.gt_dispatch_boolean.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwproto.types.GtDispatchBoolean_Maker
    :members:
