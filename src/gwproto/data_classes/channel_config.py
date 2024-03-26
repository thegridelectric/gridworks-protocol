""" ChannelConfig"""
from abc import ABC
from typing import Dict
from typing import Optional

from gwproto.data_classes.mixin import StreamlinedSerializerMixin
from gwproto.enums import Unit


class ChannelConfigDc(ABC, StreamlinedSerializerMixin):
    by_id: Dict[str, "ChannelConfigDc"] = {}

    base_props = []
    base_props.append("channel_name")
    base_props.append("poll_period_ms")
    base_props.append("capture_period_s")
    base_props.append("async_capture")
    base_props.append("async_capture_delta")
    base_props.append("exponent")
    base_props.append("unit")

    def __new__(cls, channel_name, *args, **kwargs):
        try:
            return cls.by_id[channel_name]
        except KeyError:
            instance = super().__new__(cls)
            cls.by_id[channel_name] = instance
            return instance

    def __init__(
        self,
        channel_name: str,
        poll_period_ms: int,
        capture_period_s: int,
        async_capture: bool,
        async_capture_delta: int,
        exponent: int,
        unit: Unit,
    ):
        self.channel_name = channel_name
        self.poll_period_ms = poll_period_ms
        self.capture_period_s = capture_period_s
        self.async_capture = async_capture
        self.async_capture_delta = async_capture_delta
        self.exponent = exponent
        self.unit = unit

    def __repr__(self):
        return f"{self.channel_name}: PollPeriod: {self.poll_period_ms} ms, CapturePeriod: {self.capture_period_s} s, Async: {self.async_capture}"
