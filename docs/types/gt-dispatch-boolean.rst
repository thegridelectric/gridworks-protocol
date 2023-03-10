GtDispatchBoolean
==========================
Python pydantic class corresponding to  json type ```gt.dispatch.boolean```.

.. autoclass:: gwproto.types.GtDispatchBoolean
    :members:

**AboutNodeName**:
    - Description: The Spaceheat Node getting dispatched
    - Format: LeftRightDot

**ToGNodeAlias**:
    - Description: GNodeAlias of the SCADA
    - Format: LeftRightDot

**FromGNodeAlias**:
    - Description: GNodeAlias of AtomicTNode
    - Format: LeftRightDot

**FromGNodeInstanceId**:
    - Description: GNodeInstance of the AtomicTNode
    - Format: UuidCanonicalTextual

**RelayState**:
    - Description: 0 or 1

**SendTimeUnixMs**:
    - Description: Time the AtomicTNode sends the dispatch, by its clock
    - Format: ReasonableUnixTimeMs

.. autoclass:: gwproto.types.gt_dispatch_boolean.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.gt_dispatch_boolean.check_is_left_right_dot
    :members:


.. autoclass:: gwproto.types.gt_dispatch_boolean.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwproto.types.GtDispatchBoolean_Maker
    :members:
