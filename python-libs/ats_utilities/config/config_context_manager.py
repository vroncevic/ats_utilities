# encoding: utf-8

from ats_utilities.error.ats_value_error import ATSValueError
from ats_utilities.config.file_checking import FileChecking
from ats_utilities.text.stdout_text import DBG, ERR, RST

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ConfigFile(object):
    """
    Define class ConfigFile with attribute(s) and method(s).
    
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
            __file_path - Configuration file name
            __mode - File mode
        method:
            __init__ - Initial constructor
            __enter__ - Open file and return object File
            __exit__ - Close file
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = '[CONTEXT_MANAGER]'

    def __init__(self, file_path, mode, verbose=False):
        """
        Setting filename and open mode.
        :param file_path: Configuration file name
        :type file_path: str
        :param mode: Open configuration file in mode
        :type mode: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2}\n{3}\n{4} [{5}]{6}".format(
                cls.VERBOSE, DBG, 'Setting file path', file_path,
                'Setting file mode', mode, RST
            )
            print(msg)
        self.__file_path = file_path
        check_mode = FileChecking.check_mode(mode, verbose)
        if check_mode:
            self.__mode = mode
        else:
            msg = "{0} {1}{2} [{3}] {4}".format(
                cls.VERBOSE, ERR, 'Not supported mode', mode, RST
            )
            raise ATSValueError(msg)

    def __enter__(self):
        """
        Open configuration file in mode.
        :return: File object
        :rtype: file
        """
        self.__file = open(self.__file_path, self.__mode)
        return self.__file

    def __exit__(self):
        """
        Closing configuration file.
        """
        self.__file.close()

    def __str__(self):
        """
        Return human readable string (ConfigFile).
        :return: String representation of ConfigFile
        :rtype: str
        """
        return 'File {0}'.format(self.__file_path)

    def __repr__(self):
        """
        Return unambiguous string (ConfigFile).
        :return: String representation of ConfigFile
        :rtype: str
        """
        return '{0}(\'{1}\', \'{2}\')'.format(
            type(self).__name__, self.__file_path, self.__mode
        )
