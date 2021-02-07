# -*- coding: UTF-8 -*-

"""
 Module
     ini2object.py
 Copyright
     Copyright (C) 2019 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define class Ini2Object with attribute(s) and method(s).
     Convert configuration from an ini file to an object.
"""

import sys

try:
    from configparser import ConfigParser
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config.base_read_config import BaseReadConfig
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config.config_context_manager import ConfigFile
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
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


class Ini2Object(BaseReadConfig):
    """
        Define class Ini2Object with attribute(s) and method(s).
        Convert configuration from an ini file to an object.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __FORMAT - Format of configuration content
                | __checker - ATS checker for parameters
            :methods:
                | __init__ - Initial constructor
                | read_configuration - Read configuration from file
    """

    __slots__ = ('VERBOSE', '__FORMAT', '__checker')
    VERBOSE = 'ATS_UTILITIES::CONFIG::INI::INI_TO_OBJECT'
    __FORMAT = 'ini'

    def __init__(self, configuration_file, verbose=False):
        """
            Setting configuration file path.

            :param configuration_file: Absolute configuration file path
            :type configuration_file: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        """
        self.__checker = ATSChecker()
        error, status = self.__checker.check_params(
            [('str:configuration_file', configuration_file)]
        )
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        BaseReadConfig.__init__(self)
        verbose_message(Ini2Object.VERBOSE, verbose, 'Setting INI interface')
        self.file_path = configuration_file

    def read_configuration(self, verbose=False):
        """
            Read configuration from file.

            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Configuration object | None
            :rtype: <ConfigParser> | <NoneType>
        """
        content = None
        verbose_message(
            Ini2Object.VERBOSE, verbose,
            'Read configuration from file', self.file_path
        )
        with ConfigFile(self.file_path, 'r', Ini2Object.__FORMAT) as ini:
            if bool(ini):
                content = ConfigParser()
                content.read_file(ini)
        verbose_message(Ini2Object.VERBOSE, verbose, 'Done')
        return content
