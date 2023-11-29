# -*- coding: UTF-8 -*-

'''
Module
    splash_property.py
Copyright
    Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Creates API for checking splash property.
'''

import sys
from typing import Any, Dict, List

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.9.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class SplashProperty(ATSChecker):
    '''
        Defined class SplashProperty with attribute(s) and method(s).
        Created API for checking splash property.
        Splash screen property API.

        It defines:

            :attributes:
                | _EXPECTED_PROP_KEYS - Expected property names.
                | _verbose - Enable/Disable verbose option.
                | _property - Splash property in dict format.
            :methods:
                | __init__ - Initial SplashProperty constructor.
                | validation - validation of splash property.
    '''

    _EXPECTED_PROP_KEYS: List[str] = [
        'ats_organization',
        'ats_repository',
        'ats_name',
        'ats_logo_path',
        'ats_use_github_infrastructure'
    ]

    def __init__(
        self, prop: Dict[Any, Any], verbose: bool = False
    ) -> None:
        '''
            Initial SplashProperty constructor.

            :param property: Splash property in dict form
            :type property: <dict>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        super().__init__()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([('dict:prop', prop)])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if error_id == self.VALUE_ERROR:
            raise ATSBadCallError(error_msg)
        self._verbose: bool = verbose
        self._property:  Dict[Any, Any] = prop
        verbose_message(self._verbose, [f'splash property {prop}'])

    def validate(self, verbose: bool = False) -> bool:
        '''
            Validation of splash property.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (property ok) else False
            :rtype: <bool>
            :exceptions: None
        '''
        for key in list(self._property.keys()):
            if key not in self._EXPECTED_PROP_KEYS:
                verbose_message(
                    self._verbose or verbose, [f'property {key} not expected']
                )
                return False
        verbose_message(
            self._verbose or verbose, ['property checked and all prepared']
        )
        return True
