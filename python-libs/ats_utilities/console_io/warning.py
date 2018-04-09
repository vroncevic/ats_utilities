# -*- coding: UTF-8 -*-
# warning.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# ats_utilities is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ats_utilities is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from inspect import stack

try:
    from colorama import init, Fore

    from ats_utilities.console_io import ATSConsoleIO
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSWarning(ATSConsoleIO):
    """
        Define class ATSWarning with attribute(s) and method(s).
        Define warning message container for console log mechanism.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __message - Warning message container
            method:
                __init__ - Initial constructor
                message - Public setter/getter
    """

    __slots__ = (
        'VERBOSE',  # Read-Only
        '__message'
    )
    VERBOSE = 'ATS_UTILITIES::CONSOLE_IO::WARNING'

    def __init__(self):
        """
            Initial constructor.
        """
        self.__message = ""

    @property
    def message(self):
        """
            Public property getter.
            :return: Formatted warning message
            :rtype: <str>
        """
        return self.__message

    @message.setter
    def message(self, message):
        """
            Public property setter.
            :param message: Warning message
            :type message: <str>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        cls, func = ATSWarning, stack()[0][3]
        txt = 'Argument: expected message <str> object'
        msg = "{0} {1} {2}".format('def', func, txt)
        if message is None or not message:
            raise ATSBadCallError(msg)
        if not isinstance(message, str):
            raise ATSTypeError(msg)
        init(autoreset=False)
        self.__message = "{0}{1}{2}".format(Fore.YELLOW, message, Fore.RESET)


def warning_message(warning_path, *message):
    """
        Show warning message.
        :param warning_path: Warning prefix message
        :type warning_path: <str>
        :param message: Message parts
        :type message: <tuple>
        :exceptions: ATSBadCallError | ATSTypeError
    """
    func, warning = stack()[0][3], ATSWarning()
    warning_path_txt = 'First argument: missing warning_path <str> object'
    warning_path_msg = "{0} {1} {2}".format('def', func, warning_path_txt)
    message_txt = 'Second argument: missing message <tuple> object'
    message_msg = "{0} {1} {2}".format('def', func, message_txt)
    if warning_path is None or not warning_path:
        raise ATSBadCallError(warning_path_msg)
    if message is None or not message:
        raise ATSBadCallError(message_msg)
    if not isinstance(warning_path, str):
        raise ATSTypeError(warning_path_msg)
    if not isinstance(message, tuple):
        raise ATSTypeError(message_msg)
    message = tuple([str(item) for item in message])
    warning.message = ' '.join(message)
    warning_message_log = "[{0}] {1}".format(warning_path, warning.message)
    print(warning_message_log)
