# -*- coding: UTF-8 -*-

'''
Module
    ats_cli.py
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
    Defines class ATSCli with attribute(s) and method(s).
    Creates an API for checks and loads an information argument parser.
'''

from typing import Any, List, Optional
from abc import abstractmethod
from ats_utilities.factory_class import (
    inject, get_private_attr, make_component, validate_component, format_instance_to_string
)
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.engine import ATSChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import ATSReporter
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.cli.icli import IATSCli
from ats_utilities.cli.icli import ArgSeq
from ats_utilities.cli.iconfig_manager import IConfigManager
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.cli.iconfig_manager import Config
from ats_utilities.cli.config_manager import ATSConfigManager

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

class ATSCli(IATSCli):
    '''
        Defines class ATSCli with attribute(s) and method(s).
        Creates an API for checks and loads an information argument parser.
        Command-line interface configuration.

        It defines:

            :attributes:
                | __config - CLI configuration object.
                | __config_manager - Manager for configuration loading.
                | __operational - Status for tool | generator (default False).
                | __verbose - Enable/Disable verbose option.
            :methods:
                | __init__ - Initials ATSCli constructor.
                | is_operational - Checks is tool | generator operational.
                | add_new_option - Adds a new option for the the CL interface.
                | parse_args - Parses the CLI arguments.
                | process - Processes and runs tool operations (Abstract).
    '''

    def __init__(
        self,
        info_file: Optional[str] = None,
        config_manager: Optional[IConfigManager] = None,
        config2object: Optional[IRead] = None,
        object2config: Optional[IWrite] = None,
        info_manager: Optional[IInfoManager] = None,
        strategy: Optional[IATSArgParseStrategy] = None,
        options_parser: Optional[IATSOptionParser] = None,
        checker: Optional[IChecker] = None,
        reporter: Optional[IReporter] = None,
        file_checker: Optional[IFileCheck] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSCli constructor.

            :param info_file: Information file path | None
            :type info_file: <Optional[str]>
            :param config_manager: Configuration manager | None
            :type config_manager: <Optional[IConfigManager]>
            :param reporter: ATSReporter for check operations | None
            :type reporter: <Optional[IReporter]>
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
        )
        self.__config_manager: IConfigManager = make_component(config_manager, ATSConfigManager, {
            'checker': self._checker,
            'reporter': self._reporter,
            'verbose': self._verbose
        })

        self.__config: Config = self.__config_manager.load_config(info_file, self._verbose)
        self.__operational: bool = False

    def is_operational(self) -> bool:
        '''
            Checks is tool | generator operational.

            :return: True (tool | generator is operational) | False
            :rtype: <bool>
            :exceptions: None
        '''
        if self.__config:
            self.__operational = self.__config.is_tool_ok()
        return self.__operational

    def add_new_option(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds a new option for the CL interface.

            :param args: Arguments in string form
            :type args: <str>
            :param kwargs: arguments in Any form
            :type kwargs: <Any>
            :exceptions: None
        '''
        if self.__config and self.__config.option_parser:
            self.__config.option_parser.add_operation(*args, **kwargs)

    def parse_args(self, argv: ArgSeq) -> Optional[OptionNamespace]:
        '''
            Parses the CLI arguments.

            :param argv: Sequence of arguments | None
            :type argv: <ArgSeq>
            :return: Options and arguments
            :rtype: <Optional[OptionNamespace]>
            :exceptions: ATSTypeError
        '''
        if self.__config and self.__config.option_parser:
            return self.__config.option_parser.parse_args(argv)
        return None

    @abstractmethod
    def process(self, verbose: bool = False) -> bool:
        '''
            Processes and runs tool operations (Abstract).

            :param verbose: Enable/Disable verbose option (default False)
            :type verbose: <bool>
            :return: True (successfully finished) | False
            :rtype: <bool>
            :exceptions: TypeError
        '''
        raise NotImplementedError("Method process() must be implemented.")

    @property
    def _checker(self) -> IChecker:
        '''
            Property method for getting the internal checker instance.

            :return: The checker instance in IChecker format
            :rtype: <IChecker>
            :exceptions: None
        '''
        return get_private_attr(self, 'checker')

    @property
    def _reporter(self) -> IReporter:
        '''
            Property method for getting the internal reporter instance.

            :return: The reporter instance in IReporter format
            :rtype: <IReporter>
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

    def __str__(self) -> str:
        '''
            Returns the string representation of command line interface component.

            :return: The command line interface component as string
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)


#from ats_utilities.info.iinfo_manager import IInfoManager
#from ats_utilities.info.ats_info_manager import ATSInfoManager
#from ats_utilities.option.ioption_parser import IATSOptionParser
#from ats_utilities.option.ats_option_parser import ATSOptionParser
#from ats_utilities.config_io.base_bundle import ATSBaseBundle

        #if bool(information):
        #    info_manager: IInfoManager = make_component(base_bundle.info_manager, ATSInfoManager, {
        #        'info': information.to_dict(),
        #        'checker': self._checker,
        #        'reporter': self._reporter,
        #        'verbose': self._verbose
        #    })
        #
        #    if info_manager and info_manager.base_info_is_ok(information.to_dict()):
        #        self.__option_parser = make_component(base_bundle.options_parser, ATSOptionParser, {
        #            'parameters': information.to_dict(),
        #            'strategy': base_bundle.strategy,
        #            'checker': self._checker,
        #            'reporter': self._reporter,
        #            'verbose': self._verbose
        #        })
        #
        #        if self.__option_parser:
        #            self.__option_parser.add_version_operation(info_manager.get_version())
        #            self.__tool_operational = True
