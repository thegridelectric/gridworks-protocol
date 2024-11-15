"""Tests scada.params type, version 000"""

from gwproto.named_types import ScadaParams


def test_scada_params_generated() -> None:
    d = {
        "FromGNodeAlias": "d1.isone.rose",
        "FromName": "a",
        "ToName": "h",
        "UnixTimeMs": 1731637846788,
        "MessageId": "37b64437-f5b2-4a80-b5fc-3d5a9f6b5b59",
        "TypeName": "scada.params",
        "Version": "000",
    }

    d2 = ScadaParams.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
