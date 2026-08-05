# -*- coding: UTF-8 -*-

'''
Module
    ischema.py
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
    Defines the abstract class IInfoSchema with method(s).
    Provides an interface for info schema rules, metadata, and constraints.
'''

from __future__ import annotations

from collections.abc import Sequence
from types import MappingProxyType
from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class IInfoSchema(Protocol):
    '''
        Defines the abstract class IInfoSchema with method(s).
        Provides an interface for info schema rules, metadata, and constraints.

        It defines:

            :methods:
                | get_config_keys - Returns a sequence of all information config keys.
                | is_registered_config_key - Checks if the key name is a registered config key.
                | get_config_keys_to_dependency_keys - Returns mapping of all config keys to their dependency keys.
                | get_optional_config_keys - Returns a sequence of all optional keys.
                | is_optional_config_key - Checks if the key name is an optional key.
                | is_required_config_key - Checks if the key name is a required key.
                | get_required_config_keys - Returns a sequence of all required keys.
                | get_name_of_config_key - Returns the dependency key for the given config key.
                | get_names_of_optional_config_keys - Returns a sequence of all optional keys names.
                | get_names_of_required_config_keys - Returns a sequence of all required keys names.
                | get_all_names_config_keys - Returns a sequence of all config keys names.
                | get_config_key_to_type - Returns mapping of all config keys to their types.
    '''

    @classmethod
    def get_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all information keys.

            :return: The sequence of all keys.
        '''
        ...

    @classmethod
    def is_registered_config_key(cls, name: str) -> bool:
        '''
            Checks if the key name is a registered config key.

            :param name: The name of the key to check.
            :return: True if key name is a registered config key, otherwise False.
        '''
        ...

    @classmethod
    def get_config_keys_to_dependency_keys(cls) -> MappingProxyType[str, str]:
        '''
            Returns a mapping of all config keys to their dependency keys.

            :return: The mapping of all config keys to their dependency keys.
        '''
        ...

    @classmethod
    def get_optional_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all optional keys.

            :return: The sequence of all optional keys.
        '''
        ...

    @classmethod
    def is_optional_config_key(cls, key: str) -> bool:
        '''
            Checks if the key name is an optional key.

            :param key: The name of the key to check.
            :return: True if key name is an optional key, otherwise False.
        '''
        ...

    @classmethod
    def is_required_config_key(cls, key: str) -> bool:
        '''
            Checks if the key name is a required key.

            :param key: The name of the key to check.
            :return: True if key name is a required key, otherwise False.
        '''
        ...

    @classmethod
    def get_required_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all required keys.

            :return: The sequence of all required keys.
        '''
        ...

    @classmethod
    def get_name_of_config_key(cls, config_key: str) -> str:
        '''
            Returns the dependency key for the given config key.

            :param config_key: The config key.
            :return: The dependency key.
        '''
        ...

    @classmethod
    def get_names_of_optional_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all optional config keys names.

            :return: The sequence of all optional config keys names.
        '''
        ...

    @classmethod
    def get_names_of_required_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all required config keys names.

            :return: The sequence of all required config keys names.
        '''
        ...

    @classmethod
    def get_all_names_config_keys(cls) -> Sequence[str]:
        '''
            Returns a sequence of all config keys names.

            :return: The sequence of all config keys names.
        '''
        ...

    @classmethod
    def get_config_key_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns a mapping of all config keys to their types.

            :return: The mapping of all config keys to their types.
        '''
        ...
