# -*- coding: UTF-8 -*-

'''
Module
    object2cfg.py
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
    Defines class Object2Cfg with attribute(s) and method(s).
    Creates an API for writing configuration to a CFG file.
'''

from typing import List, Optional
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.checker.ichecker import IATSChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.console_io.proxy_reporter import vreporter
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.cfg.icfg_processor import ICFGProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Object2Cfg(IWrite):
    '''
        Defines class Object2Cfg with attribute(s) and method(s).
        Creates an API for writing configuration to a CFG file.
        Conversion of Python object to CFG content.

        It defines:

            :attributes:
                | __EXT - File extension of the configuration file.
                | __MODE - File open mode.
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __file_checker - FileCheck for checking file.
                | __file_path - Configuration file path.
                | __verbose - Enable/Disable verbose option (default False).
            :methods:
                | __init__ - Initials Object2Cfg constructor.
                | write_configuration - Writes configuration to a CFG file.
    '''

    __EXT: str = 'cfg'
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
            :param checker: Parameters checker (default set ATSChecker) | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: Reporter for messaging (default set ATSReporter) | None
            :type reporter: <Optional[IATSReporter]>
            :param file_checker: FileCheck for checking file | None
            :type file_checker: <Optional[IFileCheck]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError
        '''
        # No dependency injection then use default ones.
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter(checker=self.__checker)
        self.__verbose: bool = verbose
        self.__file_checker: IFileCheck = file_checker or FileCheck(
            checker=self.__checker, reporter=self.__reporter, verbose=self.__verbose
        )
        self.__file_path: str = str(config_file)

    @validator([('Optional[ICFGProcessor]:config', None)])
    @vreporter('write configuration to file {file_path}')
    def write_configuration(self, config: Optional[ICFGProcessor], verbose: bool = False) -> bool:
        '''
            Writes a configuration to a CFG file.

            :param config: Configuration object | None
            :type config: <Optional[ICFGProcessor]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (configuration written to file) | False
            :rtype: <bool>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        status: bool = False

        if not bool(config):
            return status

        cfg_string = config.to_string()

        with ConfFile(
            self.__file_path,
            self.__MODE,
            self.__EXT,
            self.__checker,
            self.__reporter,
            self.__file_checker,
            self.__verbose or verbose
        ) as cfg:
            if bool(cfg):
                cfg.write(cfg_string)
                status = True

        return status

    def __str__(self) -> str:
        '''
            Returns the string representation of ATS version.

            :return: The ATS version string representation
            :rtype: <str>
            :exceptions: None
        '''
        file_path = str(self.__file_path).replace('\n', '\n    ')
        checker = str(self.__checker).replace('\n', '\n    ')
        reporter = str(self.__reporter).replace('\n', '\n    ')
        file_checker = str(self.__file_checker).replace('\n', '\n    ')
        verbose = str(self.__verbose).replace('\n', '\n    ')

        return (
            f'<{self.__class__.__name__}(\n'
            f'    file_path={file_path},\n'
            f'    checker={checker},\n'
            f'    reporter={reporter},\n'
            f'    file_checker={file_checker},\n'
            f'    verbose={verbose}\n)> at 0x{id(self):x}'
        )
