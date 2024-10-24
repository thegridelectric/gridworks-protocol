from gwproto import MQTTCodec, create_message_model
from tests.dummy_decoders import CHILD, PARENT


class ChildMQTTCodec(MQTTCodec):
    def __init__(self) -> None:
        super().__init__(
            create_message_model(
                "ChildMessageDecoder",
                ["gwproto.messages"],
            )
        )

    def validate_source_and_destination(self, src: str, dst: str) -> None:
        if src != PARENT or dst != CHILD:
            raise ValueError(
                "ERROR validating src and/or dst\n"
                f"  exp: {PARENT} -> {CHILD}\n"
                f"  got: {src} -> {dst}"
            )
