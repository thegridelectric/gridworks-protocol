import pytest

from gwproto import DecodedMQTTTopic, MQTTTopic
from gwproto.enums import MessageCategorySymbol


def test_mqtt_topic_encode() -> None:
    # Test ScadaWrapped
    assert MQTTTopic.encode("gw", "bar", "baz", "bla") == "gw/bar/to/baz/bla"
    assert MQTTTopic.encode("gw", "baz.bla", "x.y", "bla") == "gw/baz-bla/to/x-y/bla"
    assert MQTTTopic.encode_subscription("gw", "bar", "baz") == "gw/bar/to/baz/#"
    assert (
        MQTTTopic.encode_subscription("gw", "baz.bla", "x.y") == "gw/baz-bla/to/x-y/#"
    )

    # Test JsonDirect
    assert (
        MQTTTopic.encode(
            MessageCategorySymbol.rj,
            "hw1.keene.beech",
            "hw1.keene",
            "bid",
            from_class="atn",
            to_class="marketmaker",
        )
        == "rj/hw1-keene-beech/atn/bid/marketmaker/hw1-keene"
    )


def test_mqtt_topic_decode() -> None:
    with pytest.raises(ValueError):
        MQTTTopic.decode("")

    # envelope must be in [gw, rj, rjb]
    with pytest.raises(ValueError):
        decoded = MQTTTopic.decode("//to//")

    with pytest.raises(ValueError):
        decoded = MQTTTopic.decode("Envelope")

    # Test JsonBroadcast decoding (no dst)
    decoded = MQTTTopic.decode("rjb/hw1-keene/marketmaker/latest-price")
    assert decoded.envelope_type == "rjb"
    assert decoded.src == "hw1.keene"
    assert decoded.dst == ""  # Broadcast has no destination
    assert decoded.message_type == "latest.price"
    assert decoded.remainder == []

    # Test JsonBroadcast with radio channel
    decoded = MQTTTopic.decode("rjb/hw1-keene/marketmaker/latest-price/rt60gate5")
    assert decoded.envelope_type == "rjb"
    assert decoded.src == "hw1.keene"
    assert decoded.dst == ""
    assert decoded.message_type == "latest.price"
    assert decoded.remainder == ["rt60gate5"]

    # usual ScadaWrapped case - Envelope/Src/to/Dst/MsgType
    decoded = MQTTTopic.decode("gw/Src/to/Dst/MsgType")
    assert decoded.envelope_type == "gw"
    assert decoded.src == "Src"
    assert decoded.dst == "Dst"
    assert decoded.message_type == "MsgType"
    assert decoded.remainder == []
    assert decoded == DecodedMQTTTopic(
        envelope_type="gw", src="Src", dst="Dst", message_type="MsgType"
    )
    assert str(decoded)

    # '-', '.' conversions
    decoded = MQTTTopic.decode("gw/Src-2/to/Dst-3/MsgType")
    assert decoded.envelope_type == "gw"
    assert decoded.src == "Src.2"
    assert decoded.dst == "Dst.3"
    assert decoded.message_type == "MsgType"
    assert decoded.remainder == []
    assert decoded == DecodedMQTTTopic(
        envelope_type="gw", src="Src.2", dst="Dst.3", message_type="MsgType"
    )

    # envelope only
    decoded = MQTTTopic.decode("gw")
    assert decoded.envelope_type == "gw"
    assert decoded.src == ""
    assert decoded.dst == ""
    assert decoded.message_type == ""
    assert decoded.remainder == []

    # envelop/src only
    decoded = MQTTTopic.decode("gw/Src")
    assert decoded.envelope_type == "gw"
    assert decoded.src == "Src"
    assert decoded.dst == ""
    assert decoded.message_type == ""
    assert decoded.remainder == []

    # envelop/src, but 'to' followed by nothing or not present
    for topic, remainder in [
        ("gw/Src/to", []),
        ("gw/Src/to/", []),
        ("gw/Src/to//", []),
        ("gw/Src/to///", [""]),
        ("gw/Src/x", ["x"]),
        ("gw/Src/x/y", ["x", "y"]),
        ("gw/Src/x/y/z", ["x", "y", "z"]),
    ]:
        decoded = MQTTTopic.decode(topic)
        assert decoded.envelope_type == "gw"
        assert decoded.src == "Src"
        assert decoded.dst == ""
        assert decoded.message_type == ""
        assert decoded.remainder == remainder

    # enevelop/src/to/dst only
    decoded = MQTTTopic.decode("gw/Src/to/Dst")
    assert decoded.envelope_type == "gw"
    assert decoded.src == "Src"
    assert decoded.dst == "Dst"
    assert decoded.message_type == ""
    assert decoded.remainder == []
    assert decoded == DecodedMQTTTopic(
        envelope_type="gw", src="Src", dst="Dst", message_type=""
    )

    # 1 extra stuff
    decoded = MQTTTopic.decode("gw/Src/to/Dst/MsgType/Extra")
    assert decoded.envelope_type == "gw"
    assert decoded.src == "Src"
    assert decoded.dst == "Dst"
    assert decoded.message_type == "MsgType"
    assert decoded.remainder == ["Extra"]
    assert decoded == DecodedMQTTTopic(
        envelope_type="gw",
        src="Src",
        dst="Dst",
        message_type="MsgType",
        remainder=["Extra"],
    )

    # 2 extra stuff
    decoded = MQTTTopic.decode("gw/Src/to/Dst/MsgType/Extra/MoreExtra")
    assert decoded.envelope_type == "gw"
    assert decoded.src == "Src"
    assert decoded.dst == "Dst"
    assert decoded.message_type == "MsgType"
    assert decoded.remainder == ["Extra", "MoreExtra"]
    assert decoded == DecodedMQTTTopic(
        envelope_type="gw",
        src="Src",
        dst="Dst",
        message_type="MsgType",
        remainder=["Extra", "MoreExtra"],
    )
