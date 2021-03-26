# -*- coding: UTF-8 -*-

'''
 Module
     verbose.py
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
     Defined class ATSVerbose with attribute(s) and method(s).
     Created verbose message container for console log mechanism.
'''

import sys

try:
    from colorama import init, Fore
    from ats_utilities.final import ATSFinal
    from ats_utilities.checker import ATSChecker
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/master/LICENSE'
__version__ = '1.6.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSVerbose(object):
    '''
        Defined class ATSVerbose with attribute(s) and method(s).
        Created verbose message container for console log mechanism.
        It defines:

            :attributes:
                | __metaclass__ - Setting class ATSVerbose as final.
                | __message - Verbose message container.
            :methods:
                | __init__ - Initial constructor.
                | message - Property methods for set/get operations.
                | is_not_none - Checking is message None or not.
                | __str__ - Dunder method for ATSVerbose.
    '''

    __metaclass__ = ATSFinal

    def __init__(self):
        '''
            Initial constructor.

            :exceptions: None
        '''
        self.__message = None

    @property
    def message(self):
        '''
            Property method for getting message.

            :return: Formatted verbose message.
            :rtype: <str>
        '''
        return self.__message

    @message.setter
    def message(self, message):
        '''
            Property method for setting message.

            :param message: Verbose message.
            :type message: <str>
            :exceptions: None
        '''
        self.__message = '{0}{1}{2}'.format(
            Fore.BLUE, message, Fore.RESET
        )

    def is_not_none(self):
        '''
            Checking is message None or not.

            :return: True | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return True if self.__message is not None else False

    def __str__(self):
        '''
            Dunder method for ATSVerbose.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, self.__message
        )


def verbose_message(verbose_path, verbose=False, *message):
    '''
        Show verbose message.

        :param verbose_path: Verbose prefix message.
        :type verbose_path: <str>
        :param verbose: Enable/disable verbose option.
        :type verbose: <bool>
        :param message: Message parts.
        :type message: <tuple>
        :exceptions: ATSTypeError | ATSBadCallError
    '''
    if verbose:
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params(
            [('str:verbose_path', verbose_path), ('tuple:message', message)]
        )
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        message, ver = tuple([str(item) for item in message]), ATSVerbose()
        ver.message = ' '.join(message)
        verbose_message_log = '[{0}] {1}'.format(
            verbose_path.lower(), ver.message
        )
        print(verbose_message_log)
