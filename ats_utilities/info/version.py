# -*- coding: UTF-8 -*-

'''
Module
    version.py
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
    Defines class ATSVersion with attribute(s) and method(s).
    Creates an API for the ATS version in one property object.
'''

from typing import List, Optional
from ats_utilities.info.iversion import IATSVersion
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


class ATSVersion(IATSVersion):
    '''
        Defines class ATSVersion with attribute(s) and method(s).
        Creates an API for the ATS version in one property object.
        The ATS version container.

        It defines:

            :attributes:
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
                | __version - The ATS version (default None).
            :methods:
                | __init__ - Initials ATSVersion constructor.
                | version - Property methods for set/get operations.
                | is_version_not_none - Checks is ATS version not None.
                | __str__ - Returns the string representation of ATS version.
    '''

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSVersion constructor.

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
        self.__version: Optional[str] = None

    @property
    @vreporter('get version {version}')
    def version(self) -> Optional[str]:
        '''
            Property method for getting ATS version.

            :return: The ATS version | None
            :rtype: <Optional[str]>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__version

    @version.setter
    @validator([('Optional[str]:version', None)])
    @vreporter('set version {version}')
    def version(self, version: Optional[str]) -> None:
        '''
            Property method for setting ATS version.

            :param version: The ATS version | None
            :type version: <Optional[str]>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        self.__version = version

    @vreporter('check version {version}')
    def is_version_not_none(self) -> bool:
        '''
            Checks is ATS version not None.

            :return: True (version is not None) | False (version is None)
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__version is not None

    def __str__(self) -> str:
        '''
            Returns the string representation of ATS version.

            :return: The ATS version string representation
            :rtype: <str>
            :exceptions: None
        '''
        version = str(self.__version).replace('\n', '\n    ')
        checker = str(self.__checker).replace('\n', '\n    ')
        reporter = str(self.__reporter).replace('\n', '\n    ')
        verbose = str(self.__verbose).replace('\n', '\n    ')

        return (
            f'<{self.__class__.__name__}(\n'
            f'    version={version},\n'
            f'    checker={checker},\n'
            f'    reporter={reporter},\n'
            f'    verbose={verbose}\n)> at 0x{id(self):x} '
        )
