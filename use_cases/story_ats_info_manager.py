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

from typing import List, Dict, Any
from ats_utilities.info.version import ATSVersion
from ats_utilities.info.name import ATSName
from ats_utilities.info.licence import ATSLicence
from ats_utilities.info.build_date import ATSBuildDate
from ats_utilities.info.info_ok import ATSInfoOk
from ats_utilities.info.ats_info_manager import ATSInfoManager

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

VERBOSE: bool = False

#
# default [without DI]
# ====================
#
ats_info: Dict[Any, Any] = {
    'ats_name': 'mytool1',
    'ats_version': '1.0.0',
    'ats_licence': 'gplv3',
    'ats_build_date': 'Sun Jun 14 03:06:10 PM CEST 2026'
}
ats_info_manager_without_di = ATSInfoManager(info=ats_info, verbose=VERBOSE)
print(ats_info_manager_without_di)

#
# default [with DI and with case overwrite info (should get warning message)]
# ============================================================================
#
ats_name = ATSName(verbose=VERBOSE)
ats_name.name = 'mytool2'
ats_version = ATSVersion(verbose=VERBOSE)
ats_version.version = '1.0.1'
ats_licence = ATSLicence(verbose=VERBOSE)
ats_licence.licence = 'gplv3'
ats_build_date = ATSBuildDate(verbose=VERBOSE)
ats_build_date.build_date = 'Sun Jun 14 03:06:11 PM CEST 2026'
ats_info_ok = ATSInfoOk(verbose=VERBOSE)
ats_info_ok.info_ok = True

ats_info_overwrite: Dict[Any, Any] = {
    'ats_name': 'mytool3',
    'ats_version': '1.0.2',
    'ats_licence': 'gplv3',
    'ats_build_date': 'Sun Jun 14 03:06:12 PM CEST 2026'
}

ats_info_manager_with_di_and_case_overwrite = ATSInfoManager(
    info=ats_info_overwrite,
    name=ats_name,
    version=ats_version,
    licence=ats_licence,
    build_date=ats_build_date,
    info_ok=ats_info_ok,
    verbose=VERBOSE
)
print(ats_info_manager_with_di_and_case_overwrite)

#
# default [with DI and without case overwrite info (without warning message)]
# ============================================================================
#
ats_name = ATSName(verbose=VERBOSE)
ats_name.name = 'mytool4'
ats_version = ATSVersion(verbose=VERBOSE)
ats_version.version = '1.0.3'
ats_licence = ATSLicence(verbose=VERBOSE)
ats_licence.licence = 'gplv3'
ats_build_date = ATSBuildDate(verbose=VERBOSE)
ats_build_date.build_date = 'Sun Jun 14 03:06:13 PM CEST 2026'
ats_info_ok = ATSInfoOk(verbose=VERBOSE)
ats_info_ok.info_ok = True

ats_info_manager_with_di_and_without_case_overwrite = ATSInfoManager(
    name=ats_name,
    version=ats_version,
    licence=ats_licence,
    build_date=ats_build_date,
    info_ok=ats_info_ok,
    verbose=VERBOSE
)
print(ats_info_manager_with_di_and_without_case_overwrite)
