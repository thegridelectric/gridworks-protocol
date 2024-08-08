RelayActorConfig
==========================
Python pydantic class corresponding to json type `relay.actor.config`, version `000`.

.. autoclass:: gwproto.types.RelayActorConfig
    :members:

**RelayIdx**:
    - Description: Relay Index.
    - Format: PositiveInteger

**ActorName**:
    - Description: Name of the Actor's SpaceheatNode.
    - Format: SpaceheatName

**WiringConfig**:
    - Description: Wiring Config.Is the relay a simple Normally Open or Normally Closed or is it a double throw relay?

**EventType**:
    - Description: Finite State Machine Event Type.Every pair of  energization/de-energization actions for a relay are associated with two events for an associated finite state event.

**DeEnergizingEvent**:
    - Description: DeEnergizing Action.Which of the two choices provided by the EventType is intended to result in de-energizing the pin for the relay?

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.relay_actor_config.check_is_spaceheat_name
    :members:


.. autoclass:: gwproto.types.relay_actor_config.check_is_positive_integer
    :members:


.. autoclass:: gwproto.types.RelayActorConfig_Maker
    :members:
