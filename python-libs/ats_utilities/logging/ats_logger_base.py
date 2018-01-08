# -*- coding: UTF-8 -*-
# ats_logger_base.py
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
from abc import ABCMeta, abstractmethod

try:
    from ats_utilities.logging.ats_logger_status import ATSLoggerStatus
    from ats_utilities.logging.ats_logger_file import ATSLoggerFile
    from ats_utilities.logging.ats_logger_name import ATSLoggerName
    from ats_utilities.text.stdout_text import DBG, RST
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


class ATSLoggerBase(ATSLoggerStatus, ATSLoggerFile, ATSLoggerName):
    """
    Define class ATSLoggerBase with attribute(s) and method(s).
    Base container for logging mechanism.
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
            __logger - Object logger
        method:
            __init__ - Initial constructor
            set_logger - Setting logger object
            get_logger - Getting logger object
            write_log - Write message to log file (Abstract method)
    """

    __metaclass__ = ABCMeta
    VERBOSE = 'ATS_BASE_LOGGER'

    def __init__(self, verbose=False):
        """
        Initial constructor.
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        cls, cout = self.__class__, COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}".format('Initial base logger')
        COut.print_console_msg(msg, verbose=verbose)
        ATSLoggerStatus.__init__(self, False, verbose)
        ATSLoggerFile.__init__(self, None, verbose)
        ATSLoggerName.__init__(self, None, verbose)
        self.__logger = None

    def set_logger(self, logger, verbose=False):
        """
        Setting logger object.
        :param logger: Logger object
        :type logger: <logging.Logger>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        msg = "{0}".format('Setting logger object')
        COut.print_console_msg(msg, verbose=verbose)
        self.__logger = logger

    def get_logger(self, verbose=False):
        """
        Getting logger object.
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: Logger object
        :rtype: <logging.Logger>
        """
        msg = "{0}".format('Getting logger object')
        COut.print_console_msg(msg, verbose=verbose)
        return self.__logger

    @abstractmethod
    def write_log(self, msg, ctrl, verbose=False):
        """
        Write message to log file (Abstract method).
        :param msg: Log message
        :type msg: <str>
        :param ctrl: Control flag (debug, warning, critical, error, info)
        :type ctrl: <int>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: True (success) | False
        :rtype: <bool>
        """
        pass
