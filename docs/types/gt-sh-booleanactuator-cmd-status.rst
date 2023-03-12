GtShBooleanactuatorCmdStatus
==========================
Python pydantic class corresponding to  json type ```gt.sh.booleanactuator.cmd.status```.

.. autoclass:: gwproto.types.GtShBooleanactuatorCmdStatus
    :members:

**ShNodeAlias**:
    - Description: SpaceheatNodeAlias. The alias of the spaceheat node that is getting actuated. For example, `a.elt1.relay` would likely indicate the relay for a resistive element.
    - Format: LeftRightDot

**RelayStateCommandList**:
    - Description: List of RelayStateCommands

**CommandTimeUnixMsList**:
    - Description: List of Command Times
    - Format: ReasonableUnixTimeMs

.. autoclass:: gwproto.types.gt_sh_booleanactuator_cmd_status.check_is_left_right_dot
    :members:


.. autoclass:: gwproto.types.gt_sh_booleanactuator_cmd_status.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwproto.types.GtShBooleanactuatorCmdStatus_Maker
    :members:
