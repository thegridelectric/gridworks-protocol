from gwproto import HardwareLayout


def test_hardware_layout() -> None:
    errors = []
    HardwareLayout.load(
        "tests/config/hardware-layout.json", errors=errors, raise_errors=False
    )
    assert not errors
