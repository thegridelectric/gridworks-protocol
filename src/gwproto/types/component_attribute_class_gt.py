"""Type component.attribute.class.gt, version 000"""

from typing import Any, Callable, Dict, Literal, Optional

from pydantic import (
    BaseModel,
    ConfigDict,
    SerializationInfo,
    model_serializer,
    model_validator,
)

from gwproto.enums import MakeModel
from gwproto.enums.symbolized import desymbolize, symbolize, symbolizing
from gwproto.utils import UUID4Str


class ComponentAttributeClassGt(BaseModel):
    ComponentAttributeClassId: UUID4Str
    DisplayName: Optional[str] = None
    MakeModel: MakeModel
    TypeName: Literal["component.attribute.class.gt"] = "component.attribute.class.gt"
    Version: Literal["000"] = "000"

    model_config = ConfigDict(
        extra="allow",
        # comment these out to cut down on experimental headaches
        # alias_generator=camel_to_snake,  # noqa: ERA001
        # populate_by_name=True  # noqa: ERA001
        use_enum_values=True,
    )

    @model_validator(mode="before")
    @classmethod
    def desymbolize(cls, data: Any) -> Any:
        if symbolizing():
            desymbolize(
                data,
                symbolized_name="MakeModelGtEnumSymbol",
                enum_class=MakeModel,
            )
        return data

    @model_serializer(when_used="json", mode="wrap")
    def symbolize(self, handler: Callable, info: SerializationInfo) -> Dict[str, Any]:  # noqa: ANN001
        d = handler(self, info)
        if symbolizing():
            symbolize(d, enum_class=MakeModel)
        return d
