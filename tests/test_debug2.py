from tests.dummy_decoders.parent.codec import ParentMQTTCodec


dst_codec = ParentMQTTCodec()

encoded_m = b'{"Header": {"Src": "child", "Dst": "", "MessageType": "batched.readings", "MessageId": "", "AckRequired": false, "TypeName": "gridworks.header"}, "Payload": {"FromGNodeAlias": "d1.isone.ct.newhaven.rose.scada", "FromGNodeInstanceId": "9479051a-55fd-4da7-b14f-746853d70357", "AboutGNodeAlias": "d1.isone.ct.newhaven.rose.ta", "SlotStartUnixS": 1710010410, "BatchedTransmissionPeriodS": 30, "DataChannelList": [{"Name": "hp-idu-pwr", "DisplayName": "Hp IDU", "AboutNodeName": "hp-idu-pwr", "CapturedByNodeName": "s.pwr-meter", "Id": "50cf426b-ff3f-4a30-8415-8d3fba5e0ab7", "TypeName": "data.channel.gt", "Version": "000", "TelemetryNameGtEnumSymbol": "af39eec9"}], "ChannelReadingList": [{"ChannelId": "50cf426b-ff3f-4a30-8415-8d3fba5e0ab7", "ValueList": [1220, 1400], "ScadaReadTimeUnixMsList": [1710010425545, 1710010438720], "TypeName": "channel.readings", "Version": "000"}], "FsmActionList": [], "FsmReportList": [], "Id": "aa3dc3d6-3ef5-4b1f-8c3f-c9a4ef15195e", "TypeName": "batched.readings", "Version": "000"}, "TypeName": "gw"}'
decoded_m = dst_codec.decode(
    "gw/child/batched-readings",
    encoded_m,
)
