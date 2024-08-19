from gwproto import Decoders, MQTTCodec, create_message_payload_discriminator
from gwproto.messages import GtDispatchBoolean_Maker, GtShCliAtnCmd_Maker

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
                [
                    GtDispatchBoolean_Maker,
                    GtShCliAtnCmd_Maker,
                ],
                message_payload_discriminator=ChildMessageDecoder,
            )
        )

    def validate_source_alias(self, source_alias: str) -> None:
        if source_alias != PARENT:
            raise Exception(f"alias {source_alias} not my parent!")
