SpaceheatNodeGt
==========================
Python pydantic class corresponding to json type `spaceheat.node.gt`, version `101`.

.. autoclass:: gwproto.types.SpaceheatNodeGt
    :members:

**ShNodeId**:
    - Description: Spaceheat Node Id. Immutable identifier for a Spaceheat Node.
    - Format: UuidCanonicalTextual

**Name**:
    - Description: Functional identifier for a Spaceheat Node. Names indicate chain of command via the "dot" hierarchy. That is, `a.b` will only listen to commands from `a`. This name can and will change, in particular, for Nodes that are under the AtomicTNode chain of command when the dispatch contract is live.
    - Format: SpaceheatName

**ActorClass**:
    - Description: 

**DisplayName**:
    - Description: 

**ComponentId**:
    - Description: Unique identifier for Spaceheat Node's Component. Used if a Spaceheat Node is associated with a physical device.

**InPowerMetering**:
    - Description: This exists and is True if the SpaceheatNode is part of the power metering that is used for market participation. Small loads like circulator pumps and fans may be metered to determine their behavior but are are likely NOT part of the power metering used for market participation. 

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.spaceheat_node_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.spaceheat_node_gt.check_is_spaceheat_name
    :members:


.. autoclass:: gwproto.types.SpaceheatNodeGt_Maker
    :members:

