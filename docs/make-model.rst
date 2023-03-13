Make Model
=============

Determines Make/Model of device associated to a Spaceheat Node supervised by SCADA

Used to assign the correct driver code to various sensors. For example, if we are using an Adafruit 1-wire temp sensor
identified by Adafruit as Product Id 642, the associated SimpleSensor actor in the SCADA code knows that the HardwareLayout
will include the unique identifier for that 1-wire, and will know to use the appropriate `driver code in the repository <https://github.com/thegridelectric/gw-scada-spaceheat-python/blob/main/gw_spaceheat/drivers/simple_temp_sensor/adafruit_642__simple_temp_sensor_driver.py>`_.



`Back to Lexicon <lexicon.html>`_
