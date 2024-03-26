SnapshotSpaceheat
==========================
Python pydantic class corresponding to json type `snapshot.spaceheat`, version `001`.

.. autoclass:: gwproto.types.SnapshotSpaceheat
    :members:

**FromGNodeAlias**:
    - Description:
    - Format: LeftRightDot

**FromGNodeInstanceId**:
    - Description:
    - Format: UuidCanonicalTextual

**SnapshotTimeUnixMs**:
    - Description: The time at which the snapshot was put together.
    - Format: ReasonableUnixTimeMs

**LatestReadingList**:
    - Description: The most up-to-date values the SCADA has for all channels, with timestamps of when they were last updated.

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.snapshot_spaceheat.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.snapshot_spaceheat.check_is_left_right_dot
    :members:


.. autoclass:: gwproto.types.snapshot_spaceheat.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwproto.types.SnapshotSpaceheat_Maker
    :members:

