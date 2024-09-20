from gwproto.data_classes.sh_node import ShNode
from gwproto.types import DataChannelGt


class DataChannel(DataChannelGt):
    about_node: ShNode
    captured_by_node: ShNode

    def __hash__(self) -> int:
        return hash(self.Id)
