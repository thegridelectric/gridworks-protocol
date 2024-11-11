"""
Tests for enum admin.event.000 from the GridWorks Type Registry.
"""

from gwproto.enums import AdminEvent


def test_admin_event() -> None:
    assert set(AdminEvent.values()) == {
        "WakeUp",
        "GoDormant",
    }

    assert AdminEvent.default() == AdminEvent.WakeUp
    assert AdminEvent.enum_name() == "admin.event"
    assert AdminEvent.enum_version() == "000"
