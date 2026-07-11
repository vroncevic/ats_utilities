# -*- coding: utf-8 -*-

'''
Module
    story_ats_splasher.py
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
    Use cases for ATS splasher.
'''

from typing import Any
from os.path import dirname, realpath
from ats_utilities.splasher.engine import Splasher
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.splasher.component_bundle import SplashComponentBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'

current_dir: str = dirname(realpath(__file__))
logo_path: str = f'{current_dir}/../../tests/assets/config/app.logo'
#
# default [with GitHub]
# ======================
#
mytool_property_github: dict[Any, Any] = {
    SplashKeys.ATS_ORGANIZATION: 'myorganization',
    SplashKeys.ATS_REPOSITORY: 'myrepository',
    SplashKeys.ATS_NAME: 'mytool',
    SplashKeys.ATS_LOGO_PATH: logo_path,
    SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE: True
}
bundle_github = SplashComponentBundle(prop=mytool_property_github)
ats_splash_with_github: Splasher = Splasher(bundle_github)
print(ats_splash_with_github)
print(100 * '=')

#
# default [without GitHub]
# =========================
#
mytool_property_no_github: dict[Any, Any] = {
    SplashKeys.ATS_ORGANIZATION: 'myorganization',
    SplashKeys.ATS_REPOSITORY: 'myrepository',
    SplashKeys.ATS_NAME: 'mytool',
    SplashKeys.ATS_LOGO_PATH: logo_path,
    SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE: False
}
bundle_no_github = SplashComponentBundle(prop=mytool_property_no_github)
ats_splash_without_github = Splasher(bundle_no_github)
print(ats_splash_without_github)
print(100 * '=')

#
# default [disabled]
# ==================
#
mytool_property_disabled: dict[Any, Any] = {
    'enabled': False
}
bundle_disabled = SplashComponentBundle(prop=mytool_property_disabled)
ats_splash_disabled = Splasher(bundle_disabled)
print(ats_splash_disabled)
print(100 * '=')
