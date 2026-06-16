# -*- coding: UTF-8 -*-

'''
Module
    xml2object.py
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
    Defines class Xml2Object with attribute(s) and method(s).
    Creates an API for reading a configuration from a XML file.
'''

from typing import ClassVar, List, Optional
from ats_utilities.checker.ichecker import IATSChecker, ErrorChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.xml.ixml_processor import IXMLProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Xml2Object(IRead):
    '''
        Defines class Xml2Object with attribute(s) and method(s).
        Creates an API for reading a configuration from a XML file.
        Conversion of XML content to Python object.

        It defines:

            :attributes:
                | _EXT - File extension of the configuration file.
                | _verbose - Enable/Disable verbose option.
                | _file_path - Configuration file path.
            :methods:
                | __init__ - Initials Xml2Object constructor.
                | read_configuration - Reads a configuration from an XML file.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker
    __EXT: str = 'xml'
    __MODE: str = 'r'

    def __init__(
        self,
        config_file: Optional[str],
        xml_processor: IXMLProcessor,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        file_checker: Optional[IFileCheck] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials Xml2Object constructor.

            :param config_file: Configuration file path | None
            :type config_file: <Optional[str]>
            :param xml_processor: IXMLProcessor for processing XML content
            :type xml_processor: <IXMLProcessor>
            :param checker: ATSChecker for check operations | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: ATSReporter for check operations | None
            :type reporter: <Optional[IATSReporter]>
            :param file_checker: FileCheck for checking file | None
            :type file_checker: <Optional[IFileCheck]>
            :param verbose: Enable/Disable verbose option (default False)
            :type verbose: <bool>
            :exceptions:  ATSTypeError
        '''
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose
        self.__file_checker: IFileCheck = file_checker or FileCheck(
            self.__checker, self.__reporter, self.__verbose
        )

        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.__checker.validate_parameters([
            ('str:config_file', config_file)
        ])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)


        self.__file_path: str = str(config_file)
        self.__xml_processor: IXMLProcessor = xml_processor
        self.__reporter.verbose(self.__verbose, [f'configuration {config_file}'])

    def read_configuration(self, verbose: bool = False) -> Optional[IXMLProcessor]:
        '''
            Reads a configuration from an XML file.

            :param verbose: Enable/Disable verbose option (default False)
            :type verbose: <bool>
            :return: Configuration object | None
            :rtype: <Optional[IXMLProcessor]>
            :exceptions: None
        '''
        content: Optional[str] = None
        config: Optional[IXMLProcessor] = None

        with ConfFile(
            self.__file_path,
            self.__MODE,
            self.__EXT,
            self.__checker,
            self.__reporter,
            self.__file_checker,
            self.__verbose or verbose
        ) as xml:
            if bool(xml):
                content = xml.read()

                if bool(content):
                    if self.__xml_processor.from_string(str(content)):
                        config = self.__xml_processor

        self.__reporter.verbose(self.__verbose or verbose, [f'configuration {config}'])

        return config
