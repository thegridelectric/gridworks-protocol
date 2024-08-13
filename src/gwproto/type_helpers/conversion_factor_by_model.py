from typing import Dict

from gwproto.enums import MakeModel

CONVERSION_FACTOR_BY_MODEL: Dict[MakeModel, float] = {
    MakeModel.ISTEC_4440: 0.268132,
    MakeModel.OMEGA__FTB8007HWPT: 0.134066,
    MakeModel.OMEGA__FTB8010HWPT: 1.34066,
    MakeModel.PRMFILTRATION__WM075: 1.34066,
    MakeModel.EKM__HOTSPWM075HD: 0.08322,
}
