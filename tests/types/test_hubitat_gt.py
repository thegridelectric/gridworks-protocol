"""Test HubitatGt"""

import yarl
from gwproto.types.hubitat_gt import HubitatGt


def test_hubitat_gt() -> None:
    """Test HubitatGt"""

    mac = "00:01:02:03:0A:0B"
    listen_path_exp = mac.replace(":", "-")
    h = HubitatGt(
        Host="192.168.1.10",
        MakerApiId=1,
        AccessToken="foo",
        MacAddress=mac,
    )
    assert h.WebListenEnabled is True
    assert h.listen_path == listen_path_exp
    h2 = HubitatGt(WebListenEnabled=False, **h.model_dump(exclude_unset=True))
    assert h2.WebListenEnabled is False
    url = yarl.URL.build(scheme="http", host="192.168.1.20", port=1)
    assert str(h.listen_url(url)) == f"http://192.168.1.20:1/{listen_path_exp}"
    assert h.url_config().to_url() == yarl.URL("http://192.168.1.10")
    assert h.maker_api_url_config().to_url() == yarl.URL(
        "http://192.168.1.10/apps/api/1?access_token=foo"
    )
    assert h.devices_url_config().to_url() == yarl.URL(
        "http://192.168.1.10/apps/api/1/devices?access_token=foo"
    )
    url_configs_got = {k: v.to_url() for k, v in h.url_configs().items()}
    url_configs_exp = dict(
        base=yarl.URL("http://192.168.1.10"),
        maker_api=yarl.URL("http://192.168.1.10/apps/api/1?access_token=foo"),
        devices=yarl.URL("http://192.168.1.10/apps/api/1/devices?access_token=foo"),
    )
    assert url_configs_got == url_configs_exp
    assert h.urls() == url_configs_exp
    device_id = 1
    refresh_url_exp = yarl.URL(
        f"http://192.168.1.10/apps/api/1/devices/{device_id}/refresh?access_token=foo"
    )
    assert h.refresh_url_config(device_id).to_url() == refresh_url_exp
    assert h.refresh_url(device_id) == refresh_url_exp
