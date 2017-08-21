# encoding: utf-8

from abc import ABCMeta, abstractmethod

from ats_utilities.text.stdout_text import DBG, RST

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSBaseLogger(object):
    """
    Define class ATSBaseLogger with attribute(s) and method(s).
    Base container for logging mechanism.
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
            __logger - Object logger
            __log_file - Log file path
            __name - Logger name
        method:
            __init__ - Initial constructor
            set_logger - Setting logger object
            get_logger - Getting logger object
            set_log_file - Setting log file path
            get_log_file - Getting log file path
            set_logger_name - Setting logger name
            get_logger_name - Getting logger name
            write_log - Write message to log file (Abstract method)
    """

    __metaclass__ = ABCMeta
    VERBOSE = '[ATS_BASE_LOGGER]'

    def __init__(self, verbose=False):
        """
        Initial constructor.
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2}{3}".format(
                cls.VERBOSE, DBG, 'Initial base logger', RST
            )
            print(msg)
        self.__logger = None
        self.__log_file = None
        self.__name = None

    def set_logger(self, logger, verbose=False):
        """
        Setting logger object.
        :param logger: Logger object
        :type logger: Object logging.Logger
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2}{3}".format(
                cls.VERBOSE, DBG, 'Setting logger object', RST
            )
            print(msg)
        self.__logger = logger

    def get_logger(self, verbose=False):
        """
        Getting logger object.
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return: Logger object
        :rtype: Object logging.Logger
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2}{3}".format(
                cls.VERBOSE, DBG, 'Getting logger object', RST
            )
            print(msg)
        return self.__logger

    def set_log_file(self, log_file_path, verbose=False):
        """
        Setting log file path.
        :param log_file_path: Log file path
        :type log_file_path: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2}{3}".format(
                cls.VERBOSE, DBG, 'Setting log file path', RST
            )
            print(msg)
        self.__log_file = log_file_path

    def get_log_file(self, verbose=False):
        """
        Getting log file path.
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return: Log file path
        :rtype: str
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2}{3}".format(
                cls.VERBOSE, DBG, 'Getting log file path', RST
            )
            print(msg)
        return self.__log_file

    def set_logger_name(self, logger_name, verbose=False):
        """
        Setting logger name.
        :param logger_name:
        :type logger_name:
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return:
        :rtype:
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2}{3}".format(
                cls.VERBOSE, DBG, 'Getting logger object', RST
            )
            print(msg)
        self.__name = logger_name

    def get_logger_name(self, verbose=False):
        """
        Getting logger name.
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return:
        :rtype:
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2}{3}".format(
                cls.VERBOSE, DBG, 'Getting logger object', RST
            )
            print(msg)
        return self.__name

    @abstractmethod
    def write_log(self, msg, ctrl, verbose=False):
        """
        Write message to log file (Abstract method).
        :param msg: Log message
        :type: str
        :param ctrl: Control flag (debug, warning, critical, error, info)
        :type: int
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return: True (success) | False
        :rtype: bool
        """
        pass
