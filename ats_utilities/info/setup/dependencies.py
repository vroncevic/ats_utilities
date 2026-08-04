# -*- coding: UTF-8 -*-

'''
Module
    dependencies.py
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
    The info bundle dependencies for the info bundle.
'''

from __future__ import annotations

from typing import TypedDict, NotRequired

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

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class InfoBundleDependencies(TypedDict):
    '''
        The info bundle dependencies for the info bundle.

        It defines:

            :attributes:
                | name - The ATS name.
                | version - The ATS version.
                | licence - The ATS licence.
                | build_date - The ATS build date.
                | repository - The ATS repository.
                | organization - The ATS organization.
                | use_github - The ATS use github infrastructure.
                | logo - The ATS logo.
                | log_file - The ATS log file.
                | info_ok - The ATS information status.
                | context_bundle - The context bundle.
    '''

    # --- REQUIRED ATTRIBUTES ---
    name: IName
    version: IVersion
    licence: ILicence
    build_date: IBuildDate
    info_ok: IInfoOk
    context_bundle: ContextBundle

    # --- OPTIONAL ATTRIBUTES ---
    repository: NotRequired[IRepository]
    organization: NotRequired[IOrganization]
    use_github: NotRequired[IUseGitHub]
    logo: NotRequired[ILogo]
    log_file: NotRequired[ILogFile]
