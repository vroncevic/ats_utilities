# -*- coding: UTF-8 -*-

'''
Module
    ini2object.py
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
    Defines class Ini2Object with attribute(s) and method(s).
    Creates an API for reading configuration from an INI file.
'''

from typing import ClassVar, List, Optional
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.engine import ATSChecker
from ats_utilities.checker.ichecker import ErrorChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.ini.iini_processor import IINIProcessor
from ats_utilities.config_io.ini.ini_processor import ATSINIProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Ini2Object(IRead):
    '''
        Defines class Ini2Object with attribute(s) and method(s).
        Creates an API for reading configuration from an INI file.
        Conversion of INI config to Python object.

        It defines:

            :attributes:
                | ERRORS - Marks error types.
                | __EXT - File extension of the configuration file.
                | __MODE - File open mode.
                | __checker - ATSChecker for check operations.
                | __reporter - ATSReporter for messaging.
                | __file_checker - FileCheck for checking file.
                | __file_path - Configuration file path.
                | __verbose - Enable/Disable verbose option.
            :methods:
                | __init__ - Initials Ini2Object constructor.
                | read_configuration - reads configuration from an INI file.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker
    __EXT: str = 'ini'
    __MODE: str = 'r'

    def __init__(
        self,
        config_file: Optional[str],
        ini_processor: Optional[IINIProcessor] = None,
        checker: Optional[IChecker] = None,
        reporter: Optional[IReporter] = None,
        file_checker: Optional[IFileCheck] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials Ini2Object constructor.

            :param config_file: Configuration file path | None
            :type config_file: <Optional[str]>
            :param checker: ATSChecker for check operations | None
            :type checker: <Optional[IChecker]>
            :param reporter: ATSReporter for check operations | None
            :type reporter: <Optional[IReporter]>
            :param file_checker: FileCheck for checking file | None
            :type file_checker: <Optional[IFileCheck]>
            :param verbose: Enable/Disable verbose option (default False)
            :type verbose: <bool>
            :exceptions:  ATSTypeError
        '''
        self.__checker: IChecker = checker or ATSChecker()
        self.__reporter: IReporter = reporter or ATSReporter()
        self.__file_checker: IFileCheck = file_checker or FileCheck(checker, reporter, verbose)
        self.__verbose: bool = verbose

        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.__checker.validate_parameters([
            ('str:config_file', config_file)
        ])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)

        self.__file_path: str = str(config_file)
        self.__ini_processor: IINIProcessor = ini_processor or ATSINIProcessor()
        self.__reporter.verbose(self.__verbose, [f'configuration {config_file}'])

    def read_configuration(self, verbose: bool = False) -> Optional[IINIProcessor]:
        '''
            Reads a configuration from an INI file.

            :param verbose: Enable/Disable verbose option (default False)
            :type verbose: <bool>
            :return: Configuration object | None
            :rtype: <Optional[IINIProcessor]>
            :exceptions: None
        '''
        with ConfFile(
            self.__file_path,
            self.__MODE,
            self.__EXT,
            self.__checker,
            self.__reporter,
            self.__file_checker,
            self.__verbose or verbose
        ) as ini:
            if bool(ini):
                if self.__ini_processor.from_stream(ini):
                    self.__reporter.verbose(
                        self.__verbose or verbose, [f'configuration {self.__ini_processor}']
                    )
                    return self.__ini_processor
        return None
