# -*- coding: UTF-8 -*-
# verbose.py
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
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
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


class ATSVerbose(ATSConsoleIO):
    """
        Define class ATSVerbose with attribute(s) and method(s).
        Define verbose message container for console log mechanism.
        It defines:
            attribute:
                VERBOSE - Console text indicator for current process-phase
                __message - Verbose message container
            method:
                __init__ - Initial constructor
                message - Public setter/getter
    """

    VERBOSE = '[ATS_UTILITIES::CONSOLE_IO::VERBOSE]'

    def __init__(self):
        """
            Initial constructor.
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
        cls, func = self.__class__, stack()[0][3]
        if message is None:
            txt = 'Argument: missing message <str> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSBadCallError(msg)
        if not isinstance(message, str):
            txt = 'Argument: expected message <str> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
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
    """
    if verbose:
        func, ver = stack()[0][3], ATSVerbose()
        verbose_path_txt = 'First argument: missing success_path <str> object'
        verbose_path_msg = "{0} {1}".format(func, verbose_path_txt)
        message_txt = 'Second argument: missing message <tuple> object'
        message_msg = "{0} {1}".format(func, message_txt)
        if verbose_path is None:
            raise ATSBadCallError(verbose_path_msg)
        if message is None:
            raise ATSBadCallError(message_msg)
        if not isinstance(verbose_path, str):
            raise ATSTypeError(verbose_path_msg)
        if not isinstance(message, tuple):
            raise ATSTypeError(message_msg)
        ver.message = ' '.join(message)
        msg = "{0} {1}".format(verbose_path, ver.message)
        print(msg)
