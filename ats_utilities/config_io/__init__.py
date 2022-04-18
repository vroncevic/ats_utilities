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
     Created API for information/configuration context manager.
'''

import sys

try:
    from six import add_metaclass
    from ats_utilities import VerboseRoot
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
__version__ = '2.5.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@add_metaclass(VerboseRoot)
class ConfigFile(FileChecking):
    '''
        Defined class ConfigFile with attribute(s) and method(s).
        Created API for information/configuration context manager.
        It defines:

            :attributes:
                | __verbose - enable/disable verbose option.
                | __file_path - configuration file name.
                | __file_mode - file mode.
                | __file_format - file format.
                | __file - file object.
            :methods:
                | __init__ - initial constructor.
                | __enter__ - open configuration file in mode.
                | __exit__ - close configuration file.
                | __str__ - str dunder method for ConfigFile.
    '''

    def __init__(self, file_path, file_mode, file_format, verbose=False):
        '''
            Initial constructor.

            :param file_path: configuration file name.
            :type file_path: <str>
            :param file_mode: open configuration file in mode.
            :type file_mode: <str>
            :param file_format: file format.
            :type file_format: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:file_path', file_path), ('str:file_mode', file_mode),
            ('str:file_format', file_format)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        FileChecking.__init__(self, verbose=verbose)
        self.__verbose = verbose
        self.__file = None
        self.__file_path = None
        self.__file_mode = None
        self.__file_format = None
        self.check_path(file_path=file_path, verbose=verbose)
        self.check_mode(file_mode=file_mode, verbose=verbose)
        self.check_format(
            file_path=file_path, file_format=file_format, verbose=verbose
        )
        if self.is_file_ok():
            self.__file_path = file_path
            self.__file_mode = file_mode
            self.__file_format = file_format
        verbose_message(ConfigFile.VERBOSE, verbose, file_path, file_mode)

    def __enter__(self):
        '''
            Open configuration file in mode.

            :return: file object | None.
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
            Dunder str method for ConfigFile.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4}, {5}, {6})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            str(self.__verbose), self.__file_path, self.__file_mode,
            self.__file_format, self.__file,
        )
