# -*- coding: utf-8 -*-

'''
Module
    story_ats_info_manager.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    ats_utilities is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    ats_utilities is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Use cases for ATS info manager.
'''

from typing import Any
from ats_utilities.info.version import Version
from ats_utilities.info.name import Name
from ats_utilities.info.licence import Licence
from ats_utilities.info.build_date import BuildDate
from ats_utilities.info.info_ok import InfoOk
from ats_utilities.info.engine import InfoManager, InfoComponentBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

VERBOSE: bool = False

#
# default [without DI]
# ====================
#
ats_info_manager_without_di = InfoManager()
print(ats_info_manager_without_di)

#
# default [with DI and with case overwrite info (should get warning message)]
# ============================================================================
#
ats_name = Name()
ats_name.name = 'mytool2'
ats_version = Version()
ats_version.version = '1.0.1'
ats_licence = Licence()
ats_licence.licence = 'gplv3'
ats_build_date = BuildDate()
ats_build_date.build_date = 'Sun Jun 14 03:06:11 PM CEST 2026'
ats_info_ok = InfoOk()
ats_info_ok.info_ok = True

bundle: InfoComponentBundle = InfoComponentBundle(
    name=ats_name,
    version=ats_version,
    licence=ats_licence,
    build_date=ats_build_date,
    info_ok=ats_info_ok
)

ats_info_manager_with_di_and_case_overwrite = InfoManager(
    component_bundle=bundle, 
)
print(ats_info_manager_with_di_and_case_overwrite)

#
# default [with DI and without case overwrite info (without warning message)]
# ============================================================================
#
ats_name = Name()
ats_name.name = 'mytool4'
ats_version = Version()
ats_version.version = '1.0.3'
ats_licence = Licence()
ats_licence.licence = 'gplv3'
ats_build_date = BuildDate()
ats_build_date.build_date = 'Sun Jun 14 03:06:13 PM CEST 2026'
ats_info_ok = InfoOk()
ats_info_ok.info_ok = True

bundle: InfoComponentBundle = InfoComponentBundle(
    name=ats_name,
    version=ats_version,
    licence=ats_licence,
    build_date=ats_build_date,
    info_ok=ats_info_ok
)

ats_info_manager_with_di_and_without_case_overwrite = InfoManager(
    component_bundle=bundle, 
)
print(ats_info_manager_with_di_and_without_case_overwrite)
