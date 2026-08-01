# -*- coding: UTF-8 -*-

'''
Module
    schema.py
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
    Defines the InfoSchema class with method(s).
    Provides schema rules, metadata, and constraints for info configuration keys.
'''

from __future__ import annotations

from collections.abc import Sequence, Mapping
from types import MappingProxyType

from ats_utilities.info.setup.keys import InfoKeys
from ats_utilities.info.name.engine import Name
from ats_utilities.info.version.engine import Version
from ats_utilities.info.build_date.engine import BuildDate
from ats_utilities.info.licence.engine import Licence
from ats_utilities.info.repository.engine import Repository
from ats_utilities.info.organization.engine import Organization
from ats_utilities.info.use_github.engine import UseGitHub
from ats_utilities.info.logo.engine import Logo
from ats_utilities.info.log_file.engine import LogFile
from ats_utilities.info.info_ok.engine import InfoOk
from ats_utilities.validation.check_value import not_satisfied, not_none

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class InfoSchema:
    '''
        Defines the InfoSchema class with method(s).
        Provides schema rules, metadata, and constraints for info configuration keys.

        It defines:

            :methods:
                | get_config_keys - Returns a sequence of all information config keys.
                | is_registered_config_key - Checks if the key name is a registered config key.
                | get_config_keys_to_dependency_keys - Returns the mapping of all config keys to their dependency keys.
                | get_optional_config_keys - Returns a sequence of all optional keys.
                | is_optional_config_key - Checks if the key name is an optional key.
                | is_required_config_key - Checks if the key name is a required key.
                | get_required_config_keys - Returns a sequence of all required keys.
                | get_name_of_config_key - Returns the dependency key for the given config key.
                | get_names_of_optional_config_keys - Returns a sequence of all optional keys names.
                | get_names_of_required_config_keys - Returns a sequence of all required keys names.
                | get_all_names_config_keys - Returns a sequence of all config keys names.
                | get_config_key_to_type - Returns the mapping of all config keys to their types.
    '''

    @classmethod
    def get_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all information keys.

            :return: The sequence of all keys.
            :exceptions: None.
        '''
        return (
            InfoKeys.ATS_NAME,
            InfoKeys.ATS_VERSION,
            InfoKeys.ATS_BUILD_DATE,
            InfoKeys.ATS_LICENCE,
            InfoKeys.ATS_REPOSITORY,
            InfoKeys.ATS_ORGANIZATION,
            InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE,
            InfoKeys.ATS_LOGO_PATH,
            InfoKeys.ATS_LOG_FILE,
            InfoKeys.ATS_INFO_OK
        )

    @classmethod
    def is_registered_config_key(cls, name: str) -> bool:
        '''
            Checks if the key name is a registered config key.

            :param name: The name of the key to check.
            :return: True if key name is a registered config key, otherwise False.
            :exceptions: None.
        '''
        return name in cls.get_config_keys()

    @classmethod
    def get_config_keys_to_dependency_keys(cls) -> MappingProxyType[str, str]:
        '''
            Returns the mapping of all config keys to their dependency keys.

            :return: The mapping of all config keys to their dependency keys.
            :exceptions: None.
        '''
        return MappingProxyType({
            InfoKeys.ATS_NAME: InfoKeys.DEPENDENCY_NAME,
            InfoKeys.ATS_VERSION: InfoKeys.DEPENDENCY_VERSION,
            InfoKeys.ATS_BUILD_DATE: InfoKeys.DEPENDENCY_BUILD_DATE,
            InfoKeys.ATS_LICENCE: InfoKeys.DEPENDENCY_LICENCE,
            InfoKeys.ATS_REPOSITORY: InfoKeys.DEPENDENCY_REPOSITORY,
            InfoKeys.ATS_ORGANIZATION: InfoKeys.DEPENDENCY_ORGANIZATION,
            InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE: InfoKeys.DEPENDENCY_USE_GITHUB_INFRASTRUCTURE,
            InfoKeys.ATS_LOGO_PATH: InfoKeys.DEPENDENCY_LOGO_PATH,
            InfoKeys.ATS_LOG_FILE: InfoKeys.DEPENDENCY_LOG_FILE,
            InfoKeys.ATS_INFO_OK: InfoKeys.DEPENDENCY_INFO_OK,
        })

    @classmethod
    def get_optional_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all optional keys.

            :return: The sequence of all optional keys.
            :exceptions: None.
        '''
        return (
            InfoKeys.ATS_REPOSITORY,
            InfoKeys.ATS_ORGANIZATION,
            InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE,
            InfoKeys.ATS_LOGO_PATH,
            InfoKeys.ATS_LOG_FILE,
            InfoKeys.ATS_INFO_OK
        )

    @classmethod
    def is_optional_config_key(cls, key: str) -> bool:
        '''
            Checks if the key name is an optional key.

            :param key: The name of the key to check.
            :return: True if key name is an optional key, otherwise False.
            :exceptions: None.
        '''
        return key in cls.get_optional_config_keys()

    @classmethod
    def is_required_config_key(cls, key: str) -> bool:
        '''
            Checks if the key name is a required key.

            :param key: The name of the key to check.
            :return: True if key name is a required key, otherwise False.
            :exceptions: None.
        '''
        return cls.is_registered_config_key(key) and not cls.is_optional_config_key(key)

    @classmethod
    def get_required_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all required keys.

            :return: The sequence of all required keys.
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
        ctx: str = 'info_schema::get_name_of_config_key(...)'
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

            :return: The sequence of all optional config keys names.
            :exceptions: None.
        '''
        return tuple(cls.get_name_of_config_key(key) for key in cls.get_optional_config_keys())

    @classmethod
    def get_names_of_required_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all required config keys names.

            :return: The sequence of all required config keys names.
            :exceptions: None.
        '''
        return tuple(cls.get_name_of_config_key(key) for key in cls.get_required_config_keys())

    @classmethod
    def get_all_names_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all config keys names.

            :return: The sequence of all config keys names.
            :exceptions: None.
        '''
        return tuple(cls.get_name_of_config_key(key) for key in cls.get_config_keys())

    @classmethod
    def get_config_key_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns the mapping of all config keys to their types.

            :return: The mapping of all config keys to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            InfoKeys.ATS_NAME: Name,
            InfoKeys.ATS_VERSION: Version,
            InfoKeys.ATS_BUILD_DATE: BuildDate,
            InfoKeys.ATS_LICENCE: Licence,
            InfoKeys.ATS_REPOSITORY: Repository,
            InfoKeys.ATS_ORGANIZATION: Organization,
            InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE: UseGitHub,
            InfoKeys.ATS_LOGO_PATH: Logo,
            InfoKeys.ATS_LOG_FILE: LogFile,
            InfoKeys.ATS_INFO_OK: InfoOk
        })
