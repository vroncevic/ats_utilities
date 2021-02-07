# -*- coding: UTF-8 -*-

"""
 Module
     success.py
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
     Define class ATSSuccess with attribute(s) and method(s).
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
__version__ = '1.2.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSSuccess(ATSConsoleIO):
    """
        Define class ATSSuccess with attribute(s) and method(s).
        Define verbose message container for console log mechanism.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __checker - ATS checker for parameters
                | __message - Success message container
            :methods:
                | __init__ - Initial constructor
                | message - Public setter/getter
    """

    __slots__ = ('VERBOSE', '__message', '__checker')
    VERBOSE = 'ATS_UTILITIES::CONSOLE_IO::SUCCESS'

    def __init__(self):
        """
            Initial constructor.

            :exceptions: None
        """
        self.__checker = ATSChecker()
        self.__message = ""

    @property
    def message(self):
        """
            Public property getter.

            :return: Formatted verbose message
            :rtype: <str>
            :exceptions: None
        """
        return self.__message

    @message.setter
    def message(self, message):
        """
            Public property setter.

            :param message: Verbose message
            :type message: <str>
            :exceptions: ATSTypeError | ATSBadCallError
        """
        error, status = self.__checker.check_params([('str:message', message)])
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        init(autoreset=False)
        self.__message = "{0}{1}{2}".format(Fore.GREEN, message, Fore.RESET)


def success_message(success_path, *message):
    """
        Show success message.

        :param success_path: Success prefix message
        :type success_path: <str>
        :param message: Message parts
        :type message: <tuple>
        :exceptions: ATSTypeError | ATSBadCallError
    """
    checker = ATSChecker()
    error, status = checker.check_params(
        [('str:success_path', success_path), ('tuple:message', message)]
    )
    if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
    if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
    message, success = tuple([str(item) for item in message]), ATSSuccess()
    success.message = ' '.join(message)
    success_message_log = "[{0}] {1}".format(success_path, success.message)
    print(success_message_log)
