# -*- coding: UTF-8 -*-

'''
Module
    pro_config.py
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
    Defines class ProConfig with attribute(s) and method(s).
    Defines project configuration container.
'''

from typing import Any, List, Dict, Optional
from ats_utilities.factory import inject, format_instance_to_string
from ats_utilities.pro_config.ipro_config import IProConfig
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


class ProConfig(IProConfig):
    '''
        Defines class ProConfig with attribute(s) and method(s).
        Defines project configuration container.
        Mechanism for project configuration.

        It defines:

            :attributes:
                | TEMPLATES - Templates key used for processing template files.
                | MODULES - Modules key used for processing template files.
                | FORMAT - Format for template file extension.
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
                | __config - Tool configuration in dictionary format (default None).
            :methods:
                | __init__ - Initials ProConfig constructor.
                | config - Property methods for set/get operations.
                | is_config_ok - Checks is project configuration ok.
                | __str__ - Returns the string representation of ATS project configuration.
    '''

    TEMPLATES: str = 'templates'
    MODULES: str = 'modules'
    FORMAT: str = 'template'

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ProConfig constructor.

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
        self.__config: Optional[Dict[Any, Any]] = None

    @property
    @vreporter('get config {config}')
    def config(self) -> Optional[Dict[Any, Any]]:
        '''
            Property method for getting project configuration.

            :return: Formatted project configuration in dict format | None
            :rtype: <Optional[Dict[Any, Any]]>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__config

    @config.setter
    @validator([('Optional[dict]:pro_config', None)])
    @vreporter('get config {config}')
    def config(self, pro_config: Optional[Dict[Any, Any]]) -> None:
        '''
            Property method for setting project configuration.

            :param pro_config: Project configuration in dict format | None
            :type pro_config: <Optional[Dict[Any, Any]]>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        self.__config = pro_config

    @vreporter('check config {config}')
    def is_config_ok(self) -> bool:
        '''
            Checks is project configuration ok.

            :return: True (configuration is ok) | False (configuration is not ok)
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__config is not None

    def __str__(self) -> str:
        '''
            Returns the string representation of ATS project configuration.

            :return: The ATS project configuration as string
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
