# -*- coding: UTF-8 -*-
# ats_logger_file.py
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


class ATSLoggerFile(object):
    """
    Define class ATSLoggerFile with attribute(s) and method(s).
    Logging mechanism for App/Tool/Script.
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
            __log_file - Log file path
        method:
            __init__ - Initial constructor
            set_log_file - Setting log file path
            get_log_file - Getting log file path
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = 'ATS_LOGGER_FILE'

    def __init__(self, logger_file=None, verbose=False):
        """
        Initial constructor.
        :param logger_file: Log file path
        :type logger_file: <str>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        cls, cout = self.__class__, COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}".format('Initial logger status')
        COut.print_console_msg(msg, verbose=verbose)
        self.__log_file = logger_file

    def set_log_file(self, log_file_path, verbose=False):
        """
        Setting log file path.
        :param log_file_path: Log file path
        :type log_file_path: <str>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        msg = "{0}".format('Setting log file path')
        COut.print_console_msg(msg, verbose=verbose)
        self.__log_file = log_file_path

    def get_log_file(self, verbose=False):
        """
        Getting log file path.
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: Log file path
        :rtype: <str>
        """
        msg = "{0} {1}".format('Getting log file path', self.__log_file)
        COut.print_console_msg(msg, verbose=verbose)
        return self.__log_file

    def __str__(self):
        """
        Return human readable string (ATSLoggerFile).
        :return: String representation of ATSLoggerFile
        :rtype: <str>
        """
        return "{0} Logger file {1}".format(ATS, self.__log_file)

    def __repr__(self):
        """
        Return unambiguous string (ATSLoggerFile).
        :return: String representation of ATSLoggerFile
        :rtype: <str>
        """
        return "{0}(\'{1}\')".format(type(self).__name__, self.__log_file)
