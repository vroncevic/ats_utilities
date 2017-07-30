# encoding: utf-8

from os.path import exists
from logging import basicConfig, debug, info, warning, critical, error
from logging import DEBUG, WARNING, CRITICAL, ERROR, INFO

from ats_utilities.error.lookup_error import AppError

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLogger(object):
    """
    Define class ATSLogger with attribute(s) and method(s).
    Logging mechanism for App/Tool/Script.
    It defines:
        attribute:
            VERBOSE - Verbose prefix text
            LOG_MSG_FORMAT - Log message format
            LOG_DATE_FORMAT - Log date format
            __file_name - Log file path
        method:
            __init__ - Initial constructor
            write_log - Write message to log file
            set_log_file - Setting log file
            get_log_file - Getting log file
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = '[ATS_LOGGER]'
    LOG_MSG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    LOG_DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p'

    def __init__(self, logging_file, verbose=False):
        """
        Setting log file path, and default debug log level.
        :param logging_file: Log file path of App/Tool/Script
        :type: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        if verbose:
            msg = ATSLogger.VERBOSE
            print(msg)
        self.__file_name = None
        try:
            path_exists = exists(logging_file)
            if logging_file and path_exists:
                self.set_log_file(logging_file)
                basicConfig(
                    format=ATSLogger.LOG_MSG_FORMAT,
                    datefmt=ATSLogger.LOG_DATE_FORMAT,
                    filename=logging_file,
                    level=DEBUG
                )
            else:
                msg = 'missing tool log file path'
                raise AppError(msg)
        except AppError as e:
            print("Error: ", e)

    def set_log_file(self, logging_file):
        """
        Setting log file.
        :param logging_file: Log file
        :type logging_file: str
        """
        self.__file_name = logging_file

    def get_log_file(self):
        """
        Getting log file.
        :return: Log file
        :rtype: str
        """
        return self.__file_name

    @staticmethod
    def write_log(msg, ctrl):
        """
        Write message to log file.
        :param msg: Log message
        :type: str
        :param ctrl: Control flag (debug, warning, critical, error, info)
        :type: str
        """
        try:
            if ctrl == DEBUG:
                debug(msg)
            elif ctrl == WARNING:
                warning(msg)
            elif ctrl == CRITICAL:
                critical(msg)
            elif ctrl == ERROR:
                error(msg)
            elif ctrl == INFO:
                info(msg)
            else:
                msg = 'not implemented log level'
                raise AppError(msg)
        except AppError as e:
            print("Error: ", e)

    def __str__(self):
        """
        Return human readable string (ATSLogger).
        :return: String representation of ATSLogger
        :rtype: str
        """
        ats_log_file = self.get_log_file()
        return "App/Tool/Script log file {0}".format(ats_log_file)

    def __repr__(self):
        """
        Return unambiguous string (ATSLogger).
        :return: String representation of ATSLogger
        :rtype: str
        """
        ats_log_file = self.get_log_file()
        return "{0}(\'{1}\')".format(type(self).__name__, ats_log_file)
