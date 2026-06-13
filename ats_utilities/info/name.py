# -*- coding: UTF-8 -*-

'''
Module
    name.py
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
    Defines class ATSName with attribute(s) and method(s).
    Creates an API for the ATS name in one property object.
'''

from typing import ClassVar, List, Optional
from ats_utilities.checker.ichecker import IATSChecker, ErrorChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.info.iname import IATSName

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSName(IATSName):
    '''
        Defines class ATSName with attribute(s) and method(s).
        Creates an API for the ATS name in one property object.
        The ATS name container.

        It defines:

            :attributes:
                | ERRORS - Error checker mapping.
                | __checker - Error checker.
                | __reporter - ATSReporter for messaging.
                | __verbose - Enable/Disable verbose option. 
                | __name - The ATS name.
            :methods:
                | __init__ - Initials ATSName constructor.
                | name - Property methods for set/get operations.
                | is_name_not_none - Checks is ATS name not None.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False,
    ) -> None:
        '''
            Initials ATSName constructor.

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
        self.__name: Optional[str] = None

    @property
    def name(self) -> Optional[str]:
        '''
            Property method for getting ATS name.

            :return: The ATS name | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self.__name

    @name.setter
    def name(self, name: Optional[str]) -> None:
        '''
            Property method for setting ATS name.

            :param name: The ATS name | None
            :type name: <Optional[str]>
            :exceptions: ATSTypeError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.__checker.validate_parameters([('str:name', name)])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)

        self.__name = name
        self.__reporter.verbose(self.__verbose, [f'name {name}'])

    def is_name_not_none(self) -> bool:
        '''
            Checks is ATS name not None.

            :return: True (ATS name is not None) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return self.__name is not None
