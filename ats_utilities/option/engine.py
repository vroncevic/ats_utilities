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

from collections.abc import Sequence

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.setup.bundle import OptionBundle
from ats_utilities.option.setup.validator import OptionValidator
from ats_utilities.option.command.ioption_command import IOptionCommand
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
from ats_utilities.option.setup.types import OptArgs, OptionNamespace, ParsedCommand
from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.reporter.proxy_reporter import vreport
from ats_utilities.checker.proxy_validator import mcheck
from ats_utilities.utils.reflection import to_str, has_attrs

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class OptionManager:
    '''
        Defines class OptionManager with attribute(s) and method(s).
        Creates an option parser based on the argparse argument processor.

        It defines:

            :attributes:
                | _is_initialized - Indicates if the option manager component is initialized (default False).
                | _bundle - Bundle with components for option manager.
                | _context - Context bundle with context.
                | _strategy - Strategy for argument parsing (default ParserStrategy).
            :methods:
                | __init__ - Initials OptionManager constructor.
                | get_bundle - Gets current option configuration bundle.
                | update_bundle - Updates option configuration bundle.
                | get_context - Returns the context.
                | add_operation - Adds an option to the parser.
                | add_version_operation - Adds version option to the parser.
                | parse_input_args - Processes arguments from the start.
                | parse_args - Processes arguments from the start.
                | parse_command - Parses arguments as a command.
                | register_commands - Registers a list of commands with the parser.
                | is_initialized - Checks if the option manager component is initialized.
                | __str__ - Returns the option manager as string representation.
    '''

    _is_initialized: bool
    _bundle: OptionBundle
    _context: ContextBundle
    _strategy: IParserStrategy

    def __init__(self, own: OptionBundle) -> None:
        '''
            Initializes OptionManager constructor.

            :param own: Bundle with components for option manager.
            :exceptions:
                | ATSValueError: Option bundle must be provided and have proper values.
                | ATSTypeError:  Option bundle must be an instance of OptionBundle and its
                |                attributes must be instances of their respective types.
        '''
        self._is_initialized = False
        OptionValidator.validate(own)
        self._apply_bundle(own)
        self._is_initialized = True

    def get_bundle(self) -> OptionBundle:
        '''
            Gets current option configuration bundle.

            :return: Option configuration bundle.
            :exceptions: None.
        '''
        return self._bundle

    def update_bundle(self, bundle: OptionBundle) -> bool:
        '''
            Updates option configuration bundle.

            :param bundle: Option configuration bundle.
            :return: True if option configuration bundle is updated successfully.
            :exceptions: None.
        '''
        try:
            self._is_initialized = False
            OptionValidator.validate(bundle)
            self._apply_bundle(bundle)
            self._is_initialized = True

            return True

        except (ATSValueError, ATSTypeError):
            return False

    def _apply_bundle(self, bundle: OptionBundle) -> None:
        '''
            Applies the option configuration bundle.

            :param bundle: Option configuration bundle.
            :exceptions: None.
        '''
        self._bundle = bundle
        self._context = bundle.context_bundle
        self._strategy = bundle.strategy

    def get_context(self) -> ContextBundle:
        '''
            Returns the context.

            :return: Context.
            :exceptions: None.
        '''
        return self._context

    @property
    def strategy(self) -> IParserStrategy:
        '''
            Returns the parser strategy.

            :return: Parser strategy.
            :exceptions: None.
        '''
        return self._strategy

    @has_attrs('_strategy')
    def add_operation(self, *args: str, **kwargs: object) -> None:
        '''
            Adds an option to the parser.

            :param args: List of flags for the ATS.
            :param kwargs: Arguments in shape of dictionary.
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_strategy'.
        '''
        self._strategy.add_argument(*args, **kwargs)

    @mcheck([('str | None:version', None)])
    @vreport('add version {version}')
    def add_version_operation(self, version: str | None) -> None:
        '''
            Adds version option to the parser.

            :param version: The version in string format | None.
            :exceptions:
                | ATSRuntimeError:   Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError:      Parameter type validation failed.
                | ATSValueError:     Parameter format validation failed.
                | ATSRuntimeError:   Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        if version:
            self._strategy.add_version(version)

    @has_attrs('_strategy')
    @vreport('parse inout args arguments {arguments}')
    def parse_input_args(self, arguments: OptArgs) -> OptionNamespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None.
            :return: Option namespace object.
            :exceptions:
                | ATSValueError:     Missing or empty attribute: '_strategy'.
                | ATSRuntimeError:   Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._strategy.parse(arguments, known_only=False)

    @has_attrs('_strategy')
    @vreport('parse args arguments {arguments}')
    def parse_args(self, arguments: OptArgs) -> OptionNamespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None.
            :return: Option namespace object.
            :exceptions:
                | ATSValueError:     Missing or empty attribute: '_strategy'.
                | ATSRuntimeError:   Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._strategy.parse(arguments, known_only=True)

    @has_attrs('_strategy')
    def register_commands(self, commands: Sequence[IOptionCommand]) -> None:
        '''
            Registers a sequence of commands with the parser.

            :param commands: Sequence of commands to register (read only data).
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_strategy'.
        '''
        self._strategy.register_commands(commands)

    @has_attrs('_strategy')
    def parse_command(self, arguments: OptArgs = None) -> ParsedCommand:
        '''
            Parses arguments as a command.

            :param arguments: Sequence of arguments | None.
            :return: Parsed command result.
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_strategy'.
        '''
        return self._strategy.parse_command(arguments)

    @has_attrs('_strategy')
    def is_initialized(self) -> bool:
        '''
            Checks if option parser component is initialized.

            :return: True if successfully, otherwise False.
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_strategy'.
        '''
        return self._is_initialized and self._strategy.is_initialized()

    def __str__(self) -> str:
        '''
            Returns option manager as string representation.

            :return: Option manager as string representation.
            :exceptions: None.
        '''
        return to_str(self)
