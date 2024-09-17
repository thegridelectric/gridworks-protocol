"""Tests batched.readings type, version 000"""

from gwproto.types import BatchedReadings


def test_batched_readings_generated() -> None:
    d = {
        "FromGNodeAlias": "dwtest.isone.ct.newhaven.orange1.ta.scada",
        "FromGNodeInstanceId": "0384ef21-648b-4455-b917-58a1172d7fc1",
        "AboutGNodeAlias": "dwtest.isone.ct.newhaven.orange1.ta",
        "SlotStartUnixS": 1656945300,
        "BatchedTransmissionPeriodS": 300,
        "MessageCreatedMs": 1656945600044,
        "DataChannelList": ,
        "ChannelReadingList": [],
        "FsmActionList": [],
        "FsmReportList": [],
        "Id": ,
        "TypeName": "batched.readings",
        "Version": "000",
    }

    t = BatchedReadings(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d
