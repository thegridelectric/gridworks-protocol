GtDispatchBoolean
==========================
Python pydantic class corresponding to json type `gt.dispatch.boolean`, version `111`.

.. autoclass:: gwproto.types.GtDispatchBoolean
    :members:

**ToGNodeAlias**:
    - Description: GNodeAlias of the SCADA. 
    - Format: LeftRightDot

**FromGNodeAlias**:
    - Description: GNodeAlias of AtomicTNode. 
    - Format: LeftRightDot

**FromGNodeInstanceId**:
    - Description: GNodeInstance of the AtomicTNode. 
    - Format: UuidCanonicalTextual

**AboutNodeName**:
    - Description: About Node Name. The name of the Spaceheat Node that the dispatch request is for.
    - Format: SpaceheatName

**RelayState**:
    - Description: Relay State (0 or 1). This is not applicable for double-throw relays that do anything other than open or close a circuit. A Relay State of `0` indicates the relay is OPEN (off). A Relay State of `1` indicates the relay is CLOSED (on). Note that `0` means the relay is open whether or not the relay is normally open or normally closed (For a normally open relay, the relay is ENERGIZED when it is in state `0` and DE-ENERGIZED when it is in state `1`.) 
    - Format: Bit

**SendTimeUnixMs**:
    - Description: Time the AtomicTNode sends the dispatch, by its clock. 
    - Format: ReasonableUnixTimeMs

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.GtDispatchBoolean_Maker
    :members:

