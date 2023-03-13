Simple Sensor
==============

A SimpleSensor is an ActorClass for a SpaceheatNode. An ShNode is a SimpleSensor if
it is both the device taking a reading and the thing getting read. There can also
only be one type of reading.

Here is an example.

A 1-wire temp sensor read by a SCADA has only one type of reading: temperature in degrees
C times 1000. It also only reads one thing: say, water temp at the top of the tank where
the sensor is located.

A SpaceHeat node for  `a.tank.temp1` conflates the 1-wire reading that temperature with
the location and temperature itself. this is a SimpelSensor



`Back to Lexicon <lexicon.html>`_
