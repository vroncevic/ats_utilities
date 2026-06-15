# -*- coding: UTF-8 -*-

'''
Module
    cfg2object.py
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
    Defines class Cfg2Object with attribute(s) and method(s).
    Creates an API for reading configuration from a CFG file.
'''

from typing import List, Optional
from ats_utilities.config_io.iread import IRead
from ats_utilities.checker.ichecker import IATSChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.console_io.proxy_reporter import vreporter
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.cfg.icfg_processor import ICFGProcessor
from ats_utilities.config_io.cfg.cfg_processor import ATSCFGProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Cfg2Object(IRead):
    '''
        Defines class Cfg2Object with attribute(s) and method(s).
        Creates an API for reading configuration from a CFG file.
        Conversion of CFG content to Python object.

        It defines:

            :attributes:
                | __EXT - File extension of the configuration file.
                | __MODE - File open mode.
                | __REGEX_EXP - Regular expression for matching line.
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __file_checker - FileCheck for checking file.
                | __file_path - Configuration file path.
                | __verbose - Enable/Disable verbose option.
            :methods:
                | __init__ - Initials Cfg2Object constructor.
                | read_configuration - Reads configuration from a CFG file.
                | __str__ - Returns the string representation of cfg2object.
    '''

    __EXT: str = 'cfg'
    __MODE: str = 'r'

    def __init__(
        self,
        config_file: Optional[str],
        cfg_processor: Optional[ICFGProcessor] = None,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        file_checker: Optional[IFileCheck] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials Cfg2Object constructor.

            :param config_file: Configuration file path in string format | None
            :type config_file: <Optional[str]>
            :param cfg_processor: Processor for CFG content | None
            :type cfg_processor: <Optional[ICFGProcessor]>
            :param checker: Parameters checker (default set ATSChecker) | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: Reporter for messaging (default set ATSReporter) | None
            :type reporter: <Optional[IATSReporter]>
            :param file_checker: FileCheck for checking file | None
            :type file_checker: <Optional[IFileCheck]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions:  ATSTypeError
        '''
        # No dependency injection then use default ones.
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter(self.__checker)
        self.__verbose: bool = verbose
        self.__file_checker: IFileCheck = file_checker or FileCheck(
            self.__checker, self.__reporter, self.__verbose
        )
        self.__cfg_processor: ICFGProcessor = cfg_processor or ATSCFGProcessor()
        self.__file_path: str = str(config_file)
        self.__reporter.verbose(self.__verbose, [f'configuration {config_file}'])

    @vreporter('read configuration from file {file_path}')
    def read_configuration(self, verbose: bool = False) -> Optional[ICFGProcessor]:
        '''
            Reads a configuration from a CFG file.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Configuration object
            :rtype: <Optional[ICFGProcessor]>
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
        ) as cfg:
            if bool(cfg):
                lines = cfg.readlines()
                if self.__cfg_processor.from_lines(lines):
                    self.__reporter.verbose(
                        self.__verbose or verbose, [f'configuration {self.__cfg_processor.to_string()}']
                    )
                    return self.__cfg_processor
        return None

    def __str__(self) -> str:
        '''
            Returns the string representation of cfg2object.

            :return: The cfg2object string representation
            :rtype: <str>
            :exceptions: None
        '''
        file_path = str(self.__file_path).replace('\n', '\n    ')
        checker = str(self.__checker).replace('\n', '\n    ')
        reporter = str(self.__reporter).replace('\n', '\n    ')
        file_checker = str(self.__file_checker).replace('\n', '\n    ')
        cfg_processor = str(self.__cfg_processor).replace('\n', '\n    ')
        verbose = str(self.__verbose).replace('\n', '\n    ')

        return (
            f'<{self.__class__.__name__}(\n'
            f'    file_path={file_path},\n'
            f'    checker={checker},\n'
            f'    reporter={reporter},\n'
            f'    file_checker={file_checker},\n'
            f'    cfg_processor={cfg_processor},\n'
            f'    verbose={verbose}\n)> at 0x{id(self):x}'
        )
