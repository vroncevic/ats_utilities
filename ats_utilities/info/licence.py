# -*- coding: UTF-8 -*-

'''
Module
    licence.py
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
    Defines class ATSLicence with attribute(s) and method(s).
    Creates an API for the ATS licence in one property object.
'''

from typing import List, Optional
from ats_utilities.info.ilicence import IATSLicence
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


class ATSLicence(IATSLicence):
    '''
        Defines class ATSLicence with attribute(s) and method(s).
        Creates an API for the ATS licence in one property object.
        The ATS license container.

        It defines:

            :attributes:
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
                | __licence - The ATS licence (default None).
            :methods:
                | __init__ - Initials ATSLicence constructor.
                | licence - Property methods for set/get operations.
                | is_licence_not_none - Checks is ATS licence is not None.
                | __str__ - Returns the string representation of ATS licence.
    '''

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSLicence constructor.

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
        self.__licence: Optional[str] = None

    @property
    @vreporter('get licence {licence}')
    def licence(self) -> Optional[str]:
        '''
            Property method for getting ATS licence.

            :return: The ATS licence in string format | None
            :rtype: <Optional[str]>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__licence

    @licence.setter
    @validator([('Optional[str]:licence', None)])
    @vreporter('set licence {licence}')
    def licence(self, licence: Optional[str]) -> None:
        '''
            Property method for setting ATS licence.

            :param licence: The ATS licence in string format | None
            :type licence: <Optional[str]>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        self.__licence = licence

    @vreporter('check licence {licence}')
    def is_licence_not_none(self) -> bool:
        '''
            Checks is ATS licence not None.

            :return: True (ATS licence is not None) | False (ATS licence is None)
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__licence is not None

    def __str__(self) -> str:
        '''
            Returns the string representation of ATS licence.

            :return: The ATS licence string representation
            :rtype: <str>
            :exceptions: None
        '''
        licence = str(self.__licence).replace('\n', '\n    ')
        checker = str(self.__checker).replace('\n', '\n    ')
        reporter = str(self.__reporter).replace('\n', '\n    ')
        verbose = str(self.__verbose).replace('\n', '\n    ')

        return (
            f'<{self.__class__.__name__}(\n'
            f'    licence={licence},\n'
            f'    checker={checker},\n'
            f'    reporter={reporter},\n'
            f'    verbose={verbose}\n)> at 0x{id(self):x}'
        )
