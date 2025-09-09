import dataclasses
from dataclasses import dataclass

from gwproto.enums import MessageCategorySymbol


@dataclass
class DecodedMQTTTopic:
    envelope_type: str = ""
    src: str = ""
    dst: str = ""
    message_type: str = ""
    remainder: list[str] = dataclasses.field(default_factory=list)

    def __str__(self) -> str:
        return f"DecodedMQTTTopic type: {self.envelope_type} src: {self.src} message type:{self.message_type} remainder:{self.remainder}"


class MQTTTopic:
    """Handles encoding and decoding of MQTT topics for GridWorks message delivery.

    This class manages the conversion between different message delivery patterns
    used in GridWorks, handling the transformation between human-readable GNode
    aliases (using dots) and MQTT-compatible topics (using slashes and hyphens).

    The RabbitMQ broker uses a plugin to appear as an MQTT broker to MQTT clients
    like SCADA systems. There's a direct mapping between RabbitMQ routing keys
    and MQTT topics:
        - RabbitMQ routing key: gw.hw1-isone-ma-boston-scada.to.a.report-event
        - MQTT topic:          gw/hw1-isone-ma-boston-scada/to/a/report-event

    Supported Message Patterns:
        1. ScadaWrapped (gw): Full envelope with header/payload for acknowledgment tracking
           Format: gw/src-alias/to/dst-alias/type-name

        2. JsonDirect (rj): Point-to-point messages between specific actors
           Format: rj/src-alias/from-role/type-name/to-class/dst-alias

        3. JsonBroadcast (rjb): One-to-many broadcast messages
           Format: rjb/src-alias/from-role/type-name[/radio-channel]

    Naming Conventions:
        - GNode aliases use dots (e.g., "hw1.isone.ma.boston.scada")
        - MQTT topics replace dots with hyphens (e.g., "hw1-isone-ma-boston-scada")
        - Type names follow the same pattern (e.g., "power.watts" -> "power-watts")

    See Also:
        - [Message Delivery Architecture documentation](https://gridworks.readthedocs.io/message-delivery-architecture.md)
        - MessageCategory and MessageCategorySymbol enums
        - DecodedMQTTTopic for the decoded structure
    """

    DOT = "."
    DOT_REPLACEMENT = "-"

    @classmethod
    def encode(  # noqa: PLR0913
        cls,
        envelope_type: str | MessageCategorySymbol,
        src: str,
        dst: str = "",
        message_type: str = "",
        from_class: str = "",
        to_class: str = "",
        radio_channel: str = "",
    ) -> str:
        """
        Encode an MQTT topic/routing key based on the envelope type.

        Args:
            envelope_type: The message category symbol (gw, rj, rjb)
            src: Source GNode alias (with dots)
            dst: Destination GNode alias (with dots) - required for gw and rj
            message_type: The ASL type name (with dots)
            from_class: Sender's GNodeClass - required for rj and rjb
            to_class: Receiver's GNodeClass - required for rj
            radio_channel: Optional channel for rjb broadcasts

        ScadaWrapped: gw/src/to/dst/type
        JsonDirect: rj/from-alias/from-class/type-name/to-class/to-alias
        JsonBroadcast: rjb/from-alias/from-role/type-name[/radio-channel]

        For backwards compatibility, ScadaWrapped (gw) allows empty dst,
        producing topics like: gw/src/to//type
        """
        # Convert to string if enum passed
        if isinstance(envelope_type, MessageCategorySymbol):
            envelope_type = envelope_type.value

        # Replace dots with hyphens in all components
        src_h = src.replace(cls.DOT, cls.DOT_REPLACEMENT)
        dst_h = dst.replace(cls.DOT, cls.DOT_REPLACEMENT) if dst else ""
        type_h = (
            message_type.replace(cls.DOT, cls.DOT_REPLACEMENT) if message_type else ""
        )

        # ScadaWrapped
        if envelope_type == MessageCategorySymbol.gw.value:
            # gw/src/to/dst/type
            return f"{envelope_type}/{src_h}/to/{dst_h}/{type_h}"

        # JsonDirect
        if envelope_type == MessageCategorySymbol.rj.value:
            # rj/from-alias/from-class/type-name/to-class/to-alias
            if not all([from_class, to_class, dst]):
                raise ValueError(
                    "JsonDirect requires from_class, to_class, and destination"
                )
            return f"{envelope_type}/{src_h}/{from_class}/{type_h}/{to_class}/{dst_h}"

        if envelope_type == MessageCategorySymbol.rjb.value:
            # rjb/from-alias/from-role/type-name[/radio-channel]
            if not from_class:
                raise ValueError("JsonBroadcast requires from_class")
            base = f"{envelope_type}/{src_h}/{from_class}/{type_h}"
            if radio_channel:
                return f"{base}/{radio_channel}"
            return base

        raise ValueError(f"Unknown envelope type: {envelope_type}")

    @classmethod
    def encode_subscription(
        cls,
        envelope_type: str | MessageCategorySymbol,
        src: str = "",
        dst: str = "",
        from_class: str = "",
        to_class: str = "",
    ) -> str:
        """
        Encode an MQTT subscription pattern with wildcards.

        Args:
            envelope_type: The message category symbol (gw, rj, rjb)
            src: Source pattern (use + for single-level wildcard, # for multi-level)
            dst: Destination pattern (for gw and rj)
            from_class: Sender's role pattern (for rj and rjb)
            to_class: Receiver's role pattern (for rj)

        Examples:
            # Subscribe to all ScadaWrapped messages to me:
            encode_subscription("gw", src="+", dst="my-alias")

            # Subscribe to all JsonDirect messages to my role:
            encode_subscription("rj", to_class="scada", dst="my-alias")

            # Subscribe to all broadcasts from marketmakers:
            encode_subscription("rjb", from_class="marketmaker")
        """
        if isinstance(envelope_type, MessageCategorySymbol):
            envelope_type = envelope_type.value

        if envelope_type == MessageCategorySymbol.gw.value:
            # Use wildcards for unspecified parts
            src_part = src.replace(cls.DOT, cls.DOT_REPLACEMENT) if src else "+"
            dst_part = dst.replace(cls.DOT, cls.DOT_REPLACEMENT) if dst else "+"
            return f"{envelope_type}/{src_part}/to/{dst_part}/#"

        if envelope_type == MessageCategorySymbol.rj.value:
            src_part = src.replace(cls.DOT, cls.DOT_REPLACEMENT) if src else "+"
            from_class_part = from_class if from_class else "+"
            to_class_part = to_class if to_class else "+"
            dst_part = dst.replace(cls.DOT, cls.DOT_REPLACEMENT) if dst else "+"
            return f"{envelope_type}/{src_part}/{from_class_part}/+/{to_class_part}/{dst_part}"

        if envelope_type == MessageCategorySymbol.rjb.value:
            src_part = src.replace(cls.DOT, cls.DOT_REPLACEMENT) if src else "+"
            from_class_part = from_class if from_class else "+"
            # Use to match any remaining parts (type and optional radio channel)
            return f"{envelope_type}/{src_part}/{from_class_part}/#"

        raise ValueError(f"Unknown envelope type: {envelope_type}")

    @classmethod
    def decode(cls, topic: str) -> DecodedMQTTTopic:
        if not topic:
            raise ValueError("ERROR. Topic must have at least one character")

        topic = str(topic).replace(cls.DOT_REPLACEMENT, cls.DOT)
        parts = topic.split("/")
        envelope_type = parts[0]

        # The envelope type tells us which pattern to expect
        if envelope_type == MessageCategorySymbol.gw.value:
            # gw/src/to/dst/type[/remainder]
            return cls._decode_scada_wrapped(topic)
        if envelope_type == MessageCategorySymbol.rj.value:
            # rj/from-alias/from-class/type-name/to-class/to-alias
            return cls._decode_json_direct(parts)
        if envelope_type == MessageCategorySymbol.rjb.value:
            # rjb/from-alias/from-class/type-name[/radio-channel]
            return cls._decode_json_broadcast(parts)
        raise ValueError(f"Unknown envelope type: {envelope_type}")

    @classmethod
    def _decode_json_direct(cls, parts: list[str]) -> DecodedMQTTTopic:
        """Decode rj/from-alias/from-class/type-name/to-class/to-alias pattern"""
        if len(parts) < 6:
            raise ValueError(f"JsonDirect needs 6+ parts, got {len(parts)}")

        return DecodedMQTTTopic(
            envelope_type=MessageCategorySymbol.rj.value,
            src=parts[1],
            dst=parts[5],
            message_type=parts[3],
            remainder=parts[6:] if len(parts) > 6 else [],
        )

    @classmethod
    def _decode_json_broadcast(cls, parts: list[str]) -> DecodedMQTTTopic:
        """Decode rjb/from-alias/from-class/type-name[/radio-channel] pattern"""
        if len(parts) < 4:
            raise ValueError(f"JsonBroadcast needs 4+ parts, got {len(parts)}")

        return DecodedMQTTTopic(
            envelope_type=MessageCategorySymbol.rjb.value,
            src=parts[1],
            dst="",  # Broadcast has no destination
            message_type=parts[3],
            remainder=parts[4:] if len(parts) > 4 else [],
        )

    @classmethod
    def _decode_scada_wrapped(cls, topic: str) -> DecodedMQTTTopic:
        if not topic:
            raise ValueError("ERROR. Topic must have at least one character")
        topic = str(topic).replace(cls.DOT_REPLACEMENT, cls.DOT)
        split = topic.split("/")
        envelope_type = split[0]
        # for example: 'gw'
        remainder: list[str]
        if len(split) == 1:
            src = ""
            dst = ""
            message_type = ""
            remainder = []
        # for example: 'gw/hw1-isone-ma-boston-scada'
        elif len(split) == 2:
            src = split[1]
            dst = ""
            message_type = ""
            remainder = []
        # len > 2
        elif split[2] != "to":
            src = split[1]
            dst = ""
            message_type = ""
            remainder = split[2:]
        elif len(split) == 3:
            src = split[1]
            dst = ""
            message_type = ""
            remainder = []
        # for example: 'gw/hw1-isone-ma-boston-scada/to/a'
        elif len(split) == 4:
            src = split[1]
            dst = split[3]
            message_type = ""
            remainder = []
        # for example: 'gw/hw1-isone-ma-boston-scada/to/a/report-event'
        #          or: 'gw/hw1-isone-ma-boston-scada/to/a/report-event/x'
        else:
            src = split[1]
            dst = split[3]
            message_type = split[4]
            remainder = split[5:]
        return DecodedMQTTTopic(
            envelope_type=envelope_type,
            src=src,
            dst=dst,
            message_type=message_type,
            remainder=remainder,
        )
