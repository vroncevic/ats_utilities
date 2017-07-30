# encoding: utf-8

from abc import ABCMeta, abstractmethod

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class BaseWriteConfig(object):
    """
    Define class BaseWriteConfig with attribute(s) and method(s).
    Class for write operation.
    It defines:
        attribute:
            VERBOSE - Verbose prefix text
            __file_path - Configuration file path
        method:
            __init__ - Initial constructor
            set_file_path - Setting configuration file path
            get_file_path - Getting configuration file path
            write_configuration - Write configuration to file (Abstract method)
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    __metaclass__ = ABCMeta
    VERBOSE = '[BASE_WRITE_CONFIG]'

    def __init__(self, verbose=False):
        """
        Initial file path.
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        if verbose:
            msg = BaseWriteConfig.VERBOSE + ' Init file path'
            print(msg)
        self.__file_path = None

    def set_file_path(self, file_path):
        """
        Setting configuration file path.
        :param file_path: Configuration file path
        :type file_path: str
        """
        self.__file_path = file_path

    def get_file_path(self):
        """
        Getting configuration file path.
        :return: Configuration file path
        :rtype: str
        """
        return self.__file_path

    @abstractmethod
    def write_configuration(self, configuration, verbose=False):
        """
        Write configuration to file (Abstract method).
        :param configuration: Configuration object
        :type configuration: dict
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        pass

    def __str__(self):
        """
        Return human readable string (BaseWriteConfig).
        :return: String representation of BaseWriteConfig
        :rtype: str
        """
        file_path = self.get_file_path()
        return 'File path {0}'.format(file_path)

    def __repr__(self):
        """
        Return unambiguous string (BaseWriteConfig).
        :return: String representation of BaseWriteConfig
        :rtype: str
        """
        return '{0}()'.format(type(self).__name__)
