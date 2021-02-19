# -*- coding: UTF-8 -*-

"""
 Module
     verbose.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define class ATSVerbose with attribute(s) and method(s).
     Define verbose message container for console log mechanism.
"""

import sys

try:
    from colorama import init, Fore
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io import ATSConsoleIO
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error_message:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSVerbose(ATSConsoleIO):
    """
        Define class ATSVerbose with attribute(s) and method(s).
        Define verbose message container for console log mechanism.
        It defines:

            :attributes:
                | __message - Verbose message container.
            :methods:
                | __init__ - Initial constructor.
                | message - Property methods for set/get operations.
    """

    def __init__(self):
        """
            Initial constructor.

            :exceptions: None
        """
        self.__message = ""

    @property
    def message(self):
        """
            Property method for getting message.

            :return: Formatted verbose message.
            :rtype: <str>
        """
        return self.__message

    @message.setter
    def message(self, message):
        """
            Property method for setting message.

            :param message: Verbose message.
            :type message: <str>
            :exceptions: None
        """
        self.__message = "{0}{1}{2}".format(
            Fore.BLUE, message, Fore.RESET
        )


def verbose_message(verbose_path, verbose=False, *message):
    """
        Show verbose message.

        :param verbose_path: Verbose prefix message.
        :type verbose_path: <str>
        :param verbose: Enable/disable verbose option.
        :type verbose: <bool>
        :param message: Message parts.
        :type message: <tuple>
        :exceptions: ATSTypeError | ATSBadCallError
    """
    if verbose:
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params(
            [('str:verbose_path', verbose_path), ('tuple:message', message)]
        )
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        message, ver = tuple([str(item) for item in message]), ATSVerbose()
        ver.message = ' '.join(message)
        verbose_message_log = "[{0}] {1}".format(
            verbose_path.lower(), ver.message
        )
        print(verbose_message_log)
