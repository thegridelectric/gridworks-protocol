from gwproto import Decoders
from gwproto import MQTTCodec
from gwproto import create_message_payload_discriminator
from gwproto.messages import GtShCliAtnCmd_Maker
from tests.dummy_decoders import PARENT


ChildMessageDecoder = create_message_payload_discriminator(
    "ChildMessageDecoder",
    [
        "gwproto.messages",
    ],
)


class ChildMQTTCodec(MQTTCodec):
    def __init__(self):
        super().__init__(
            Decoders.from_objects(
                [
                    GtShCliAtnCmd_Maker,
                ],
                message_payload_discriminator=ChildMessageDecoder,
            )
        )

    def validate_source_handle(self, source_handle: str):
        if source_handle != PARENT:
            raise Exception(f"alias {source_handle} not my boss!")
