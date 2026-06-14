# -*- coding: UTF-8 -*-

'''
Module
    pro_name.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    ats_utilities is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    ats_utilities is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class ProName with attribute(s) and method(s).
    Defines project name container.
'''

from typing import List, Optional
from ats_utilities.pro_config.ipro_name import IProName
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


class ProName(IProName):
    '''
        Defines class ProName with attribute(s) and method(s).
        Defines project name container.
        Mechanism for project configuration.

        It defines:

            :attributes:
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
                | __pro_name - Project name.
            :methods:
                | __init__ - Initials ProName constructor.
                | pro_name - Property methods for set/get operations.
                | is_pro_name_ok - Checks is project name ok.
                | __str__ - Returns the string representation of ATS project name.
    '''

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ProName constructor.

            :param checker: Parameters checker (default set ATSChecker) | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: Reporter for messaging (default set ATSReporter) | None
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        # No dependency injection then use default ones.
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter(checker=self.__checker)
        self.__verbose: bool = verbose
        self.__pro_name: Optional[str] = None

    @property
    @vreporter('get pro name {pro_name}')
    def pro_name(self) -> Optional[str]:
        '''
            Property method for getting project name in string format.

            :return: Formatted project name in string format | None
            :rtype: <Optional[str]>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__pro_name

    @pro_name.setter
    @validator([('Optional[str]:name', None)])
    @vreporter('get pro name {pro_name}')
    def pro_name(self, name: Optional[str]) -> None:
        '''
            Property method for setting project name.

            :param name: Project name in string format | None
            :type name: <Optional[str]>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        self.__pro_name = name

    @vreporter('check pro name {pro_name}')
    def is_pro_name_ok(self) -> bool:
        '''
            Checks is project name ok.

            :return: True (project name is not None) | False (project name is None)
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__pro_name is not None

    def __str__(self) -> str:
        '''
            Returns the string representation of ATS project name.

            :return: The ATS project name as string
            :rtype: <str>
            :exceptions: None
        '''
        pro_name = str(self.__pro_name).replace('\n', '\n    ')
        checker = str(self.__checker).replace('\n', '\n    ')
        reporter = str(self.__reporter).replace('\n', '\n    ')
        verbose = str(self.__verbose).replace('\n', '\n    ')

        return (
            f'<{self.__class__.__name__}(\n'
            f'    pro_name={pro_name},\n'
            f'    checker={checker},\n'
            f'    reporter={reporter},\n'
            f'    verbose={verbose}\n)> at 0x{id(self):x}'
        )
