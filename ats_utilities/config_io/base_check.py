# -*- coding: utf-8 -*-

'''
 Module
     base_check.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class FileChecking with attribute(s) and method(s).
     Created API for checking operations with files.
'''

import sys

try:
    from pathlib import Path
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class FileChecking(object):
    '''
        Defined class FileChecking with attribute(s) and method(s).
        Created API for checking operations with files.
        It defines:

            :attributes:
                | VERBOSE - Console text indicator for current process-phase.
                | MODES - Mode file operations.
                | file_path_ok - File exist, path ok.
                | file_mode_ok - Supported file mode.
                | file_format_ok - File format is (not) expected.
            :methods:
                | __init__ - Initial constructor.
                | check_path - Check file path.
                | check_mode -  Check operation mode for file.
                | check_format - Check file format by extension.
                | is_file_ok - Status of file.
                | __str__ - Dunder method for FileChecking.
    '''

    VERBOSE = 'ATS_UTILITIES::CONFIG_IO::FILE_CHECKING'
    MODES = ['r', 'w', 'a', 'b', 'x', 't', '+']

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(FileChecking.VERBOSE, verbose, 'init ATS check file')
        self.file_path_ok = False
        self.file_mode_ok = False
        self.file_format_ok = False

    def check_path(self, file_path, verbose=False):
        '''
            Check file path.

            :param file_path: File path.
            :type file_path: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(
            FileChecking.VERBOSE, verbose, 'check ATS file path', file_path
        )
        if not Path(file_path).is_file():
            error_message(FileChecking.VERBOSE, 'check file', file_path)
        else:
            self.file_path_ok = True

    def check_mode(self, file_mode, verbose=False):
        '''
            Check operation mode for file.

            :param file_mode: File mode ('r', 'w', 'a', 'b', 'x', 't', '+').
            :type file_mode: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: True (regular file mode) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        verbose_message(
            FileChecking.VERBOSE, verbose, 'check ATS operation mode'
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
                FileChecking.VERBOSE, verbose, 'supported mode', file_mode
            )
        else:
            self.file_mode_ok = False
            error_message(
                FileChecking.VERBOSE, '{0} [{1}]'.format(
                    'not supported mode', file_mode
                )
            )

    def check_format(self, file_path, file_format, verbose=False):
        '''
            Check file format by extension.

            :param file_path: File path.
            :type file_path: <str>
            :param file_format: File format (file extension).
            :type file_format: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(
            FileChecking.VERBOSE, verbose, 'check ATS file format', file_path
        )
        extension = Path(file_path).suffix.lower().replace('.', '')
        status = extension == file_format
        if not status:
            error_message(
                FileChecking.VERBOSE, '{0} [{1}] {2}'.format(
                    'not matched file extension', file_format, file_path
                )
            )
            self.file_format_ok = False
        else:
            self.file_format_ok = True

    def is_file_ok(self):
        '''
            Status of file.

            :return: True (correct file), else False.
            :rtype: <bool>
            :exceptions: None
        '''
        return all([self.file_path_ok, self.file_mode_ok, self.file_format_ok])

    def __str__(self):
        '''
            Dunder method for FileChecking.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3})'.format(
            self.__class__.__name__, self.file_path_ok,
            self.file_mode_ok, self.file_format_ok
        )
