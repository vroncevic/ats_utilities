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
    Defines class XmlBase with attribute(s) and method(s).
    Loads the ATS configuration for the ATS.
'''

import sys
from typing import Any, List, Dict, Optional

try:
    from bs4 import BeautifulSoup, Tag, NavigableString
    from ats_utilities.info import ATSInfo
    from ats_utilities.checker import ATSChecker
    from ats_utilities.option import ATSOptionParser
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.xml.xml2object import Xml2Object
    from ats_utilities.config_io.xml.object2xml import Object2Xml
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


class XmlBase(ATSChecker):
    '''
        Defines class XmlBase with attribute(s) and method(s).
        Loads the ATS configuration for the ATS.
        XML configuration-based API support.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | tool_operational - Control ATS operational functionality.
                | xml2obj - In API for tool_info.
                | obj2xml - Out API for tool_info.
                | option_parser - Option parser for ATS.
            :methods:
                | __init__ - Initials XmlBase constructor.
                | is_tool_ok - Checks is tool operational.
    '''

    def __init__(
        self, info_file: Optional[str], verbose: bool = False
    ) -> None:
        '''
            Initials XmlBase constructor.

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
        if not bool(info_file):
            raise ATSValueError(error_msg)
        self._verbose: bool = verbose
        info_dict: Dict[Any, Any] = {}
        self.tool_operational: bool = False
        self.xml2obj: Optional[Xml2Object] = Xml2Object(
            info_file, self._verbose
        )
        self.obj2xml: Optional[Object2Xml] = Object2Xml(
            info_file, self._verbose
        )
        if bool(self.xml2obj) and bool(self.obj2xml):
            tool_info: Optional[
                BeautifulSoup
            ] = self.xml2obj.read_configuration(self._verbose)
            if bool(tool_info):
                ats_name:  Optional[Tag | NavigableString] = tool_info.find(
                    'ats_name'
                )
                if ats_name:
                    info_dict['ats_name'] = str(ats_name.get_text())
                ats_version: Optional[Tag | NavigableString] = tool_info.find(
                    'ats_version'
                )
                if ats_version:
                    info_dict['ats_version'] = str(ats_version.get_text())
                ats_build_date: Optional[
                    Tag | NavigableString
                ] = tool_info.find('ats_build_date')
                if ats_build_date:
                    info_dict['ats_build_date'] = str(
                        ats_build_date.get_text()
                    )
                ats_licence: Optional[Tag | NavigableString] = tool_info.find(
                    'ats_licence'
                )
                if ats_licence:
                    info_dict['ats_licence'] = str(ats_licence.get_text())
                info: ATSInfo = ATSInfo(info_dict, self._verbose)
                if info.ats_info_ok:
                    self.option_parser: ATSOptionParser = ATSOptionParser(
                        f'{info.name} {info.build_date}',
                        info.version, info.licence, self._verbose
                    )
                    self.tool_operational = True
                    verbose_message(self._verbose, ['loaded ATS XML info'])

    def is_tool_ok(self) -> bool:
        '''
            Checks is tool operational.

            :return: True (tool is operational) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return self.tool_operational
