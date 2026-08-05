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
    Validator for the info bundle.
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
from ats_utilities.context.validator import ContextBundleValidator
from ats_utilities.validation.check_value import not_empty, not_none
from ats_utilities.validation.check_type import istype

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class InfoBundleValidator:
    '''
        Validator for the info bundle.

        It defines:

            :methods:
                | validate - Validates the info bundle.
    '''

    @classmethod
    def validate(cls, bundle: InfoBundle) -> None:
        '''
            Validates the info bundle.

            :param bundle: The info bundle instance to be validated.
            :exceptions:
                | ATSValueError: The info bundle must be provided and have proper values.
                | ATSTypeError:  The info bundle must be an instance of InfoBundle and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'info_bundle_validator::validate(...)'
        msg_bundle_not_provided: str = 'the info bundle must be provided and have proper values'
        msg_bundle_not_instance: str = 'the info bundle must be an instance of InfoBundle'
        msg_name_not_provided: str = 'the name must be provided'
        msg_version_not_provided: str = 'the version must be provided'
        msg_licence_not_provided: str = 'the licence must be provided'
        msg_build_date_not_provided: str = 'the build date must be provided'
        msg_repository_not_provided: str = 'the repository must be provided'
        msg_organization_not_provided: str = 'the organization must be provided'
        msg_use_github_not_provided: str = 'the use github must be provided'
        msg_logo_not_provided: str = 'the logo must be provided'
        msg_log_file_not_provided: str = 'the log file must be provided'
        msg_info_ok_not_provided: str = 'the info ok must be provided'
        msg_context_bundle_not_provided: str = 'the context bundle must be provided'
        msg_name_not_empty: str = 'the name must be not empty'
        msg_version_not_empty: str = 'the version must be not empty'
        msg_licence_not_empty: str = 'the licence must be not empty'
        msg_build_date_not_empty: str = 'the build date must be not empty'
        msg_name_not_instance: str = 'the name must be an instance of IName'
        msg_version_not_instance: str = 'the version must be an instance of IVersion'
        msg_licence_not_instance: str = 'the licence must be an instance of ILicence'
        msg_build_date_not_instance: str = 'the build date must be an instance of IBuildDate'
        msg_repository_not_instance: str = 'the repository must be an instance of IRepository'
        msg_organization_not_instance: str = 'the organization must be an instance of IOrganization'
        msg_use_github_not_instance: str = 'the use github must be an instance of IUseGitHub'
        msg_logo_not_instance: str = 'the logo must be an instance of ILogo'
        msg_log_file_not_instance: str = 'the log file must be an instance of ILogFile'
        msg_info_ok_not_instance: str = 'the info ok must be an instance of IInfoOk'
        msg_context_bundle_not_instance: str = 'the context bundle must be an instance of ContextBundle'

        not_none(bundle, ctx, msg_bundle_not_provided)
        istype(bundle, InfoBundle, ctx, msg_bundle_not_instance)

        not_none(bundle.name, ctx, msg_name_not_provided)
        not_none(bundle.version, ctx, msg_version_not_provided)
        not_none(bundle.licence, ctx, msg_licence_not_provided)
        not_none(bundle.build_date, ctx, msg_build_date_not_provided)
        not_none(bundle.repository, ctx, msg_repository_not_provided)
        not_none(bundle.organization, ctx, msg_organization_not_provided)
        not_none(bundle.use_github, ctx, msg_use_github_not_provided)
        not_none(bundle.logo, ctx, msg_logo_not_provided)
        not_none(bundle.log_file, ctx, msg_log_file_not_provided)
        not_none(bundle.info_ok, ctx, msg_info_ok_not_provided)
        not_none(bundle.context_bundle, ctx, msg_context_bundle_not_provided)

        not_empty(bundle.name, ctx, msg_name_not_empty)
        not_empty(bundle.version, ctx, msg_version_not_empty)
        not_empty(bundle.licence, ctx, msg_licence_not_empty)
        not_empty(bundle.build_date, ctx, msg_build_date_not_empty)

        istype(bundle.name, IName, ctx, msg_name_not_instance)
        istype(bundle.version, IVersion, ctx, msg_version_not_instance)
        istype(bundle.licence, ILicence, ctx, msg_licence_not_instance)
        istype(bundle.build_date, IBuildDate, ctx, msg_build_date_not_instance)
        istype(bundle.repository, IRepository, ctx, msg_repository_not_instance)
        istype(bundle.organization, IOrganization, ctx, msg_organization_not_instance)
        istype(bundle.use_github, IUseGitHub, ctx, msg_use_github_not_instance)
        istype(bundle.logo, ILogo, ctx, msg_logo_not_instance)
        istype(bundle.log_file, ILogFile, ctx, msg_log_file_not_instance)
        istype(bundle.info_ok, IInfoOk, ctx, msg_info_ok_not_instance)
        istype(bundle.context_bundle, ContextBundle, ctx, msg_context_bundle_not_instance)

        ContextBundleValidator.validate(bundle.context_bundle)
