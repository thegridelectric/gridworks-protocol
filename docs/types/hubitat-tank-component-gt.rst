HubitatTankComponentGt
==========================
Python pydantic class corresponding to json type `hubitat.tank.component.gt`, version `000`.

.. autoclass:: gwproto.types.HubitatTankComponentGt
    :members:

**ComponentId**:
    - Description: Component Id. Primary GridWorks identifier for a specific physical instance of a GridWorks TankModule1 and also as a more generic Component. 
    - Format: UUID4Str

**ComponentAttributeClassId**:
    - Description: ComponentAttributeClassId. Unique identifier for the device class. Authority for these, as well as the relationship between Components and ComponentAttributeClasses (Cacs) is maintained by the World Registry. 
    - Format: UuidCanonicalTextual

**Tank**:
    - Description: Tank. The configuration information (HubitatTankSettingsGt) about the 4 analog temperature sensors for a GridWorks TankModule1.

**DisplayName**:
    - Description: Sample: GridWorks TankModule <buffer>  SN 1010

**HwUid**:
    - Description: Hardware Unique Id. Use the GridWorks Serial number for GridWorks TankModule1.

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.HubitatTankComponentGt_Maker
    :members:

