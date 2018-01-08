# -*- coding: UTF-8 -*-
# ats_logger_name.py
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

try:
    from ats_utilities.text.stdout_text import ATS, DBG, RST
    from ats_utilities.text import COut
except ImportError as e:
    msg = "\n{0}\n".format(e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLoggerName(object):
    """
    Define class ATSLoggerName with attribute(s) and method(s).
    Logging mechanism for App/Tool/Script.
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
            __logger_name - Logger name
        method:
            __init__ - Initial constructor
            set_logger_name - Setting logger name
            get_logger_name - Getting logger name
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = 'ATS_LOGGER_NAME'

    def __init__(self, logger_name=None, verbose=False):
        """
        Initial constructor.
        :param logger_name: Logger name
        :type logger_name: <str>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        cls, cout = self.__class__, COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}".format('Initial logger name')
        COut.print_console_msg(msg, verbose=verbose)
        self.__logger_name = logger_name

    def set_logger_name(self, logger_name, verbose=False):
        """
        Setting logger name.
        :param logger_name: Logger name
        :type logger_name: <str>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        msg = "{0}".format('Setting logger name')
        COut.print_console_msg(msg, verbose=verbose)
        self.__logger_name = logger_name

    def get_logger_name(self, verbose=False):
        """
        Getting logger name.
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: Logger name
        :rtype: <str>
        """
        msg = "{0} {1}".format('Getting logger name', self.__logger_name)
        COut.print_console_msg(msg, verbose=verbose)
        return self.__logger_name

    def __str__(self):
        """
        Return human readable string (ATSLoggerName).
        :return: String representation of ATSLoggerName
        :rtype: <str>
        """
        return "{0} Logger name {1}".format(ATS, self.__logger_name)

    def __repr__(self):
        """
        Return unambiguous string (ATSLoggerName).
        :return: String representation of ATSLoggerName
        :rtype: <str>
        """
        return "{0}(\'{1}\')".format(type(self).__name__, self.__logger_name)
