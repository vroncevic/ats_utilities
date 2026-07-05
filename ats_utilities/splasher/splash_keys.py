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
from typing import Any, ClassVar

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


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
                | get_all_keys - Returns a list of all defined ClassVar keys for the splash screen.
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

    def __post_init__(self) -> None:
        '''
            Post initials SplashKeys constructor.
            Safely bypasses frozen restriction via object.__setattr__.

            :exceptions: None.
        '''
        if not self.enabled:
            object.__setattr__(self, 'name', None)
            object.__setattr__(self, 'repository', None)
            object.__setattr__(self, 'organization', None)
            object.__setattr__(self, 'logo_path', None)
            object.__setattr__(self, 'use_github_infrastructure', None)

    @classmethod
    def from_dict(cls, config: Mapping[str, Any]) -> SplashKeys:
        '''
            Factory method to safely parse a dictionary into a SplashKeys instance.

            :param config: Configuration mapping.
            :type config: <Mapping[str, Any]>
            :return: Fully initialized SplashKeys instance.
            :rtype: <SplashKeys>
            :exceptions: None.
        '''
        is_enabled: bool = bool(config.get('enabled', True))

        return cls(
            name=config.get(cls.ATS_NAME, None) if is_enabled else None,
            repository=config.get(cls.ATS_REPOSITORY, None) if is_enabled else None,
            organization=config.get(cls.ATS_ORGANIZATION, None) if is_enabled else None,
            logo_path=config.get(cls.ATS_LOGO_PATH, None) if is_enabled else None,
            use_github_infrastructure=config.get(cls.ATS_USE_GITHUB_INFRASTRUCTURE, None) if is_enabled else None,
            enabled=is_enabled
        )

    @classmethod
    def get_all_keys(cls) -> list[str]:
        '''
            Returns a list of all defined ClassVar keys for the splash screen.

            :return: List of all defined ClassVar keys for the splash screen.
            :rtype: <list[str]>
            :exceptions: None.
        '''
        return [
            cls.ATS_NAME,
            cls.ATS_REPOSITORY,
            cls.ATS_ORGANIZATION,
            cls.ATS_LOGO_PATH,
            cls.ATS_USE_GITHUB_INFRASTRUCTURE
        ]

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the SplashKeys instance to a dictionary.

            :return: SplashKeys instance in dict format.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        if not self.enabled:
            return {'enabled': False}
        return {
            self.ATS_NAME: self.name,
            self.ATS_REPOSITORY: self.repository,
            self.ATS_ORGANIZATION: self.organization,
            self.ATS_LOGO_PATH: self.logo_path,
            self.ATS_USE_GITHUB_INFRASTRUCTURE: self.use_github_infrastructure
        }
