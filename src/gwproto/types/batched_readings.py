"""Type batched.readings, version 000"""
import json
import logging
from typing import Any
from typing import Dict
from typing import List
from typing import Literal

from pydantic import BaseModel
from pydantic import Extra
from pydantic import Field
from pydantic import validator

from gwproto.errors import SchemaError
from gwproto.types.channel_readings import ChannelReadings
from gwproto.types.channel_readings import ChannelReadings_Maker
from gwproto.types.data_channel_gt import DataChannelGt
from gwproto.types.data_channel_gt import DataChannelGt_Maker
from gwproto.types.fsm_atomic_report import FsmAtomicReport
from gwproto.types.fsm_atomic_report import FsmAtomicReport_Maker
from gwproto.types.fsm_full_report import FsmFullReport
from gwproto.types.fsm_full_report import FsmFullReport_Maker


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class BatchedReadings(BaseModel):
    """
    Batched Readings.

    A collection of telemetry readings sent up in periodic reports from a SCADA to an AtomicTNode.
    These are organized into data channels (a triple of TelemetryName, AboutNode, and CapturedByNode).
    This replaces GtShStatus. Changes include: FromGNodeId -> FromGNodeInstanveId ReportPeriodS
    -> BatchedTransmissionPeriodS
    """

    FromGNodeAlias: str = Field(
        title="FromGNodeAlias",
    )
    FromGNodeInstanceId: str = Field(
        title="FromGNodeInstanceId",
    )
    AboutGNodeAlias: str = Field(
        title="AboutGNodeAlias",
    )
    SlotStartUnixS: int = Field(
        title="SlotStartUnixS",
    )
    BatchedTransmissionPeriodS: int = Field(
        title="BatchedTransmissionPeriodS",
    )
    DataChannelList: List[DataChannelGt] = Field(
        title="DataChannel List",
        description=(
            "The list of data channels for which there is data getting reported in this batched "
            "reading. It is a subset of all the data channels for the SCADA - may not be all "
            "of them."
        ),
    )
    ChannelReadingList: List[ChannelReadings] = Field(
        title="ChannelReadingList",
    )
    FsmActionList: List[FsmAtomicReport] = Field(
        title="Finite State Machine Action List",
        description=(
            "FSM Actions (that is, side-effects of state machine transitions with real-world "
            "changes to the underlying TerminalAsset)."
            "[More info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)"
        ),
    )
    FsmReportList: List[FsmFullReport] = Field(
        title="Finite State Machine Report List",
        description=(
            "FSM Reports are the cacading events, actions and transitions caused by a single "
            "high-level event. There is duplication with the action list."
            "[More info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)"
        ),
    )
    Id: str = Field(
        title="Batched Reading Id",
        description="Globally Unique identifier for a BatchedReadings message",
    )
    TypeName: Literal["batched.readings"] = "batched.readings"
    Version: Literal["000"] = "000"

    class Config:
        extra = Extra.allow

    @validator("FromGNodeAlias")
    def _check_from_g_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(
                f"FromGNodeAlias failed LeftRightDot format validation: {e}"
            )
        return v

    @validator("FromGNodeInstanceId")
    def _check_from_g_node_instance_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"FromGNodeInstanceId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("AboutGNodeAlias")
    def _check_about_g_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(
                f"AboutGNodeAlias failed LeftRightDot format validation: {e}"
            )
        return v

    @validator("SlotStartUnixS")
    def _check_slot_start_unix_s(cls, v: int) -> int:
        try:
            check_is_reasonable_unix_time_s(v)
        except ValueError as e:
            raise ValueError(
                f"SlotStartUnixS failed ReasonableUnixTimeS format validation: {e}"
            )
        return v

    @validator("BatchedTransmissionPeriodS")
    def _check_batched_transmission_period_s(cls, v: int) -> int:
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"BatchedTransmissionPeriodS failed PositiveInteger format validation: {e}"
            )
        return v

    @validator("FsmActionList")
    def check_fsm_action_list(cls, v: List[FsmAtomicReport]) -> List[FsmAtomicReport]:
        """
        Axiom 1: Each of the fsm.atomic.reports in this list must be actions (i.e. IsAction = true).
        """
        ...
        # TODO: Implement Axiom(s)

    @validator("Id")
    def _check_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(f"Id failed UuidCanonicalTextual format validation: {e}")
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        batched.readings.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        batched.readings.000 type. Unlike the standard python dict method,
        it makes the following substantive changes:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.
        """
        d = {
            key: value
            for key, value in self.dict(
                include=self.__fields_set__ | {"TypeName", "Version"}
            ).items()
            if value is not None
        }
        # Recursively calling as_dict()
        data_channel_list = []
        for elt in self.DataChannelList:
            data_channel_list.append(elt.as_dict())
        d["DataChannelList"] = data_channel_list
        # Recursively calling as_dict()
        channel_reading_list = []
        for elt in self.ChannelReadingList:
            channel_reading_list.append(elt.as_dict())
        d["ChannelReadingList"] = channel_reading_list
        # Recursively calling as_dict()
        fsm_action_list = []
        for elt in self.FsmActionList:
            fsm_action_list.append(elt.as_dict())
        d["FsmActionList"] = fsm_action_list
        # Recursively calling as_dict()
        fsm_report_list = []
        for elt in self.FsmReportList:
            fsm_report_list.append(elt.as_dict())
        d["FsmReportList"] = fsm_report_list
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the batched.readings.000 representation.

        Instances in the class are python-native representations of batched.readings.000
        objects, while the actual batched.readings.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is BatchedReadings.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class BatchedReadings_Maker:
    type_name = "batched.readings"
    version = "000"

    @classmethod
    def tuple_to_type(cls, tuple: BatchedReadings) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> BatchedReadings:
        """
        Given a serialized JSON type object, returns the Python class object.
        """
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing <{t}> must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> BatchedReadings:
        """
        Deserialize a dictionary representation of a batched.readings.000 message object
        into a BatchedReadings python object for internal use.

        This is the near-inverse of the BatchedReadings.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a BatchedReadings object.

        Returns:
            BatchedReadings
        """
        d2 = dict(d)
        if "FromGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict missing FromGNodeAlias: <{d2}>")
        if "FromGNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict missing FromGNodeInstanceId: <{d2}>")
        if "AboutGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict missing AboutGNodeAlias: <{d2}>")
        if "SlotStartUnixS" not in d2.keys():
            raise SchemaError(f"dict missing SlotStartUnixS: <{d2}>")
        if "BatchedTransmissionPeriodS" not in d2.keys():
            raise SchemaError(f"dict missing BatchedTransmissionPeriodS: <{d2}>")
        if "DataChannelList" not in d2.keys():
            raise SchemaError(f"dict missing DataChannelList: <{d2}>")
        if not isinstance(d2["DataChannelList"], List):
            raise SchemaError(
                f"DataChannelList <{d2['DataChannelList']}> must be a List!"
            )
        data_channel_list = []
        for elt in d2["DataChannelList"]:
            if not isinstance(elt, dict):
                raise SchemaError(
                    f"DataChannelList <{d2['DataChannelList']}> must be a List of DataChannelGt types"
                )
            t = DataChannelGt_Maker.dict_to_tuple(elt)
            data_channel_list.append(t)
        d2["DataChannelList"] = data_channel_list
        if "ChannelReadingList" not in d2.keys():
            raise SchemaError(f"dict missing ChannelReadingList: <{d2}>")
        if not isinstance(d2["ChannelReadingList"], List):
            raise SchemaError(
                f"ChannelReadingList <{d2['ChannelReadingList']}> must be a List!"
            )
        channel_reading_list = []
        for elt in d2["ChannelReadingList"]:
            if not isinstance(elt, dict):
                raise SchemaError(
                    f"ChannelReadingList <{d2['ChannelReadingList']}> must be a List of ChannelReadings types"
                )
            t = ChannelReadings_Maker.dict_to_tuple(elt)
            channel_reading_list.append(t)
        d2["ChannelReadingList"] = channel_reading_list
        if "FsmActionList" not in d2.keys():
            raise SchemaError(f"dict missing FsmActionList: <{d2}>")
        if not isinstance(d2["FsmActionList"], List):
            raise SchemaError(f"FsmActionList <{d2['FsmActionList']}> must be a List!")
        fsm_action_list = []
        for elt in d2["FsmActionList"]:
            if not isinstance(elt, dict):
                raise SchemaError(
                    f"FsmActionList <{d2['FsmActionList']}> must be a List of FsmAtomicReport types"
                )
            t = FsmAtomicReport_Maker.dict_to_tuple(elt)
            fsm_action_list.append(t)
        d2["FsmActionList"] = fsm_action_list
        if "FsmReportList" not in d2.keys():
            raise SchemaError(f"dict missing FsmReportList: <{d2}>")
        if not isinstance(d2["FsmReportList"], List):
            raise SchemaError(f"FsmReportList <{d2['FsmReportList']}> must be a List!")
        fsm_report_list = []
        for elt in d2["FsmReportList"]:
            if not isinstance(elt, dict):
                raise SchemaError(
                    f"FsmReportList <{d2['FsmReportList']}> must be a List of FsmFullReport types"
                )
            t = FsmFullReport_Maker.dict_to_tuple(elt)
            fsm_report_list.append(t)
        d2["FsmReportList"] = fsm_report_list
        if "Id" not in d2.keys():
            raise SchemaError(f"dict missing Id: <{d2}>")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret batched.readings version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return BatchedReadings(**d2)


def check_is_left_right_dot(v: str) -> None:
    """Checks LeftRightDot Format

    LeftRightDot format: Lowercase alphanumeric words separated by periods, with
    the most significant word (on the left) starting with an alphabet character.

    Args:
        v (str): the candidate

    Raises:
        ValueError: if v is not LeftRightDot format
    """
    from typing import List

    try:
        x: List[str] = v.split(".")
    except:
        raise ValueError(f"Failed to seperate <{v}> into words with split'.'")
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(
            f"Most significant word of <{v}> must start with alphabet char."
        )
    for word in x:
        if not word.isalnum():
            raise ValueError(f"words of <{v}> split by by '.' must be alphanumeric.")
    if not v.islower():
        raise ValueError(f"All characters of <{v}> must be lowercase.")


def check_is_positive_integer(v: int) -> None:
    """
    Must be positive when interpreted as an integer. Interpretation as an
    integer follows the pydantic rules for this - which will round down
    rational numbers. So 1.7 will be interpreted as 1 and is also fine,
    while 0.5 is interpreted as 0 and will raise an exception.

    Args:
        v (int): the candidate

    Raises:
        ValueError: if v < 1
    """
    v2 = int(v)
    if v2 < 1:
        raise ValueError(f"<{v}> is not PositiveInteger")


def check_is_reasonable_unix_time_s(v: int) -> None:
    """Checks ReasonableUnixTimeS format

    ReasonableUnixTimeS format: unix seconds between Jan 1 2000 and Jan 1 3000

    Args:
        v (int): the candidate

    Raises:
        ValueError: if v is not ReasonableUnixTimeS format
    """
    import pendulum

    if pendulum.parse("2000-01-01T00:00:00Z").int_timestamp > v:  # type: ignore[attr-defined]
        raise ValueError(f"<{v}> must be after Jan 1 2000")
    if pendulum.parse("3000-01-01T00:00:00Z").int_timestamp < v:  # type: ignore[attr-defined]
        raise ValueError(f"<{v}> must be before Jan 1 3000")


def check_is_uuid_canonical_textual(v: str) -> None:
    """Checks UuidCanonicalTextual format

    UuidCanonicalTextual format:  A string of hex words separated by hyphens
    of length 8-4-4-4-12.

    Args:
        v (str): the candidate

    Raises:
        ValueError: if v is not UuidCanonicalTextual format
    """
    try:
        x = v.split("-")
    except AttributeError as e:
        raise ValueError(f"Failed to split on -: {e}")
    if len(x) != 5:
        raise ValueError(f"<{v}> split by '-' did not have 5 words")
    for hex_word in x:
        try:
            int(hex_word, 16)
        except ValueError:
            raise ValueError(f"Words of <{v}> are not all hex")
    if len(x[0]) != 8:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[1]) != 4:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[2]) != 4:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[3]) != 4:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[4]) != 12:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
