from gw.utils import snake_to_pascal
from pydantic import BaseModel, ConfigDict

DEFAULT_WEB_SERVER_NAME = "default"


class WebServerGt(BaseModel):
    Name: str = DEFAULT_WEB_SERVER_NAME
    Host: str = "localhost"
    Port: int = 8080
    Enabled: bool = True
    Kwargs: dict = {}
    model_config = ConfigDict(
        extra="allow", populate_by_name=True, alias_generator=snake_to_pascal
    )
