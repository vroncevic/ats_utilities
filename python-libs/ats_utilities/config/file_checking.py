# -*- coding: utf-8 -*-

import sys
from os.path import exists, isfile, splitext

try:
    from ats_utilities.error.ats_file_error import ATSFileError
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


class FileChecking(object):
    """
    Define class FileChecking with attribute(s) and method(s).
    File can contain config in next formats:
        XML  -  Configuration described by Extensible Markup Language.
        INI  -  Configuration described by basic structure composed of
                sections, properties, and values.
        CFG  -  Configuration described by keys and values.
        YAML -  Configuration described by basic structure composed of
                sections, properties, and values.
        JSON -  Configuration described by basic structure composed of
                sections, properties, and values.
    It defines:
        attribute:
            __MODES - Mode options
            VERBOSE - Verbose prefix console text
        method:
            check_file - Check configuration file path
            check_format - Check configuration file format by extension
            check_mode -  Checking operation mode for configuration file
    """

    __MODES = ['r', 'w', 'a', 'b', 'x', 't', '+']
    VERBOSE = 'FILE_CONFIG'

    @classmethod
    def check_file(cls, file_path, verbose=False):
        """
        Check config file path.
        :param file_path: Absolute config file path
        :type file_path: <str>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: True (exist and regular) | False
        :rtype: <bool>
        """
        file_path_exist, file_path_regular, cout = False, False, COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}\n{1}".format('Checking configuration file', file_path)
        COut.print_console_msg(msg, verbose=verbose)
        try:
            file_path_exist = exists(file_path)
            file_path_regular = isfile(file_path)
            if not file_path_exist:
                msg = "\n{0} {1}{2}\n{3}{4}\n".format(
                    cls.VERBOSE, ERR, 'File does not exist', file_path, RST
                )
                raise ATSFileError(msg)
            elif not file_path_regular:
                msg = "\n{0} {1}{2}\n{3}{4}\n".format(
                    cls.VERBOSE, ERR, 'File is not regular', file_path, RST
                )
                raise ATSFileError(msg)
        except ATSFileError as e:
            print(e)
        return True if file_path_exist and file_path_regular else False

    @classmethod
    def check_format(cls, file_path, file_extension, verbose=False):
        """
        Check config file format by extension.
        :param file_path: Absolute config file path
        :type file_path: <str>
        :param file_extension: File format (file extension)
        :type file_extension: <str>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: True (correct format) | False
        :rtype: <bool>
        """
        status, cout = False, COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}\n{1}".format('Checking file extension', file_path)
        COut.print_console_msg(msg, verbose=verbose)
        try:
            ext = splitext(file_path)[-1].lower()
            status = ext == file_extension
            if not status:
                msg = "\n{0} {1}{2} [{3}]\n{4}{5}\n".format(
                    cls.VERBOSE, ERR, 'Not matched file extension',
                    file_extension, file_path, RST
                )
                raise ATSFileError(msg)
        except ATSFileError as e:
            print(e)
        return True if status else False

    @classmethod
    def check_mode(cls, mode, verbose=False):
        """
        Checking operation mode for configuration file.
        :param mode: File mode
        :type mode: <str>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: True (regular mode) | False
        :rtype: <bool>
        """
        cout, split_mode, status = COut(), list(mode), False
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}".format('Checking operation mode')
        COut.print_console_msg(msg, verbose=verbose)
        try:
            for item_mode in split_mode:
                if item_mode not in cls.__MODES:
                    msg = "\n{0} {1}{2} [{3}]{4}\n".format(
                        cls.VERBOSE, ERR, 'Not supported mode', mode, RST
                    )
                    raise ATSValueError(msg)
        except ATSValueError as e:
            print(e)
        else:
            msg = "{0}".format('Operation mode supported')
            COut.print_console_msg(msg, verbose=verbose)
            status = True
        return True if status else False
