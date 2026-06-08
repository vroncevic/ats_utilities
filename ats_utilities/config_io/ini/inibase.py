# -*- coding: UTF-8 -*-

'''
Module
    inibase.py
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
    Defines class IniBase with attribute(s) and method(s).
    Loads the ATS configuration for the ATS.
'''

from typing import Any, ClassVar, Dict, List, Optional
from configparser import ConfigParser
from ats_utilities.checker import IATSChecker, ATSChecker, ErrorChecker
from ats_utilities.info import ATSInfo
from ats_utilities.option import ATSOptionParser
from ats_utilities.console_io import IATSReporter, ATSReporter
from ats_utilities.config_io import IRead, IWrite, IFileCheck, FileCheck
from ats_utilities.option import IATSArgParseStrategy
from .ini2object import Ini2Object
from .object2ini import Object2Ini

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IniBase:
    '''
        Defines class IniBase with attribute(s) and method(s).
        Loads the ATS configuration for the ATS.
        INI configuration-based API support.

        It defines:

            :attributes:
                | ERRORS - Error checker mapping.
                | __checker - Error checker.
                | __reporter - ATSReporter for check operations.
                | __verbose - Enable/Disable verbose option.
                | __file_checker - FileCheck for checking file.
                | __ini2obj - In API for information.
                | __obj2ini - Out API for information.
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
        ini2obj: Optional[IRead] = None,
        obj2ini: Optional[IWrite] = None,
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
            :param ini2obj: In API for information (Dependency Injected)
            :type ini2obj: <IRead>
            :param obj2ini: Out API for information (Dependency Injected)
            :type obj2ini: <IWrite>
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

        # Dependency Injection for Ini2Object and Object2Ini or use defaults if not provided
        self.__ini2obj: Optional[IRead] = ini2obj or Ini2Object(
            info_file, self.__checker, self.__reporter, self.__file_checker, self.__verbose
        ) 
        self.__obj2ini: Optional[IWrite] = obj2ini or Object2Ini(
            info_file, self.__checker, self.__reporter, self.__file_checker, self.__verbose
        )

        information: Optional[ConfigParser] = None
        info_dict: Dict[Any, Any] = {}
        self.__tool_operational: bool = False

        if bool(self.__ini2obj) and bool(self.__obj2ini):
            information = self.__ini2obj.read_configuration(self.__verbose)

        if bool(information):
            info_dict['ats_name'] = str(information.get('ats_info', 'ats_name'))
            info_dict['ats_version'] = str(information.get('ats_info', 'ats_version'))
            info_dict['ats_build_date'] = str(information.get('ats_info', 'ats_build_date'))
            info_dict['ats_licence'] = str(information.get('ats_info', 'ats_licence'))

            info: ATSInfo = ATSInfo(info_dict, self.__checker, self.__reporter, self.__verbose)

            if info.ats_info_ok:
                # Dependecy injection for option parser or use default if not provided
                # Dependecy injection for argument strategy
                self.__option_parser: ATSOptionParser = options_parser or ATSOptionParser(
                    info_dict, strategy, self.__checker, self.__reporter, verbose
                )
                self.__option_parser.add_version_operation(info.version)
                self.__tool_operational = True
                self.__reporter.verbose(self.__verbose, ['loaded ATS INI info'])

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
