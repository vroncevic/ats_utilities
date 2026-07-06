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

from __future__ import annotations

from abc import abstractmethod
from typing import Any, override

from ats_utilities.base.component_bundle import BaseComponentBundle
from ats_utilities.base.ibase import ArgSeq, IBase
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.config_io.iconfig_loader import IConfigLoader
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.exceptions import ATSAttributeError, ATSRuntimeError, ATSTypeError, ATSValueError
from ats_utilities.factory_class import to_str, cls_name, has_attrs
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.logging.ilogger_manager import ILoggerManager
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.splasher.isplasher import ISplasher

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Base(IBase):
    '''
        Defines class Base with attribute(s) and method(s).
        Creates an API for setup ATS (application, tool, script).

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _shared_context - Shared context for components.
                | _config_loader - Manager for configuration loading (default ConfigLoader).
                | _info_manager - Manager for info component (default InfoManager).
                | _splasher - Manager for splash component (default Splasher).
                | _options_parser - Manager for options parser (default OptionManager).
                | _logger_manager - Manager for logger component (default LoggerManager).
                | _generator - Generator manager (default Generator).
                | _is_initialized - Indicates if the base component is initialized (default False).
            :methods:
                | __init__ - Initializes Base constructor.
                | get_shared_context - Returns the shared context.
                | is_initialized - Checks if the base component is initialized.
                | add_new_option - Adds a new option for the the CL interface.
                | parse_args - Parses the CLI arguments.
                | process - Processes and runs tool operations (Abstract).
                | __str__ - Returns the ATS base as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool
    _is_initialized: bool
    _shared_context: ContextBundle
    _config_loader: IConfigLoader
    _info_manager: IInfoManager
    _splasher: ISplasher
    _options_parser: IOptionManager
    _logger_manager: ILoggerManager
    _generator: IGenerator

    def __init__(self, component_bundle: BaseComponentBundle | None = None) -> None:
        '''
            Initializes Base constructor.

            :param component_bundle: Component bundle for base package | None.
            :type component_bundle: <BaseComponentBundle | None>
            :exceptions: None.
        '''
        self._is_initialized = False

        try:
            bundle: BaseComponentBundle = component_bundle or BaseComponentBundle()
            factory_context_bundle(self, bundle.context_bundle)
            self._shared_context = bundle.context_bundle
            self._config_loader = bundle.config_loader
            self._info_manager = bundle.info_manager
            self._splasher = bundle.splasher
            self._options_parser = bundle.options_parser
            self._logger_manager = bundle.logger_manager

            components: list[Any] = [self._info_manager, self._splasher, self._options_parser, self._logger_manager]

            if bundle.use_generator:
                self._generator = bundle.generator
                components.append(self._generator)

            # All components initialized successfully.
            self._is_initialized = all(
                component is not None and component.is_initialized() for component in components
            )

        except (ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError) as exc:
            print(f"\x1b[31m{cls_name(self)} {exc}\x1b[0m")

        except Exception as exc:
            print(f"\x1b[31m{cls_name(self)} unexpected exception: {exc}\x1b[0m")

    @override
    def get_shared_context(self) -> ContextBundle:
        '''
            Returns the shared context.

            :return: Shared context.
            :rtype: <ContextBundle>
            :exceptions: None.
        '''
        return self._shared_context

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if the base component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        return self._is_initialized

    @has_attrs('_options_parser')
    @override
    def add_new_option(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds a new option for the CL interface.

            :param args: Arguments in string form.
            :type args: <str>
            :param kwargs: arguments in Any form.
            :type kwargs: <Any>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_options_parser'.
        '''
        if self.is_initialized():
            self._options_parser.add_operation(*args, **kwargs)

    @has_attrs('_options_parser')
    @override
    def parse_args(self, argv: ArgSeq) -> OptionNamespace | None:
        '''
            Parses the CLI arguments.

            :param argv: Sequence of arguments | None.
            :type argv: <ArgSeq>
            :return: Options and arguments.
            :rtype: <OptionNamespace | None>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_options_parser'.
        '''
        if self.is_initialized():
            return self._options_parser.parse_args(argv)

        return None

    @abstractmethod
    @override
    def process(self, verbose: bool = False) -> bool:
        '''
            Processes and runs tool operations (Abstract).

            :param verbose: Enable/Disable verbose option (default False).
            :type verbose: <bool>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @override
    def __str__(self) -> str:
        '''
            Returns the ATS base as string representation.

            :return: The ATS base as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
