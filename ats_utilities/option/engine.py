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
    Defines class OptionManager with attribute(s) and method(s).
    Creates an option parser based on the argparse argument processor.
'''

from __future__ import annotations

from collections.abc import Sequence, Mapping
from typing import Any, override
from sys import stderr

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.checker.proxy_validator import vcheck
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.exceptions import ATSAttributeError, ATSRuntimeError, ATSTypeError, ATSValueError
from ats_utilities.factory_class import to_str, cls_name, has_attrs
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.option.component_bundle import OptionComponentBundle
from ats_utilities.option.command.ioption_command import IOptionCommand
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
from ats_utilities.option.option_namespace import OptArgs, OptionNamespace
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.proxy_reporter import vreport

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class OptionManager(IOptionManager):
    '''
        Defines class OptionManager with attribute(s) and method(s).
        Creates an option parser based on the argparse argument processor.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger (default Logger).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _shared_context - Context bundle with shared context.
                | _is_initialized - Indicates if the option manager component is initialized (default False).
                | _strategy - Strategy for argument parsing (default ParserStrategy).
            :methods:
                | __init__ - Initials OptionManager constructor.
                | get_shared_context - Returns the shared context.
                | add_operation - Adds an option to the parser.
                | add_version_operation - Adds version option to the parser.
                | parse_input_args - Processes arguments from the start.
                | parse_args - Processes arguments from the start.
                | parse_command - Parses arguments as a command.
                | register_commands - Registers a list of commands with the parser.
                | is_initialized - Checks if the option manager component is initialized.
                | __str__ - Returns the string representation of OptionManager.
    '''

    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _is_initialized: bool
    _shared_context: ContextBundle
    _strategy: IParserStrategy

    def __init__(self, component_bundle: OptionComponentBundle | None = None) -> None:
        '''
            Initializes OptionManager constructor.

            :param component_bundle: Bundle with components for option manager | None.
            :type component_bundle: <OptionComponentBundle | None>
            :exceptions: None.
        ''' 
        self._is_initialized = False

        try:
            bundle: OptionComponentBundle = component_bundle or OptionComponentBundle()
            factory_context_bundle(self, bundle.context_bundle)
            self._shared_context = bundle.context_bundle
            self._strategy = bundle.strategy
            self._strategy.setup(bundle.parameters)

            # All components initialized successfully.
            self._is_initialized = True
 
        except (ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError) as exc:
            stderr.write(f'\x1b[31m{cls_name(self)} {exc}\x1b[0m\n')

        except Exception as exc:
            stderr.write(f'\x1b[31m{cls_name(self)} unexpected exception: {exc}\x1b[0m\n')

    @override
    def get_shared_context(self) -> ContextBundle:
        '''
            Returns the shared context.

            :return: Shared context.
            :rtype: <ContextBundle>
            :exceptions: None.
        '''
        return self._shared_context

    @has_attrs('_strategy')
    @override
    def add_operation(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds an option to the parser.

            :param args: List of flags for the ATS.
            :type args: <str>
            :param kwargs: Arguments in shape of dictionary.
            :type kwargs: <Any>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_strategy'.
        '''
        self._strategy.add_argument(*args, **kwargs)

    @vcheck([('str | None:version', None)])
    @vreport('add version {version}')
    @override
    def add_version_operation(self, version: str | None) -> None:
        '''
            Adds version option to the parser.

            :param version: The version in string format | None.
            :type version: <str | None>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        if version:
            self._strategy.add_version(version)

    @has_attrs('_strategy')
    @vreport('parse inout args arguments {arguments}')
    @override
    def parse_input_args(self, arguments: OptArgs) -> OptionNamespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None.
            :type arguments: <OptArgs>
            :return: Option namespace object.
            :rtype: <OptionNamespace>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_strategy'.
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._strategy.parse(arguments, known_only=False)

    @has_attrs('_strategy')
    @vreport('parse args arguments {arguments}')
    @override
    def parse_args(self, arguments: OptArgs) -> OptionNamespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None.
            :type arguments: <OptArgs>
            :return: Option namespace object.
            :rtype: <OptionNamespace>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_strategy'.
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._strategy.parse(arguments, known_only=True)

    @has_attrs('_strategy')
    @override
    def register_commands(self, commands: Sequence[IOptionCommand]) -> None:
        '''
            Registers a sequence of commands with the parser.

            :param commands: Sequence of commands to register (read only data).
            :type commands: <Sequence[IOptionCommand]>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_strategy'.
        '''
        self._strategy.register_commands(commands)

    @has_attrs('_strategy')
    @override
    def parse_command(self, arguments: OptArgs = None) -> tuple[str, Mapping[str, Any]]:
        '''
            Parses arguments as a command.

            :param arguments: Sequence of arguments | None.
            :type arguments: <OptArgs>
            :return: Tuple of (command name, command arguments) (read only data).
            :rtype: <tuple[str, Mapping[str, Any]]>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_strategy'.
        '''
        return self._strategy.parse_command(arguments)

    @has_attrs('_strategy')
    @override
    def is_initialized(self) -> bool:
        '''
            Checks if option parser component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_strategy'.
        '''
        return self._is_initialized and self._strategy.is_initialized()

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of OptionManager.

            :return: The option parser as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
