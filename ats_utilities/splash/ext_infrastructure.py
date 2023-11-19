# -*- coding: UTF-8 -*-

'''
 Module
     ext_infrastructure.py
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
     Defined class ExtInfrastructure with attribute(s) and method(s).
     Created API for processing hyperlinks for splash.
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
class ExtInfrastructure:
    '''
        Defined class ExtInfrastructure with attribute(s) and method(s).
        Created API for processing hyperlinks for splash.
        It defines:

            :attributes:
                | __verbose - enable/disable verbose option.
                | __property - splash property in dict format.
            :methods:
                | __init__ - initial constructor.
                | get_info_text - pre-processed info text.
                | get_issue_text - pre-processed issue text.
                | get_author_text - pre-processed author text.
                | __str__ - dunder method for ExtInfrastructure.
    '''

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
        self.__verbose = verbose
        self.__ats_splash_property = property
        verbose_message(
            ExtInfrastructure.verbose, self.__verbose, property
        )

    def get_info_text(self):
        '''
            Pre-processed info text for splash.

            :return: hyperlink with info text.
            :rtype: <str>
            :exceptions: None
        '''
        return '\x1b]8;;{0}\a{1}\x1b]8;;\a'.format(
            '{0}'.format(self.__ats_splash_property['ats_name']),
            '{0}'.format(self.__ats_splash_property['ats_name'])
        )

    def get_issue_text(self):
        '''
            Pre-processed issue text for splash.

            :return: hyperlink with issue info.
            :rtype: <str>
            :exceptions: None
        '''
        return '\x1b]8;;{0}\a{1}\x1b]8;;\a'.format(
            self.__ats_splash_property['ats_repository'],
            self.__ats_splash_property['ats_repository']
        )

    def get_author_text(self):
        '''
            Pre-processed author text for splash.

            :return: hyperlink with author info.
            :rtype: <str>
            :exceptions: None
        '''
        return '\x1b]8;;{0}\a{1}\x1b]8;;\a'.format(
            self.__ats_splash_property['ats_organization'],
            self.__ats_splash_property['ats_organization']
        )

    def __str__(self):
        '''
            Dunder method for ExtInfrastructure.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, str(self.__ats_splash_property)
        )
