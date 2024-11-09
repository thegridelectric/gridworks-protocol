"""Tests machine.states type, version 000"""

from gwproto.named_types import MachineStates


def test_machine_states_generated() -> None:
    d = {
        "MachineHandle": "h.pico-cycler",
        "StateEnum": "pico.cycler.state",
        "StateList": ["PicosLive"],
        "UnixMsList": [1731168353695],
        "TypeName": "machine.states",
        "Version": "000",
    }

    d2 = MachineStates.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
