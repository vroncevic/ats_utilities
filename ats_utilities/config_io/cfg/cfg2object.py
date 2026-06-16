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
from ats_utilities.factory import inject, get_private_attr, format_instance_to_string
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
                | __file_checker - FileCheck for checking file (default set FileCheck).
                | __cfg_processor - Processor for CFG content (default set ATSCFGProcessor).
                | __file_path - Configuration file path (default set None).
                | __verbose - Enable/Disable verbose option (default False).
            :methods:
                | __init__ - Initials Cfg2Object constructor.
                | read_configuration - Reads configuration from a CFG file.
                | _checker - Property method for getting the internal checker instance.
                | _reporter - Property method for getting the internal reporter instance.
                | _verbose - Property method for getting the internal verbose flag.
                | _file_checker - Property method for getting the internal file checker instance.
                | _cfg_processor - Property method for getting the internal cfg processor.
                | __str__ - Returns the string representation of cfg2object.
    '''

    __EXT: str = 'cfg'
    __MODE: str = 'r'

    def __init__(
        self,
        config_file: Optional[str],
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        file_checker: Optional[IFileCheck] = None,
        cfg_processor: Optional[ICFGProcessor] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials Cfg2Object constructor.

            :param config_file: Configuration file path in string format | None
            :type config_file: <Optional[str]>
            :param checker: Parameters checker (default set ATSChecker) | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: Reporter for messaging (default set ATSReporter) | None
            :type reporter: <Optional[IATSReporter]>
            :param file_checker: FileCheck for checking file | None
            :type file_checker: <Optional[IFileCheck]>
            :param cfg_processor: Processor for CFG content | None
            :type cfg_processor: <Optional[ICFGProcessor]>
            :param verbose: Enable/Disable verbose option (default False)
            :type verbose: <bool>
            :exceptions: None
        '''
        # No dependency injection then use default ones.
        inject(
            self,
            ('checker', checker, ATSChecker, None),
            ('reporter', reporter, ATSReporter, ['checker']),
            ('verbose', verbose, False, None),
            ('file_checker', file_checker, FileCheck, ['checker', 'reporter', 'verbose']),
            ('cfg_processor', cfg_processor, ATSCFGProcessor, None)
        )
        self.__file_path: str = str(config_file)

    @vreporter('read configuration from file {file_path}')
    def read_configuration(self, verbose: bool = False) -> Optional[ICFGProcessor]:
        '''
            Reads a configuration from a CFG file.

            :param verbose: Enable/Disable verbose option (default False)
            :type verbose: <bool>
            :return: Configuration object
            :rtype: <Optional[ICFGProcessor]>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        with ConfFile(
            self.__file_path,
            self.__MODE,
            self.__EXT,
            self._checker,
            self._reporter,
            self._file_checker,
            self._verbose or verbose
        ) as cfg:
            if bool(cfg):
                lines = cfg.readlines()
                if self._cfg_processor.from_lines(lines):
                    return self._cfg_processor
        return None

    @property
    def _checker(self) -> IATSChecker:
        '''
            Property method for getting the internal checker instance.

            :return: The checker instance in IATSChecker format
            :rtype: <IATSChecker>
            :exceptions: None
        '''
        return get_private_attr(self, 'checker')

    @property
    def _reporter(self) -> IATSReporter:
        '''
            Property method for getting the internal reporter instance.

            :return: The reporter instance in IATSReporter format
            :rtype: <IATSReporter>
            :exceptions: None
        '''
        return get_private_attr(self, 'reporter')

    @property
    def _verbose(self) -> bool:
        '''
            Property method for getting the internal verbose flag.

            :return: The verbose flag in bool format
            :rtype: <bool>
            :exceptions: None
        '''
        return get_private_attr(self, 'verbose')

    @property
    def _file_checker(self) -> IFileCheck:
        '''
            Property method for getting the internal file checker instance.

            :return: The file checker instance in IFileCheck format
            :rtype: <IFileCheck>
            :exceptions: None
        '''
        return get_private_attr(self, 'file_checker')

    @property
    def _cfg_processor(self) -> ICFGProcessor:
        '''
            Property method for getting the internal cfg processor.

            :return: The cfg processor instance in ICFGProcessor format
            :rtype: <ICFGProcessor>
            :exceptions: None
        '''
        return get_private_attr(self, 'cfg_processor')

    def __str__(self) -> str:
        '''
            Returns the string representation of CFG object.

            :return: The CFG object as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
