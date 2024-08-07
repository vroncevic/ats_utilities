# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
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
    Defines class CfgBase with attribute(s) and method(s).
    Loads the ATS configuration for the ATS.
'''

import sys
from typing import Any, Dict, List, Optional

try:
    from ats_utilities.info import ATSInfo
    from ats_utilities.checker import ATSChecker
    from ats_utilities.option import ATSOptionParser
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.cfg.cfg2object import Cfg2Object
    from ats_utilities.config_io.cfg.object2cfg import Object2Cfg
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


class CfgBase(ATSChecker):
    '''
        Defines class CfgBase with attribute(s) and method(s).
        Loads the ATS configuration for the ATS.
        CFG configuration-based API support.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | tool_operational - Control ATS operational functionality.
                | cfg2obj - In API for information.
                | obj2cfg - Out API for information.
                | option_parser - Option parser for ATS.
            :methods:
                | __init__ - Initials CfgBase constructor.
                | is_tool_ok - Checks is tool operational.
    '''

    def __init__(
        self, info_file: Optional[str], verbose: bool = False
    ) -> None:
        '''
            Initials CfgBase constructor.

            :param info_file: Information file path | None
            :type info_file: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        super().__init__()
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([('str:info_file', info_file)])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(Optional[str]):
            raise ATSValueError(error_msg)
        self._verbose: bool = verbose
        information: Dict[Any, Any] = {}
        self.tool_operational: bool = False
        self.cfg2obj: Optional[Cfg2Object] = Cfg2Object(
            info_file, self._verbose
        )
        self.obj2cfg: Optional[Object2Cfg] = Object2Cfg(
            info_file, self._verbose
        )
        if bool(self.cfg2obj) and bool(self.obj2cfg):
            information = self.cfg2obj.read_configuration(self._verbose)
        if bool(information):
            info: ATSInfo = ATSInfo(information, self._verbose)
            if info.ats_info_ok:
                self.option_parser: ATSOptionParser = ATSOptionParser(
                    f'{info.name} {info.build_date}',
                    info.version, info.licence, self._verbose
                )
                self.tool_operational = True
                verbose_message(self._verbose, ['loaded ATS CFG info'])

    def is_tool_ok(self) -> bool:
        '''
            Checks is tool operational.

            :return: True (tool is operational) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return self.tool_operational
