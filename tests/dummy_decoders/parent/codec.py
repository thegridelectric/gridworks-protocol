from gwproto import CallableDecoder
from gwproto import Decoders
from gwproto import MQTTCodec
from gwproto import create_message_payload_discriminator
from gwproto.gs import GsPwr_Maker
from gwproto.messages import BatchedReadings_Maker
from gwproto.messages import Snapshot_Maker
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
                    BatchedReadings_Maker,
                    Snapshot_Maker,
                ],
                message_payload_discriminator=ParentMessageDecoder,
            ).add_decoder(
                "p", CallableDecoder(lambda decoded: GsPwr_Maker(decoded[0]).tuple)
            )
        )

    def validate_source_alias(self, source_alias: str):
        if source_alias != CHILD:
            raise Exception(f"alias {source_alias} not my child")
