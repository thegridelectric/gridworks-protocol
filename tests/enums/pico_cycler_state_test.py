"""
Tests for enum pico.cycler.state.000 from the GridWorks Type Registry.
"""

from gwproto.enums import PicoCyclerState


def test_pico_cycler_state() -> None:
    assert set(PicoCyclerState.values()) == {
        "PicosLive",
        "RelayOpening",
        "RelayOpen",
        "RelayClosing",
        "PicosRebooting",
    }

    assert PicoCyclerState.default() == PicoCyclerState.PicosLive
    assert PicoCyclerState.enum_name() == "pico.cycler.state"
    assert PicoCyclerState.enum_version() == "000"
