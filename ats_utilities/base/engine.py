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
    Defines class Base with attribute(s) and method(s).
    Creates an API for setup ATS (application, tool, script).
'''

from abc import abstractmethod
from typing import Any
from ats_utilities.base.ibase import IBase
from ats_utilities.base.ibase import ArgSeq
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.base.component_bundle import BaseComponentBundle
from ats_utilities.config_io.config_loader_bundle import ATSConfigLoaderBundle
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.option.component_bundle import OptionComponentBundle
from ats_utilities.logging.component_bundle import LoggingComponentBundle
from ats_utilities.logging.engine import ATSLoggerManager
from ats_utilities.logging.ilogger_manager import ILoggerManager
from ats_utilities.config_io.iconfig_loader import IConfigLoader, Config
from ats_utilities.config_io.config_loader import ConfigLoader
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.info.engine import InfoManager
from ats_utilities.info.component_bundle import InfoComponentBundle
from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.splasher.engine import Splasher
from ats_utilities.splasher.component_bundle import SplashComponentBundle
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.option.engine import OptionManager
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import get_class_name, format_instance_to_string
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.exceptions.ats_runtime_error import ATSRuntimeError
from ats_utilities.exceptions.ats_attribute_error import ATSAttributeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Base(IBase):
    '''
        Defines class Base with attribute(s) and method(s).
        Creates an API for setup ATS (application, tool, script).

        It defines:

            :attributes:
                | _checker - Factoriezed parameters checker (default Checker).
                | _reporter - Factoriezed reporter for messaging (default Reporter).
                | _verbose - Factoriezed Enable/Disable verbose option (default False).
                | _operational - Status for ATS (default False).
                | _config_loader - Manager for configuration loading.
                | _info_manager - Manager for info component.
                | _splasher - Manager for splash component.
                | _options_parser - Manager for options parser.
                | _logger_manager - Manager for logger component.
                | _is_initialized - Indicates if the base component is initialized (default False).
            :methods:
                | __init__ - Initializes Base constructor.
                | is_operational - Checks is ATS operational.
                | is_initialized - Checks if the base component is initialized.
                | add_new_option - Adds a new option for the the CL interface.
                | parse_args - Parses the CLI arguments.
                | process - Processes and runs tool operations (Abstract).
                | __str__ - Returns the ATS base as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(self, component_bundle: BaseComponentBundle | None = None) -> None:
        '''
            Initializes Base constructor.

            :param component_bundle: Component bundle for base package | None.
            :type component_bundle: <BaseComponentBundle | None>
            :exceptions: None.
        '''
        # No dependency injection then use default ones.
        bundle: BaseComponentBundle = component_bundle or BaseComponentBundle()
        factory_context_bundle(self, bundle.context_bundle)
        shared_context: ContextBundle = ContextBundle(
            checker=self._checker, reporter=self._reporter, verbose=self._verbose
        )
        self._operational: bool = False
        self._is_initialized: bool = False
        self._config_loader: IConfigLoader | None = None
        self._info_manager: IInfoManager | None = None
        self._splasher: ISplasher | None = None
        self._options_parser: IOptionManager | None = None
        self._logger_manager: ILoggerManager | None = None

        try:
            shared_config_file_bundle: ATSConfigFileBundle = ATSConfigFileBundle(context=shared_context)
            share_config_loader_bundle: ATSConfigLoaderBundle = ATSConfigLoaderBundle(
                info_file=bundle.info_file, config_bundle=shared_config_file_bundle
            )
            info_component_bundle: InfoComponentBundle = InfoComponentBundle(context_bundle=shared_context)

            self._config_loader: IConfigLoader = make_component(
                bundle.config_loader, ConfigLoader, {'config_loader_bundle': share_config_loader_bundle}
            )
            validate_component(self._config_loader, type(self._config_loader), type(self._config_loader).__name__)
            loader: Config = self._config_loader.setup_config_loader()

            self._info_manager: IInfoManager = make_component(bundle.info_manager, InfoManager, {'component_bundle': info_component_bundle})
            validate_component(self._info_manager, type(self._info_manager), type(self._info_manager).__name__)
            self._info_manager.set_info(loader.load_configuration())

            splash_component_bundle: SplashComponentBundle = SplashComponentBundle(
                prop=self._info_manager.get_info(), context_bundle=shared_context
            )

            self._splasher: ISplasher = make_component(bundle.splasher, Splasher, {'component_bundle': splash_component_bundle})
            validate_component(self._splasher, type(self._splasher), type(self._splasher).__name__)

            option_component_bundle: OptionComponentBundle = OptionComponentBundle(
                parameters=self._info_manager.get_info(), context_bundle=shared_context
            )

            self._options_parser: IOptionManager = make_component(
                bundle.options_parser, OptionManager, {'component_bundle': option_component_bundle}
            )
            validate_component(self._options_parser, type(self._options_parser), type(self._options_parser).__name__)

            logging_component_bundle: LoggingComponentBundle = LoggingComponentBundle(context_bundle=shared_context)

            self._logger_manager: ILoggerManager = make_component(
                bundle.logger_manager, ATSLoggerManager, {'component_bundle': logging_component_bundle}
            )
            validate_component(self._logger_manager, type(self._logger_manager), type(self._logger_manager).__name__)

            self._operational = all(
                component.is_initialized() for component in [self._info_manager, self._options_parser, self._logger_manager]
            )
            self._is_initialized = True

        except (ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError) as exc:
            self._reporter.error([f"{get_class_name(self)} - error during initialization: {exc}"])

    def is_operational(self) -> bool:
        '''
            Checks is ATS operational.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None..
        '''
        return self._operational

    def is_initialized(self) -> bool:
        '''
            Checks if the base component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        return self._is_initialized and self._operational

    def add_new_option(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds a new option for the CL interface.

            :param args: Arguments in string form.
            :type args: <str>
            :param kwargs: arguments in Any form.
            :type kwargs: <Any>
            :exceptions: None..
        '''
        if self._options_parser:
            self._options_parser.add_operation(*args, **kwargs)

    def parse_args(self, argv: ArgSeq) -> OptionNamespace | None:
        '''
            Parses the CLI arguments.

            :param argv: Sequence of arguments | None.
            :type argv: <ArgSeq>
            :return: Options and arguments.
            :rtype: <OptionNamespace | None>
            :exceptions: ATSTypeError.
        '''
        if self._options_parser:
            return self._options_parser.parse_args(argv)

        return None

    @abstractmethod
    def process(self, verbose: bool = False) -> bool:
        '''
            Processes and runs tool operations (Abstract).

            :param verbose: Enable/Disable verbose option (default False).
            :type verbose: <bool>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: TypeError.
        '''
        raise NotImplementedError("Method process() must be implemented.")

    def __str__(self) -> str:
        '''
            Returns the ATS base as string representation.

            :return: The ATS base as string representation.
            :rtype: <str>
            :exceptions: None..
        '''
        return format_instance_to_string(self)

