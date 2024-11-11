"""
Tests for enum admin.state.000 from the GridWorks Type Registry.
"""

from gwproto.enums import AdminState


def test_admin_state() -> None:
    assert set(AdminState.values()) == {
        "Awake",
        "Dormant",
    }

    assert AdminState.default() == AdminState.Dormant
    assert AdminState.enum_name() == "admin.state"
    assert AdminState.enum_version() == "000"
