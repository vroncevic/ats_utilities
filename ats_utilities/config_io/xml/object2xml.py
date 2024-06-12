# -*- coding: UTF-8 -*-

'''
Module
    object2xml.py
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
    Defines class Object2Xml with attribute(s) and method(s).
    Creates an API for writing a configuration to a XML file.
'''

import sys
from typing import List

try:
    from bs4 import BeautifulSoup
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io import ConfFile
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.1.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Object2Xml(ATSChecker):
    '''
        Defines class Object2Xml with attribute(s) and method(s).
        Creates an API for writing a configuration to a XML file.
        Conversion of Python object to XML content.

        It defines:

            :attributes:
                | _EXT - File extension of the configuration file.
                | _verbose - Enable/Disable verbose option.
                | _file_path - Configuration file path.
            :methods:
                | __init__ - Initials Object2Xml constructor.
                | write_configuration - Writes configuration to a XML file.
    '''

    _EXT: str = 'xml'

    def __init__(self, config_file: str | None, verbose: bool = False) -> None:
        '''
            Initial Object2Xml constructor.

            :param config_file: Configuration file path | None
            :type config_file: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError
        '''
        super().__init__()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('str:config_file', config_file)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        self._verbose: bool = verbose
        self._file_path: str = str(config_file)
        verbose_message(self._verbose, [f'configuration file {config_file}'])

    def write_configuration(
        self, config: BeautifulSoup | None, verbose: bool = False
    ) -> bool:
        '''
            Writes configuration to a XML file.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :param config: Configuration object
            :type: <BeautifulSoup> | <NoneType>
            :return: True (configuration written to file) | False
            :rtype: <bool>
            :exception: ATSTypeError
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('BeautifulSoup:config', config)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        status: bool = False
        verbose_message(
            self._verbose or verbose, [f'configuration {config}']
        )
        if bool(config):
            if not bool(config.contents):
                return status
            with ConfFile(self._file_path, 'w', self._EXT) as xml:
                if bool(xml):
                    if xml.write(f'{config}'):
                        status = True
        return status
