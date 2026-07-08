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

from __future__ import annotations

from typing import Any
from dataclasses import dataclass, asdict

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
from ats_utilities.info.info_ok.iinfo_ok import IInfoOk
from ats_utilities.info.info_ok.engine import InfoOk
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.factory_component import validate_component
from ats_utilities.factory_value import require_not_empty
from ats_utilities.factory_type import check_type

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


@dataclass(slots=True, kw_only=True)
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
                | logo - The ATS logo path (default None).
                | info_ok - The ATS information status (default None).
                | context_bundle - The context bundle (default None).
            :methods:
                | validate - Validates that ComponentBundle is valid (can be called after merge).
                | merge - Merges non-None values from another InfoComponentBundle into this one.
                | to_dict - Converts the InfoComponentBundle instance to a dictionary.
    '''

    name: IName | None = None
    version: IVersion | None = None
    licence: ILicence | None = None
    build_date: IBuildDate | None = None
    repository: IRepository | None = None
    organization: IOrganization | None = None
    use_github: IUseGitHub | None = None
    logo: ILogo | None = None
    info_ok: IInfoOk | None = None
    context_bundle: ContextBundle | None = None

    def __post_init__(self) -> None:
        '''
            Performs post-initialization validation.

            :exceptions:
                | ATSAttributeError - Name must be an IName implementation.
                | ATSAttributeError - Version must be an IVersion implementation.
                | ATSAttributeError - Licence must be an ILicence implementation.
                | ATSAttributeError - Build date must be an IBuildDate implementation.
                | ATSAttributeError - Repository must be an IRepository implementation.
                | ATSAttributeError - Organization must be an IOrganization implementation.
                | ATSAttributeError - Use GitHub must be an IUseGitHub implementation.
                | ATSAttributeError - Logo path must be an ILogo implementation.
                | ATSAttributeError - Info ok must be an IInfoOk implementation.
        '''
        if self.context_bundle is None:
            self.context_bundle = ContextBundle()

        if self.name is None:
            self.name = Name(self.context_bundle)
            validate_component(self.name, IName, r'name must be an IName instance')

        if self.version is None:
            self.version = Version(self.context_bundle)
            validate_component(self.version, IVersion, r'version must be an IVersion instance')

        if self.licence is None:
            self.licence = Licence(self.context_bundle)
            validate_component(self.licence, ILicence, r'licence must be an ILicence instance')

        if self.build_date is None:
            self.build_date = BuildDate(self.context_bundle)
            validate_component(self.build_date, IBuildDate, r'build_date must be an IBuildDate instance')

        if self.repository is None:
            self.repository = Repository(self.context_bundle)
            validate_component(self.repository, IRepository, r'repository must be an IRepository instance')

        if self.organization is None:
            self.organization = Organization(self.context_bundle)
            validate_component(self.organization, IOrganization, r'organization must be an IOrganization instance')

        if self.use_github is None:
            self.use_github = UseGitHub(self.context_bundle)
            validate_component(self.use_github, IUseGitHub, r'use_github must be an IUseGitHub instance')

        if self.logo is None:
            self.logo = Logo(self.context_bundle)
            validate_component(self.logo, ILogo, r'logo must be an ILogo instance')

        if self.info_ok is None:
            self.info_ok = InfoOk(self.context_bundle)
            validate_component(self.info_ok, IInfoOk, r'info_ok must be an IInfoOk instance')

    def validate(self) -> None:
        '''
            Validates that ComponentBundle is valid (can be called after merge).
            Performs validation of name, version, licence, build_date, repository,
            organization, use_github, logo and info_ok attributes.
            Name must be non-None and an instance of IName interface.
            Version must be non-None and an instance of IVersion interface.
            Licence must be non-None and an instance of ILicence interface.
            Build date must be non-None and an instance of IBuildDate interface.
            Repository must be non-None and an instance of IRepository interface.
            Organization must be non-None and an instance of IOrganization interface.
            Use GitHub must be non-None and an instance of IUseGitHub interface.
            Logo path must be non-None and an instance of ILogo interface.
            Info ok must be non-None and an instance of IInfoOk interface.

            :exceptions:
                | ATSValueError: Name must be provided.
                | ATSValueError: Version must be provided.
                | ATSValueError: Licence must be provided.
                | ATSValueError: Build date must be provided.
                | ATSValueError: Repository must be provided.
                | ATSValueError: Organization must be provided.
                | ATSValueError: Use GitHub must be provided.
                | ATSValueError: Logo path must be provided.
                | ATSValueError: Info ok must be provided.
                | ATSTypeError: Name must be an instance of IName interface.
                | ATSTypeError: Version must be an instance of IVersion interface.
                | ATSTypeError: Licence must be an instance of ILicence interface.
                | ATSTypeError: Build date must be an instance of IBuildDate interface.
                | ATSTypeError: Repository must be an instance of IRepository interface.
                | ATSTypeError: Organization must be an instance of IOrganization interface.
                | ATSTypeError: Use GitHub must be an instance of IUseGitHub interface.
                | ATSTypeError: Logo path must be an instance of ILogo interface.
                | ATSTypeError: Info ok must be an instance of IInfoOk interface.
        '''
        require_not_empty(self.name, r'name must be provided')
        require_not_empty(self.version, r'version must be provided')
        require_not_empty(self.licence, r'licence must be provided')
        require_not_empty(self.build_date, r'build date must be provided')
        require_not_empty(self.repository, r'repository must be provided')
        require_not_empty(self.organization, r'organization must be provided')
        require_not_empty(self.use_github, r'use github must be provided')
        require_not_empty(self.logo, r'logo path must be provided')
        require_not_empty(self.info_ok, r'info ok must be provided')
        check_type(self.name, IName, r'name must be an instance of IName interface')
        check_type(self.version, IVersion, r'version must be an instance of IVersion interface')
        check_type(self.licence, ILicence, r'licence must be an instance of ILicence interface')
        check_type(self.build_date, IBuildDate, r'build date must be an instance of IBuildDate interface')
        check_type(self.repository, IRepository, r'repository must be an instance of IRepository interface')
        check_type(self.organization, IOrganization, r'organization must be an instance of IOrganization interface')
        check_type(self.use_github, IUseGitHub, r'use github must be an instance of IUseGitHub interface')
        check_type(self.logo, ILogo, r'logo path must be an instance of ILogo interface')
        check_type(self.info_ok, IInfoOk, r'info ok must be an instance of IInfoOk interface')

    def merge(self, other: InfoComponentBundle) -> None:
        '''
            Merges non-None values from another InfoComponentBundle into this one.

            :param other: Another InfoComponentBundle to merge into this one.
            :type other: <InfoComponentBundle>
            :exceptions:
                | ATSTypeError: Other must be an InfoComponentBundle instance.
        '''
        check_type(other, InfoComponentBundle, r'other must be an InfoComponentBundle instance')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the InfoComponentBundle instance to a dictionary.

            :return: Dictionary representation of the InfoComponentBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return asdict(self)
