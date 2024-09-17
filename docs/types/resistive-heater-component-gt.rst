ResistiveHeaterComponentGt
==========================
Python pydantic class corresponding to json type `resistive.heater.component.gt`, version `000`.

.. autoclass:: gwproto.types.ResistiveHeaterComponentGt
    :members:

**ComponentId**:
    - Description: Component Id. Primary GridWorks identifier for a specific physical instance of a ResistiveHeater, and also as a more generic Component. 
    - Format: UUID4Str

**ComponentAttributeClassId**:
    - Description: ComponentAttributeClassId. Unique identifier for the device class. Authority for these, as well as the relationship between Components and ComponentAttributeClasses (Cacs) is maintained by the World Registry. 
    - Format: UuidCanonicalTextual

**DisplayName**:
    - Description: 

**HwUid**:
    - Description: Hardware Unique Id. 

**TestedMaxHotMilliOhms**:
    - Description: 

**TestedMaxColdMilliOhms**:
    - Description: 

**ConfigList**:
    - Description: ConfigList. 

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.resistive_heater_component_gt.check_is_u_u_i_d4_str
    :members:


.. autoclass:: gwproto.types.ResistiveHeaterComponentGt_Maker
    :members:

