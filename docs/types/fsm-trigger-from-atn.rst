FsmTriggerFromAtn
==========================
Python pydantic class corresponding to json type `fsm.trigger.from.atn`, version `000`.

.. autoclass:: gwproto.types.FsmTriggerFromAtn
    :members:

**ToGNodeAlias**:
    - Description: GNodeAlias of the receiving SCADA. 
    - Format: LeftRightDot

**FromGNodeAlias**:
    - Description: GNodeAlias of the sending AtomicTNode. 
    - Format: LeftRightDot

**FromGNodeInstanceId**:
    - Description: GNodeInstance of the sending AtomicTNode. 
    - Format: UUID4Str

**Trigger**:
    - Description: Trigger. This remote event will triggers a cascade of local events, transitions and actions in the Spaceheat Nodes of the SCADA.  This comes from the language of Finite State Machines

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.fsm_trigger_from_atn.check_is_u_u_i_d4_str
    :members:


.. autoclass:: gwproto.types.fsm_trigger_from_atn.check_is_left_right_dot
    :members:


.. autoclass:: gwproto.types.FsmTriggerFromAtn_Maker
    :members:

