RelayComponentGt
==========================
Python pydantic class corresponding to json type `relay.component.gt`, version `000`.

.. autoclass:: gwproto.types.RelayComponentGt
    :members:

**ComponentId**:
    - Description: Component Id. Primary GridWorks identifier for a specific physical instance of a Relay, and also as a more generic Component. 
    - Format: UuidCanonicalTextual

**ComponentAttributeClassId**:
    - Description: ComponentAttributeClassId. Unique identifier for the device class. Authority for these, as well as the relationship between Components and ComponentAttributeClasses (Cacs) is maintained by the World Registry. 
    - Format: UuidCanonicalTextual

**DisplayName**:
    - Description: 

**Gpio**:
    - Description: 

**HwUid**:
    - Description: Hardware Unique Id. 

**NormallyOpen**:
    - Description: Normally Open. Normally open relays default in the open position, meaning that when they're not in use, there is no contact between the circuits. When power is introduced, an electromagnet pulls the first circuit into contact with the second, thereby closing the circuit and allowing power to flow through

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.relay_component_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.RelayComponentGt_Maker
    :members:

