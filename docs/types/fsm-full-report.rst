FsmFullReport
==========================
Python pydantic class corresponding to json type `fsm.full.report`, version `000`.

.. autoclass:: gwproto.types.FsmFullReport
    :members:

**FromName**:
    - Description: From Name. The name (not the handle, so immutable) of the Node issuing the report. This will typically be the scada node itself.
    - Format: SpaceheatName

**Trigger**:
    - Description: Trigger. The event that triggered the collected list of actions, transitions and further events.

**AtomicList**:
    - Description: Atomic List. The list of cascading events, transitions and actions triggered by a single high-level event in a hierarchical finite state machine.

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.fsm_full_report.check_is_spaceheat_name
    :members:


.. autoclass:: gwproto.types.FsmFullReport_Maker
    :members:

