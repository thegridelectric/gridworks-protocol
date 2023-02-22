

SDK for `gridworks-protocol <https://pypi.org/project/gridworks-protocol/>`_  Types
===========================================================================

The Python classes enumerated below provide an interpretation of gridworks-protocol
type instances (serialized JSON) as Python objects. Types are the building
blocks for all GridWorks APIs. You can read more about how they work
`here <https://gridworks.readthedocs.io/en/latest/api-sdk-abi.html>`_, and
examine their API specifications `here <apis/types.html>`_.
The Python classes below also come with methods for translating back and
forth between type instances and Python objects.


.. automodule:: gwproto.types

.. toctree::
   :maxdepth: 1
   :caption: TYPE SDKS

    GtDispatchBoolean  <types/gt-dispatch-boolean>
    GtDispatchBooleanLocal  <types/gt-dispatch-boolean-local>
    GtDriverBooleanactuatorCmd  <types/gt-driver-booleanactuator-cmd>
    GtShBooleanactuatorCmdStatus  <types/gt-sh-booleanactuator-cmd-status>
    GtShCliAtnCmd  <types/gt-sh-cli-atn-cmd>
    GtShMultipurposeTelemetryStatus  <types/gt-sh-multipurpose-telemetry-status>
    GtShSimpleTelemetryStatus  <types/gt-sh-simple-telemetry-status>
    GtShStatus  <types/gt-sh-status>
    GtShTelemetryFromMultipurposeSensor  <types/gt-sh-telemetry-from-multipurpose-sensor>
    GtTelemetry  <types/gt-telemetry>
    HeartbeatB  <types/heartbeat-b>
    SnapshotSpaceheat  <types/snapshot-spaceheat>
    TelemetrySnapshotSpaceheat  <types/telemetry-snapshot-spaceheat>
