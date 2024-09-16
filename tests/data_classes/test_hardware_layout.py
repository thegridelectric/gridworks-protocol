from gwproto import HardwareLayout


def test_hardware_layout() -> None:
    HardwareLayout.load("tests/config/hardware-layout.json")
