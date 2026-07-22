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

from ats_utilities.context.factory import ContextFactory
from ats_utilities.info.setup.factory import InfoFactory
from ats_utilities.info.engine import InfoManager

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

VERBOSE: bool = False

#
# default [without DI]
# ====================
#
context_bundle = ContextFactory.create_default_bundle()
default_bundle = InfoFactory.create_info_bundle_from_dict({}, context_bundle)
ats_info_manager_without_di = InfoManager(own=default_bundle)
print(ats_info_manager_without_di)

#
# default [with DI and with case overwrite info (should get warning message)]
# ============================================================================
#
info_dict_overwrite = {
    'ats_name': 'mytool2',
    'ats_version': '1.0.1',
    'ats_licence': 'gplv3',
    'ats_build_date': 'Sun Jun 14 03:06:11 PM CEST 2026',
    'ats_info_ok': True
}
bundle_overwrite = InfoFactory.create_info_bundle_from_dict(info_dict_overwrite, context_bundle)
ats_info_manager_with_di_and_case_overwrite = InfoManager(
    own=bundle_overwrite, 
)
print(ats_info_manager_with_di_and_case_overwrite)

#
# default [with DI and without case overwrite info (without warning message)]
# ============================================================================
#
info_dict_no_overwrite = {
    'ats_name': 'mytool4',
    'ats_version': '1.0.3',
    'ats_licence': 'gplv3',
    'ats_build_date': 'Sun Jun 14 03:06:13 PM CEST 2026',
    'ats_info_ok': True
}
bundle_no_overwrite = InfoFactory.create_info_bundle_from_dict(info_dict_no_overwrite, context_bundle)
ats_info_manager_with_di_and_without_case_overwrite = InfoManager(
    own=bundle_no_overwrite, 
)
print(ats_info_manager_with_di_and_without_case_overwrite)
