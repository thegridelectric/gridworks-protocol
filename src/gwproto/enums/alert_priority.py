from enum import auto
from typing import Optional

from gw.enums import GwStrEnum


class AlertPriority(GwStrEnum):
    """
    The GridWorks in-house enum for prioritizing alerts in a context where distributed equipment
    maintenance affects people's comfort and well-being.

    Enum alert.priority version 000 in the GridWorks Type registry.

    Used by multiple Application Shared Languages (ASLs). For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#alertpriority)

    Values:
      - P1Critical: Critical alerts represent situations where immediate action is required
        to prevent significant impact or harm. These alerts should be addressed immediately,
        as they have the potential to cause significant disruption or endangerment to people's
        comfort and well-being.
      - P2High: High-priority alerts represent situations that require urgent attention
        to prevent significant impact or harm. While not as critical as P1 alerts, P2 alerts
        still require prompt action to address the issue and prevent further escalation.
      - P3Medium: Medium-priority alerts represent situations that require attention to
        prevent potential impact or harm. These alerts should be addressed in a timely manner
        to prevent any negative impact on people's comfort and well-being.
      - P4Low: Low-priority alerts represent situations that require attention but are
        not urgent. While not as critical as P1, P2, or P3 alerts, P4 alerts should still be
        addressed in a reasonable timeframe to prevent any negative impact on people's comfort
        and well-being.
      - P5Info: Informational alerts provide general information and do not require immediate
        action. These alerts may include notifications, status updates, or routine maintenance
        reminders.
    """

    P1Critical = auto()
    P2High = auto()
    P3Medium = auto()
    P4Low = auto()
    P5Info = auto()

    @classmethod
    def default(cls) -> "AlertPriority":
        """
        Returns default value (in this case P3Medium)
        """
        return cls.P3Medium

    @classmethod
    def version(cls, value: Optional[str] = None) -> str:
        if value is None:
            return "000"
        if not isinstance(value, str):
            raise TypeError("This method applies to strings, not enums")
        if value not in value_to_version:
            raise ValueError(f"Unknown enum value: {value}")
        return value_to_version[value]

    @classmethod
    def enum_name(cls) -> str:
        """
        The name in the GridWorks Type Registry (alert.priority)
        """
        return "alert.priority"

    @classmethod
    def enum_version(cls) -> str:
        """
        The version in the GridWorks Type Registry (000)
        """
        return "000"


value_to_version = {
    "P1Critical": "000",
    "P2High": "000",
    "P3Medium": "000",
    "P4Low": "000",
    "P5Info": "000",
}
