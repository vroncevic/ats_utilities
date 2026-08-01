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

from os.path import dirname, realpath
from ats_utilities.splash.engine import SplashManager
from ats_utilities.splash.setup.keys import SplashKeys
from ats_utilities.info.setup.keys import InfoKeys
from ats_utilities.splash.setup.factory import SplashFactory
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextFactory

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'

current_dir: str = dirname(realpath(__file__))
logo_path: str = f'{current_dir}/../../tests/assets/config/read_only/app.logo'
context_bundle: ContextBundle = ContextFactory.create_bundle()

#
# default [with GitHub]
# ======================
#
mytool_property_github: dict[object, object] = {
    InfoKeys.ATS_ORGANIZATION: 'myorganization',
    InfoKeys.ATS_REPOSITORY: 'myrepository',
    InfoKeys.ATS_NAME: 'mytool',
    InfoKeys.ATS_LOGO_PATH: logo_path,
    InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE: True
}
ats_splash_with_github: SplashManager = SplashManager(
    own=SplashFactory.create_bundle(
        {
            SplashKeys.OPTION_PROP: mytool_property_github,
            SplashKeys.OPTION_CONTEXT_BUNDLE: context_bundle
        }
    )
)
print(ats_splash_with_github)
print(100 * '=')

#
# default [without GitHub]
# =========================
#
mytool_property_no_github: dict[object, object] = {
    InfoKeys.ATS_ORGANIZATION: 'myorganization',
    InfoKeys.ATS_REPOSITORY: 'myrepository',
    InfoKeys.ATS_NAME: 'mytool',
    InfoKeys.ATS_LOGO_PATH: logo_path,
    InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE: False
}
ats_splash_without_github = SplashManager(
    own=SplashFactory.create_bundle(
        {
            SplashKeys.OPTION_PROP: mytool_property_no_github,
            SplashKeys.OPTION_CONTEXT_BUNDLE: context_bundle
        }
    )
)
print(ats_splash_without_github)
print(100 * '=')

#
# default [disabled]
# ==================
#
mytool_property_disabled: dict[object, object] = {}
ats_splash_disabled: SplashManager = SplashManager(
    own=SplashFactory.create_bundle(
        {
            SplashKeys.OPTION_PROP: mytool_property_disabled,
            SplashKeys.OPTION_CONTEXT_BUNDLE: context_bundle
        }
    )
)
print(ats_splash_disabled)
print(100 * '=')
