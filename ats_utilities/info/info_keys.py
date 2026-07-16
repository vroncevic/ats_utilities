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
    Defines constants for information keys.
'''

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar
from types import MappingProxyType

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(frozen=True, slots=True, kw_only=True)
class InfoKeys:
    '''
        Defines class InfoKeys with attribute(s).
        Defines constants for information keys.
        The information keys are used for information container.
        The information container store data for App/Tool/Script.

        It defines:

            :attributes:
                | ATS_NAME - The key for name.
                | ATS_VERSION - The key for version.
                | ATS_BUILD_DATE - The key for build date.
                | ATS_LICENCE - The key for licence.
                | ATS_REPOSITORY - The key for repository.
                | ATS_ORGANIZATION - The key for organization.
                | ATS_USE_GITHUB_INFRASTRUCTURE - The key for use github infrastructure.
                | ATS_LOGO_PATH - The key for logo path.
                | ATS_LOG_FILE - The key for log file path (Optional).
    '''

    ATS_NAME: ClassVar[str] = r'ats_name'
    ATS_VERSION: ClassVar[str] = r'ats_version'
    ATS_BUILD_DATE: ClassVar[str] = r'ats_build_date'
    ATS_LICENCE: ClassVar[str] = r'ats_licence'
    ATS_REPOSITORY: ClassVar[str] = r'ats_repository'
    ATS_ORGANIZATION: ClassVar[str] = r'ats_organization'
    ATS_USE_GITHUB_INFRASTRUCTURE: ClassVar[str] = r'ats_use_github_infrastructure'
    ATS_LOGO_PATH: ClassVar[str] = r'ats_logo_path'
    ATS_LOG_FILE: ClassVar[str] = r'ats_log_file'
    ATS_INFO_OK: ClassVar[str] = r'ats_info_ok'

    @classmethod
    def get_keys(cls) -> tuple[str, ...]:
        '''
            Returns a tuple of all information keys.

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
            cls.ATS_LOGO_PATH,
            cls.ATS_LOG_FILE,
            cls.ATS_INFO_OK
        )

    @classmethod
    def get_key_to_attr(cls) -> MappingProxyType[str, str]:
        '''
            Returns a mapping of information keys to attributes.

            :return: Key to attribute mapping.
            :rtype: <MappingProxyType[str, str]>
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.ATS_NAME: r'name',
            cls.ATS_VERSION: r'version',
            cls.ATS_BUILD_DATE: r'build_date',
            cls.ATS_LICENCE: r'licence',
            cls.ATS_REPOSITORY: r'repository',
            cls.ATS_ORGANIZATION: r'organization',
            cls.ATS_USE_GITHUB_INFRASTRUCTURE: r'use_github',
            cls.ATS_LOGO_PATH: r'logo',
            cls.ATS_LOG_FILE: r'log_file',
            cls.ATS_INFO_OK: r'info_ok'
        })
