from gwproto import Decoders, MQTTCodec, create_message_payload_discriminator
from tests.dummy_decoders import PARENT

ChildMessageDecoder = create_message_payload_discriminator(
    "ChildMessageDecoder",
    [
        "gwproto.messages",
    ],
)


class ChildMQTTCodec(MQTTCodec):
    def __init__(self) -> None:
        super().__init__(
            Decoders.from_objects(
                message_payload_discriminator=ChildMessageDecoder,
            )
        )

    def validate_source_alias(self, source_alias: str) -> None:  # noqa: PLR6301, RUF100
        if source_alias != PARENT:
            raise ValueError(f"alias {source_alias} not my parent!")
