# -*- coding: UTF-8 -*-

'''
Module
    component_bundle.py
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
    Defines component bundle data classe for dependency group simplification.
    Encapsulates info components to minimize constructor overhead.
'''

from typing import List, Optional
from dataclasses import dataclass, field
from ats_utilities.info.iname import IName
from ats_utilities.info.iversion import IVersion
from ats_utilities.info.ilicence import ILicence
from ats_utilities.info.ibuild_date import IBuildDate
from ats_utilities.info.irepository import IRepository
from ats_utilities.info.iorganization import IOrganization
from ats_utilities.info.iuse_github import IUseGitHub
from ats_utilities.info.ilogo_path import ILogoPath
from ats_utilities.info.iinfo_ok import IInfoOk
from ats_utilities.context_bundle import ContextBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class InfoComponentBundle:
    '''
        Defines component bundle data classe for dependency group simplification.
        Encapsulates info components to minimize constructor overhead.

        It defines:

            :attributes:
                | name - The ATS name (default None).
                | version - The ATS version (default None).
                | licence - The ATS licence (default None).
                | build_date - The ATS build date (default None).
                | repository - The ATS repository (default None).
                | organization - The ATS organization (default None).
                | use_github - The ATS use GitHub infrastructure status (default None).
                | logo_path - The ATS logo path (default None).
                | info_ok - The ATS information status (default None).
                | context_bundle - The context bundle (default ContextBundle).
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    name: Optional[IName] = None
    version: Optional[IVersion] = None
    licence: Optional[ILicence] = None
    build_date: Optional[IBuildDate] = None
    repository: Optional[IRepository] = None
    organization: Optional[IOrganization] = None
    use_github: Optional[IUseGitHub] = None
    logo_path: Optional[ILogoPath] = None
    info_ok: Optional[IInfoOk] = None
    context_bundle: Optional[ContextBundle] = field(default_factory=ContextBundle)

    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :return: None.
            :rtype: <None>
            :exceptions: ValueError
        '''
        if self.name is None:
            raise ValueError("Name must be provided.")
        if self.version is None:
            raise ValueError("Version must be provided.")
        if self.licence is None:
            raise ValueError("Licence must be provided.")
        if self.build_date is None:
            raise ValueError("Build date must be provided.")
        if self.repository is None:
            raise ValueError("Repository must be provided.")
        if self.organization is None:
            raise ValueError("Organization must be provided.")
        if self.use_github is None:
            raise ValueError("Use GitHub must be provided.")
        if self.logo_path is None:
            raise ValueError("Logo path must be provided.")
        if self.info_ok is None:
            raise ValueError("Info ok must be provided.")

    def merge(self, other: 'InfoComponentBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <InfoComponentBundle>
            :return: None.
            :rtype: <None>
            :exceptions: None
        '''
        for field_name in self.__dataclass_fields__:
            other_value = getattr(other, field_name)
            if other_value is not None:
                setattr(self, field_name, other_value)

    def to_dict(self) -> dict:
        '''
            Converts the bundle attributes to a dictionary.

            :return: Dictionary representation of the bundle attributes.
            :rtype: <dict>
            :exceptions: None
        '''
        return {
            name: value
            for name, value in self.__dict__.items()
            if not name.startswith('_')
        }

