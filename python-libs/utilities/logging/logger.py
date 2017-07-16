# encoding: utf-8

from os.path import exists
from logging import basicConfig, debug, info, warning, critical, error
from logging import DEBUG, WARNING, CRITICAL, ERROR, INFO
from utilities.error.lookup_error import AppError

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Logger(object):
    """
    Define class Logger with attribute(s) and method(s).
    Logging mechanism for App/Tool/Script.
    It defines:
        attribute:
            __file_name - Log file path
        method:
            __init__ - Initial constructor
            write_log - Write message to log file
    """

    def __init__(self, logging_file):
        """
        Setting log file path, and default debug log level.
        :param logging_file: Log file path of App/Tool/Script
        :type: str
        """
        try:
            path_exists = exists(logging_file)
            if logging_file and path_exists:
                self.__file_name = logging_file
                basicConfig(
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p",
                    filename=self.__file_name,
                    level=DEBUG
                )
            else:
                msg = 'missing tool log file path'
                raise AppError(msg)
        except AppError as e:
            print("Error: ", e)

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
