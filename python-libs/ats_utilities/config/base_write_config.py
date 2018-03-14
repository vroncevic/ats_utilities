# -*- coding: UTF-8 -*-
# base_write_config.py
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

from abc import ABCMeta, abstractmethod

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class BaseWriteConfig(object):
    """
        Define class BaseWriteConfig with attribute(s) and method(s).
        Class for write operation (configuration).
        It defines:
            attribute:
                VERBOSE - Console text indicator for current process-phase
                __file_path - Configuration file path
            method:
                __init__ - Initial constructor
                set_file_path - Setting configuration file path
                get_file_path - Getting configuration file path
                write_configuration - Write configuration to file
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    __metaclass__ = ABCMeta
    VERBOSE = '[ATS_UTILITIES::CONFIG::BASE_WRITE_CONFIG]'

    def __init__(self, verbose=False):
        """
            Initial file path.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        self.__file_path = ""

    def set_file_path(self, file_path, verbose=False):
        """
            Setting configuration file path.
            :param file_path: Configuration file path
            :type file_path: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        self.__file_path = file_path

    def get_file_path(self, verbose=False):
        """
            Getting configuration file path.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Configuration file path | None
            :rtype: <str> | <NoneType>
        """
        return self.__file_path

    @abstractmethod
    def write_configuration(self, configuration, verbose=False):
        """
            Write configuration to file (Abstract method).
            :param configuration: Configuration object
            :type configuration: <dict>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
        """
        pass

    def __str__(self):
        """
            Return human readable string (BaseWriteConfig).
            :return: String representation of BaseWriteConfig
            :rtype: <str>
        """
        return "File path {0}".format(self.__file_path)

    def __repr__(self):
        """
            Return unambiguous string (BaseWriteConfig).
            :return: String representation of BaseWriteConfig
            :rtype: <str>
        """
        return "{0}()".format(type(self).__name__)
