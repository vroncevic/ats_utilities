# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Defines class ATSBase with attribute(s) and method(s).
    Creates an API for setup ATS (application, tool, script).
'''

from typing import Any, Dict, List, Optional
from abc import abstractmethod

from ats_utilities.base.ibase import IBase
from ats_utilities.base.ibase import ArgSeq
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.base.component_bundle import BaseComponentBundle
from ats_utilities.config_io.config_loader_bundle import ATSConfigLoaderBundle
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.option.component_bundle import OptionComponentBundle
from ats_utilities.logging.component_bundle import LoggingComponentBundle
from ats_utilities.logging.engine import ATSLoggerManager
from ats_utilities.logging.ilogger_manager import ILoggerManager
from ats_utilities.config_io.iconfig_loader import IConfigLoader, Config
from ats_utilities.config_io.config_loader import ATSConfigLoader
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.info.engine import InfoManager
from ats_utilities.info.component_bundle import InfoComponentBundle
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.option.engine import OptionManager
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import get_private_attr, format_instance_to_string
from ats_utilities.factory_component import make_component, validate_component

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSBase(IBase):
    '''
        Defines class ATSBase with attribute(s) and method(s).
        Creates an API for setup ATS (application, tool, script).

        It defines:

            :attributes:
                | __config - CLI configuration object.
                | __config_loader - Manager for configuration loading.
                | __operational - Status for tool | generator (default False).
                | __verbose - Enable/Disable verbose option.
            :methods:
                | __init__ - Initializes ATSBase constructor.
                | is_operational - Checks is tool | generator operational.
                | add_new_option - Adds a new option for the the CL interface.
                | parse_args - Parses the CLI arguments.
                | process - Processes and runs tool operations (Abstract).
    '''

    def __init__(self, component_bundle: Optional[BaseComponentBundle] = None) -> None:
        '''
            Initializes ATSBase constructor.

            :param component_bundle: Component bundle for base package | None.
            :type component_bundle: <Optional[BaseComponentBundle]>
            :exceptions: ATSTypeError.
        '''
        bundle: BaseComponentBundle = component_bundle or BaseComponentBundle()
        factory_context_bundle(self, bundle.context_bundle)
        shared_context: ContextBundle = ContextBundle(
            checker=get_private_attr(self, 'checker'),
            reporter=get_private_attr(self, 'reporter'),
            verbose=get_private_attr(self, 'verbose')
        )
        shared_config_file_bundle: ATSConfigFileBundle = ATSConfigFileBundle(context=shared_context)

        share_config_loader_bundle: ATSConfigLoaderBundle = ATSConfigLoaderBundle(
            info_file=bundle.info_file, config_bundle=shared_config_file_bundle
        )

        self.__config_loader: IConfigLoader = make_component(
            bundle.config_loader, ATSConfigLoader, {'config_loader_bundle': share_config_loader_bundle}
        )
        validate_component(self.__config_loader, type(self.__config_loader), type(self.__config_loader).__name__)
        loader: Config = self.__config_loader.setup_config_loader()
        configuration: Dict[str, str] = loader.get_configuration()

        info_component_bundle: InfoComponentBundle = InfoComponentBundle(
            context_bundle=shared_context
        )

        self.__info_manager = make_component(bundle.info_manager, InfoManager, {'component_bundle': info_component_bundle})
        validate_component(self.__info_manager, type(self.__info_manager), type(self.__info_manager).__name__)
        self.__info_manager.set_info(configuration)

        option_component_bundle: OptionComponentBundle = OptionComponentBundle(
            parameters=configuration, context_bundle=shared_context
        )

        self.__options_parser = make_component(
            bundle.options_parser, OptionManager, {'component_bundle': option_component_bundle}
        )
        validate_component(self.__options_parser, type(self.__options_parser), type(self.__options_parser).__name__)

        logging_component_bundle: LoggingComponentBundle = LoggingComponentBundle(
            context_bundle=shared_context
        )

        self.__logger_manager: ILoggerManager = make_component(
            bundle.logger_manager, ATSLoggerManager, {'component_bundle': logging_component_bundle}
        )
        validate_component(self.__logger_manager, type(self.__logger_manager), type(self.__logger_manager).__name__)

        self.__operational: bool = False

    def is_operational(self) -> bool:
        '''
            Checks is tool | generator operational.

            :return: True (tool | generator is operational) | False.
            :rtype: <bool>
            :exceptions: None.
        '''
        if self.__config:
            self.__operational = self.__config.is_tool_ok()
        return self.__operational

    def add_new_option(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds a new option for the CL interface.

            :param args: Arguments in string form.
            :type args: <str>
            :param kwargs: arguments in Any form.
            :type kwargs: <Any>
            :exceptions: None.
        '''
        if self.__config and self.__config.option_parser:
            self.__config.option_parser.add_operation(*args, **kwargs)

    def parse_args(self, argv: ArgSeq) -> Optional[OptionNamespace]:
        '''
            Parses the CLI arguments.

            :param argv: Sequence of arguments | None.
            :type argv: <ArgSeq>
            :return: Options and arguments.
            :rtype: <Optional[OptionNamespace]>
            :exceptions: ATSTypeError.
        '''
        if self.__config and self.__config.option_parser:
            return self.__config.option_parser.parse_args(argv)
        return None

    @abstractmethod
    def process(self, verbose: bool = False) -> bool:
        '''
            Processes and runs tool operations (Abstract).

            :param verbose: Enable/Disable verbose option (default False).
            :type verbose: <bool>
            :return: True (successfully finished) | False.
            :rtype: <bool>
            :exceptions: TypeError.
        '''
        raise NotImplementedError("Method process() must be implemented.")

    def __str__(self) -> str:
        '''
            Returns the ATS base as string representation.

            :return: The ATS base as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)

