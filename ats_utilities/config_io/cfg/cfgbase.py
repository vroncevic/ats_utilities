# -*- coding: UTF-8 -*-

'''
Module
    cfgbase.py
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
    Defines class CfgBase with attribute(s) and method(s).
    Loads the ATS configuration for the ATS.
'''

from typing import List, Optional
from ats_utilities.factory import (
    inject, get_private_attr, make_component, validate_component, format_instance_to_string
)
from ats_utilities.info.iinfo_manager import IATSInfoManager
from ats_utilities.info.ats_info_manager import ATSInfoManager
from ats_utilities.option.ioption_parser import IATSOptionParser
from ats_utilities.option.ats_option_parser import ATSOptionParser
from ats_utilities.checker.ichecker import IATSChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.option.iparser_strategy import IATSArgParseStrategy
from ats_utilities.config_io.cfg.cfg2object import Cfg2Object
from ats_utilities.config_io.cfg.object2cfg import Object2Cfg
from ats_utilities.config_io.cfg.cfg_processor import ATSCFGProcessor
from ats_utilities.config_io.cfg.icfg_processor import ICFGProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class CfgBase:
    '''
        Defines class CfgBase with attribute(s) and method(s).
        Loads the ATS configuration for the ATS.
        CFG configuration-based API support.

        It defines:

            :attributes:
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
                | __file_checker - FileCheck for checking file (default set FileCheck).
                | __cfg2obj - In API for information (default set Cfg2Object).
                | __obj2cfg - Out API for information (default set Object2Cfg).
                | __tool_operational - Control ATS operational functionality (default False).
                | __info_manager - Information manager (default set ATSInfoManager).
                | __option_parser - Option parser for ATS (default set ATSOptionParser).
            :methods:
                | __init__ - Initials CfgBase constructor.
                | is_tool_ok - Checks is tool operational.
                | _checker - Property method for getting the internal checker instance.
                | _reporter - Property method for getting the internal reporter instance.
                | _verbose - Property method for getting the internal verbose flag.
                | _file_checker - Property method for getting the internal file checker instance.
                | option_parser - Property method for getting the internal option parser instance.
                | __str__ - Returns the string representation of cfgbase.
    '''

    def __init__(
        self,
        info_file: Optional[str] = None,
        cfg2object: Optional[IRead] = None,
        object2cfg: Optional[IWrite] = None,
        info_manager: Optional[IATSInfoManager] = None,
        strategy: Optional[IATSArgParseStrategy] = None,
        options_parser: Optional[IATSOptionParser] = None,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        file_checker: Optional[IFileCheck] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials CfgBase constructor.

            :param info_file: Path to the info file | None
            :type info_file: <Optional[str]>
            :param cfg2object: In API for information (default set Cfg2Object) | None
            :type cfg2object: <Optional[IRead]>
            :param object2cfg: Out API for information (default set Object2Cfg) | None
            :type object2cfg: <Optional[IWrite]>
            :param options_parser: Option parser for ATS | None
            :type options_parser: <Optional[IATSOptionParser]>
            :param checker: Parameters checker (default set ATSChecker) | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: Reporter for messaging (default set ATSReporter) | None
            :type reporter: <Optional[IATSReporter]>
            :param file_checker: FileCheck for checking file (default set FileCheck) | None
            :type file_checker: <Optional[IFileCheck]>
            :param strategy: Strategy for argument parsing (default set ATSArgParseStrategy) | None
            :type strategy: <Optional[IATSArgParseStrategy]>
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
            ('file_checker', file_checker, FileCheck, ['checker', 'reporter', 'verbose'])
        )
        self.__option_parser: Optional[IATSOptionParser] = None

        self.__cfg2obj: IRead = make_component(cfg2object, Cfg2Object, {
            'config_file': info_file,
            'cfg_processor': ATSCFGProcessor(),
            'checker': self._checker,
            'reporter': self._reporter,
            'file_checker': self._file_checker,
            'verbose': self._verbose
        })
        validate_component(self.__cfg2obj, IRead, 'cfg2object')

        self.__obj2cfg: IWrite = make_component(object2cfg, Object2Cfg, {
            'config_file': info_file,
            'checker': self._checker,
            'reporter': self._reporter,
            'file_checker': self._file_checker,
            'verbose': self._verbose
        })
        validate_component(self.__obj2cfg, IWrite, 'object2cfg')

        information: Optional[ICFGProcessor] = None
        self.__tool_operational: bool = False

        if bool(self.__cfg2obj) and bool(self.__obj2cfg):
            information = self.__cfg2obj.read_configuration(self._verbose)

        if bool(information):
            self.__info_manager: IATSInfoManager = make_component(info_manager, ATSInfoManager, {
                'info': information.to_dict(),
                'checker': self._checker,
                'reporter': self._reporter,
                'verbose': self._verbose
            })

            if self.__info_manager and self.__info_manager.base_info_is_ok(information.to_dict()):
                self.__option_parser = make_component(options_parser, ATSOptionParser, {
                    'parameters': information.to_dict(),
                    'strategy': strategy,
                    'checker': self._checker,
                    'reporter': self._reporter,
                    'verbose': self._verbose
                })

                if self.__option_parser:
                    self.__option_parser.add_version_operation(self.__info_manager.get_version())
                    self.__tool_operational = True

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
    def option_parser(self) -> Optional[IATSOptionParser]:
        '''
            Property method for getting the internal option parser instance.

            :return: Option parser for ATS | None
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

    def __str__(self) -> str:
        '''
            Returns the string representation of CFG base object.

            :return: The CFG base object as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
