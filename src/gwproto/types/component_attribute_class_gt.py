"""Type component.attribute.class.gt, version 000"""

from typing import Any, Dict, Literal, Optional

from pydantic import BaseModel, ConfigDict, model_serializer, model_validator

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
    def desymbolize(cls, data: Any) -> Any:  # noqa: ANN401
        if symbolizing():
            desymbolize(
                data,
                symbolized_name="MakeModelGtEnumSymbol",
                enum_class=MakeModel,
            )
        return data

    @model_serializer(when_used="json")
    def symbolize(self) -> Dict[str, Any]:
        # DRAWBACK: we lose parameters passed to model_dump_json
        d = self.model_dump()
        if symbolizing():
            symbolize(d, enum_class=MakeModel)
        return d
