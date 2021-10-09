# -*- encoding: utf-8 -*-
"""
 Created by Ênio Viana at 03/10/2021 at 01:59:42
 Project: py-dss-tools [out, 2021]
"""
from enum import Enum


class EarthModel(Enum):
    Carson = "Carson"
    FullCarson = "FullCarson"
    Deri = "Deri"


class Units(Enum):
    none = "none"
    mi = "mi"
    kft = "kft"
    km = "km"
    m = "m"
    ft = "ft"
    inc = "in"
    cm = "cm"


class LineType(Enum):
    OH = "OH"
    UG = "UG"
    UG_TS = "UG_TS"
    UG_CN = "UG_CN"
    SWT_LDBRK = "SWT_LDBRK"
    SWT_FUSE = "SWT_FUSE"
    SWT_SECT = "SWT_SECT"
    SWT_REC = "SWT_REC"
    SWT_DISC = "SWT_DISC"
    SWT_BRK = "SWT_BRK"
    SWT_ELBOW = "SWT_ELBOW"
