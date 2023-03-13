ActorClass
============


The opensource GridWorks `Spaceheat Scada software <https://github.com/thegridelectric/gw-scada-spaceheat-python>`_
is organized internally as a set of actors, with the prime actor being the SCADA itself.  The SCADA must be
able to deal with and process a wide variety of heating system arrangements. This is done in a Hardware Layout,
which among other things organizes relevant physical devices in the heating system (thermal stores, circulator pumps, the
heat pump, resistive heating elements, relays for heating elements). The primary objects in the Hardware Layout
are space heat nodes, although the `Hardware Layout <hardware-layout.html>`_ also organizes and captures information about the specific
hardware getting used (i.e. a serial number for a component, as well as its make/model).

All of the actors in the Spaceheat Scada are associated with space heat nodes. The Space heat Node's
`ActorClass` is an Actor enum used to determine the code used to run the actor. One node in the hardware layout will have
an actor class of `Actor.Scada` (ActorClassEnumSymbol 6d37aa41): this is the SpaceHeat Node running the main
SCADA code and supervising/managing all the other Actors.



TODO: discuss pro-actors

`Back to Lexicon <lexicon.html>`_
