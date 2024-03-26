ComponentGt
==========================
Python pydantic class corresponding to json type `component.gt`, version `001`.

.. autoclass:: gwproto.types.ComponentGt
    :members:

**ComponentId**:
    - Description: ComponentId. Immutable unique identifier for this specific device.
    - Format: UuidCanonicalTextual

**ComponentAttributeClassId**:
    - Description: ComponentAttributeClassId. Unique identifier for the device class. Authority for these, as well as the relationship between Components and ComponentAttributeClasses (Cacs) is maintained by the World Registry.
    - Format: UuidCanonicalTextual

**ConfigList**:
    - Description: ConfigList. This list is expected to have length 0, except for nodes that do some kind of sensing - in which case it includes the information re timing of data polling and capture for the channels read by the node.

**DisplayName**:
    - Description: Display Name. This is an optional, mutable field whose use is strongly encouraged. It may include information about HOW the component is used in a hardware layout. It may also include the HwUid for the component.

**HwUid**:
    - Description: Hardware Unique Id. Usually this is determined by the inheriting class.

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.component_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.ComponentGt_Maker
    :members:

