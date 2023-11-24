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
     Defined class SplashProperty with attribute(s) and method(s).
     Created API for checking splash property.
'''

import sys

try:
    from six import add_metaclass
    from ats_utilities import VerboseRoot
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
__version__ = '2.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@add_metaclass(VerboseRoot)
class SplashProperty:
    '''
        Defined class SplashProperty with attribute(s) and method(s).
        Created API for checking splash property.
        It defines:

            :attributes:
                | __EXPECTED_PROPERY_KEYS - expected property names.
                | _verbose - Enable/Disable verbose option.
                | __property - splash property in dict format.
            :methods:
                | __init__ - initial constructor.
                | validation - validation of splash property.
                | __str__ - dunder method for SplashProperty.
    '''

    __EXPECTED_PROPERY_KEYS = [
        'ats_organization', 'ats_repository', 'ats_name', 'ats_logo_path',
        'ats_use_github_infrastructure'
    ]

    def __init__(self, property, verbose=False):
        '''
            Initial constructor.

            :param property: splash property in dict form.
            :type property: <dict>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('dict:property', property)
        ])
        if status == ATSChecker.type_error:
            raise ATSTypeError(error)
        if status == ATSChecker.value_error:
            raise ATSBadCallError(error)
        self._verbose = verbose
        self.__property = property
        verbose_message(SplashProperty.verbose, self._verbose, property)

    def validate(self, verbose=False):
        '''
            Validation of splash property.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: Boolean status True - property ok else False.
            :rtype: <bool>
            :exceptions: None
        '''
        for key in list(self.__property.keys()):
            if key not in SplashProperty.__EXPECTED_PROPERY_KEYS:
                verbose_message(
                    SplashProperty.verbose, self._verbose or verbose,
                    'property name {0} not expected'.format(key)
                )
                return False
        verbose_message(
            SplashProperty.verbose, self._verbose or verbose,
            'property checked and all prepared'
        )
        return True

    def __str__(self):
        '''
                Dunder method for SplashProperty.

                :return: object in a human-readable format.
                :rtype: <str>
                :exceptions: None
            '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, str(self._verbose), str(self.__property)
        )
