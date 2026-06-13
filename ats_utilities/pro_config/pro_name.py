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

from typing import ClassVar, List, Optional
from ats_utilities.checker.iats_checker import IATSChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.checker.iats_checker import ErrorChecker
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.pro_config.ipro_name import IProName

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.6'
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
                | ERRORS - Error checker.
                | __checker - Error checker.
                | __reporter - ATSReporter for outputting messages.
                | __verbose - Enable/Disable verbose option.
                | __pro_name - Project name.
            :methods:
                | __init__ - Initials ProName constructor.
                | pro_name - Property methods for set/get operations.
                | is_pro_name_ok - Checks is project name ok.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ProName constructor.

            :param checker: Error checker | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: ATSReporter for outputting messages | None
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose
        self.__pro_name: Optional[str] = None
        self.__reporter.verbose(self.__verbose, ['init project name'])

    @property
    def pro_name(self) -> Optional[str]:
        '''
            Property method for getting project name.

            :return: Formatted project name | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self.__pro_name

    @pro_name.setter
    def pro_name(self, name: Optional[str]) -> None:
        '''
            Property method for setting project name.

            :param name: Project name | None
            :type name: <Optional[str]>
            :exceptions: ATSTypeError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.__checker.validate_parameters([('str:name', name)])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)

        self.__reporter.verbose(self.__verbose, [f'set project name: {name}'])
        self.__pro_name = name

    def is_pro_name_ok(self) -> bool:
        '''
            Checks is project name ok.

            :return: True (project name is not None) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return self.__pro_name is not None
