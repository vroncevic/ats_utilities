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
from os.path import splitext, isfile

try:
    from six import add_metaclass
    from ats_utilities import VerboseRoot
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.5.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@add_metaclass(VerboseRoot)
class FileChecking:
    '''
        Defined class FileChecking with attribute(s) and method(s).
        Created API for checking operations with files.
        It defines:

            :attributes:
                | MODES - mode file operations.
                | __verbose - enable/disable verbose option.
                | __file_path_ok - file exist, path ok.
                | __file_mode_ok - supported file mode.
                | __file_format_ok - file format is (not) expected.
            :methods:
                | __init__ - initial constructor.
                | check_path - check file path.
                | check_mode -  check operation mode for file.
                | check_format - check file format by extension.
                | is_file_ok - status of file for processing.
                | __str__ - str dunder method for FileChecking.
    '''

    MODES = ['r', 'w', 'a', 'b', 'x', 't', '+']

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__verbose = verbose
        self.__file_path_ok = False
        self.__file_mode_ok = False
        self.__file_format_ok = False
        verbose_message(FileChecking.VERBOSE, verbose, 'init ATS check file')

    def check_path(self, file_path, verbose=False):
        '''
            Check file path.

            :param file_path: file path.
            :type file_path: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        if not isfile(file_path):
            error_message(FileChecking.VERBOSE, 'check file', file_path)
        else:
            self.__file_path_ok = True
        verbose_message(
            FileChecking.VERBOSE, self.__verbose or verbose, file_path
        )

    def check_mode(self, file_mode, verbose=False):
        '''
            Check operation mode for file.

            :param file_mode: file mode ('r', 'w', 'a', 'b', 'x', 't', '+').
            :type file_mode: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: True (regular file mode) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        modes, mode_checks = list(file_mode), []
        for mode in modes:
            if mode not in FileChecking.MODES:
                mode_checks.append(False)
            else:
                mode_checks.append(True)
        if all(mode_checks):
            self.__file_mode_ok = True
            verbose_message(
                FileChecking.VERBOSE, self.__verbose or verbose, file_mode
            )
        else:
            self.__file_mode_ok = False
            error_message(
                FileChecking.VERBOSE, '{0} [{1}]'.format(
                    'not supported mode', file_mode
                )
            )

    def check_format(self, file_path, file_format, verbose=False):
        '''
            Check file format by extension.

            :param file_path: file path.
            :type file_path: <str>
            :param file_format: file format (file extension).
            :type file_format: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        if file_format != 'makefile':
            file_name_path, extension = splitext(file_path)
            extension = extension.replace('.', '')
            if extension == '':
                extension = file_format
        else:
            if file_format.capitalize() in file_path:
                extension = 'makefile'
            else:
                extension = 'wrong_format'
        if not extension == file_format or extension == 'wrong_format':
            error_message(
                FileChecking.VERBOSE, '{0} [{1}] {2}'.format(
                    'not matched file extension', file_format, file_path
                )
            )
            self.__file_format_ok = False
        else:
            self.__file_format_ok = True
        verbose_message(
            FileChecking.VERBOSE, self.__verbose or verbose, file_path
        )

    def is_file_ok(self):
        '''
            Status of file for processing.

            :return: boolean status, True (correct file) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return all([
            self.__file_path_ok, self.__file_mode_ok, self.__file_format_ok
        ])

    def __str__(self):
        '''
            Dunder str method for FileChecking.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4})'.format(
            self.__class__.__name__, str(self.__verbose),
            str(self.__file_path_ok), str(self.__file_mode_ok),
            str(self.__file_format_ok)
        )
