from gwproto import MQTTCodec, create_message_model
from tests.dummy_decoders import PARENT


class ChildMQTTCodec(MQTTCodec):
    def __init__(self) -> None:
        super().__init__(
            create_message_model(
                "ChildMessageDecoder",
                ["gwproto.messages"],
            )
        )

    def validate_source_alias(self, source_alias: str) -> None:  # noqa: PLR6301, RUF100
        if source_alias != PARENT:
            raise ValueError(f"alias {source_alias} not my parent!")
