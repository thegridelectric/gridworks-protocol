
# gwproto Repository Structure

```
gridworks-protocol/
├─src/gwproto
  ├── data_classes/
  │   ├── components/
  │   │       ├── ads111x_based_component.py, electric_meter_component.py, etc #  move to gridworks-scada   
  │   │       └── component.py # keep in gwproto; matches named type ComponentGt
  │   ├── data_channel.py  #  matches named type DataChannelGt
  │   ├── hardware_layout.py # TODO: SIMPLIFY. create named type association
  │   ├── sh_node.py # matches ShNodeGt. SIMPLIFY. move specifics to gridworks-scada
  │   └── synth_channel.py # matches SynthChannelGt
  ├── enums/ # enums used in the gwproto Application Shared Language (ASL)
  │   ├── actor_class.py # too specific to GridWorks. Used by GridWorks to assign code to ShNodes Probably move to 
  │   ├── make_model.py # Used by GridWorks to categorize the hardware used for sensing and actuating.
  │   └── telemetry_name.py # used for data channels. Perhaps also too specific for GridWorks
  ├── named_types/ # gwproto Application Shared Language
  │   ├── ads111x_based_component_gt.py etc # a bunch of named types will definitely move to scada 
  │   ├── data_channel_gt.py 
  │   ├── channel_readings.py
  │   ├── fsm_full_report.py # CONSIDER REMOVING FROM REPORT
  │   ├── hardware_layout_gt.py # NEED TO ADD
  │   ├── machine_states.py
  │   ├── power_watts.py # core async nessage 
  │   ├── report.py  # primary reporting nmessage, sends every 5 minutes
  │   ├── spaceheat_node_gt.py
  │   └── synth_channel_gt.py
  ├── type_helpers/ # MOVE TO SCADA OR REMOVE
  │   └── cacs_by_make_model.py # enforces bijection between known make models and UUIDs
  ├── errors.py, message.py, topic.py # Stuff used by Andrew
  ├── decoders, default_decoders.py - codec stuff for Andrew
  └── utils.py # primarily snake_to_camel and camel_to_snake

```