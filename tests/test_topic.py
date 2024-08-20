import pytest

from gwproto import DecodedMQTTTopic, MQTTTopic


def test_mqtt_topic_encode() -> None:
    assert MQTTTopic.encode("foo", "bar", "baz") == "foo/bar/baz"
    assert MQTTTopic.encode("foo.bar", "baz.bla", "bla") == "foo-bar/baz-bla/bla"
    assert MQTTTopic.encode_subscription("foo", "bar") == "foo/bar/#"
    assert MQTTTopic.encode_subscription("foo.bar", "baz.bla") == "foo-bar/baz-bla/#"


def test_mqtt_topic_decode() -> None:
    with pytest.raises(ValueError):  # noqa: PT011
        MQTTTopic.decode("")

    decoded = MQTTTopic.decode("foo/bar/baz")
    assert decoded.envelope_type == "foo"
    assert decoded.src == "bar"
    assert decoded.message_type == "baz"
    assert decoded.remainder == []
    assert decoded == DecodedMQTTTopic(
        envelope_type="foo", src="bar", message_type="baz"
    )
    assert str(decoded)

    decoded = MQTTTopic.decode("foo-bar/baz-bla/bla")
    assert decoded.envelope_type == "foo.bar"
    assert decoded.src == "baz.bla"
    assert decoded.message_type == "bla"
    assert decoded.remainder == []
    assert decoded == DecodedMQTTTopic(
        envelope_type="foo.bar", src="baz.bla", message_type="bla"
    )

    decoded = MQTTTopic.decode("foo")
    assert decoded.envelope_type == "foo"
    assert not decoded.src
    assert not decoded.message_type
    assert decoded.remainder == []

    decoded = MQTTTopic.decode("foo/bar")
    assert decoded.envelope_type == "foo"
    assert decoded.src == "bar"
    assert not decoded.message_type
    assert decoded.remainder == []

    decoded = MQTTTopic.decode("foo/bar/baz/a/b/c")
    assert decoded.envelope_type == "foo"
    assert decoded.src == "bar"
    assert decoded.message_type == "baz"
    assert decoded.remainder == ["a", "b", "c"]
