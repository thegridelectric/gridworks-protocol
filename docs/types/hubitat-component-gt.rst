HubitatComponentGt
==========================
Python pydantic class corresponding to json type `hubitat.component.gt`, version `000`.

.. autoclass:: gwproto.types.HubitatComponentGt
    :members:

**ComponentId**:
    - Description: Component Id. Primary GridWorks identifier for a specific physical instance of a Hubitat, and also as a more generic Component.
    - Format: UuidCanonicalTextual

**ComponentAttributeClass**:
    - Description: ComponentAttributeClassId. Unique identifier for the device class. Authority for these, as well as the relationship between Components and ComponentAttributeClasses (Cacs) is maintained by the World Registry.

**Hubitat**:
    - Description: Hubitat Type Helper. Includes the information needed to access the MakerAPI of a Hubitat on the Local area network: Host, MakerApiID, AccessToken and MacAddress for the Hubitat.

**DisplayName**:
    - Description: Sample: Oak Hubitat 81:37:82  (using the last 6 digits of the Hubitat MacId in the display name, as well as the short alias for the associated g node.)

**HwUid**:
    - Description: Hardware Unique Id. Use the final 6 characters of the Hubitat mac address.

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.HubitatComponentGt_Maker
    :members:
