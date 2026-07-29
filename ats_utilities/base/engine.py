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
    Provides an API for setup (application, tool, script).
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.ibase import ArgSeq
from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.generation.imanager import IGeneratorManager
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.splash.imanager import ISplashManager
from ats_utilities.utils.reflection import to_str, has_attrs
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class Base:
    '''
        Defines class Base with attribute(s) and method(s).
        Provides an API for setup (App/Tool/Script).

        It defines:

            :attributes:
                | _is_initialized - Indicates if the base is initialized (default False).
                | _context - Context for components.
                | _config_loader - Manager for configuration loading (default ConfigLoader).
                | _info_manager - Manager for info property (default InfoManager).
                | _splasher - Manager for splash screen (default SplashManager).
                | _options_parser - Manager for options parser (default OptionManager).
                | _generator - GeneratorManager manager (default GeneratorManager).
            :methods:
                | __init__ - Initializes Base constructor.
                | get_context - Returns the context.
                | is_initialized - Checks if App/Tool/Script base engine is initialized.
                | add_new_option - Adds a new option for App/Tool/Script.
                | parse_args - Parses App/Tool/Script arguments.
                | process - Processes and runs App/Tool/Script (Abstract).
                | __str__ - Returns the Base as string representation.
    '''

    _is_initialized: bool
    _context: ContextBundle
    _config_loader: ILoader
    _info_manager: IInfoManager
    _splasher: ISplashManager
    _options_parser: IOptionManager
    _generator: IGeneratorManager

    def __init__(self, own: BaseBundle) -> None:
        '''
            Initializes Base constructor.

            :param own: Component bundle for base package.
            :exceptions:
                | ATSValueError: Base bundle must be provided and have proper values.
                | ATSTypeError:  Base bundle must be an instance of BaseBundle
                |                and its attributes must be instances of their
                |                respective interfaces and types.
        '''
        context: str = 'base::init(...)'
        not_none(own, context, 'component bundle must be provided')
        istype(own, BaseBundle, context, 'component bundle must be an instance of BaseBundle')
        self._context = own.context_bundle
        self._config_loader = own.config_loader
        self._info_manager = own.info_manager
        self._splasher = own.splasher
        self._options_parser = own.options_parser
        components: list[object] = [self._info_manager, self._splasher, self._options_parser]

        if own.use_generator:
            self._generator = own.generator
            components.append(self._generator)

        self._is_initialized = all(
            component is not None and component.is_initialized() for component in components
        )

    def get_context(self) -> ContextBundle:
        '''
            Returns the context.

            :return: Context.
            :exceptions: None.
        '''
        return self._context

    def is_initialized(self) -> bool:
        '''
            Checks if App/Tool/Script base engine is initialized.

            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        return self._is_initialized

    @has_attrs('_options_parser')
    def add_new_option(self, *args: str, **kwargs: object) -> None:
        '''
            Adds a new option for App/Tool/Script.

            :param args: Arguments in string format.
            :param kwargs: Arguments in object format.
            :exceptions:
                | ATSValueError: Missing or None attribute: '_options_parser'.
        '''
        if self.is_initialized():
            self._options_parser.add_operation(*args, **kwargs)

    @has_attrs('_options_parser')
    def parse_args(self, argv: ArgSeq) -> OptionNamespace | None:
        '''
            Parses App/Tool/Script arguments.

            :param argv: Sequence of arguments | None.
            :return: Options and arguments.
            :exceptions:
                | ATSValueError: Missing or None attribute: '_options_parser'.
        '''
        if self.is_initialized():
            return self._options_parser.parse_args(argv)

        return None

    def process(self, verbose: bool = False) -> bool:
        '''
            Processes and runs App/Tool/Script (Abstract).

            :param verbose: Enable/Disable verbose option (default False).
            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns the Base as string representation.

            :return: The Base as string representation.
            :exceptions: None.
        '''
        return to_str(self)
