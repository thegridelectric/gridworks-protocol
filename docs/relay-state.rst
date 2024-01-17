Relay State
============
A Relay State of `0` indicates the relay is OPEN (off). A Relay State of `1` indicates the 
relay is CLOSED (on). Note that `0` means the relay is open whether or not the relay is 
normally open or normally closed (For a normally open relay, the relay is ENERGIZED when it 
is in state `0` and DE-ENERGIZED when it is in state `1`.)


REPORTING THE RELAY STATE.

Boolean actuator actors report when they send an actuation command to its driver so 
that the  SCADA  can add this to information to be sent up to the AtomicTNode. 

Boolean actuator actors read the state of their relay, when possible.

Note that a  reading of the state of the actuator may not mean the relay is in the 
reported position. For example, the NCD relay requires two power sources - one from 
the Pi and one a lowish DC voltage from another plug (12 or 24V). If the second power 
source is off, the relay will still report being on when it is actually off.

Note also that the thing getting actuated (for example the boost element in the water
tank) may not be getting any power because of another relay in series. For example, we
can throw a large 240V breaker in the test garage and the NCD relay will actuate without
the boost element turning on. Or the element could be burned out.

So measuring the current and/or power of the thing getting
actuated is really the best test.

`Back to Lexicon <lexicon.html>`_