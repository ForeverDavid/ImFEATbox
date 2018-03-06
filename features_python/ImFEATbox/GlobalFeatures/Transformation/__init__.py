# -*- coding: utf-8 -*-

import ImFEATbox.FeatureGroup as __fg
from ImFEATbox.__Features__ import __Feature

# we use the __ to hide objects from the python IDE,
# you will only see the needed objects

from _DCTF import DCTF as __DCTF


# Moment features
dct = __Feature('discrete cosine transform', __DCTF, [__fg.global_, __fg.moments])