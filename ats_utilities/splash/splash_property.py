# -*- coding: UTF-8 -*-

'''
Module
    splash_property.py
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
    Defines class SplashProperty with attribute(s) and method(s).
    Creates an API for checking splash property.
'''

from typing import Any, Dict, List, Optional
from ats_utilities.splash.isplash_property import ISplashProperty
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


class SplashProperty(ISplashProperty):
    '''
        Defines class SplashProperty with attribute(s) and method(s).
        Creates an API for checking splash property.
        Splash screen property API.

        It defines:

            :attributes:
                | _EXPECTED_PROP_KEYS - Expected property names.
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
                | __splash_property - Splash property in dict format (default None).
            :methods:
                | __init__ - Initials SplashProperty constructor.
                | splash_property - Property method for get/set splash property.  
                | validation - Validates splash property.
                | __str__ - Returns the string representation of splash property.
    '''

    _EXPECTED_PROP_KEYS: List[str] = [
        'ats_organization',
        'ats_repository',
        'ats_name',
        'ats_logo_path',
        'ats_use_github_infrastructure'
    ]

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials SplashProperty constructor.

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
        self.__splash_property:  Optional[Dict[Any, Any]] = None

    @property
    @vreporter('get splash property {splash_property}')
    def splash_property(self) -> Optional[Dict[Any, Any]]:
        '''
            Property method for getting splash property.

            :return: Formatted splash property in dict format | None
            :rtype: <Optional[str]>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__splash_property

    @splash_property.setter
    @validator([('dict:splash_property_setup', None)])
    @vreporter('set splash property {splash_property}')
    def splash_property(self, splash_property_setup: Optional[Dict[Any, Any]]) -> None:
        '''
            Property method for setting project splash property.

            :param splash_property_setup: Project splash property in dict format | None
            :type splash_property_setup: <Optional[Dict[Any, Any]]>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        self.__splash_property = splash_property_setup

    @vreporter('validation or splash property {splash_property}')
    def validates(self) -> bool:
        '''
            Validates splash property.

            :return: True (splash property ok) else False (splash property not ok)
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        if not self.__splash_property:
            self.__reporter.error(['missing splash property'])
            return False

        for key in self._EXPECTED_PROP_KEYS:
            if key not in self.__splash_property.keys():
                self.__reporter.error([f'missing property {key}'])
                return False

        return True

    def __str__(self) -> str:
        '''
            Returns the string representation of splash property.

            :return: The splash property as string
            :rtype: <str>
            :exceptions: None
        '''
        splash_property = str(self.__splash_property).replace('\n', '\n    ')
        checker = str(self.__checker).replace('\n', '\n    ')
        reporter = str(self.__reporter).replace('\n', '\n    ')
        verbose = str(self.__verbose).replace('\n', '\n    ')

        return (
            f'<{self.__class__.__name__}(\n'
            f'    splash_property={splash_property},\n'
            f'    checker={checker},\n'
            f'    reporter={reporter},\n'
            f'    verbose={verbose}\n)> at 0x{id(self):x}'
        )
