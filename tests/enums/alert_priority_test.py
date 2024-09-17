"""
Tests for enum alert.priority.000 from the GridWorks Type Registry.
"""

from gwproto.enums import AlertPriority


def test_alert_priority() -> None:
    assert set(AlertPriority.values()) == {
        "P1Critical",
        "P2High",
        "P3Medium",
        "P4Low",
        "P5Info",
    }

    assert AlertPriority.default() == AlertPriority.P3Medium
    assert AlertPriority.enum_name() == "alert.priority"
    assert AlertPriority.enum_version() == "000"

    assert AlertPriority.version("P1Critical") == "000"
    assert AlertPriority.version("P2High") == "000"
    assert AlertPriority.version("P3Medium") == "000"
    assert AlertPriority.version("P4Low") == "000"
    assert AlertPriority.version("P5Info") == "000"

    for value in AlertPriority.values():
        symbol = AlertPriority.value_to_symbol(value)
        assert AlertPriority.symbol_to_value(symbol) == value
