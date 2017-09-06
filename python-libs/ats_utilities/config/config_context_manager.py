# -*- coding: utf-8 -*-

import sys

try:
    from ats_utilities.config.file_checking import FileChecking
    from ats_utilities.error.ats_value_error import ATSValueError
    from ats_utilities.text.stdout_text import DBG, ERR, RST
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


class ConfigFile(FileChecking):
    """
    Define class ConfigFile with attribute(s) and method(s).
    Configuration context manager.
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
            __file_path - Configuration file name
            __file_mode - File mode
            __file_format - File format
        method:
            __init__ - Initial constructor
            __enter__ - Open file and return object File
            __exit__ - Close file
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = 'CONFIG_FILE'

    def __init__(self, file_path, file_mode, file_format, verbose=False):
        """
        Setting filename and open mode.
        :param file_path: Configuration file name
        :type file_path: <str>
        :param file_mode: Open configuration file in mode
        :type file_mode: <str>
        :param file_format: File format
        :type file_format: <str>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        cls, cout = self.__class__, COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}\n{1}\n{2} [{3}]".format(
            'Setting file path', file_path, 'Setting file mode', file_mode
        )
        COut.print_console_msg(msg, verbose=verbose)
        super(ConfigFile, verbose).__init__()
        check_file = self.check_file(file_path, verbose)
        if check_file:
            self.__file_path = file_path
        else:
            msg = "\n{0} {1}{2}\n{3} {4}\n".format(
                cls.VERBOSE, ERR, 'Check file path', file_path, RST
            )
            raise ATSValueError(msg)
        check_mode = self.check_mode(file_mode, verbose)
        if check_mode:
            self.__file_mode = file_mode
        else:
            msg = "\n{0} {1}{2} [{3}] {4}\n".format(
                cls.VERBOSE, ERR, 'Not supported mode', file_mode, RST
            )
            raise ATSValueError(msg)
        check_format = self.check_format(file_path, file_format, verbose)
        if check_format:
            self.__file_format = file_format
        else:
            msg = "\n{0} {1}{2} [{3}] {4}\n".format(
                cls.VERBOSE, ERR, 'Check file format', file_mode, RST
            )
            raise ATSValueError(msg)

    def __enter__(self):
        """
        Open configuration file in mode.
        :return: File object | None
        :rtype: <file> | <NoneType>
        """
        cls = self.__class__
        try:
            self.__file = open(self.__file_path, self.__file_mode)
        except IOError as e:
            msg = "\n{0} {1}{2}{3}\n".format(cls.VERBOSE, ERR, e, RST)
            COut.print_console_msg(msg, error=True)
            self.__file = None
        return self.__file

    def __exit__(self, *args):
        """
        Closing configuration file.
        """
        try:
            self.__file.close()
        except AttributeError:
            pass

    def __str__(self):
        """
        Return human readable string (ConfigFile).
        :return: String representation of ConfigFile
        :rtype: <str>
        """
        return "File {0}".format(self.__file_path)

    def __repr__(self):
        """
        Return unambiguous string (ConfigFile).
        :return: String representation of ConfigFile
        :rtype: <str>
        """
        return "{0}(\'{1}\', \'{2}\', \'{3}\')".format(
            type(self).__name__, self.__file_path,
            self.__file_mode, self.__file_format
        )
