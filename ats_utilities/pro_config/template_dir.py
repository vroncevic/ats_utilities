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

from typing import List, Optional
from ats_utilities.pro_config.itemplate_dir import ITemplateDir
from ats_utilities.factory import inject, format_instance_to_string
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


class TemplateDir(ITemplateDir):
    '''
        Defines class TemplateDir with attribute(s) and method(s).
        Defines project template directory container.
        Mechanism for project configuration.

        It defines:

            :attributes:
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
                | __template_dir - Project template dir path (default None).
            :methods:
                | __init__ - Initials TemplateDir constructor.
                | template_dir - Property methods for set/get operations.
                | is_template_dir_ok - Checks is template dir ok.
                | __str__ - Returns the string representation of ATS project template directory.
    '''

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials TemplateDir constructor.

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
        self.__template_dir: Optional[str] = None

    @property
    @vreporter('get template dir {template_dir}')
    def template_dir(self) -> Optional[str]:
        '''
            Property method for getting template dir.

            :return: Formatted template dir in string format | None
            :rtype: <Optional[str]>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__template_dir

    @template_dir.setter
    @validator([('Optional[str]:dir_path', None)])
    @vreporter('get template dir {template_dir}')
    def template_dir(self, dir_path: Optional[str]) -> None:
        '''
            Property method for setting project template dir.

            :param dir_path: Project template dir path in string format | None
            :type dir_path: <Optional[str]>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        self.__template_dir = dir_path

    @vreporter('check template dir {template_dir}')
    def is_template_dir_ok(self) -> bool:
        '''
            Checks is project template dir ok.

            :return: True (template dir is ok) | False (template dir is not ok)
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__template_dir is not None

    def __str__(self) -> str:
        '''
            Returns the string representation of ATS project template directory.

            :return: The ATS project directory as string
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
