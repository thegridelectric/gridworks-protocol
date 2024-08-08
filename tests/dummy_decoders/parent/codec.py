from gwproto import (
    CallableDecoder,
    Decoders,
    MQTTCodec,
    create_message_payload_discriminator,
)
from gwproto.gs import PowerMaker
from gwproto.messages import BatchedReadingsMaker, SnapshotSpaceheatMaker

from tests.dummy_decoders import CHILD

ParentMessageDecoder = create_message_payload_discriminator(
    model_name="ParentMessageDecoder",
    module_names=["gwproto.messages"],
)


class ParentMQTTCodec(MQTTCodec):
    def __init__(self):
        super().__init__(
            Decoders.from_objects(
                [
                    BatchedReadingsMaker,
                    SnapshotSpaceheatMaker,
                ],
                message_payload_discriminator=ParentMessageDecoder,
            ).add_decoder(
                "p", CallableDecoder(lambda decoded: PowerMaker(decoded[0]).tuple)
            )
        )

    def validate_source_alias(self, source_alias: str):
        if source_alias != CHILD:
            raise Exception(f"alias {source_alias} not my child")
