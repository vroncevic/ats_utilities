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
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.cfg.icfg_processor import ICFGProcessor
from ats_utilities.checker.decorator import validates_parameters

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
                | __reporter - ATSReporter for messaging.
                | __file_checker - FileCheck for checking file.
                | __file_path - Configuration file path.
                | __verbose - Enable/Disable verbose option.
            :methods:
                | __init__ - Initials Object2Cfg constructor.
                | write_configuration - Writes configuration to a CFG file.
    '''

    __EXT: str = 'cfg'
    __MODE: str = 'w'

    @validates_parameters([('Optional[str]:config_file', None)])
    def __init__(
        self,
        config_file: Optional[str],
        reporter: Optional[IATSReporter] = None,
        file_checker: Optional[IFileCheck] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials Object2Cfg constructor.

            :param config_file: Configuration file path | None
            :type config_file: <Optional[str]>
            :param reporter: ATSReporter for check operations | None
            :type reporter: <Optional[IATSReporter]>
            :param file_checker: FileCheck for checking file | None
            :type file_checker: <Optional[IFileCheck]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError
        '''
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__file_checker: IFileCheck = file_checker or FileCheck(reporter, verbose)
        self.__verbose: bool = verbose
        self.__file_path: str = str(config_file)
        self.__reporter.verbose(self.__verbose, [f'configuration file {config_file}'])

    @validates_parameters([('Optional[ICFGProcessor]:config', None)])
    def write_configuration(self, config: Optional[ICFGProcessor], verbose: bool = False) -> bool:
        '''
            Writes a configuration to a CFG file.

            :param config: Configuration object | None
            :type config: <Optional[ICFGProcessor]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (configuration written to file) | False
            :rtype: <bool>
            :exceptions: ATSTypeError
        '''
        status: bool = False

        if not bool(config):
            return status

        self.__reporter.verbose(self.__verbose or verbose, [f'configuration {config}'])
        cfg_string = config.to_string()

        with ConfFile(
            self.__file_path,
            self.__MODE,
            self.__EXT,
            self.__reporter,
            self.__file_checker,
            self.__verbose or verbose
        ) as cfg:
            if bool(cfg):
                cfg.write(cfg_string)
                status = True
        return status
