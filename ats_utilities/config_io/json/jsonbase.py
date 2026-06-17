# -*- coding: UTF-8 -*-

'''
Module
    jsonbase.py
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
    Defines class JsonBase with attribute(s) and method(s).
    Loads the ATS configuration for the ATS.
'''

from typing import ClassVar, List, Optional
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.engine import ATSChecker
from ats_utilities.checker.ichecker import ErrorChecker
from ats_utilities.info.engine import ATSInfo
from ats_utilities.option.ioption_parser import IATSOptionParser
from ats_utilities.option.ats_option_parser import ATSOptionParser
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import ATSReporter
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.option.iparser_strategy import IATSArgParseStrategy
from ats_utilities.config_io.json.json2object import Json2Object
from ats_utilities.config_io.json.object2json import Object2Json
from ats_utilities.config_io.json.ijson_processor import IJSONProcessor
from ats_utilities.config_io.json.json_processor import ATSJSONProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class JsonBase:
    '''
        Defines class JsonBase with attribute(s) and method(s).
        Loads the ATS configuration for the ATS.
        JSON configuration-based API support.

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
                | __init__ - Initials JsonBase constructor.
                | is_tool_ok - Checks is tool operational.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker

    def __init__(
        self,
        info_file: Optional[str] = None,
        json2obj: Optional[IRead] = None,
        obj2json: Optional[IWrite] = None,
        options_parser: Optional[IATSOptionParser] = None,
        checker: Optional[IChecker] = None,
        reporter: Optional[IReporter] = None,
        file_checker: Optional[IFileCheck] = None,
        strategy: Optional[IATSArgParseStrategy] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials JsonBase constructor.

            :param info_file: Path to the info file | None
            :type info_file: <Optional[str]>
            :param json2obj: In API for information (Dependency Injected)
            :type json2obj: <Optional[IRead]>
            :param obj2json: Out API for information (Dependency Injected)
            :type obj2json: <Optional[IWrite]>
            :param options_parser: Option parser for ATS | None
            :type options_parser: <Optional[IATSOptionParser]>
            :param checker: Error checker | None
            :type checker: <Optional[IChecker]>
            :param reporter: ATSReporter for check operations | None
            :type reporter: <Optional[IReporter]>
            :param file_checker: FileCheck for checking file | None
            :type file_checker: <Optional[IFileCheck]>
            :param strategy: Strategy for argument parsing | None
            :type strategy: <Optional[IATSArgParseStrategy]>
            :param verbose: Enable/Disable verbose option (default False)
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__checker: IChecker = checker or ATSChecker()
        self.__reporter: IReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose
        self.__file_checker: IFileCheck = file_checker or FileCheck(
            self.__checker, self.__reporter, verbose
        )
        self.__option_parser: Optional[IATSOptionParser] = None

        # Dependency Injection for Json2Object and Object2Json or use defaults if not provided
        self.__json2obj: Optional[IRead] = json2obj or Json2Object(
            info_file, ATSJSONProcessor(), self.__checker, self.__reporter, self.__file_checker, self.__verbose
        )
        self.__obj2json: Optional[IWrite] = obj2json or Object2Json(
            info_file, self.__checker, self.__reporter, self.__file_checker, self.__verbose
        )

        information: Optional[IJSONProcessor] = None
        self.__tool_operational: bool = False

        if bool(self.__json2obj) and bool(self.__obj2json):
            information = self.__json2obj.read_configuration(self.__verbose)

        if bool(information):
            info: ATSInfo = ATSInfo(information.to_dict(), self.__checker, self.__reporter, self.__verbose)

            if info.ats_info_ok:
                # Dependecy injection for option parser or use default if not provided
                # Dependecy injection for argument strategy
                self.__option_parser = options_parser or ATSOptionParser(
                    information.to_dict(), strategy, self.__checker, self.__reporter, verbose
                )
                self.__option_parser.add_version_operation(info.version)
                self.__tool_operational = True
                self.__reporter.verbose(self.__verbose, ['loaded ATS JSON info'])

    @property
    def option_parser(self) -> Optional[IATSOptionParser]:
        '''
            Option parser for ATS.

            :return: Option parser for ATS
            :rtype: <Optional[IATSOptionParser]>
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
