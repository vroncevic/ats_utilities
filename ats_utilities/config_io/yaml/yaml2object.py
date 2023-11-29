# -*- coding: UTF-8 -*-

'''
Module
    yaml2object.py
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
    Defines class Yaml2Object with attribute(s) and method(s).
    Creates API for reading a configuration/information from a yaml file.
'''

import sys
from typing import Any

try:
    from yaml import load, FullLoader
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io import ConfFile
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.9.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Yaml2Object(ATSChecker):
    '''
        Defines class Yaml2Object with attribute(s) and method(s).
        Creates API for reading a configuration/information from a yaml file.
        Conversion YAML to configuration content.

        It defines:

            :attributes:
                | _FORMAT - Format of configuration content.
                | _verbose - Enable/Disable verbose option.
                | _file_path - Configuration file path.
            :methods:
                | __init__ - Initial Yaml2Object constructor.
                | read_configuration - Read a configuration from file.
    '''

    _FORMAT: str = 'yaml'

    def __init__(
        self, configuration_file: str | None, verbose: bool = False
    ) -> None:
        '''
            Initial Yaml2Object constructor.

            :param configuration_file: Configuration file path | None
            :type configuration_file: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        super().__init__()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('str:configuration_file', configuration_file)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if error_id == self.VALUE_ERROR:
            raise ATSBadCallError(error_msg)
        self._verbose: bool = verbose
        configuration_file = str(configuration_file)
        self._file_path: str = configuration_file
        verbose_message(
            self._verbose, [f'configuration file {configuration_file}']
        )

    def read_configuration(self, verbose: bool = False) -> Any | None:
        '''
            Read a configuration from yaml file.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Configuration object | None
            :rtype: <Any> | <NoneType>
            :exceptions: None
        '''
        config: Any | None = None
        with ConfFile(self._file_path, 'r', self._FORMAT) as yaml:
            if bool(yaml):
                config = load(yaml, Loader=FullLoader)
        verbose_message(self._verbose or verbose, [f'configuration {config}'])
        return config
