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
from ats_utilities.factory import inject, format_instance_to_string
from ats_utilities.info.iinfo_ok import IATSInfoOk
from ats_utilities.checker.ichecker import IATSChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.console_io.proxy_reporter import vreporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSInfoOk(IATSInfoOk):
    '''
        Defines class ATSInfoOk with attribute(s) and method(s).
        Creates an API for the ATS info status in one property object.
        The ATS info status container.

        It defines:

            :attributes:
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
                | __info_ok - The ATS information status (default False).
            :methods:
                | __init__ - Initials ATSInfoOk constructor.
                | ats_info_ok - Property methods for set/get operations.
                | __str__ - Returns the string representation of ATS info status.
    '''

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSInfoOk constructor.

            :param checker: Parameters checker (default set ATSChecker) | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: Reporter for messaging (default set ATSReporter) | None
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option (default False)
            :type verbose: <bool>
            :exceptions: None
        '''
        # No dependency injection then use default ones.
        inject(
            self,
            ('checker', checker, ATSChecker, None),
            ('reporter', reporter, ATSReporter, ['checker']),
            ('verbose', verbose, False, None)
        )
        self.__info_ok: bool = False

    @property
    @vreporter('get info_ok {info_ok}')
    def info_ok(self) -> bool:
        '''
            Property method for getting ATS information status.

            :return: The ATS information status in bool format
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError by vreporter
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
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        self.__info_ok = info_ok

    def __str__(self) -> str:
        '''
            Returns the string representation of ATS info status.

            :return: The ATS info status string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
