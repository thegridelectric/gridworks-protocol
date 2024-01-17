HubitatPollerComponentGt
==========================
Python pydantic class corresponding to json type `hubitat.poller.component.gt`, version `000`.

.. autoclass:: gwproto.types.HubitatPollerComponentGt
    :members:

**ComponentId**:
    - Description: ComponentId.

**ComponentAttributeClassId**:
    - Description: ComponentAttributeClassId.
    - Format: UuidCanonicalTextual

**DisplayName**:
    - Description: DisplayName. Sample: Downstairs Thermostat

**HwUid**:
    - Description: HwUid. Unique Hardware Identifier

**Poller**:
    - Description: Poller. Includes hubitat_component_id (str), device_id (int), enabled (bool), poll_period_s (int) and attributes.

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.hubitat_poller_component_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.HubitatPollerComponentGt_Maker
    :members:
