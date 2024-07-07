# -*- coding: UTF-8 -*-

'''
Module
    json2object.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class Json2Object with attribute(s) and method(s).
    Creates an API for reading a configuration from a JSON file.
'''

import sys
from typing import Any, Dict, List, Optional
from json import load

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io import ConfFile
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Json2Object(ATSChecker):
    '''
        Defines class Json2Object with attribute(s) and method(s).
        Creates an API for reading a configuration from a JSON file.
        Conversion of Python object to JSON config.

        It defines:

            :attributes:
                | _EXT - File extension of the configuration file.
                | _verbose - Enable/Disable verbose option.
                | _file_path - Configuration file path.
            :methods:
                | __init__ - Initials Json2Object constructor.
                | read_configuration - Reads configuration from a JSON file.
    '''

    _EXT: str = 'json'

    def __init__(
        self, config_file: Optional[str], verbose: bool = False
    ) -> None:
        '''
            Initials Ini2Object constructor.

            :param config_file: Configuration file path | None
            :type config_file: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        super().__init__()
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([
            ('str:config_file', config_file)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(config_file):
            raise ATSValueError(error_msg)
        self._verbose: bool = verbose
        self._file_path: str = str(config_file)
        verbose_message(self._verbose, [f'configuration file {config_file}'])

    def read_configuration(self, verbose: bool = False) -> Dict[Any, Any]:
        '''
            Reads a configuration from a JSON file.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Configuration object
            :rtype: <Dict[Any, Any]>
            :exceptions: None
        '''
        config: Dict[Any, Any] = {}
        with ConfFile(self._file_path, 'r', self._EXT) as json:
            if bool(json):
                config = load(json)
        verbose_message(self._verbose or verbose, [f'configuration {config}'])
        return config
