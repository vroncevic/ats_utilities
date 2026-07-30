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
    Defines class InfoKeys with attribute(s) and method(s).
    Provides constants for information keys required for setup and configuration.
'''

from __future__ import annotations

from collections.abc import Sequence, Mapping
from typing import ClassVar
from types import MappingProxyType

from ats_utilities.info.name.iname import IName
from ats_utilities.info.name.engine import Name
from ats_utilities.info.version.iversion import IVersion
from ats_utilities.info.version.engine import Version
from ats_utilities.info.licence.ilicence import ILicence
from ats_utilities.info.licence.engine import Licence
from ats_utilities.info.build_date.ibuild_date import IBuildDate
from ats_utilities.info.build_date.engine import BuildDate
from ats_utilities.info.repository.irepository import IRepository
from ats_utilities.info.repository.engine import Repository
from ats_utilities.info.organization.iorganization import IOrganization
from ats_utilities.info.organization.engine import Organization
from ats_utilities.info.use_github.iuse_github import IUseGitHub
from ats_utilities.info.use_github.engine import UseGitHub
from ats_utilities.info.logo.ilogo import ILogo
from ats_utilities.info.logo.engine import Logo
from ats_utilities.info.log_file.ilog_file import ILogFile
from ats_utilities.info.log_file.engine import LogFile
from ats_utilities.info.info_ok.iinfo_ok import IInfoOk
from ats_utilities.info.info_ok.engine import InfoOk
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.validation.check_value import not_satisfied, not_none
from ats_utilities.utils.dicts import is_present_required_key

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class InfoKeys:
    '''
        Defines class InfoKeys with attribute(s) and method(s).
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
                | DEPENDENCY_NAME - The key for name.
                | DEPENDENCY_VERSION - The key for version.
                | DEPENDENCY_BUILD_DATE - The key for build date.
                | DEPENDENCY_LICENCE - The key for licence.
                | DEPENDENCY_REPOSITORY - The key for repository.
                | DEPENDENCY_ORGANIZATION - The key for organization.
                | DEPENDENCY_USE_GITHUB_INFRASTRUCTURE - The key for use github infrastructure.
                | DEPENDENCY_LOGO_PATH - The key for logo path.
                | DEPENDENCY_LOG_FILE - The key for log file path.
                | DEPENDENCY_INFO_OK - The key for info ok.
                | DEPENDENCY_CONTEXT_BUNDLE - The key for context bundle.
                | OPTION_INFO - The key for info.
                | OPTION_CONTEXT_BUNDLE - The key for context bundle.
                | ATS_NAME - The key for name.
                | ATS_VERSION - The key for version.
                | ATS_BUILD_DATE - The key for build date.
                | ATS_LICENCE - The key for licence.
                | ATS_REPOSITORY - The key for repository.
                | ATS_ORGANIZATION - The key for organization.
                | ATS_USE_GITHUB_INFRASTRUCTURE - The key for use github infrastructure.
                | ATS_LOGO_PATH - The key for logo path.
                | ATS_LOG_FILE - The key for log file path.
                | ATS_INFO_OK - The key for info ok.
            :methods:
                | get_dependency_to_type - Returns mapping of info dependencies to their types.
                | get_option_to_type - Returns mapping of info options to their types.
                | get_config_keys - Returns a sequence of all information config keys.
                | is_registered_config_key - Checks if key name is a registered config key.
                | get_config_keys - Returns mapping of all config keys to their dependency keys.
                | get_optional_config_keys - Returns a sequence of all optional keys.
                | is_optional_config_key - Checks if key name is an optional key.
                | get_required_config_keys - Returns a sequence of all required keys.
                | is_required_config_key - Checks if key name is a required key.
                | get_name_of_config_key - Returns the dependency key for the given config key.
                | get_config_key_to_type - Returns mapping of all config keys to their types.
                | get_name - Returns the name of the application from config.
                | get_version - Returns the version of the application from config.
                | get_build_date - Returns the build date of the application from config.
                | get_licence - Returns the licence of the application from config.
                | get_repository - Returns the repository of the application from config.
                | get_organization - Returns the organization of the application from config.
                | get_use_github_infrastructure - Returns the use github infrastructure of the application from config.
                | get_logo_path - Returns the logo path of the application from config.
                | get_log_file - Returns the log file of the application from config.
                | get_info_ok - Returns the info ok of the application from config.
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
            Returns mapping of info dependencies to their types.

            :return: Mapping of info dependencies to their types.
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
            Returns mapping of info options to their types.

            :return: Mapping of info options to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.OPTION_INFO: Mapping[str, object],
            cls.OPTION_CONTEXT_BUNDLE: ContextBundle,
        })

    @classmethod
    def get_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all information keys.

            :return: Sequence of all keys.
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
    def is_registered_config_key(cls, name: str) -> bool:
        '''
            Checks if key name is a registered config key.

            :param name: Name of the key to check.
            :return: True if key name is a registered config key, otherwise False.
            :exceptions: None.
        '''
        return name in cls.get_config_keys()

    @classmethod
    def get_config_keys_to_dependency_keys(cls) -> MappingProxyType[str, str]:
        '''
            Returns a mapping of all config keys to their dependency keys.

            :return: Mapping of all config keys to their dependency keys.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.ATS_NAME: cls.DEPENDENCY_NAME,
            cls.ATS_VERSION: cls.DEPENDENCY_VERSION,
            cls.ATS_BUILD_DATE: cls.DEPENDENCY_BUILD_DATE,
            cls.ATS_LICENCE: cls.DEPENDENCY_LICENCE,
            cls.ATS_REPOSITORY: cls.DEPENDENCY_REPOSITORY,
            cls.ATS_ORGANIZATION: cls.DEPENDENCY_ORGANIZATION,
            cls.ATS_USE_GITHUB_INFRASTRUCTURE: cls.DEPENDENCY_USE_GITHUB_INFRASTRUCTURE,
            cls.ATS_LOGO_PATH: cls.DEPENDENCY_LOGO_PATH,
            cls.ATS_LOG_FILE: cls.DEPENDENCY_LOG_FILE,
            cls.ATS_INFO_OK: cls.DEPENDENCY_INFO_OK,
        })

    @classmethod
    def get_optional_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all optional keys.

            :return: Sequence of all optional keys.
            :exceptions: None.
        '''
        return (
            cls.ATS_REPOSITORY,
            cls.ATS_ORGANIZATION,
            cls.ATS_USE_GITHUB_INFRASTRUCTURE,
            cls.ATS_LOGO_PATH,
            cls.ATS_LOG_FILE,
        )

    @classmethod
    def is_optional_config_key(cls, key: str) -> bool:
        '''
            Checks if key name is an optional key.

            :param name: Name of the key to check.
            :return: True if key name is an optional key, otherwise False.
            :exceptions: None.
        '''
        return key in cls.get_optional_config_keys()

    @classmethod
    def is_required_config_key(cls, key: str) -> bool:
        '''
            Checks if key name is a required key.

            :param name: Name of the key to check.
            :return: True if key name is a required key, otherwise False.
            :exceptions: None.
        '''
        return key in cls.get_config_keys() and not cls.is_optional_config_key(key)

    @classmethod
    def get_required_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all required keys.

            :return: Sequence of all required keys.
            :exceptions: None.
        '''
        return tuple(key for key in cls.get_config_keys() if cls.is_required_config_key(key))

    @classmethod
    def get_name_of_config_key(cls, config_key: str) -> str:
        '''
            Returns the dependency key for the given config key.

            :param config_key: The config key.
            :return: The dependency key.
            :exceptions:
                | ATSValueError: Config key is not registered.
                | ATSValueError: Instance key for config key is not defined.
        '''
        ctx: str = 'info_keys::get_name_of_config_key(...)'
        is_registered: bool = cls.is_registered_config_key(config_key)
        not_satisfied(not is_registered, ctx, f'{config_key} is not registered as a config key')
        config_key_to_name: Mapping[str, str] = cls.get_config_keys_to_dependency_keys()
        name: str | None = config_key_to_name.get(config_key)
        not_none(name, ctx, f'instance key for {config_key} is not defined')

        return name

    @classmethod
    def get_names_of_optional_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all optional config keys names.

            :return: Sequence of all optional config keys names.
            :exceptions: None.
        '''
        return tuple(cls.get_name_of_config_key(key) for key in cls.get_optional_config_keys())

    @classmethod
    def get_names_of_required_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all required config keys names.

            :return: Sequence of all required config keys names.
            :exceptions: None.
        '''
        return tuple(cls.get_name_of_config_key(key) for key in cls.get_required_config_keys())

    @classmethod
    def get_all_names_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all config keys names.

            :return: Sequence of all config keys names.
            :exceptions: None.
        '''
        return tuple(cls.get_name_of_config_key(key) for key in cls.get_config_keys())

    @classmethod
    def get_config_key_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns a mapping of all config keys to their types.

            :return: Mapping of all config keys to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.ATS_NAME: Name,
            cls.ATS_VERSION: Version,
            cls.ATS_BUILD_DATE: BuildDate,
            cls.ATS_LICENCE: Licence,
            cls.ATS_REPOSITORY: Repository,
            cls.ATS_ORGANIZATION: Organization,
            cls.ATS_USE_GITHUB_INFRASTRUCTURE: UseGitHub,
            cls.ATS_LOGO_PATH: Logo,
            cls.ATS_LOG_FILE: LogFile,
            cls.ATS_INFO_OK: InfoOk
        })

    @classmethod
    def get_name(cls, config: Mapping[str, str]) -> str:
        '''
            Returns the name of the application from config.

            :param config: Configuration mapping.
            :return: Name of the application if defined, otherwise None.
            :exceptions:
                | ATSValueError: Key ATS_NAME is not present in config.
        '''
        ctx: str = 'info_keys::get_name(...)'
        msg: str = f'{cls.ATS_NAME} is not present in config'
        is_present_required_key(config, cls.ATS_NAME, ctx, msg)

        return config.get(cls.ATS_NAME)

    @classmethod
    def get_version(cls, config: Mapping[str, str]) -> str:
        '''
            Returns the version of the application from config.

            :param config: Configuration mapping.
            :return: Version of the application if defined, otherwise None.
            :exceptions:
                | ATSValueError: Key ATS_VERSION is not present in config.
        '''
        ctx: str = 'info_keys::get_version(...)'
        msg: str = f'{cls.ATS_VERSION} is not present in config'
        is_present_required_key(config, cls.ATS_VERSION, ctx, msg)

        return config.get(cls.ATS_VERSION)

    @classmethod
    def get_build_date(cls, config: Mapping[str, str]) -> str:
        '''
            Returns the build date of the application from config.

            :param config: Configuration mapping.
            :return: Build date of the application if defined, otherwise None.
            :exceptions:
                | ATSValueError: Key ATS_BUILD_DATE is not present in config.
        '''
        ctx: str = 'info_keys::get_build_date(...)'
        msg: str = f'{cls.ATS_BUILD_DATE} is not present in config'
        is_present_required_key(config, cls.ATS_BUILD_DATE, ctx, msg)

        return config.get(cls.ATS_BUILD_DATE)

    @classmethod
    def get_licence(cls, config: Mapping[str, str]) -> str:
        '''
            Returns the licence of the application from config.

            :param config: Configuration mapping.
            :return: Licence of the application if defined, otherwise None.
            :exceptions:
                | ATSValueError: Key ATS_LICENCE is not present in config.
        '''
        ctx: str = 'info_keys::get_licence(...)'
        msg: str = f'{cls.ATS_LICENCE} is not present in config'
        is_present_required_key(config, cls.ATS_LICENCE, ctx, msg)

        return config.get(cls.ATS_LICENCE)

    @classmethod
    def get_repository(cls, config: Mapping[str, str]) -> str:
        '''
            Returns the repository of the application from config.

            :param config: Configuration mapping.
            :return: Repository of the application if defined, otherwise None.
            :exceptions:
                | ATSValueError: Key ATS_REPOSITORY is not present in config.
        '''
        ctx: str = 'info_keys::get_repository(...)'
        msg: str = f'{cls.ATS_REPOSITORY} is not present in config'
        is_present_required_key(config, cls.ATS_REPOSITORY, ctx, msg)

        return config.get(cls.ATS_REPOSITORY)

    @classmethod
    def get_organization(cls, config: Mapping[str, str]) -> str:
        '''
            Returns the organization of the application from config.

            :param config: Configuration mapping.
            :return: Organization of the application if defined, otherwise None.
            :exceptions:
                | ATSValueError: Key ATS_ORGANIZATION is not present in config.
        '''
        ctx: str = 'info_keys::get_organization(...)'
        msg: str = f'{cls.ATS_ORGANIZATION} is not present in config'
        is_present_required_key(config, cls.ATS_ORGANIZATION, ctx, msg)

        return config.get(cls.ATS_ORGANIZATION)

    @classmethod
    def get_use_github_infrastructure(cls, config: Mapping[str, str]) -> bool:
        '''
            Returns the use github infrastructure of the application from config.

            :param config: Configuration mapping.
            :return: Use github infrastructure of the application if defined, otherwise None.
            :exceptions:
                | ATSValueError: Key ATS_USE_GITHUB_INFRASTRUCTURE is not present in config.
        '''
        ctx: str = 'info_keys::get_use_github_infrastructure(...)'
        msg: str = f'{cls.ATS_USE_GITHUB_INFRASTRUCTURE} is not present in config'
        is_present_required_key(config, cls.ATS_USE_GITHUB_INFRASTRUCTURE, ctx, msg)

        return config.get(cls.ATS_USE_GITHUB_INFRASTRUCTURE)

    @classmethod
    def get_logo_path(cls, config: Mapping[str, str]) -> str:
        '''
            Returns the logo path of the application from config.

            :param config: Configuration mapping.
            :return: Logo path of the application if defined, otherwise None.
            :exceptions:
                | ATSValueError: Key ATS_LOGO_PATH is not present in config.
        '''
        ctx: str = 'info_keys::get_logo_path(...)'
        msg: str = f'{cls.ATS_LOGO_PATH} is not present in config'
        is_present_required_key(config, cls.ATS_LOGO_PATH, ctx, msg)

        return config.get(cls.ATS_LOGO_PATH)

    @classmethod
    def get_log_file(cls, config: Mapping[str, str]) -> str:
        '''
            Returns the log file of the application from config.

            :param config: Configuration mapping.
            :return: Log file of the application if defined, otherwise None.
            :exceptions:
                | ATSValueError: Key ATS_LOG_FILE is not present in config.
        '''
        ctx: str = 'info_keys::get_log_file(...)'
        msg: str = f'{cls.ATS_LOG_FILE} is not present in config'
        is_present_required_key(config, cls.ATS_LOG_FILE, ctx, msg)

        return config.get(cls.ATS_LOG_FILE)

    @classmethod
    def get_info_ok(cls, config: Mapping[str, str]) -> bool:
        '''
            Returns the info ok of the application from config.

            :param config: Configuration mapping.
            :return: Info ok of the application if defined, otherwise None.
            :exceptions:
                | ATSValueError: Key ATS_INFO_OK is not present in config.
        '''
        ctx: str = 'info_keys::get_info_ok(...)'
        msg: str = f'{cls.ATS_INFO_OK} is not present in config'
        is_present_required_key(config, cls.ATS_INFO_OK, ctx, msg)

        return config.get(cls.ATS_INFO_OK)
