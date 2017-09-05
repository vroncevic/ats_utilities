# -*- coding: utf-8 -*-

import sys

try:
    from ats_utilities.text.stdout_text import ATS, DBG, RST
    from ats_utilities.text import COut
except ImportError as e:
    msg = "\n{0}\n".format(e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLoggerStatus(object):
    """
    Define class ATSLoggerStatus with attribute(s) and method(s).
    Logging mechanism for App/Tool/Script.
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
            __log_status - Logger operative (enabled/disabled)
        method:
            __init__ - Initial constructor
            set_logger_status - Setting logger status
            get_logger_status - Getting logger status
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = 'ATS_LOGGER_STATUS'

    def __init__(self, log_status=False, verbose=False):
        """
        Initial constructor.
        :param log_status: Logger status
        :type log_status: <bool>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        cls, cout = self.__class__, COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}".format('Initial logger status')
        COut.print_console_msg(msg, verbose=verbose)
        self.__log_status = log_status

    def set_logger_status(self, status, verbose=False):
        """
        Setting logger status.
        :param status: Logger status (enable/disable logging mechanism)
        :type status: <bool>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        msg = "{0}".format('Setting logger status')
        COut.print_console_msg(msg, verbose=verbose)
        self.__log_status = status

    def get_logger_status(self, verbose=False):
        """
        Getting logger status.
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: True (logger operative) | False
        :rtype: <bool>
        """
        msg = "{0}".format('Getting logger status')
        COut.print_console_msg(msg, verbose=verbose)
        return self.__log_status

    def __str__(self):
        """
        Return human readable string (ATSLoggerStatus).
        :return: String representation of ATSLoggerStatus
        :rtype: <str>
        """
        return "{0} Logger status {1}".format(ATS, self.__log_status)

    def __repr__(self):
        """
        Return unambiguous string (ATSLoggerStatus).
        :return: String representation of ATSLoggerStatus
        :rtype: <str>
        """
        return "{0}(\'{1}\')".format(type(self).__name__, self.__log_status)
