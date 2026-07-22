# -*- coding: UTF-8 -*-

'''
Module
    info_params.py
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
    TypedDict for InfoRegistry parameters.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypedDict, NotRequired

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.info.name.engine import Name
from ats_utilities.info.version.engine import Version
from ats_utilities.info.licence.engine import Licence
from ats_utilities.info.build_date.engine import BuildDate
from ats_utilities.info.repository.engine import Repository
from ats_utilities.info.organization.engine import Organization
from ats_utilities.info.use_github.engine import UseGitHub
from ats_utilities.info.logo.engine import Logo
from ats_utilities.info.log_file.engine import LogFile
from ats_utilities.info.info_ok.engine import InfoOk

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class InfoParams(TypedDict):
    '''TypedDict defining parameter types for InfoRegistry.'''
    info: NotRequired[Mapping[str, Any]]
    context_bundle: ContextBundle
    name: NotRequired[Name]
    version: NotRequired[Version]
    licence: NotRequired[Licence]
    build_date: NotRequired[BuildDate]
    repository: NotRequired[Repository]
    organization: NotRequired[Organization]
    use_github: NotRequired[UseGitHub]
    logo: NotRequired[Logo]
    log_file: NotRequired[LogFile]
    info_ok: NotRequired[InfoOk]

