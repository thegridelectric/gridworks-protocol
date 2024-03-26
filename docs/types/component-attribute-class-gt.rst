ComponentAttributeClassGt
==========================
Python pydantic class corresponding to json type `component.attribute.class.gt`, version `001`.

.. autoclass:: gwproto.types.ComponentAttributeClassGt
    :members:

**ComponentAttributeClassId**:
    - Description: ComponentAttributeClassId. Unique identifier for the device class (aka 'cac' or Component Attribute Class). This identifier is used to associate a make/model with a specific component (i.e. the component will point to its ComponentAttributeClassId).
    - Format: UuidCanonicalTextual

**MakeModel**:
    - Description: MakeModel. MakeModel of the component.

**DisplayName**:
    - Description: DisplayName. Optional Mutable field to include manufacturer's model name. Note that several different models may be given the same spaceheat.make.model enum name.

**MinPollPeriodMs**:
    - Description: Min Poll Period Ms. The minimum amount of time between polls of this device.
    - Format: PositiveInteger

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.component_attribute_class_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.component_attribute_class_gt.check_is_positive_integer
    :members:


.. autoclass:: gwproto.types.ComponentAttributeClassGt_Maker
    :members:

