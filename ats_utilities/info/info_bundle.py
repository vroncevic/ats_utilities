# -*- coding: UTF-8 -*-

'''
Module
    info_bundle.py
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
    Encapsulates info components for InfoBundle creation.
    Enables passing info components to other objects.
'''

from __future__ import annotations

from typing import Any
from dataclasses import dataclass

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
from ats_utilities.validation.check_value import not_empty, not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class InfoBundle:
    '''
        Encapsulates info components for InfoBundle creation.
        Enables passing info components to other objects.

        It defines:

            :attributes:
                | name - The ATS name.
                | version - The ATS version.
                | licence - The ATS licence.
                | build_date - The ATS build date.
                | repository - The ATS repository.
                | organization - The ATS organization.
                | use_github - The ATS use GitHub infrastructure status.
                | logo - The ATS logo path.
                | log_file - The ATS log file.
                | info_ok - The ATS information status.
                | context_bundle - The context bundle.
            :methods:
                | __post_init__ - Post-initialization hook to validate info bundle.
                | validate - Validates info bundle.
                | to_dict - Converts the info bundle instance to a dictionary.
    '''

    name: IName
    version: IVersion
    licence: ILicence
    build_date: IBuildDate
    repository: IRepository
    organization: IOrganization
    use_github: IUseGitHub
    logo: ILogo
    log_file: ILogFile
    info_ok: IInfoOk
    context_bundle: ContextBundle

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to validate info bundle.

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
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Name must be an instance of IName interface.
                | ATSTypeError: Version must be an instance of IVersion interface.
                | ATSTypeError: Licence must be an instance of ILicence interface.
                | ATSTypeError: Build date must be an instance of IBuildDate interface.
                | ATSTypeError: Repository must be an instance of IRepository interface.
                | ATSTypeError: Organization must be an instance of IOrganization interface.
                | ATSTypeError: Use GitHub must be an instance of IUseGitHub interface.
                | ATSTypeError: Logo path must be an instance of ILogo interface.
                | ATSTypeError: Info ok must be an instance of IInfoOk interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle class.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates info bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

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
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Name must be an instance of IName interface.
                | ATSTypeError: Version must be an instance of IVersion interface.
                | ATSTypeError: Licence must be an instance of ILicence interface.
                | ATSTypeError: Build date must be an instance of IBuildDate interface.
                | ATSTypeError: Repository must be an instance of IRepository interface.
                | ATSTypeError: Organization must be an instance of IOrganization interface.
                | ATSTypeError: Use GitHub must be an instance of IUseGitHub interface.
                | ATSTypeError: Logo path must be an instance of ILogo interface.
                | ATSTypeError: Info ok must be an instance of IInfoOk interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle class.
        '''
        context: str = r'info_bundle::validate(...)'
        not_empty(self.name, context, r'name must be provided')
        not_empty(self.version, context, r'version must be provided')
        not_empty(self.licence, context, r'licence must be provided')
        not_empty(self.build_date, context, r'build date must be provided')
        not_empty(self.repository, context, r'repository must be provided')
        not_empty(self.organization, context, r'organization must be provided')
        not_empty(self.use_github, context, r'use github must be provided')
        not_empty(self.logo, context, r'logo must be provided')
        not_empty(self.log_file, context, r'log file must be provided')
        not_empty(self.info_ok, context, r'info ok must be provided')
        not_none(self.context_bundle, context, r'context bundle must be provided')
        istype(self.name, IName, context, r'name must be an instance of IName interface')
        istype(self.version, IVersion, context, r'version must be an instance of IVersion interface')
        istype(self.licence, ILicence, context, r'licence must be an instance of ILicence interface')
        istype(self.build_date, IBuildDate, context, r'build date must be an instance of IBuildDate interface')
        istype(self.repository, IRepository, context, r'repository must be an instance of IRepository interface')
        istype(self.organization, IOrganization, context, r'organization must be an instance of IOrganization interface')
        istype(self.use_github, IUseGitHub, context, r'use github must be an instance of IUseGitHub interface')
        istype(self.logo, ILogo, context, r'logo must be an instance of ILogo interface')
        istype(self.log_file, ILogFile, context, r'log file must be an instance of ILogFile interface')
        istype(self.info_ok, IInfoOk, context, r'info ok must be an instance of IInfoOk interface')
        istype(self.context_bundle, ContextBundle, context, r'context bundle must be an instance of ContextBundle class')

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the info bundle instance to a dictionary.

            :return: Dictionary representation of the info bundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
