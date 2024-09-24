import json
from pathlib import Path

import pytest
from gw.errors import DcError

from gwproto import HardwareLayout


def test_hardware_layout() -> None:
    HardwareLayout.load("tests/config/hardware-layout.json")

    # test Ads111x Terminal Block consistency
    with Path("tests/config/hardware-layout.json").open() as f:
        layout_dict = json.loads(f.read())

        # Ads111xBasedCacs have at most 12 terminal blocks. Make an impossible one
        layout_dict["Ads111xBasedComponents"][0]["ThermistorConfigList"][0][
            "TerminalBlockIdx"
        ] = 13

        with pytest.raises(DcError):
            HardwareLayout.load_dict(layout_dict)
