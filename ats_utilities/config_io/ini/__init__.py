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
    Defines class IniBase with attribute(s) and method(s).
    Loads ATS configuration/information, setup ATS CL interface.
'''

import sys
from typing import Any, Dict
from configparser import ConfigParser

try:
    from ats_utilities.info import ATSInfo
    from ats_utilities.checker import ATSChecker
    from ats_utilities.option import ATSOptionParser
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.ini.ini2object import Ini2Object
    from ats_utilities.config_io.ini.object2ini import Object2Ini
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


class IniBase(ATSChecker):
    '''
        Defines class IniBase with attribute(s) and method(s).
        Loads ATS configuration/information, setup ATS CL interface.
        Configuration base ini API support.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | tool_operational - Control ATS operational functionality.
                | ini2obj - In API for information.
                | obj2ini - Out API for information.
                | option_parser - Option parser for ATS configuration.
            :methods:
                | __init__ - Initial IniBase constructor.
                | is_tool_ok - Check is tool operational.
    '''

    def __init__(
        self, information_file: str | None, verbose: bool = False
    ) -> None:
        '''
            Initial IniBase constructor.

            :param information_file: Information file path | None
            :type information_file: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        super().__init__()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('str:information_file', information_file)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if error_id == self.VALUE_ERROR:
            raise ATSBadCallError(error_msg)
        self._verbose: bool = verbose
        information: ConfigParser | None = None
        info_dict: Dict[Any, Any] = {}
        self.tool_operational: bool = False
        self.ini2obj: Ini2Object = Ini2Object(information_file, self._verbose)
        self.obj2ini: Object2Ini = Object2Ini(information_file, self._verbose)
        if all([self.ini2obj, self.obj2ini]):
            information = self.ini2obj.read_configuration(self._verbose)
        if information:
            info_dict['ats_name'] = str(information.get(
                'ats_info', 'ats_name'
            ))
            info_dict['ats_version'] = str(information.get(
                'ats_info', 'ats_version'
            ))
            info_dict['ats_build_date'] = str(information.get(
                'ats_info', 'ats_build_date'
            ))
            info_dict['ats_licence'] = str(information.get(
                'ats_info', 'ats_licence'
            ))
            info: ATSInfo = ATSInfo(info_dict, self._verbose)
            if info.ats_info_ok:
                self.option_parser: ATSOptionParser = ATSOptionParser(
                    f'{info.name} {info.build_date}',
                    info.version, info.licence, self._verbose
                )
                self.tool_operational = True
                verbose_message(self._verbose, ['loaded ATS INI base info'])

    def is_tool_ok(self) -> bool:
        '''
            Check is tool operational.

            :return: True (tool is operational) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return self.tool_operational
