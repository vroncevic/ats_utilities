# -*- coding: UTF-8 -*-

'''
Module
    info_ok.py
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
    Defines class ATSInfoOk with attribute(s) and method(s).
    Creates an API for the ATS info status in one property object.
'''

from typing import List, Optional
from ats_utilities.info.iinfo_ok import IInfoOk
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.proxy_reporter import vreporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSInfoOk(IInfoOk):
    '''
        Defines class ATSInfoOk with attribute(s) and method(s).
        Creates an API for the ATS info status in one property object.

        It defines:

            :attributes:
                | __checker - Factoriezed parameters checker (default ATSChecker).
                | __reporter - Factoriezed reporter for messaging (default ATSReporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __info_ok - The ATS information status (default False).
            :methods:
                | __init__ - Initials ATSInfoOk constructor.
                | info_ok - Property methods for set/get information status.
                | __str__ - Returns the string representation of ATS info status.
    '''

    def __init__(self, info_bundle: Optional[ContextBundle] = None) -> None:
        '''
            Initials ATSInfoOk constructor.

            :param info_bundle: Bundle with checker, reporter and verbose | None
            :type info_bundle: <Optional[ContextBundle]>
            :exceptions: None
        '''
        factory_context_bundle(self, info_bundle)
        self.__info_ok: bool = False

    @property
    @vreporter('get info_ok {info_ok}')
    def info_ok(self) -> bool:
        '''
            Property method for getting ATS information status.

            :return: The ATS information status in bool format
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError
        '''
        return self.__info_ok

    @info_ok.setter
    @validator([('bool:info_ok', None)])
    @vreporter('set info_ok {info_ok}')
    def info_ok(self, info_ok: bool) -> None:
        '''
            Property method for setting ATS information status.

            :param info_ok: The ATS information status in bool format
            :type info_ok: <bool>
            :exceptions:
                | ATSTypeError, ATSValueError, RuntimeError, AttributeError
                | RuntimeError, AttributeError
        '''
        self.__info_ok = info_ok

    def __str__(self) -> str:
        '''
            Returns the string representation of the ATS info status.

            :return: The ATS info status instance as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
