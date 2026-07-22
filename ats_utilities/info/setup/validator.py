# -*- coding: UTF-8 -*-

'''
Module
    validator.py
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
    Validates InfoBundle instance.
'''

from __future__ import annotations

from typing import override

from ats_utilities.info.setup.bundle import InfoBundle
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
from ats_utilities.utils.ivalidator import IValidator
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


class InfoValidator(IValidator[InfoBundle]):
    '''
        Validates InfoBundle instance.

        It defines:
            
            :methods:
                | validate - Validates info bundle instance.
    '''

    @classmethod
    @override
    def validate(cls, bundle: InfoBundle) -> None:
        '''
            Validates info bundle instance.

            :param bundle: InfoBundle instance to be validated.
            :type bundle: InfoBundle
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
        ctx: str = r'info_bundle::validate(...)'

        not_empty(bundle.name, ctx, r'name must be provided')
        not_empty(bundle.version, ctx, r'version must be provided')
        not_empty(bundle.licence, ctx, r'licence must be provided')
        not_empty(bundle.build_date, ctx, r'build date must be provided')
        not_empty(bundle.repository, ctx, r'repository must be provided')
        not_empty(bundle.organization, ctx, r'organization must be provided')
        not_empty(bundle.use_github, ctx, r'use github must be provided')
        not_empty(bundle.logo, ctx, r'logo must be provided')
        not_empty(bundle.log_file, ctx, r'log file must be provided')
        not_empty(bundle.info_ok, ctx, r'info ok must be provided')
        not_none(bundle.context_bundle, ctx, r'context bundle must be provided')

        istype(bundle.name, IName, ctx, r'name must be an instance of IName interface')
        istype(bundle.version, IVersion, ctx, r'version must be an instance of IVersion interface')
        istype(bundle.licence, ILicence, ctx, r'licence must be an instance of ILicence interface')
        istype(bundle.build_date, IBuildDate, ctx, r'build date must be an instance of IBuildDate interface')
        istype(bundle.repository, IRepository, ctx, r'repository must be an instance of IRepository interface')
        istype(bundle.organization, IOrganization, ctx, r'organization must be an instance of IOrganization interface')
        istype(bundle.use_github, IUseGitHub, ctx, r'use github must be an instance of IUseGitHub interface')
        istype(bundle.logo, ILogo, ctx, r'logo must be an instance of ILogo interface')
        istype(bundle.log_file, ILogFile, ctx, r'log file must be an instance of ILogFile interface')
        istype(bundle.info_ok, IInfoOk, ctx, r'info ok must be an instance of IInfoOk interface')
        istype(bundle.context_bundle, ContextBundle, ctx, r'context bundle must be an instance of ContextBundle class')
