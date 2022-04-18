# -*- coding: UTF-8 -*-

'''
 Module
     ats_build_date.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class ATSBuildDate with attribute(s) and method(s).
     Created API for ATS build date in one property object.
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
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.5.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@add_metaclass(VerboseRoot)
class ATSBuildDate:
    '''
        Defined class ATSBuildDate with attribute(s) and method(s).
        Created API for ATS build date in one property object.
        It defines:

            :attributes:
                | __verbose - enable/disable verbose option.
                | __build_date - ATS build date.
            :methods:
                | __init__ - initial constructor.
                | build_date - property methods for set/get operations.
                | is_not_none - checking is ATS build date None.
                | __str__ - str dunder method for ATSBuildDate.
    '''

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__verbose = verbose
        self.__build_date = None

    @property
    def build_date(self):
        '''
            Property method for getting ATS build date.

            :return: ATS build date | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.__build_date

    @build_date.setter
    def build_date(self, build_date):
        '''
            Property method for setting ATS build date.

            :param build_date: ATS build date.
            :type build_date: <str>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('str:build_date', build_date)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        self.__build_date = build_date
        verbose_message(ATSBuildDate.VERBOSE, self.__verbose, build_date)

    def is_not_none(self):
        '''
            Checking is ATS build date None.

            :return: boolean status, True | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return bool(self.__build_date)

    def __str__(self):
        '''
            Dunder str method for ATSBuildDate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, str(self.__verbose), self.__build_date
        )
