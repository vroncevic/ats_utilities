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

from typing import Any, ClassVar, Dict, List, Optional
from ats_utilities.checker.iats_checker import IATSChecker, ErrorChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.splash.isplash_screen import ISplashProperty

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.6'
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
                | ERRORS - Error checker.
                | _EXPECTED_PROP_KEYS - Expected property names.
                | __checker - Error checker.
                | __reporter - ATSReporter for outputting messages.
                | __verbose - Enable/Disable verbose option.
                | __property - Splash property in dict format.
            :methods:
                | __init__ - Initials SplashProperty constructor.
                | validation - Validates splash property.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker
    _EXPECTED_PROP_KEYS: List[str] = [
        'ats_organization',
        'ats_repository',
        'ats_name',
        'ats_logo_path',
        'ats_use_github_infrastructure'
    ]

    def __init__(
        self,
        prop: Dict[Any, Any],
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials SplashProperty constructor.

            :param prop: Splash property in dict form
            :type prop: <Dict[Any, Any]>
            :param checker: Error checker | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: ATSReporter for outputting messages | None
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose

        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.__checker.validate_parameters([('dict:prop', prop)])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)

        if not bool(prop):
            raise ATSValueError(error_msg)

        self.__property:  Dict[Any, Any] = prop
        self.__reporter.verbose(self.__verbose, [f'splash property {prop}'])

    def validate(self, verbose: bool = False) -> bool:
        '''
            Validates splash property.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (property ok) else False
            :rtype: <bool>
            :exceptions: None
        '''
        for key in self._EXPECTED_PROP_KEYS:
            if key not in self.__property.keys():
                self.__reporter.error([f'missing property {key}'])
                return False

        self.__reporter.verbose(self.__verbose or verbose, ['property checked and all prepared'])

        return True
