FsmAtomicReport
==========================
Python pydantic class corresponding to json type `fsm.atomic.report`, version `000`.

.. autoclass:: gwproto.types.FsmAtomicReport
    :members:

**FromHandle**:
    - Description: From Name. The Name (as opposed to the handle) of the Spaceheat Node actor issuing the Finite State Machine report.  The actor is meant to realize and be the authority on the FSM in question. Its handle reflects the state it is in.
    - Format: SpaceheatName

**IsEvent**:
    - Description: Is Event. An Action refers to some side effect of a state transition that results in a physical change to an underlying TerminalAsset. 

**EventType**:
    - Description: Event Type. The FiniteState Machine Action taken

**Event**:
    - Description: Event. Should belong to the associated enum element chosen in ActionType. For example, if ActionType is ChangeStoreFlowDirection, then Action should be either 'Discharge' or 'Charge.'

**UnixTimeMs**:
    - Description: Unix Time in Milliseconds. 
    - Format: ReasonableUnixTimeMs

**TriggerId**:
    - Description: TriggerId. Reference uuid for the triggering event that started a cascade of transitions, events and  side-effect actions - of which this report is one.
    - Format: UuidCanonicalTextual

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.fsm_atomic_report.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.fsm_atomic_report.check_is_spaceheat_name
    :members:


.. autoclass:: gwproto.types.fsm_atomic_report.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwproto.types.FsmAtomicReport_Maker
    :members:

