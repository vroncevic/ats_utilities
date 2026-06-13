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

from typing import ClassVar, List, Optional
from ats_utilities.checker.iats_checker import IATSChecker, ErrorChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.info.iversion import IATSVersion

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.6'
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
                | ERRORS - Error checker mapping.
                | __checker - Error checker.
                | __reporter - ATSReporter for messaging.
                | __verbose - Enable/Disable verbose option.
                | __version - The ATS version.
            :methods:
                | __init__ - Initials ATSVersion constructor.
                | version - Property methods for set/get operations.
                | is_version_not_none - Checks is ATS version not None.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSVersion constructor.

            :param checker: Error checker | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: ATSReporter for messaging | None
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose
        self.__version: Optional[str] = None

    @property
    def version(self) -> Optional[str]:
        '''
            Property method for getting ATS version.

            :return: The ATS version | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self.__version

    @version.setter
    def version(self, version: Optional[str]) -> None:
        '''
            Property method for setting ATS version.

            :param version: The ATS version | None
            :type version: <Optional[str]>
            :exceptions: ATSTypeError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.__checker.validate_parameters([('str:version', version)])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)

        self.__version = version
        self.__reporter.verbose(self.__verbose, [f'version {version}'])

    def is_version_not_none(self) -> bool:
        '''
            Checks is ATS version not None.

            :return: True (ATS version is not None) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return self.__version is not None
