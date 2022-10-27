import abc
import json
from abc import abstractmethod
from typing import Any
from typing import Callable
from typing import NamedTuple
from typing import Optional
from typing import Type

from pydantic import BaseModel


class Decoder(abc.ABC):
    def decode_str(self, content: str | bytes, encoding: str = "utf-8") -> Any:
        if isinstance(content, bytes):
            content = content.decode(encoding)
        return self.decode_obj(json.loads(content))

    @abstractmethod
    def decode_obj(self, o: Any) -> Any:
        ...


class CallableDecoder(Decoder):
    _decode_obj: Callable[[Any], Any]

    def __init__(self, decode_obj: Callable[[Any], Any]):
        if not callable(decode_obj):
            raise ValueError(
                f"ERROR. decode_obj {decode_obj}/{type(decode_obj)} attribute is not Callable"
            )
        self._decode_obj = decode_obj

    def decode_obj(self, o: Any) -> Any:
        return self._decode_obj(o)


class PydanticDecoder(CallableDecoder):
    def __init__(self, model: Type["BaseModel"]):
        super().__init__(model.parse_obj)


class MakerDecoder(CallableDecoder):
    DECODER_FUNCTION_NAME: str = "dict_to_tuple"

    def __init__(self, model: Any):
        decoder_function = getattr(model, self.DECODER_FUNCTION_NAME, None)
        if decoder_function is None:
            raise ValueError(
                f"ERROR. {model} has no function {self.DECODER_FUNCTION_NAME}"
            )
        super().__init__(decoder_function)


class DecoderItem(NamedTuple):
    type_name: str
    decoder: Decoder


class Decoders:
    _decoders: dict[str, Decoder]

    def __init__(self, decoders: Optional[dict[str, Decoder]] = None):
        self._decoders = dict()
        if decoders is not None:
            self._decoders.update(decoders)

    def decoder(self, type_name: str) -> Decoder:
        return self._decoders[type_name]

    def decode_str(self, type_name: str, content: str | bytes, encoding="utf-8") -> Any:
        return self.decoder(type_name).decode_str(content, encoding=encoding)

    def decode_obj(self, type_name: str, o: Any) -> Any:
        return self.decoder(type_name).decode_obj(o)

    def add_decoder(self, type_name: str, decoder: Decoder) -> "Decoders":
        self._validate(type_name, decoder)
        self._decoders[type_name] = decoder
        return self

    def add_decoders(self, decoders: dict[str, Decoder]) -> "Decoders":
        for type_name, decoder in decoders.items():
            self._validate(type_name, decoder)
        self._decoders.update(decoders)
        for type_name, decoder in decoders.items():
            self._validate(type_name, decoder)
        return self

    def merge(self, other: "Decoders") -> "Decoders":
        self.add_decoders(other._decoders)
        return self

    def __contains__(self, type_name: str) -> bool:
        return type_name in self._decoders

    def types(self) -> list[str]:
        return list(self._decoders.keys())

    def _validate(self, type_name: str, decoder: Decoder) -> None:
        if type_name in self._decoders:
            if self._decoders[type_name] is not decoder:
                raise ValueError(
                    f"ERROR. decoder for [{type_name}] is already present as [{self._decoders[type_name]}]"
                )
