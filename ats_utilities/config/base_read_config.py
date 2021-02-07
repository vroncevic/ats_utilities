# -*- coding: UTF-8 -*-

"""
 Module
     base_read_config.py
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
     Define class BaseReadConfig with attribute(s) and method(s).
     Class for read operation (configuration).
"""

import sys

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.abstract import abstract_method
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


class BaseReadConfig(object):
    """
        Define class BaseReadConfig with attribute(s) and method(s).
        Class for read operation (configuration).
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __checker - ATS checker for parameters
                | __file_path - Configuration file path
            :methods:
                | __init__ - Initial constructor
                | file_path - Getting/Setting configuration file path
                | read_configuration - Read configuration (Abstract method)
    """

    __slots__ = ('VERBOSE', '__file_path', '__checker')
    VERBOSE = 'ATS_UTILITIES::CONFIG::BASE_READ_CONFIG'

    def __init__(self):
        """
            Initial file path.

            :exceptions: None
        """
        self.__checker = ATSChecker()
        self.__file_path = ""

    @property
    def file_path(self):
        """
            Getting configuration file path.

            :return: Configuration file path | None
            :rtype: <str> | <NoneType>
            :exception: None
        """
        return self.__file_path

    @file_path.setter
    def file_path(self, file_path):
        """
            Setting configuration file path.

            :param file_path: Configuration file path
            :type file_path: <str>
            :exceptions: ATSTypeError | ATSBadCallError
        """
        error, status = self.__checker.check_params(
            [('str:file_path', file_path)]
        )
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        self.__file_path = file_path

    @abstract_method
    def read_configuration(self, verbose=False):
        """
            Read configuration from file (Abstract method).

            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Configuration object
            :rtype: <Python object(s)> | <NoneType>
            :exception: NotImplementedError
        """
        pass
