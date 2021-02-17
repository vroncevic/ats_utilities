# -*- coding: UTF-8 -*-

"""
 Module
     warning.py
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
     Define class ATSWarning with attribute(s) and method(s).
     Define warning message container for console log mechanism.
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
__version__ = '1.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSWarning(ATSConsoleIO):
    """
        Define class ATSWarning with attribute(s) and method(s).
        Define warning message container for console log mechanism.
        It defines:

            :attributes:
                | __message - Warning message container.
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

            :return: Formatted warning message.
            :rtype: <str>
            :exceptions: None
        """
        return self.__message

    @message.setter
    def message(self, message):
        """
            Property method for setting message.

            :param message: Warning message.
            :type message: <str>
            :exceptions: None
        """
        init(autoreset=False)
        self.__message = "{0}{1}{2}".format(
            Fore.YELLOW, message, Fore.RESET
        )


def warning_message(warning_path, *message):
    """
        Show warning message.

        :param warning_path: Warning prefix message.
        :type warning_path: <str>
        :param message: Message parts.
        :type message: <tuple>
        :exceptions: ATSTypeError | ATSBadCallError
    """
    checker, error, status = ATSChecker(), None, False
    error, status = checker.check_params(
        [('str:warning_path', warning_path), ('tuple:message', message)]
    )
    if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
    if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
    message, warning = tuple([str(item) for item in message]), ATSWarning()
    warning.message = ' '.join(message)
    warning_message_log = "[{0}] {1}".format(
        warning_path.lower(), warning.message
    )
    print(warning_message_log)
