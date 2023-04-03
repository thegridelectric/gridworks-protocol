EgaugeIo
==========================
Python pydantic class corresponding to  json type ```egauge.io```.

.. autoclass:: gwproto.types.EgaugeIo
    :members:

**InputConfig**:
    - Description: Input config for one channel of data for a specific eGauge meter. This is the data available from the modbus csv map provided by eGauge for this component, for example http://egauge14875.egaug.es/6001C/settings.html for a eGauge device with ID 14875

**OutputConfig**:
    - Description: Output config for the same channel . This is the data as the Scada proactor expects to consume it from the power meter driver proactor.

.. autoclass:: gwproto.types.EgaugeIo_Maker
    :members:
