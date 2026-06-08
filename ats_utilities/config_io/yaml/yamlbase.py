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
    Defines class YamlBase with attribute(s) and method(s).
    Loads the ATS configuration for the ATS.
'''

from typing import ClassVar, List, Optional
from ats_utilities.checker import IATSChecker, ATSChecker, ErrorChecker
from ats_utilities.info import ATSInfo
from ats_utilities.option import IATSOptionParser, ATSOptionParser
from ats_utilities.console_io import IATSReporter, ATSReporter
from ats_utilities.config_io import IRead, IWrite, IFileCheck, FileCheck
from ats_utilities.option import IATSArgParseStrategy
from .yaml2object import Yaml2Object
from .object2yaml import Object2Yaml
from .iyaml_processor import IYAMLProcessor
from .default_yaml_processor import ATSYAMLProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class YamlBase:
    '''
        Defines class YamlBase with attribute(s) and method(s).
        Loads the ATS configuration for the ATS.
        YAML configuration-based API support.

        It defines:

            :attributes:
                | ERRORS - Error checker mapping.
                | __checker - Error checker.
                | __reporter - ATSReporter for check operations.
                | __verbose - Enable/Disable verbose option.
                | __file_checker - FileCheck for checking file.
                | __yaml2obj - In API for information.
                | __obj2yaml - Out API for information.
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
        yaml2obj: Optional[IRead] = None,
        obj2yaml: Optional[IWrite] = None,
        options_parser: Optional[IATSOptionParser] = None,
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
            :param yaml2obj: In API for information (Dependency Injected)
            :type yaml2obj: :class:`~ats_utilities.config_io.iread.IRead`
            :param obj2yaml: Out API for information (Dependency Injected)
            :type obj2yaml: :class:`~ats_utilities.config_io.iwrite.IWrite`
            :param options_parser: Option parser for ATS | None
            :type options_parser: :class:`~ats_utilities.option.ioption_parser.IATSOptionParser`
            :param checker: Error checker | None
            :type checker: :class:`~ats_utilities.checker.IATSChecker`
            :param reporter: ATSReporter for check operations | None
            :type reporter: :class:`~ats_utilities.console_io.iats_reporter.IATSReporter`onsole_io.iats_reporter.IATSReporter`          
            :param file_checker: FileCheck for checking file | None
            :type file_checker: :class:`~ats_utilities.config_io.ifile_check.IFileCheck`
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

        # Dependency Injection for Yaml2Object and Object2Yaml or use defaults if not provided
        self.__yaml2obj: IRead = yaml2obj or Yaml2Object(
            info_file, ATSYAMLProcessor(), self.__checker, self.__reporter, self.__file_checker, self.__verbose
        )
        self.__obj2yaml: IWrite = obj2yaml or Object2Yaml(
            info_file, self.__checker, self.__reporter, self.__file_checker, self.__verbose
        )

        information: Optional[IYAMLProcessor] = None
        self.__tool_operational: bool = False

        if bool(self.__yaml2obj) and bool(self.__obj2yaml):
            information = self.__yaml2obj.read_configuration(self.__verbose)

        if bool(information):
            info: ATSInfo = ATSInfo(information.to_dict(), self.__checker, self.__reporter, self.__verbose)

            if info.ats_info_ok:
                # Dependecy injection for option parser or use default if not provided
                # Dependecy injection for argument strategy
                self.__option_parser: IATSOptionParser = options_parser or ATSOptionParser(
                    information.to_dict(), strategy, self.__checker, self.__reporter, verbose
                )
                self.__option_parser.add_version_operation(info.version)
                self.__tool_operational = True
                self.__reporter.verbose(self.__verbose, ['loaded ATS INI info'])

    @property
    def option_parser(self) -> IATSOptionParser:
        '''
            Option parser for ATS.

            :return: Option parser for ATS
            :rtype: :class:`~ats_utilities.option.ioption_parser.IATSOptionParser`
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
