FsmEvent
==========================
Python pydantic class corresponding to json type `fsm.event`, version `000`.

.. autoclass:: gwproto.types.FsmEvent
    :members:

**FromHandle**:
    - Description: From Handle. 
    - Format: SpaceheatName

**ToHandle**:
    - Description: To Handle. 
    - Format: SpaceheatName

**Name**:
    - Description: Event Name. This should be the name that the receiving Spaceheat Node's finite state machine uses for an event that triggers a transition.

**SendTimeUnixMs**:
    - Description: Sent Time Unix Ms. 
    - Format: ReasonableUnixTimeMs

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.fsm_event.check_is_spaceheat_name
    :members:


.. autoclass:: gwproto.types.fsm_event.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwproto.types.FsmEvent_Maker
    :members:

