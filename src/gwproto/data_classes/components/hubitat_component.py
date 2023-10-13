from typing import Optional

from gwproto.data_classes.component import Component


class HubitatComponent(Component):
    host: str
    maker_api_id: int
    access_token: str

    def __init__(
        self,
        component_id: str,
        component_attribute_class_id: str,
        host: str,
        maker_api_id: int,
        access_token: str,
        display_name: Optional[str] = None,
        hw_uid: Optional[str] = None,
    ):
        self.host = host
        self.maker_api_id = maker_api_id
        self.access_token = access_token
        super().__init__(
            component_id=component_id,
            component_attribute_class_id=component_attribute_class_id,
            display_name=display_name,
            hw_uid=hw_uid,
        )
