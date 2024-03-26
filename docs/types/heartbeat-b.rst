HeartbeatB
==========================
Python pydantic class corresponding to json type `heartbeat.b`, version `001`.

.. autoclass:: gwproto.types.HeartbeatB
    :members:

**FromGNodeAlias**:
    - Description: My GNodeAlias.
    - Format: LeftRightDot

**FromGNodeInstanceId**:
    - Description: My GNodeInstanceId.
    - Format: UuidCanonicalTextual

**MyHex**:
    - Description: Hex character getting sent.
    - Format: HexChar

**YourLastHex**:
    - Description: Last hex character received from heartbeat partner..
    - Format: HexChar

**LastReceivedTimeUnixMs**:
    - Description: Time YourLastHex was received on my clock.
    - Format: ReasonableUnixTimeMs

**SendTimeUnixMs**:
    - Description: Time this message is made and sent on my clock.
    - Format: ReasonableUnixTimeMs

**StartingOver**:
    - Description: True if the heartbeat initiator wants to start the volley over.  (typically the AtomicTNode in an AtomicTNode / SCADA pair) wants to start the heartbeating volley over. The result is that its partner will not expect the initiator to know its last Hex.

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.heartbeat_b.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.heartbeat_b.check_is_hex_char
    :members:


.. autoclass:: gwproto.types.heartbeat_b.check_is_left_right_dot
    :members:


.. autoclass:: gwproto.types.heartbeat_b.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwproto.types.HeartbeatB_Maker
    :members:

