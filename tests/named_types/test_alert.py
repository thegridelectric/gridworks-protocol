"""Tests alert type, version 000"""

from gwproto.named_types import Alert


def test_alert_generated() -> None:
    d = {
        "FromGNodeAlias": "d1.isone.ct.orange",
        "AboutNode": "hp-odu",
        "UnixS": 1732385186,
        "Summary": "This heating system is lonely",
        "OpsGenieAlias": "ScadaNotRunning",
        "TypeName": "alert",
        "Version": "000",
    }

    d2 = Alert.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
