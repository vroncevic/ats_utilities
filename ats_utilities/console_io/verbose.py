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
from inspect import stack

try:
    from colorama import init, Fore

    from ats_utilities.console_io import ATSConsoleIO
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSVerbose(ATSConsoleIO):
    """
        Define class ATSVerbose with attribute(s) and method(s).
        Define verbose message container for console log mechanism.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __message - Verbose message container
            :methods:
                | __init__ - Initial constructor
                | message - Public setter/getter
    """

    __slots__ = ('VERBOSE', '__message')
    VERBOSE = 'ATS_UTILITIES::CONSOLE_IO::VERBOSE'

    def __init__(self):
        """
            Initial constructor.

            :exceptions: None
        """
        self.__message = ""

    @property
    def message(self):
        """
            Public property getter.

            :return: Formatted verbose message
            :rtype: <str>
        """
        return self.__message

    @message.setter
    def message(self, message):
        """
            Public property setter.

            :param message: Verbose message
            :type message: <str>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        txt = 'Argument: expected message <str> object'
        msg = "{0} {1} {2}".format('def', func, txt)
        if message is None or not message:
            raise ATSBadCallError(msg)
        if not isinstance(message, str):
            raise ATSTypeError(msg)
        init(autoreset=False)
        self.__message = "{0}{1}{2}".format(Fore.BLUE, message, Fore.RESET)


def verbose_message(verbose_path, verbose=False, *message):
    """
        Show verbose message.

        :param verbose_path: Verbose prefix message
        :type verbose_path: <str>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :param message: Message parts
        :type message: <tuple>
        :exceptions: ATSBadCallError | ATSTypeError
    """
    if verbose:
        func, ver = stack()[0][3], ATSVerbose()
        verbose_path_txt = 'First argument: missing success_path <str> object'
        verbose_path_msg = "{0} {1} {2}".format('def', func, verbose_path_txt)
        message_txt = 'Second argument: missing message <tuple> object'
        message_msg = "{0} {1} {2}".format('def', func, message_txt)
        if verbose_path is None or not verbose_path:
            raise ATSBadCallError(verbose_path_msg)
        if message is None or not message:
            raise ATSBadCallError(message_msg)
        if not isinstance(verbose_path, str):
            raise ATSTypeError(verbose_path_msg)
        if not isinstance(message, tuple):
            raise ATSTypeError(message_msg)
        message = tuple([str(item) for item in message])
        ver.message = ' '.join(message)
        verbose_message_log = "[{0}] {1}".format(verbose_path, ver.message)
        print(verbose_message_log)
