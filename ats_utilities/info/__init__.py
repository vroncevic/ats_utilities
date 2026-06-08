# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
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
    Defines ats_utilities.info package.
'''

from typing import List
from .name import ATSName
from .iname import IATSName
from .ilicence import IATSLicence
from .ibuild_date import IATSBuildDate
from .iversion import IATSVersion
from .version import ATSVersion
from .licence import ATSLicence
from .build_date import ATSBuildDate
from .info_ok import ATSInfoOk
from .iinfo_ok import IATSInfoOk
from .ats_info import ATSInfo

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

__all__: List[str] = [
    'ATSName',
    'IATSName',
    'IATSLicence',
    'IATSBuildDate',
    'IATSVersion',
    'ATSVersion',
    'ATSLicence',
    'ATSBuildDate',
    'ATSInfoOk',
    'IATSInfoOk',
    'ATSInfo'
]
