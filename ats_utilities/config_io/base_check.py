# -*- coding: utf-8 -*-

"""
 Module
     base_check.py
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
     Define class FileChecking with attribute(s) and method(s).
     Check operations with configuration files.
"""

import sys

try:
    from pathlib import Path
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
except ImportError as error_message:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.2.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class FileChecking(object):
    """
        Define class FileChecking with attribute(s) and method(s).
        Check operations with configuration files.
        It defines:

            :attributes:
                | VERBOSE - Console text indicator for current process-phase.
                | MODES - Mode file operations.
                | file_path_ok - File exist, path ok.
                | file_mode_ok - Supported file mode.
                | file_format_ok - File format is (not) expected.
            :methods:
                | __init__ - Initial constructor.
                | check_path - Check configuration file path.
                | check_mode -  Check operation mode for configuration file.
                | check_format - Check configuration file format by extension.
                | is_file_ok - Status of configuration file.
    """

    VERBOSE = 'ATS_UTILITIES::CONFIG_IO::FILE_CHECKING'
    MODES = ['r', 'w', 'a', 'b', 'x', 't', '+']

    def __init__(self, verbose=False):
        """
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(
            FileChecking.VERBOSE, verbose, 'ATS init check file.'
        )
        self.file_path_ok = False
        self.file_mode_ok = False
        self.file_format_ok = False

    def check_path(self, file_path, verbose=False):
        """
            Check configuration file path.

            :param file_path: Configuration file path.
            :type file_path: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(
            FileChecking.VERBOSE, verbose, 'ATS Check file path', file_path
        )
        if not Path(file_path).is_file():
            error_message(FileChecking.VERBOSE, 'Check file', file_path)
        else:
            self.file_path_ok = True

    def check_mode(self, file_mode, verbose=False):
        """
            Check operation mode for configuration file.

            :param file_mode: File mode ('r', 'w', 'a', 'b', 'x', 't', '+').
            :type file_mode: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: True (regular file mode) | False.
            :rtype: <bool>
            :exceptions: None
        """
        verbose_message(
            FileChecking.VERBOSE, verbose, 'Check ATS operation mode'
        )
        modes, mode_checks = list(file_mode), []
        for mode in modes:
            if mode not in FileChecking.MODES:
                mode_checks.append(False)
            else:
                mode_checks.append(True)
        if all(mode_checks):
            self.file_mode_ok = True
            verbose_message(
                FileChecking.VERBOSE, verbose, 'Supported mode', file_mode
            )
        else:
            self.file_mode_ok = False
            error_message(
                FileChecking.VERBOSE, "{0} [{1}]".format(
                    'Not supported mode', file_mode
                )
            )

    def check_format(self, file_path, file_format, verbose=False):
        """
            Check configuration file format by extension.

            :param file_path: Absolute configuration file path.
            :type file_path: <str>
            :param file_format: File format (file extension).
            :type file_format: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(
            FileChecking.VERBOSE, verbose, 'ATS Check file format', file_path
        )
        extension = Path(file_path).suffix.lower().replace('.', '')
        status = extension == file_format
        if not status:
            error_message(
                FileChecking.VERBOSE, "{0} [{1}] {2}".format(
                    'Not matched file extension', file_format, file_path
                )
            )
            self.file_format_ok = False
        else:
            self.file_format_ok = True

    def is_file_ok(self):
        """
            Status of configuration file.

            :return: True (correct file), else False.
            :rtype: <bool>
            :exceptions: None
        """
        return all([self.file_path_ok, self.file_mode_ok, self.file_format_ok])
