# -*- coding: UTF-8 -*-

'''
Module
    splash_keys.py
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
    Defines constants for ATS splash screen keys.
'''

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, ClassVar, Self
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
class SplashKeys:
    '''
        Defines keys for splash screen.

        It defines:

            :attributes:
                | ATS_NAME - Name of the application.
                | ATS_REPOSITORY - Repository URL for the application.
                | ATS_ORGANIZATION - Organization URL for the application.
                | ATS_LOGO_PATH - Path to the logo image.
                | ATS_USE_GITHUB_INFRASTRUCTURE - Use GitHub infrastructure (True/False).
                | name - Name of the application (default None).
                | repository - Repository URL for the application (default None).
                | organization - Organization URL for the application (default None).
                | logo_path - Path to the logo image (default None).
                | use_github_infrastructure - Use GitHub infrastructure (default None).
                | enabled - Enable/disable splash screen (default True).
            :methods:
                | __init__ - Initials SplashKeys constructor.
                | from_dict - Factory method to safely parse a dictionary into a SplashKeys instance.
                | get_all_keys - Returns a tuple of all defined ClassVar keys for the splash screen.
                | to_dict - Converts the SplashKeys instance to a dictionary.
    '''

    ATS_NAME: ClassVar[str] = 'ats_name'
    ATS_REPOSITORY: ClassVar[str] = 'ats_repository'
    ATS_ORGANIZATION: ClassVar[str] = 'ats_organization'
    ATS_LOGO_PATH: ClassVar[str] = 'ats_logo_path'
    ATS_USE_GITHUB_INFRASTRUCTURE: ClassVar[str] = 'ats_use_github_infrastructure'

    name: str | None = None
    repository: str | None = None
    organization: str | None = None
    logo_path: str | None = None
    use_github_infrastructure: bool | None = None
    enabled: bool = True

    _key_to_attr: ClassVar[MappingProxyType[str, str] | None] = None

    @classmethod
    def get_key_to_attr(cls) -> MappingProxyType[str, str]:
        '''
            Returns a read-only mapping of constant keys to instance attributes.

            :return: Read-only mapping of constant keys to instance attributes.
            :rtype: <MappingProxyType[str, str]>
            :exceptions: None.
        '''
        if cls._key_to_attr is None:
            mapping: dict[str, str] = {}

            attr: str
            for attr in dir(cls):
                if attr.startswith('ATS_'):
                    key: str = getattr(cls, attr)
                    attr_name: str = key.replace('ats_', '', 1)
                    mapping[key] = attr_name

            cls._key_to_attr = MappingProxyType(mapping)

        return cls._key_to_attr

    def __post_init__(self) -> None:
        '''
            Post initials SplashKeys constructor.
            Safely bypasses frozen restriction via object.__setattr__.

            :exceptions: None.
        '''
        if not self.enabled:
            attr_name: str

            for attr_name in self.get_key_to_attr().values():
                object.__setattr__(self, attr_name, None)

    @classmethod
    def from_dict(cls, config: Mapping[str, Any]) -> Self:
        '''
            Factory method to safely parse a dictionary into a SplashKeys instance.

            :param config: Configuration mapping.
            :type config: <Mapping[str, Any]>
            :return: Fully initialized SplashKeys instance.
            :rtype: <Self>
            :exceptions: None.
        '''
        is_enabled: bool = bool(config.get('enabled', True))
        kwargs: dict[str, Any] = {'enabled': is_enabled}
        key: str
        attr_name: str

        for key, attr_name in cls.get_key_to_attr().items():
            kwargs[attr_name] = config.get(key, None) if is_enabled else None

        return cls(**kwargs)

    @classmethod
    def get_all_keys(cls) -> tuple[str, ...]:
        '''
            Returns an immutable tuple of all defined ClassVar keys for the splash screen.

            :return: Immutable tuple of all defined ClassVar keys for the splash screen.
            :rtype: <tuple[str, ...]>
            :exceptions: None.
        '''
        return tuple(cls.get_key_to_attr().keys())

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the SplashKeys instance to a dictionary.

            :return: SplashKeys instance in dict format.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        if not self.enabled:
            return {'enabled': False}

        d: dict[str, Any] = {}
        key: str
        attr_name: str

        for key, attr_name in self.get_key_to_attr().items():
            d[key] = getattr(self, attr_name)

        return d
