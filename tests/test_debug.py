from tests.dummy_decoders.parent.codec import ParentMQTTCodec


dst_codec = ParentMQTTCodec()

encoded_m = b'{"Header": {"Src": "child", "Dst": "", "MessageType": "gt.sh.status", "MessageId": "", "AckRequired": false, "TypeName": "gridworks.header"}, "Payload": {"AboutGNodeAlias": "hw1.isone.ct.newhaven.orange1.ta", "BooleanactuatorCmdList": [], "FromGNodeAlias": "hw1.isone.ct.newhaven.orange1.ta.scada", "FromGNodeId": "28817671-3899-4e24-a337-abcb8633e47a", "MultipurposeTelemetryList": [{"AboutNodeAlias": "a.elt1", "ReadTimeUnixMsList": [1676592055586], "SensorNodeAlias": "a.m", "TelemetryNameGtEnumSymbol": "af39eec9", "TypeName": "gt.sh.multipurpose.telemetry.status", "Version": "100", "ValueList": [0]}, {"AboutNodeAlias": "a.tank.out.temp2", "ReadTimeUnixMsList": [1676592000232, 1676592060801, 1676592120037, 1676592180555, 1676592240089], "SensorNodeAlias": "a.s.analog.temp", "TelemetryNameGtEnumSymbol": "c89d0ba1", "TypeName": "gt.sh.multipurpose.telemetry.status", "Version": "100", "ValueList": [77, 361, -115, -9, -44]}, {"AboutNodeAlias": "a.tank.in.temp2", "ReadTimeUnixMsList": [1676592000232, 1676592060801, 1676592120037, 1676592180555, 1676592240089], "SensorNodeAlias": "a.s.analog.temp", "TelemetryNameGtEnumSymbol": "c89d0ba1", "TypeName": "gt.sh.multipurpose.telemetry.status", "Version": "100", "ValueList": [-3587, -3574, -3771, -3656, -3626]}, {"AboutNodeAlias": "a.garage.temp2", "ReadTimeUnixMsList": [1676592000232, 1676592060801, 1676592120037, 1676592180555, 1676592240089], "SensorNodeAlias": "a.s.analog.temp", "TelemetryNameGtEnumSymbol": "c89d0ba1", "TypeName": "gt.sh.multipurpose.telemetry.status", "Version": "100", "ValueList": [-3222, -3036, -3264, -3087, -3015]}, {"AboutNodeAlias": "a.tankoutside.temp2", "ReadTimeUnixMsList": [1676592000232, 1676592060801, 1676592120037, 1676592180555, 1676592240089], "SensorNodeAlias": "a.s.analog.temp", "TelemetryNameGtEnumSymbol": "c89d0ba1", "TypeName": "gt.sh.multipurpose.telemetry.status", "Version": "100", "ValueList": [3011, 3037, 2893, 3037, 3041]}], "ReportingPeriodS": 300, "SimpleTelemetryList": [{"ReadTimeUnixMsList": [1676592052038], "ShNodeAlias": "a.elt1.relay", "TelemetryNameGtEnumSymbol": "5a71d4b3", "TypeName": "gt.sh.simple.telemetry.status", "Version": "100", "ValueList": [0]}, {"ReadTimeUnixMsList": [1676592232171], "ShNodeAlias": "a.tank.out.pump.relay", "TelemetryNameGtEnumSymbol": "5a71d4b3", "TypeName": "gt.sh.simple.telemetry.status", "Version": "100", "ValueList": [0]}, {"ReadTimeUnixMsList": [1676592079160], "ShNodeAlias": "a.tank.out.pump.baseboard1.fan.relay", "TelemetryNameGtEnumSymbol": "5a71d4b3", "TypeName": "gt.sh.simple.telemetry.status", "Version": "100", "ValueList": [0]}, {"ReadTimeUnixMsList": [1676592033601, 1676592094057, 1676592154524, 1676592215130, 1676592275685], "ShNodeAlias": "a.tank.out.temp1", "TelemetryNameGtEnumSymbol": "c89d0ba1", "TypeName": "gt.sh.simple.telemetry.status", "Version": "100", "ValueList": [18000, 17937, 17937, 17875, 17812]}, {"ReadTimeUnixMsList": [1676592044721, 1676592104326, 1676592164389, 1676592224395, 1676592284085], "ShNodeAlias": "a.tank.out.far.temp1", "TelemetryNameGtEnumSymbol": "c89d0ba1", "TypeName": "gt.sh.simple.telemetry.status", "Version": "100", "ValueList": [15375, 15312, 15312, 15312, 15250]}, {"ReadTimeUnixMsList": [1676592034321, 1676592095091, 1676592155316, 1676592215161, 1676592275192], "ShNodeAlias": "a.tank.in.temp1", "TelemetryNameGtEnumSymbol": "c89d0ba1", "TypeName": "gt.sh.simple.telemetry.status", "Version": "100", "ValueList": [14437, 14375, 14312, 14312, 14312]}, {"ReadTimeUnixMsList": [1676592035601, 1676592095132, 1676592155706, 1676592215733, 1676592275380], "ShNodeAlias": "a.tank.temp0", "TelemetryNameGtEnumSymbol": "c89d0ba1", "TypeName": "gt.sh.simple.telemetry.status", "Version": "100", "ValueList": [21812, 21812, 21812, 21812, 21812]}, {"ReadTimeUnixMsList": [1676592024051, 1676592084160, 1676592144739, 1676592204239, 1676592264435], "ShNodeAlias": "a.garage.temp1", "TelemetryNameGtEnumSymbol": "c89d0ba1", "TypeName": "gt.sh.simple.telemetry.status", "Version": "100", "ValueList": [15125, 15062, 15062, 15062, 15062]}], "SlotStartUnixS": 1676592000, "StatusUid": "82abba64-d0df-4907-9b2b-6cb585421068", "TypeName": "gt.sh.status", "Version": "110"}, "TypeName": "gw"}'
decoded_m = dst_codec.decode(
    "gw/child/gt-sh-status",
    encoded_m,
)
