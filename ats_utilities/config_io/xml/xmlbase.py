# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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

from typing import Any, ClassVar, Dict, List, Optional
from bs4 import Tag, NavigableString
from ats_utilities.checker import IATSChecker, ATSChecker, ErrorChecker
from ats_utilities.info import ATSInfo
from ats_utilities.option import ATSOptionParser
from ats_utilities.console_io import IATSReporter, ATSReporter
from ats_utilities.config_io import IRead, IWrite, IFileCheck, FileCheck
from ats_utilities.option import IATSArgParseStrategy
from .xml2object import Xml2Object
from .object2xml import Object2Xml

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class XmlBase:
    '''
        Defines class XmlBase with attribute(s) and method(s).
        Loads the ATS configuration for the ATS.
        XML configuration-based API support.

        It defines:

            :attributes:
                | ERRORS - Error checker mapping.
                | __checker - Error checker.
                | __reporter - ATSReporter for check operations.
                | __verbose - Enable/Disable verbose option.
                | __file_checker - FileCheck for checking file.
                | __json2obj - In API for information.
                | __obj2json - Out API for information.
                | __tool_operational - Control ATS operational functionality.
                | __option_parser - Option parser for ATS.
            :methods:
                | __init__ - Initials IniBase constructor.
                | is_tool_ok - Checks is tool operational.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker

    def __init__(
        self,
        info_file: Optional[str] = None,
        xml2obj: Optional[IRead] = None,
        obj2xml: Optional[IWrite] = None,
        options_parser: Optional[ATSOptionParser] = None,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        file_checker: Optional[IFileCheck] = None,
        strategy: Optional[IATSArgParseStrategy] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials IniBase constructor.

            :param info_file: Path to the info file | None
            :type info_file: <Optional[str]>
            :param xml2obj: In API for information (Dependency Injected)
            :type xml2obj: <IRead>
            :param obj2xml: Out API for information (Dependency Injected)
            :type obj2xml: <IWrite>
            :param options_parser: Option parser for ATS | None
            :type options_parser: <Optional[IATSOptionParser]>
            :param checker: Error checker | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: ATSReporter for check operations | None
            :type reporter: <Optional[IATSReporter]>
            :param file_checker: FileCheck for checking file | None
            :type file_checker: <Optional[IFileCheck]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose
        self.__file_checker: IFileCheck = file_checker or FileCheck(
            self.__checker, self.__reporter, verbose
        )

        # Dependency Injection for Xml2Object and Object2Xml or use defaults if not provided
        self.__xml2obj: Optional[IRead] = xml2obj or Xml2Object(
            info_file, self.__checker, self.__reporter, self.__file_checker, self.__verbose
        )
        self.__obj2xml: Optional[IWrite] = obj2xml or Object2Xml(
            info_file, self.__checker, self.__reporter, self.__file_checker, self.__verbose
        )

        info_dict: Dict[Any, Any] = {}
        self.__tool_operational: bool = False

        if bool(self.__xml2obj) and bool(self.__obj2xml):
            tool_info = self.__xml2obj.read_configuration(self.__verbose)

        if bool(tool_info):

            if bool(tool_info):
                ats_name:  Optional[Tag | NavigableString] = tool_info.find('ats_name')

                if ats_name:
                    info_dict['ats_name'] = str(ats_name.get_text())

                ats_version: Optional[Tag | NavigableString] = tool_info.find('ats_version')

                if ats_version:
                    info_dict['ats_version'] = str(ats_version.get_text())

                ats_build_date: Optional[Tag | NavigableString] = tool_info.find('ats_build_date')

                if ats_build_date:
                    info_dict['ats_build_date'] = str(ats_build_date.get_text())

                ats_licence: Optional[Tag | NavigableString] = tool_info.find('ats_licence')

                if ats_licence:
                    info_dict['ats_licence'] = str(ats_licence.get_text())

                info: ATSInfo = ATSInfo(info_dict, self.__checker, self.__reporter, self.__verbose)

                if info.ats_info_ok:
                    # Dependecy injection for option parser or use default if not provided
                    # Dependecy injection for argument strategy
                    self.__option_parser: ATSOptionParser = options_parser or ATSOptionParser(
                        info_dict, strategy, self.__checker, self.__reporter, verbose
                    )
                    self.__option_parser.add_version_operation(info.version)
                    self.__tool_operational = True
                    self.__reporter.verbose(self.__verbose, ['loaded ATS XML info'])

    @property
    def option_parser(self) -> ATSOptionParser:
        '''
            Option parser for ATS.

            :return: Option parser for ATS
            :rtype: <ATSO
            ptionParser>
            :exceptions: None
        '''
        return self.__option_parser

    def is_tool_ok(self) -> bool:
        '''
            Checks is tool operational.

            :return: True (tool is operational) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return self.__tool_operational
