# encoding: utf-8

from os.path import exists
from logging import (
    getLogger, basicConfig, DEBUG, WARNING, CRITICAL, ERROR, INFO
)

from ats_utilities.error.ats_value_error import ATSValueError
from ats_utilities.error.ats_file_error import ATSFileError

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
            __logger - Object logger
            __log_file - Log file path
        method:
            __init__ - Initial constructor
            set_ats_logger - Setting logger object
            get_ats_logger - Getting logger object
            write_log - Write message to log file
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = '[ATS_LOGGER]'
    LOG_MSG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    LOG_DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p'
    ATS_DEBUG, ATS_WARNING, ATS_CRITICAL, ATS_ERROR, ATS_INFO = (
        DEBUG, WARNING, CRITICAL, ERROR, INFO
    )

    def __init__(self, ats_name, ats_log_file, verbose=False):
        """
        Setting log file path, and default debug log level.
        :param ats_name: App/Tool/Script name
        :type ats_name: str
        :param ats_log_file: Log file path of App/Tool/Script
        :type ats_log_file: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        if verbose:
            msg = ATSLogger.VERBOSE
            print(msg)
        self.__logger = None
        self.__log_file = None
        try:
            path_exists = exists(ats_log_file)
            if ats_log_file and path_exists:
                self.__log_file = ats_log_file
                basicConfig(
                    format=ATSLogger.LOG_MSG_FORMAT,
                    datefmt=ATSLogger.LOG_DATE_FORMAT,
                    filename=ats_log_file,
                    level=DEBUG
                )
                self.__logger = getLogger(ats_name)
            else:
                msg = "{0} {1} \n{2}".format(
                    ATSLogger.VERBOSE,
                    'missing tool log file path',
                    ats_log_file
                )
                raise ATSFileError(msg)
        except ATSFileError as e:
            print(e)

    def set_ats_logger(self, logger):
        """
        Setting logger object.
        :param logger: Logger object
        :type logger: Object logging.Logger
        """
        self.__logger = logger

    def get_ats_logger(self):
        """
        Getting logger object.
        :return: Logger object
        :rtype: Object logging.Logger
        """
        return self.__logger

    def write_log(self, msg, ctrl):
        """
        Write message to log file.
        :param msg: Log message
        :type: str
        :param ctrl: Control flag (debug, warning, critical, error, info)
        :type: int
        """
        try:
            if ctrl == ATSLogger.ATS_DEBUG:
                self.__logger.debug(msg)
            elif ctrl == ATSLogger.ATS_WARNING:
                self.__logger.warning(msg)
            elif ctrl == ATSLogger.ATS_CRITICAL:
                self.__logger.critical(msg)
            elif ctrl == ATSLogger.ATS_ERROR:
                self.__logger.error(msg)
            elif ctrl == ATSLogger.ATS_INFO:
                self.__logger.info(msg)
            else:
                msg = "{0} [{1}]".format(
                    ATSLogger.VERBOSE, 'not implemented log level', ctrl
                )
                raise ATSValueError(msg)
        except ATSValueError as e:
            print(e)

    def __str__(self):
        """
        Return human readable string (ATSLogger).
        :return: String representation of ATSLogger
        :rtype: str
        """
        return "App/Tool/Script log file {0}".format(self.__log_file)

    def __repr__(self):
        """
        Return unambiguous string (ATSLogger).
        :return: String representation of ATSLogger
        :rtype: str
        """
        return "{0}(\'{1}\')".format(type(self).__name__, self.__log_file)
