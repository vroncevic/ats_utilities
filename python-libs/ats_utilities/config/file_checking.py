# -*- coding: utf-8 -*-
# file_checking.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# ats_utilities is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ats_utilities is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from inspect import stack

try:
    from pathlib import Path

    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ##################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class FileChecking(object):
    """
        Define class FileChecking with attribute(s) and method(s).
        Operations with configuration files.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __MODES - Mode file operations
                __file_path_ok - File path exist
                __file_extension_ok - File extension is expected
                __file_mode_ok - Supported file mode
            method:
                __init__ - Initial constructor
                check_file - Check configuration file path
                check_format - Check configuration file format by extension
                check_mode -  Checking operation mode for configuration file
                is_file_ok - final status of configuration file
    """

    __slots__ = (
        'VERBOSE',
        '__MODES',
        '__file_path_ok',
        '__file_extension_ok',
        '__file_mode_ok'
    )
    VERBOSE = 'ATS_UTILITIES::CONFIG::FILE_CHECKING'
    __MODES = ['r', 'w', 'a', 'b', 'x', 't', '+']

    def __init__(self, verbose=False):
        """
            Initial constructor.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(
            FileChecking.VERBOSE, verbose, 'ATS file checking interface'
        )
        self.__file_path_ok = False
        self.__file_extension_ok = False
        self.__file_mode_ok = False

    def check_file(self, file_path, verbose=False):
        """
            Check configuration file path.
            :param file_path: Absolute configuration file path
            :type file_path: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (exist and regular file) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        file_path_txt = 'Argument: expected file_path <str> object'
        file_path_msg = "{0} {1} {2}".format('def', func, file_path_txt)
        if file_path is None or not file_path:
            raise ATSBadCallError(file_path_msg)
        if not isinstance(file_path, str):
            raise ATSTypeError(file_path_msg)
        verbose_message(
            FileChecking.VERBOSE, verbose, 'Checking ATS file', file_path
        )
        configuration_file_path = Path(file_path)
        file_path_exist = configuration_file_path.is_file()
        if not file_path_exist:
            error_message(FileChecking.VERBOSE, 'Check file', file_path)
        if file_path_exist:
            self.__file_path_ok = True
        return True if file_path_exist else False

    def check_format(self, file_path, file_extension, verbose=False):
        """
            Check configuration file format by extension.
            :param file_path: Absolute configuration file path
            :type file_path: <str>
            :param file_extension: File format (file extension)
            :type file_extension: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (correct file format) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        status, func = False, stack()[0][3]
        file_path_txt = 'Argument: expected file_path <str> object'
        file_path_msg = "{0} {1} {2}".format('def', func, file_path_txt)
        file_extension_txt = 'Argument: expected file_extension <str> object'
        file_extension_msg = "{0} {1} {2}".format(
            'def', func, file_extension_txt
        )
        if file_path is None or not file_path:
            raise ATSBadCallError(file_path_msg)
        if not isinstance(file_path, str):
            raise ATSTypeError(file_path_msg)
        if file_extension is None or not file_extension:
            raise ATSBadCallError(file_extension_msg)
        if not isinstance(file_extension, str):
            raise ATSTypeError(file_extension_msg)
        verbose_message(
            FileChecking.VERBOSE, verbose, 'Checking file format', file_path
        )
        extension = Path(file_path).suffix.lower().replace('.', '')
        status = extension == file_extension
        if not status:
            error_message(
                FileChecking.VERBOSE, "{0} [{1}] {2}".format(
                    'Not matched file extension', file_extension, file_path
                )
            )
            self.__file_extension_ok = False
        else:
            self.__file_extension_ok = True
            status = True
        return True if status else False

    def check_mode(self, file_mode, verbose=False):
        """
            Checking operation mode for configuration file.
            :param file_mode: File mode ('r', 'w', 'a', 'b', 'x', 't', '+')
            :type file_mode: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (regular file mode) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        split_mode, func = list(file_mode), stack()[0][3]
        file_mode_txt = 'Argument: expected mode <str> object'
        file_mode_msg = "{0} {1} {2}".format('def', func, file_mode_txt)
        if file_mode is None or not file_mode:
            raise ATSBadCallError(file_mode_msg)
        if not isinstance(file_mode, str):
            raise ATSTypeError(file_mode_msg)
        verbose_message(
            FileChecking.VERBOSE, verbose, 'Checking ATS operation mode'
        )
        for item_mode in split_mode:
            if item_mode not in FileChecking.__MODES:
                error_message(
                    FileChecking.VERBOSE, "{0} [{1}]".format(
                        'Not supported mode', file_mode
                    )
                )
                self.__file_mode_ok = False
                return False
        self.__file_mode_ok = True
        return True

    def is_file_ok(self):
        """
            Return final status of configuration file.
            :return: Boolean value (correct file) True, else False
            :rtype: <bool>
            :exceptions: None
        """
        status = all([
            self.__file_path_ok, self.__file_extension_ok, self.__file_mode_ok
        ])
        return True if status else False

