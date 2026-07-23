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
    Creates an API for setup (application, tool, script).
'''

from __future__ import annotations

from abc import abstractmethod
from typing import Any, override

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.ibase import ArgSeq, IBase
from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.info.iinfo_manager import IInfoManager
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.utils.reflection import to_str, has_attrs
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Base(IBase):
    '''
        Defines class Base with attribute(s) and method(s).
        Creates an API for setup (App/Tool/Script).

        It defines:

            :attributes:
                | _is_initialized - Indicates if the base is initialized (default False).
                | _context - Context for components.
                | _config_loader - Manager for configuration loading (default ConfigLoader).
                | _info_manager - Manager for info property (default InfoManager).
                | _splasher - Manager for splash screen (default Splasher).
                | _options_parser - Manager for options parser (default OptionManager).
                | _generator - Generator manager (default Generator).
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
    _splasher: ISplasher
    _options_parser: IOptionManager
    _generator: IGenerator

    def __init__(self, own: BaseBundle) -> None:
        '''
            Initializes Base constructor.

            :param own: Component bundle for base package.
            :type own: BaseBundle
            :exceptions:
                | ATSValueError: Component bundle must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSValueError: Information file must be provided.
                | ATSValueError: Config loader must be provided.
                | ATSValueError: Info manager must be provided.
                | ATSValueError: Options parser must be provided.
                | ATSValueError: Splasher must be provided.
                | ATSValueError: Use generator must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Information file must be str.
                | ATSTypeError: Config loader must be IConfigLoadManager interface.
                | ATSTypeError: Info manager must be IInfoManager interface.
                | ATSTypeError: Options parser must be IOptionManager interface.
                | ATSTypeError: Splasher must be ISplasher interface.
                | ATSTypeError: Use generator must be bool.
                | ATSTypeError: Generator must be IGenerator interface or None.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        context: str = r'base::init(...)'
        not_none(own, context, r'component bundle must be provided')
        istype(own, BaseBundle, context, r'component bundle must be an instance of BaseBundle')
        self._context = own.context_bundle
        self._config_loader = own.config_loader
        self._info_manager = own.info_manager
        self._splasher = own.splasher
        self._options_parser = own.options_parser
        components: list[Any] = [self._info_manager, self._splasher, self._options_parser]

        if own.use_generator:
            self._generator = own.generator
            components.append(self._generator)

        self._is_initialized = all(
            component is not None and component.is_initialized() for component in components
        )

    @override
    def get_context(self) -> ContextBundle:
        '''
            Returns the context.

            :return: Context.
            :rtype: ContextBundle
            :exceptions: None.
        '''
        return self._context

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if App/Tool/Script base engine is initialized.

            :return: True if successful, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        return self._is_initialized

    @has_attrs('_options_parser')
    @override
    def add_new_option(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds a new option for App/Tool/Script.

            :param args: Arguments in string format.
            :type args: str
            :param kwargs: Arguments in Any format.
            :type kwargs: Any
            :exceptions:
                | ATSValueError: Missing or None attribute: '_options_parser'.
        '''
        if self.is_initialized():
            self._options_parser.add_operation(*args, **kwargs)

    @has_attrs('_options_parser')
    @override
    def parse_args(self, argv: ArgSeq) -> OptionNamespace | None:
        '''
            Parses App/Tool/Script arguments.

            :param argv: Sequence of arguments | None.
            :type argv: ArgSeq
            :return: Options and arguments.
            :rtype: OptionNamespace | None
            :exceptions:
                | ATSValueError: Missing or None attribute: '_options_parser'.
        '''
        if self.is_initialized():
            return self._options_parser.parse_args(argv)

        return None

    @abstractmethod
    def process(self, verbose: bool = False) -> bool:
        '''
            Processes and runs App/Tool/Script (Abstract).

            :param verbose: Enable/Disable verbose option (default False).
            :type verbose: bool
            :return: True if successful, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        pass

    @override
    def __str__(self) -> str:
        '''
            Returns the Base as string representation.

            :return: The Base as string representation.
            :rtype: str
            :exceptions: None.
        '''
        return to_str(self)
