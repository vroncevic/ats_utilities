# -*- coding: UTF-8 -*-

'''
Module
    keys.py
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
    Defines the InfoBundleKeys class with attribute(s) and method(s).
    Provides constants for information keys required for setup and configuration.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import ClassVar
from types import MappingProxyType

from ats_utilities.info.name.iname import IName
from ats_utilities.info.version.iversion import IVersion
from ats_utilities.info.licence.ilicence import ILicence
from ats_utilities.info.build_date.ibuild_date import IBuildDate
from ats_utilities.info.repository.irepository import IRepository
from ats_utilities.info.organization.iorganization import IOrganization
from ats_utilities.info.use_github.iuse_github import IUseGitHub
from ats_utilities.info.logo.ilogo import ILogo
from ats_utilities.info.log_file.ilog_file import ILogFile
from ats_utilities.info.info_ok.iinfo_ok import IInfoOk
from ats_utilities.context.bundle import ContextBundle

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class InfoBundleKeys:
    '''
        Defines the InfoBundleKeys class with attribute(s) and method(s).
        Provides constants for information keys required for setup and configuration.

        Here we have three groups of keys:
            | - dependency keys
            | - option keys
            | - information (configuration) keys

        The main difference is in their usage:
            | - dependency keys are used to define dependencies of the class
            | - option keys are used to define options of the class
            | - information (configuration) keys are used to define behavior of:
            |   - Info class instance
            |   - SplashManager class instance
            |   - Logging class instance
            |   - Option class instance

        It defines:

            :attributes:
                | DEPENDENCY_NAME - The key for name for the info bundle.
                | DEPENDENCY_VERSION - The key for version for the info bundle.
                | DEPENDENCY_BUILD_DATE - The key for build date for the info bundle.
                | DEPENDENCY_LICENCE - The key for licence for the info bundle.
                | DEPENDENCY_REPOSITORY - The key for repository for the info bundle.
                | DEPENDENCY_ORGANIZATION - The key for organization for the info bundle.
                | DEPENDENCY_USE_GITHUB_INFRASTRUCTURE - The key for use github infrastructure for the info bundle.
                | DEPENDENCY_LOGO_PATH - The key for logo path for the info bundle.
                | DEPENDENCY_LOG_FILE - The key for log file path for the info bundle.
                | DEPENDENCY_INFO_OK - The key for info ok for the info bundle.
                | DEPENDENCY_CONTEXT_BUNDLE - The key for context bundle for the info bundle.
                | OPTION_INFO - The key for info for the info bundle.
                | OPTION_CONTEXT_BUNDLE - The key for context bundle for the info bundle.
                | ATS_NAME - The key for name for the info bundle.
                | ATS_VERSION - The key for version for the info bundle.
                | ATS_BUILD_DATE - The key for build date for the info bundle.
                | ATS_LICENCE - The key for licence for the info bundle.
                | ATS_REPOSITORY - The key for repository for the info bundle.
                | ATS_ORGANIZATION - The key for organization for the info bundle.
                | ATS_USE_GITHUB_INFRASTRUCTURE - The key for use github infrastructure for the info bundle.
                | ATS_LOGO_PATH - The key for logo path for the info bundle.
                | ATS_LOG_FILE - The key for log file path for the info bundle.
                | ATS_INFO_OK - The key for info ok for the info bundle.
            :methods:
                | get_dependency_to_type - Returns the mapping of the info bundle dependencies to their types.
                | get_option_to_type - Returns the mapping of the info bundle options to their types.
    '''

    # Dependency Keys
    DEPENDENCY_NAME: ClassVar[str] = 'name'
    DEPENDENCY_VERSION: ClassVar[str] = 'version'
    DEPENDENCY_BUILD_DATE: ClassVar[str] = 'build_date'
    DEPENDENCY_LICENCE: ClassVar[str] = 'licence'
    DEPENDENCY_REPOSITORY: ClassVar[str] = 'repository'
    DEPENDENCY_ORGANIZATION: ClassVar[str] = 'organization'
    DEPENDENCY_USE_GITHUB_INFRASTRUCTURE: ClassVar[str] = 'use_github'
    DEPENDENCY_LOGO_PATH: ClassVar[str] = 'logo'
    DEPENDENCY_LOG_FILE: ClassVar[str] = 'log_file'
    DEPENDENCY_INFO_OK: ClassVar[str] = 'info_ok'
    DEPENDENCY_CONTEXT_BUNDLE: ClassVar[str] = 'context_bundle'

    # Option Keys
    OPTION_INFO: ClassVar[str] = 'info'
    OPTION_CONTEXT_BUNDLE: ClassVar[str] = 'context_bundle'

    # Information Keys
    ATS_NAME: ClassVar[str] = 'ats_name'
    ATS_VERSION: ClassVar[str] = 'ats_version'
    ATS_BUILD_DATE: ClassVar[str] = 'ats_build_date'
    ATS_LICENCE: ClassVar[str] = 'ats_licence'
    ATS_REPOSITORY: ClassVar[str] = 'ats_repository'
    ATS_ORGANIZATION: ClassVar[str] = 'ats_organization'
    ATS_USE_GITHUB_INFRASTRUCTURE: ClassVar[str] = 'ats_use_github_infrastructure'
    ATS_LOGO_PATH: ClassVar[str] = 'ats_logo_path'
    ATS_LOG_FILE: ClassVar[str] = 'ats_log_file'
    ATS_INFO_OK: ClassVar[str] = 'ats_info_ok'

    @classmethod
    def get_dependency_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns the mapping of the info bundle dependencies to their types.

            :return: The mapping of the info bundle dependencies to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.DEPENDENCY_NAME: IName,
            cls.DEPENDENCY_VERSION: IVersion,
            cls.DEPENDENCY_BUILD_DATE: IBuildDate,
            cls.DEPENDENCY_LICENCE: ILicence,
            cls.DEPENDENCY_REPOSITORY: IRepository,
            cls.DEPENDENCY_ORGANIZATION: IOrganization,
            cls.DEPENDENCY_USE_GITHUB_INFRASTRUCTURE: IUseGitHub,
            cls.DEPENDENCY_LOGO_PATH: ILogo,
            cls.DEPENDENCY_LOG_FILE: ILogFile,
            cls.DEPENDENCY_INFO_OK: IInfoOk,
            cls.DEPENDENCY_CONTEXT_BUNDLE: ContextBundle,
        })

    @classmethod
    def get_option_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns the mapping of the info bundle options to their types.

            :return: The mapping of the info bundle options to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.OPTION_INFO: Mapping[str, object],
            cls.OPTION_CONTEXT_BUNDLE: ContextBundle,
        })
