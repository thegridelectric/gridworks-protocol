from gwproto import (
    MQTTCodec,
    create_message_model,
)
from tests.dummy_decoders import CHILD, PARENT


class ParentMQTTCodec(MQTTCodec):
    def __init__(self) -> None:
        super().__init__(
            create_message_model(
                model_name="ParentMessageDecoder",
                module_names=["gwproto.messages"],
            )
        )

    def validate_source_and_destination(self, src: str, dst: str) -> None:
        if src != CHILD or dst != PARENT:
            raise ValueError(
                "ERROR validating src and/or dst\n"
                f"  exp: {CHILD} -> {PARENT}\n"
                f"  got: {src} -> {dst}"
            )
