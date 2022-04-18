# -*- coding: UTF-8 -*-

'''
 Module
     base_read.py
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
     Defined class BaseReadConfig with attribute(s) and method(s).
     Created API for read operation for information/configuration files.
'''

import sys

try:
    from six import add_metaclass
    from ats_utilities import VerboseRoot
    from ats_utilities.checker import ATSChecker
    from ats_utilities.abstract import AbstractMethod
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
class BaseReadConfig:
    '''
        Defined class BaseReadConfig with attribute(s) and method(s).
        Created API for read operation for information/configuration files.
        It defines:

            :attributes:
                | __verbose - enable/disable verbose option.
                | __file_path - configuration file path.
            :methods:
                | __init__ - initial constructor.
                | file_path - property methods for set/get operations.
                | is_not_none - checking is file path None.
                | read_configuration - read configuration (Abstract method).
                | __str__ - str dunder method for BaseReadConfig.
    '''

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__verbose = verbose
        self.__file_path = None

    @property
    def file_path(self):
        '''
            Property method for getting file path.

            :return: configuration file path | None.
            :rtype: <str> | <NoneType>
            :exception: None
        '''
        return self.__file_path

    @file_path.setter
    def file_path(self, file_path):
        '''
            Property method for setting file path.

            :param file_path: configuration file path.
            :type file_path: <str>
            :exceptions: None
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('str:file_path', file_path)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        self.__file_path = file_path
        verbose_message(BaseReadConfig.VERBOSE, self.__verbose, file_path)

    def is_not_none(self):
        '''
            Checking is file path None.

            :return: boolean status, True (file path ok) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return bool(self.__file_path)

    @AbstractMethod
    def read_configuration(self, verbose=False):
        '''
            Read configuration from file (Abstract method).

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exception: NotImplementedError
        '''

    def __str__(self):
        '''
            Dunder str method for BaseReadConfig.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, str(self.__verbose), self.__file_path
        )
