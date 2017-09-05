# -*- coding: utf-8 -*-

import sys

try:
    from ats_utilities.error.ats_value_error import ATSValueError
    from ats_utilities.config.file_checking import FileChecking
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


class ConfigFile(object):
    """
    Define class ConfigFile with attribute(s) and method(s).
    Configuration context manager.
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

    VERBOSE = 'CONTEXT_MANAGER'

    def __init__(self, file_path, mode, verbose=False):
        """
        Setting filename and open mode.
        :param file_path: Configuration file name
        :type file_path: <str>
        :param mode: Open configuration file in mode
        :type mode: <str>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        cls, cout = self.__class__, COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}\n{1}\n{2} [{3}]".format(
            'Setting file path', file_path, 'Setting file mode', mode
        )
        COut.print_console_msg(msg, verbose=verbose)
        self.__file_path = file_path
        check_mode = FileChecking.check_mode(mode, verbose)
        if check_mode:
            self.__mode = mode
        else:
            msg = "\n{0} {1}{2} [{3}] {4}\n".format(
                cls.VERBOSE, ERR, 'Not supported mode', mode, RST
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
            self.__file = open(self.__file_path, self.__mode)
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
        return "{0}(\'{1}\', \'{2}\')".format(
            type(self).__name__, self.__file_path, self.__mode
        )
