# -*- coding: UTF-8 -*-

"""
 Module
     config_context_manager.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
     ats_utilities is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     ats_utilities is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class GenAVR8 with attribute(s) and method(s).
     Load a settings, create an interface and run operation(s).
"""

import sys
from inspect import stack

try:
    from ats_utilities.config.file_checking import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE) # Force close python ATS ###############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
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
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __file_path - Configuration file name
                __file_mode - File mode
                __file_format - File format
                __file - File object
            method:
                __init__ - Initial constructor
                __enter__ - Open file and return object File
                __exit__ - Close file
    """

    __slots__ = (
        'VERBOSE',
        '__file_path',
        '__file_mode',
        '__file_format',
        '__file'
    )
    VERBOSE = 'ATS_UTILITIES::CONFIG::CONFIG_FILE'

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
            :exceptions: ATSBadCallError | ATSTypeError
        """
        status, func = False, stack()[0][3]
        file_path_txt = 'Argument: expected file_path <str> object'
        file_path_msg = "{0} {1} {2}".format('def', func, file_path_txt)
        file_mode_txt = 'Argument: expected file_mode <str> object'
        file_mode_msg = "{0} {1} {2}".format('def', func, file_mode_txt)
        file_format_txt = 'Argument: expected file_format <str> object'
        file_format_msg = "{0} {1} {2}".format('def', func, file_format_txt)
        if file_path is None or not file_path:
            raise ATSBadCallError(file_path_msg)
        if not isinstance(file_path, str):
            raise ATSTypeError(file_path_msg)
        if file_mode is None or not file_mode:
            raise ATSBadCallError(file_mode_msg)
        if not isinstance(file_mode, str):
            raise ATSTypeError(file_mode_msg)
        if file_format is None or not file_format:
            raise ATSBadCallError(file_format_msg)
        if not isinstance(file_format, str):
            raise ATSTypeError(file_format_msg)
        verbose_message(
            ConfigFile.VERBOSE, verbose, "{0}\n{1}\n{2} [{3}]".format(
                'Setting file path', file_path, 'Setting file mode', file_mode
            )
        )
        FileChecking.__init__(self)
        check_file = self.check_file(file_path=file_path, verbose=verbose)
        check_mode = self.check_mode(file_mode=file_mode, verbose=verbose)
        check_format = self.check_format(
            file_path=file_path, file_extension=file_format, verbose=verbose
        )
        if all([check_file, check_mode, check_format]):
            self.__file_path = file_path
            self.__file_mode = file_mode
            self.__file_format = file_format
        else:
            self.__file_path = None
            self.__file_mode = None
            self.__file_format = None

    def __enter__(self):
        """
            Open configuration file in mode.
            :return: File object | None
            :rtype: <file> | <NoneType>
            :exceptions: None
        """
        if self.is_file_ok():
            self.__file = open(self.__file_path, self.__file_mode)
        else:
            error_message(ConfigFile.VERBOSE, 'Check file', self.__file_path)
            self.__file = None
        return self.__file

    def __exit__(self, *args):
        """
            Closing configuration file.
            :exceptions: None
        """
        try:
            self.__file.close()
        except AttributeError:
            pass
