# -*- coding: UTF-8 -*-

'''
Module
    info_keys.py
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
    Defines class InfoKeys with attribute(s).
    Defines constants for ATS information keys.
'''

from dataclasses import dataclass
from typing import ClassVar, List

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass(frozen=True)
class InfoKeys:
    '''
        Defines class InfoKeys with attribute(s).
        Defines constants for ATS information keys.

        It defines:

            :attributes:
                | ATS_NAME - The key for ATS name.
                | ATS_VERSION - The key for ATS version.
                | ATS_BUILD_DATE - The key for ATS build date.
                | ATS_LICENCE - The key for ATS licence.
                | ATS_REPOSITORY - The key for ATS repository.
                | ATS_ORGANIZATION - The key for ATS organization.
                | ATS_USE_GITHUB_INFRASTRUCTURE - The key for ATS use github infrastructure.
                | ATS_LOGO_PATH - The key for ATS logo path.
            :methods: None
    '''

    ATS_NAME: ClassVar[str] = 'ats_name'
    ATS_VERSION: ClassVar[str] = 'ats_version'
    ATS_BUILD_DATE: ClassVar[str] = 'ats_build_date'
    ATS_LICENCE: ClassVar[str] = 'ats_licence'
    ATS_REPOSITORY: ClassVar[str] = 'ats_repository'
    ATS_ORGANIZATION: ClassVar[str] = 'ats_organization'
    ATS_USE_GITHUB_INFRASTRUCTURE: ClassVar[str] = 'ats_use_github_infrastructure'
    ATS_LOGO_PATH: ClassVar[str] = 'ats_logo_path'
