# -*- coding: UTF-8 -*-

'''
Module
    cfg2object.py
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
    Defines class Cfg2Object with attribute(s) and method(s).
    Creates API for reading configuration/information from a cfg file.
'''

import sys
from typing import Any, Dict
from re import match

try:
    from ats_utilities import auto_str
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io import ConfigFile
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.base_read import BaseReadConfig
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
    from ats_utilities.config_io.cfg.cfg2object_meta import Cfg2ObjectMeta
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@auto_str
class Cfg2Object(BaseReadConfig, metaclass=Cfg2ObjectMeta):
    '''
        Defines class Cfg2Object with attribute(s) and method(s).
        Creates API for read configuration/information from a cfg file.
        Conversion configuration content to dictionary.

        It defines:

            :attributes:
                | _format - Format of configuration content.
                | _regex_match - Regular expression for matching line.
                | _file_path - Configuration file path.
                | _verbose - Enable/Disable verbose option.
            :methods:
                | __init__ - Initial Cfg2Object constructor.
                | read_configuration - Read configuration from file.
    '''

    _format: str = 'cfg'
    _regex_match: str = r'^\s*$'
    _file_path: str | None
    _verbose: bool

    def __init__(
        self, configuration_file: str | None, verbose: bool = False
    ) -> None:
        '''
            Initial Cfg2Object constructor.

            :param configuration_file: Configuration file path | None
            :type configuration_file: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = checker.check_params([
            ('str:configuration_file', configuration_file)
        ])
        if error_id == ATSChecker.type_error:
            raise ATSTypeError(error_msg)
        if error_id == ATSChecker.value_error:
            raise ATSBadCallError(error_msg)
        BaseReadConfig.__init__(self, verbose)
        self._verbose = verbose
        configuration_file = str(configuration_file)
        self._file_path = configuration_file
        verbose_message(
            Cfg2Object.verbose,  # pylint: disable=no-member
            verbose,
            tuple(configuration_file)
        )

    def read_configuration(self, verbose: bool = False) -> Dict[Any, Any]:
        '''
            Getting a configuration from cfg file.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Configuration object
            :rtype: <Dict[Any, Any]>
            :exceptions: None
        '''
        config: Dict[Any, Any] = {}
        if bool(self._file_path):
            with ConfigFile(self._file_path, 'r', Cfg2Object._format) as cfg:
                if bool(cfg):
                    for line in cfg.read().splitlines():
                        if not match(Cfg2Object._regex_match, line):
                            pairs: Any = line.split('=')
                            config[pairs[0].strip()] = pairs[1].strip()
            verbose_message(
                Cfg2Object.verbose,  # pylint: disable=no-member
                self._verbose or verbose,
                tuple(str(config))
            )
        return config
