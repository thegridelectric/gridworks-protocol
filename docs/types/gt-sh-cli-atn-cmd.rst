GtShCliAtnCmd
==========================
Python pydantic class corresponding to json type `gt.sh.cli.atn.cmd`, version `110`.

.. autoclass:: gwproto.types.GtShCliAtnCmd
    :members:

**FromGNodeAlias**:
    - Description: GNodeAlias. Must be the SCADA's AtomicTNode.
    - Format: LeftRightDot

**SendSnapshot**:
    - Description: Send Snapshot. Asks SCADA to send back a snapshot. For this version of the type, nothing would happen if SendSnapshot were set to False. However, we include this in case additional variations are added later.

**FromGNodeId**:
    - Description: GNodeId. 
    - Format: UuidCanonicalTextual

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.gt_sh_cli_atn_cmd.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.gt_sh_cli_atn_cmd.check_is_left_right_dot
    :members:


.. autoclass:: gwproto.types.GtShCliAtnCmd_Maker
    :members:

