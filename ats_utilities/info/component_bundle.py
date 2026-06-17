# -*- coding: utf-8 -*-

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
    Encapsulates core utilities to minimize constructor overhead.
'''

from typing import List, Optional
from dataclasses import dataclass
from ats_utilities.info.iname import IName
from ats_utilities.info.iversion import IVersion
from ats_utilities.info.ilicence import ILicence
from ats_utilities.info.ibuild_date import IBuildDate
from ats_utilities.info.iinfo_ok import IInfoOk

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class ATSInfoComponentBundle:
    '''
        Parameter Object pattern wrapper encapsulating all core info domain elements.
        Simplifies dependency passing and signatures for higher-level managers.

        :param name: The ATS name | None
        :type name: <Optional[IName]>
        :param version: The ATS version | None
        :type version: <Optional[IVersion]>
        :param licence: The ATS licence | None
        :type licence: <Optional[ILicence]>
        :param build_date: The ATS build date | None
        :type build_date: <Optional[IBuildDate]>
        :param info_ok: The ATS information status | None
        :type info_ok: <Optional[IInfoOk]>
    '''
    name: Optional[IName] = None
    version: Optional[IVersion] = None
    licence: Optional[ILicence] = None
    build_date: Optional[IBuildDate] = None
    info_ok: Optional[IInfoOk] = None
