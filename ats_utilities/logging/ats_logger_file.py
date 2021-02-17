# -*- coding: UTF-8 -*-

"""
 Module
     ats_logger_file.py
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
     Define class ATSLoggerFile with attribute(s) and method(s).
     Keep App/Tool/Script logger file path in one propery object.
"""

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLoggerFile(object):
    """
        Define class ATSLoggerFile with attribute(s) and method(s).
        Keep App/Tool/Script logger file path in one propery object.
        It defines:

            :attributes:
                | __log_file - Log file path.
            :methods:
                | __init__ - Initial constructor.
                | log_file - Property methods for set/get operations.
    """

    def __init__(self):
        """
            Initial constructor.

            :exceptions: None
        """
        self.__log_file = None

    @property
    def log_file(self):
        """
            Property method for getting log file path.

            :return: Log file path | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        """
        return self.__log_file

    @log_file.setter
    def log_file(self, log_file):
        """
            Property method for setting log file path.

            :param log_file: Log file path.
            :type log_file: <str>
            :exceptions: None
        """
        self.__log_file = log_file
