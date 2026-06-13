# -*- coding: UTF-8 -*-

'''
Module
    template_dir.py
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
    Defines class TemplateDir with attribute(s) and method(s).
    Defines project template directory container.
'''

from typing import ClassVar, List, Optional
from ats_utilities.checker.ichecker import IATSChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.checker.ichecker import ErrorChecker
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.pro_config.itemplate_dir import ITemplateDir

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class TemplateDir(ITemplateDir):
    '''
        Defines class TemplateDir with attribute(s) and method(s).
        Defines project template directory container.
        Mechanism for project configuration.

        It defines:

            :attributes:
                | ERRORS - Error checker.
                | __checker - Error checker.
                | __reporter - ATSReporter for outputting messages.
                | __verbose - Enable/Disable verbose option.
                | __template_dir - Project template dir.
            :methods:
                | __init__ - Initials TemplateDir constructor.
                | template_dir - Property methods for set/get operations.
                | is_template_dir_ok - Checks is template dir ok.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials TemplateDir constructor.

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
        self.__template_dir: Optional[str] = None
        self.__reporter.verbose(self.__verbose, ['init template dir'])

    @property
    def template_dir(self) -> Optional[str]:
        '''
            Property method for getting template dir.

            :return: Formatted template dir | None.
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self.__template_dir

    @template_dir.setter
    def template_dir(self, dir_path: Optional[str]) -> None:
        '''
            Property method for setting project template dir.

            :param dir_path: Project template dir path | None
            :type dir_path: <Optional[str]>
            :exceptions: ATSTypeError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.__checker.validate_parameters([('str:dir_path', dir_path)])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)

        self.__reporter.verbose(self.__verbose, [f'set template dir: {dir_path}'])
        self.__template_dir = dir_path

    def is_template_dir_ok(self) -> bool:
        '''
            Checks is project template dir ok.

            :return: True (tempalte dir is not None) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return self.__template_dir is not None
