FibaroSmartImplantComponentGt
==========================
Python pydantic class corresponding to json type `fibaro.smart.implant.component.gt`, version `000`.

.. autoclass:: gwproto.types.FibaroSmartImplantComponentGt
    :members:

**ComponentId**:
    - Description: Component Id. Primary GridWorks identifier for a specific physical instance of an  Fibaro, and also as a more generic Component. 
    - Format: UuidCanonicalTextual

**ComponentAttributeClass**:
    - Description: ComponentAttributeClassId. Unique identifier for the device class. Authority for these, as well as the relationship between Components and ComponentAttributeClasses (Cacs) is maintained by the World Registry. 

**ZWaveDSK**:
    - Description: The Z-Wave DSK  (Device Specific Key) is a unique identifier associated with a Z-Wave device, used during the process of securely including the device into a Z-Wave network. It helps establish secure communication between the Z-Wave controller and the device, ensuring that only authorized devices can join the network. Unfortunately Hubitat does not currently provide a way to view the ZWave DSK of a Fibaro.

**DisplayName**:
    - Description: Sample: Fibaro Smart Implant 1010 A (For Fibaro A as opposed to B for GridWorks TankModule1  with Serial Number 1010).

**HwUid**:
    - Description: Hardware Unique Id. Use the Fibaro S2 PIN Code, which is printed on the back of each Fibaro Implant.

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.fibaro_smart_implant_component_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwproto.types.FibaroSmartImplantComponentGt_Maker
    :members:

