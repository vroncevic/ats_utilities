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

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

current_dir: str = dirname(realpath(__file__))
logo_path: str = f'{current_dir}/../../tests/config/app.logo'
mytool_property: dict[Any, Any] = {}
bundle: SplashComponentBundle = SplashComponentBundle(prop=mytool_property)

#
# default [with GitHub]
# ======================
#
bundle.prop[SplashKeys.ATS_ORGANIZATION] = 'myorganization'
bundle.prop[SplashKeys.ATS_REPOSITORY] = 'myrepository'
bundle.prop[SplashKeys.ATS_NAME] = 'mytool'
bundle.prop[SplashKeys.ATS_LOGO_PATH] = logo_path
bundle.prop[SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE] = True

ats_splash_with_github: Splasher = Splasher(bundle)
print(ats_splash_with_github)
print(50 * '=')

#
# default [without GitHub]
# =========================
#
bundle.prop[SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE] = False

ats_splash_without_github = Splasher(bundle)
print(ats_splash_without_github)
print(50 * '=')
