import pytest

from gwproto import DecodedMQTTTopic, MQTTTopic


def test_mqtt_topic_encode() -> None:
    assert MQTTTopic.encode("foo", "bar", "baz", "bla") == "foo/bar/to/baz/bla"
    assert (
        MQTTTopic.encode("foo.bar", "baz.bla", "x.y", "bla")
        == "foo-bar/baz-bla/to/x-y/bla"
    )
    assert MQTTTopic.encode_subscription("foo", "bar", "baz") == "foo/bar/to/baz/#"
    assert (
        MQTTTopic.encode_subscription("foo.bar", "baz.bla", "x.y")
        == "foo-bar/baz-bla/to/x-y/#"
    )


def test_mqtt_topic_decode() -> None:
    with pytest.raises(ValueError):
        MQTTTopic.decode("")

    # ususal case - Envelope/Src/to/Dst/MsgType
    decoded = MQTTTopic.decode("Envelope/Src/to/Dst/MsgType")
    assert decoded.envelope_type == "Envelope"
    assert decoded.src == "Src"
    assert decoded.dst == "Dst"
    assert decoded.message_type == "MsgType"
    assert decoded.remainder == []
    assert decoded == DecodedMQTTTopic(
        envelope_type="Envelope", src="Src", dst="Dst", message_type="MsgType"
    )
    assert str(decoded)

    # '-', '.' conversions
    decoded = MQTTTopic.decode("Envelope-1/Src-2/to/Dst-3/MsgType")
    assert decoded.envelope_type == "Envelope.1"
    assert decoded.src == "Src.2"
    assert decoded.dst == "Dst.3"
    assert decoded.message_type == "MsgType"
    assert decoded.remainder == []
    assert decoded == DecodedMQTTTopic(
        envelope_type="Envelope.1", src="Src.2", dst="Dst.3", message_type="MsgType"
    )

    # envelope only
    decoded = MQTTTopic.decode("Envelope")
    assert decoded.envelope_type == "Envelope"
    assert decoded.src == ""
    assert decoded.dst == ""
    assert decoded.message_type == ""
    assert decoded.remainder == []

    # envelop/src only
    decoded = MQTTTopic.decode("Envelope/Src")
    assert decoded.envelope_type == "Envelope"
    assert decoded.src == "Src"
    assert decoded.dst == ""
    assert decoded.message_type == ""
    assert decoded.remainder == []

    # envelop/src, but 'to' followed by nothing or not present
    for topic, remainder in [
        ("Envelope/Src/to", []),
        ("Envelope/Src/to/", []),
        ("Envelope/Src/to//", []),
        ("Envelope/Src/to///", [""]),
        ("Envelope/Src/x", ["x"]),
        ("Envelope/Src/x/y", ["x", "y"]),
        ("Envelope/Src/x/y/z", ["x", "y", "z"]),
    ]:
        decoded = MQTTTopic.decode(topic)
        assert decoded.envelope_type == "Envelope"
        assert decoded.src == "Src"
        assert decoded.dst == ""
        assert decoded.message_type == ""
        assert decoded.remainder == remainder

    # enevelop/src/to/dst only
    decoded = MQTTTopic.decode("Envelope/Src/to/Dst")
    assert decoded.envelope_type == "Envelope"
    assert decoded.src == "Src"
    assert decoded.dst == "Dst"
    assert decoded.message_type == ""
    assert decoded.remainder == []
    assert decoded == DecodedMQTTTopic(
        envelope_type="Envelope", src="Src", dst="Dst", message_type=""
    )

    # 1 extra stuff
    decoded = MQTTTopic.decode("Envelope/Src/to/Dst/MsgType/Extra")
    assert decoded.envelope_type == "Envelope"
    assert decoded.src == "Src"
    assert decoded.dst == "Dst"
    assert decoded.message_type == "MsgType"
    assert decoded.remainder == ["Extra"]
    assert decoded == DecodedMQTTTopic(
        envelope_type="Envelope",
        src="Src",
        dst="Dst",
        message_type="MsgType",
        remainder=["Extra"],
    )

    # 2 extra stuff
    decoded = MQTTTopic.decode("Envelope/Src/to/Dst/MsgType/Extra/MoreExtra")
    assert decoded.envelope_type == "Envelope"
    assert decoded.src == "Src"
    assert decoded.dst == "Dst"
    assert decoded.message_type == "MsgType"
    assert decoded.remainder == ["Extra", "MoreExtra"]
    assert decoded == DecodedMQTTTopic(
        envelope_type="Envelope",
        src="Src",
        dst="Dst",
        message_type="MsgType",
        remainder=["Extra", "MoreExtra"],
    )

    # various odd cases
    decoded = MQTTTopic.decode("//to//")
    assert decoded.envelope_type == ""
    assert decoded.src == ""
    assert decoded.dst == ""
    assert decoded.message_type == ""
    assert decoded.remainder == []

    decoded = MQTTTopic.decode("//to////")
    assert decoded.envelope_type == ""
    assert decoded.src == ""
    assert decoded.dst == ""
    assert decoded.message_type == ""
    assert decoded.remainder == ["", ""]
