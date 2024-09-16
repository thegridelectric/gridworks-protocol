from gwproto.data_classes.components.component import Component
from gwproto.types import RESTPollerCacGt, RESTPollerComponentGt
from gwproto.types.rest_poller_gt import RESTPollerSettings


class RESTPollerComponent(Component[RESTPollerComponentGt, RESTPollerCacGt]):
    @property
    def rest(self) -> RESTPollerSettings:
        return self.gt.Rest
