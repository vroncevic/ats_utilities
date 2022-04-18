# -*- coding: UTF-8 -*-

'''
 Module
     ats_info_ok.py
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
     Defined class ATSInfoOk with attribute(s) and method(s).
     Created API for ATS info status in one property object.
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
class ATSInfoOk:
    '''
        Defined class ATSInfoOk with attribute(s) and method(s).
        Created API for ATS info status in one property object.
        It defines:

            :attributes:
                | __verbose - enable/disable verbose option.
                | __ats_info_ok - ATS information status.
            :methods:
                | __init__ - initial constructor.
                | ats_info_ok - property methods for set/get operations.
                | __str__ - str dunder method for ATSInfoOk.
    '''

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__verbose = verbose
        self.__ats_info_ok = False

    @property
    def ats_info_ok(self):
        '''
            Property method for getting ATS information status.

            :return: boolean status, ATS information status.
            :rtype: <bool>
            :exceptions: None
        '''
        return self.__ats_info_ok

    @ats_info_ok.setter
    def ats_info_ok(self, ats_info_ok):
        '''
            Property method for setting ATS information status.

            :param ats_info_ok: ATS information status.
            :type ats_info_ok: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('bool:ats_info_ok', ats_info_ok)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        self.__ats_info_ok = ats_info_ok
        verbose_message(ATSInfoOk.VERBOSE, self.__verbose, str(ats_info_ok))

    def __str__(self):
        '''
            Dunder str method for ATSInfoOk.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, str(self.__verbose),
            str(self.__ats_info_ok)
        )
