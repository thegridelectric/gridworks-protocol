from gwproto import (
    MQTTCodec,
    create_message_model,
)
from tests.dummy_decoders import CHILD


class ParentMQTTCodec(MQTTCodec):
    def __init__(self) -> None:
        super().__init__(
            create_message_model(
                model_name="ParentMessageDecoder",
                module_names=["gwproto.messages"],
            )
        )

    def validate_source_alias(self, source_alias: str) -> None:  # noqa: PLR6301, RUF100
        if source_alias != CHILD:
            raise ValueError(f"alias {source_alias} not my child")
