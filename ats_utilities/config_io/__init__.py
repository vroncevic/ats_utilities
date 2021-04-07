# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
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
     Defined class ConfigFile with attribute(s) and method(s).
     Created API for configuration context manager.
'''

import sys

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
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


class ConfigFile(FileChecking):
    '''
        Defined class ConfigFile with attribute(s) and method(s).
        Created API for configuration context manager.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __file_path - Configuration file name.
                | __file_mode - File mode.
                | __file_format - File format.
                | __file - File object.
            :methods:
                | __init__ - Initial constructor.
                | __enter__ - Open configuration file in mode.
                | __exit__ - Close configuration file.
                | __str__ - Dunder method for ConfigFile.
    '''

    __slots__ = (
        'VERBOSE', 'MODES', 'file_path_ok', 'file_mode_ok', 'file_format_ok',
        '__file_path', '__file_mode', '__file_format', '__file'
    )
    VERBOSE = 'ATS_UTILITIES::CONFIG_IO'

    def __init__(self, file_path, file_mode, file_format, verbose=False):
        '''
            Initial constructor.

            :param file_path: Configuration file name.
            :type file_path: <str>
            :param file_mode: Open configuration file in mode.
            :type file_mode: <str>
            :param file_format: File format.
            :type file_format: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:file_path', file_path),
            ('str:file_mode', file_mode),
            ('str:file_format', file_format)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        FileChecking.__init__(self, verbose=verbose)
        self.__file = None
        self.__file_path = None
        self.__file_mode = None
        self.__file_format = None
        verbose_message(
            ConfigFile.VERBOSE, verbose, '{0}\n{1}\n{2} [{3}]'.format(
                'setting file path', file_path, 'setting file mode', file_mode
            )
        )
        self.check_path(file_path=file_path, verbose=verbose)
        self.check_mode(file_mode=file_mode, verbose=verbose)
        self.check_format(
            file_path=file_path, file_format=file_format, verbose=verbose
        )
        if self.is_file_ok():
            self.__file_path = file_path
            self.__file_mode = file_mode
            self.__file_format = file_format

    def __enter__(self):
        '''
            Open configuration file in mode.

            :return: File object | None.
            :rtype: <file> | <NoneType>
            :exceptions: None
        '''
        if self.is_file_ok():
            self.__file = open(self.__file_path, self.__file_mode)
        else:
            error_message(ConfigFile.VERBOSE, 'check file', self.__file_path)
            self.__file = None
        return self.__file

    def __exit__(self, *args):
        '''
            Close configuration file.

            :exceptions: None
        '''
        try:
            self.__file.close()
        except AttributeError:
            pass

    def __str__(self):
        '''
            Dunder method for ConfigFile.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, FileChecking.__str__(self)
        )
