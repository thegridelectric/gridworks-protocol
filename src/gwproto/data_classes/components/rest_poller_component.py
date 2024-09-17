from gwproto.data_classes.components.component import Component
from gwproto.types import ComponentAttributeClassGt, RESTPollerComponentGt
from gwproto.types.rest_poller_gt import RESTPollerSettings


class RESTPollerComponent(Component[RESTPollerComponentGt, ComponentAttributeClassGt]):
    @property
    def rest(self) -> RESTPollerSettings:
        return self.gt.Rest
