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

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar
from types import MappingProxyType

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


@dataclass(frozen=True, slots=True, kw_only=True)
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
    '''

    ATS_NAME: ClassVar[str] = 'ats_name'
    ATS_VERSION: ClassVar[str] = 'ats_version'
    ATS_BUILD_DATE: ClassVar[str] = 'ats_build_date'
    ATS_LICENCE: ClassVar[str] = 'ats_licence'
    ATS_REPOSITORY: ClassVar[str] = 'ats_repository'
    ATS_ORGANIZATION: ClassVar[str] = 'ats_organization'
    ATS_USE_GITHUB_INFRASTRUCTURE: ClassVar[str] = 'ats_use_github_infrastructure'
    ATS_LOGO_PATH: ClassVar[str] = 'ats_logo_path'

    @classmethod
    def get_keys(cls) -> tuple[str, ...]:
        '''
            Returns a tuple of all ATS information keys.

            :return: Tuple of all keys.
            :rtype: <tuple[str, ...]>
            :exceptions: None.
        '''
        return (
            cls.ATS_NAME,
            cls.ATS_VERSION,
            cls.ATS_BUILD_DATE,
            cls.ATS_LICENCE,
            cls.ATS_REPOSITORY,
            cls.ATS_ORGANIZATION,
            cls.ATS_USE_GITHUB_INFRASTRUCTURE,
            cls.ATS_LOGO_PATH
        )

    @classmethod
    def get_key_to_attr(cls) -> MappingProxyType[str, str]:
        '''
            Returns a mapping of ATS information keys to attributes.

            :return: Key to attribute mapping.
            :rtype: <MappingProxyType[str, str]>
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.ATS_NAME: 'name',
            cls.ATS_VERSION: 'version',
            cls.ATS_BUILD_DATE: 'build_date',
            cls.ATS_LICENCE: 'licence',
            cls.ATS_REPOSITORY: 'repository',
            cls.ATS_ORGANIZATION: 'organization',
            cls.ATS_USE_GITHUB_INFRASTRUCTURE: 'use_github',
            cls.ATS_LOGO_PATH: 'logo'
        })
