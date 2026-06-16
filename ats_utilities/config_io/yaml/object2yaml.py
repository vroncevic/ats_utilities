# -*- coding: UTF-8 -*-

'''
Module
    object2yaml.py
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
    Defines class Object2Yaml with attribute(s) and method(s).
    Creates an API for writing a configuration to a YAML file.
'''

from typing import ClassVar, List, Optional
from ats_utilities.checker.ichecker import IATSChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.checker.ichecker import ErrorChecker
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.yaml.iyaml_processor import IYAMLProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Object2Yaml(IWrite):
    '''
        Defines class Object2Yaml with attribute(s) and method(s).
        Creates an API for writing a configuration to a YAML file.
        Conversion of Python object to YAML content.

        It defines:

            :attributes:
                | _EXT - File extension of the configuration file.
                | _verbose - Enable/Disable verbose option.
                | _file_path - Configuration file path.
            :methods:
                | __init__ - Initials Object2Yaml constructor.
                | write_configuration - Writes configuration to a YAML file.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker
    __EXT: str = 'yaml'
    __MODE: str = 'w'

    def __init__(
        self,
        config_file: Optional[str],
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        file_checker: Optional[IFileCheck] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials Object2Cfg constructor.

            :param config_file: Configuration file path | None
            :type config_file: <Optional[str]>
            :param checker: ATSChecker for check operations | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: ATSReporter for check operations | None
            :type reporter: <Optional[IATSReporter]>
            :param file_checker: FileCheck for checking file | None
            :type file_checker: <Optional[IFileCheck]>
            :param verbose: Enable/Disable verbose option (default False)
            :type verbose: <bool>
            :exceptions: ATSTypeError
        '''
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter()
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
        self.__reporter.verbose(self.__verbose, [f'configuration file {config_file}'])

    def write_configuration(self, config: Optional[IYAMLProcessor], verbose: bool = False) -> bool:
        '''
            Writes configuration to a YAML file.

            :param verbose: Enable/Disable verbose option (default False)
            :type verbose: <bool>
            :param config: Configuration object | None
            :type config: <Optional[IYAMLProcessor]>
            :return: True (configuration written to the file) | False
            :rtype: <bool>
            :exception: ATSTypeError
        '''
        status: bool = False
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.__checker.validate_parameters([('IYAMLProcessor:config', config)])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)

        if not bool(config):
            return status

        self.__reporter.verbose(self.__verbose or verbose, [f'configuration {config}'])

        with ConfFile(
            self.__file_path,
            self.__MODE,
            self.__EXT,
            self.__checker,
            self.__reporter,
            self.__file_checker,
            self.__verbose or verbose
        ) as yaml:
            if bool(yaml):
                yaml.write(config.encode())
                status = True
        return status
