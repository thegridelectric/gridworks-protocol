GtShBooleanactuatorCmdStatus
==========================
Python pydantic class corresponding to json type `gt.sh.booleanactuator.cmd.status`, version `100`.

.. autoclass:: gwproto.types.GtShBooleanactuatorCmdStatus
    :members:

**ShNodeAlias**:
    - Description: SpaceheatNodeAlias. The alias of the spaceheat node that is getting actuated. For example, `a.elt1.relay` would likely indicate the relay for a resistive element.
    - Format: LeftRightDot

**RelayStateCommandList**:
    - Description: List of RelayStateCommands. 

**CommandTimeUnixMsList**:
    - Description: List of Command Times. 
    - Format: ReasonableUnixTimeMs

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.gt_sh_booleanactuator_cmd_status.check_is_left_right_dot
    :members:


.. autoclass:: gwproto.types.gt_sh_booleanactuator_cmd_status.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwproto.types.GtShBooleanactuatorCmdStatus_Maker
    :members:

