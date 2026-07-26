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
    Validator for info bundle instance.
'''

from __future__ import annotations

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
from ats_utilities.context.validator import ContextValidator
from ats_utilities.validation.check_value import not_empty, not_none
from ats_utilities.validation.check_type import istype

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class InfoValidator:
    '''
        Validator for info bundle instance.

        It defines:

            :methods:
                | validate - Validates info bundle instance.
    '''

    @classmethod
    def validate(cls, bundle: InfoBundle) -> None:
        '''
            Validates info bundle instance.

            :param bundle: Info bundle instance to be validated.
            :exceptions:
                | ATSValueError: Info bundle must be provided and have proper values.
                | ATSTypeError:  Info bundle must be an instance of InfoBundle and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'info_validator::validate(...)'

        not_none(bundle, ctx, 'bundle must be provided and have proper values')
        istype(bundle, InfoBundle, ctx, 'bundle must be an instance of InfoBundle')

        not_none(bundle.name, ctx, 'name must be provided')
        not_none(bundle.version, ctx, 'version must be provided')
        not_none(bundle.licence, ctx, 'licence must be provided')
        not_none(bundle.build_date, ctx, 'build date must be provided')
        not_none(bundle.repository, ctx, 'repository must be provided')
        not_none(bundle.organization, ctx, 'organization must be provided')
        not_none(bundle.use_github, ctx, 'use github must be provided')
        not_none(bundle.logo, ctx, 'logo must be provided')
        not_none(bundle.log_file, ctx, 'log file must be provided')
        not_none(bundle.info_ok, ctx, 'info ok must be provided')
        not_none(bundle.context_bundle, ctx, 'context bundle must be provided')

        not_empty(bundle.name, ctx, 'name must be not empty')
        not_empty(bundle.version, ctx, 'version must be not empty')
        not_empty(bundle.licence, ctx, 'licence must be not empty')
        not_empty(bundle.build_date, ctx, 'build date must be not empty')

        istype(bundle.name, IName, ctx, 'name must be an instance of IName')
        istype(bundle.version, IVersion, ctx, 'version must be an instance of IVersion')
        istype(bundle.licence, ILicence, ctx, 'licence must be an instance of ILicence')
        istype(bundle.build_date, IBuildDate, ctx, 'build date must be an instance of IBuildDate')
        istype(bundle.repository, IRepository, ctx, 'repository must be an instance of IRepository')
        istype(bundle.organization, IOrganization, ctx, 'organization must be an instance of IOrganization')
        istype(bundle.use_github, IUseGitHub, ctx, 'use github must be an instance of IUseGitHub')
        istype(bundle.logo, ILogo, ctx, 'logo must be an instance of ILogo')
        istype(bundle.log_file, ILogFile, ctx, 'log file must be an instance of ILogFile')
        istype(bundle.info_ok, IInfoOk, ctx, 'info ok must be an instance of IInfoOk')
        istype(bundle.context_bundle, ContextBundle, ctx, 'context bundle must be an instance of ContextBundle')

        ContextValidator.validate(bundle.context_bundle)
