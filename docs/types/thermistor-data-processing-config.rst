ThermistorDataProcessingConfig
==========================
Python pydantic class corresponding to json type `thermistor.data.processing.config`, version `000`.

.. autoclass:: gwproto.types.ThermistorDataProcessingConfig
    :members:

**ChannelName**:
    - Description: Channel Name.The name of the data channel associated with this thermistor
    - Format: SpaceheatName

**TerminalBlockIdx**:
    - Description: Terminal Block Index.If the reading Node uses terminal blocks for inputs (e.g. thermistors or current transformers), and it has multiple terminal blocks, then one needs to know which terminal block to read. For example, al Ads111xBasedComponents use this.
    - Format: PositiveInteger

**ThermistorMakeModel**:
    - Description: Thermistor MakeModel.The Make/Model of the thermistor attached to this terminal block.

**DataProcessingMethod**:
    - Description: Data Processing Method.What method is used to go from polled raw voltage to captured temperature readings? Not applicable if the data channel is voltage.
    - Format: thermistor.data.method

**DataProcessingDescription**:
    - Description: Data Processing Description.Additional information to flesh out and articulate the data processing method enum. For example, if the method is an exponential weighted average of temperature readings achieved with the beta formula, how is the weighting determined?

**TypeName**:
    - Description: All GridWorks Versioned Types have a fixed TypeName, which is a string of lowercase alphanumeric words separated by periods, most significant word (on the left) starting with an alphabet character, and final word NOT all Hindu-Arabic numerals.

**Version**:
    - Description: All GridWorks Versioned Types have a fixed version, which is a string of three Hindu-Arabic numerals.



.. autoclass:: gwproto.types.thermistor_data_processing_config.check_is_spaceheat_name
    :members:


.. autoclass:: gwproto.types.thermistor_data_processing_config.check_is_positive_integer
    :members:


.. autoclass:: gwproto.types.ThermistorDataProcessingConfig_Maker
    :members:
