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
