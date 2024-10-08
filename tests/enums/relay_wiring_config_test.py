"""
Tests for enum relay.wiring.config.000 from the GridWorks Type Registry.
"""

from gwproto.enums import RelayWiringConfig


def test_relay_wiring_config() -> None:
    assert set(RelayWiringConfig.values()) == {
        "NormallyClosed",
        "NormallyOpen",
        "DoubleThrow",
    }

    assert RelayWiringConfig.default() == RelayWiringConfig.NormallyClosed
    assert RelayWiringConfig.enum_name() == "relay.wiring.config"
    assert RelayWiringConfig.enum_version() == "000"

    assert RelayWiringConfig.version("NormallyClosed") == "000"
    assert RelayWiringConfig.version("NormallyOpen") == "000"
    assert RelayWiringConfig.version("DoubleThrow") == "000"
