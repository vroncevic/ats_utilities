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
    Provides an API for base engine (application, tool, script).
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.validator import BaseValidator
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.generation.imanager import IGeneratorManager
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.splash.imanager import ISplashManager
from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.utils.reflection import to_str

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
        Provides an API for base engine (application, tool, script).

        It defines:

            :attributes:
                | _is_initialized - Indicates if the base is initialized.
                | _context - Context with core utilities.
                | _info_manager - Manager for application/tool/script information.
                | _splash_manager - Manager for application/tool/script splash screen.
                | _option_manager - Manager for application/tool/script command line arguments parsing.
                | _generation_manager - Manager for application/tool/script outputs generation.
            :methods:
                | __init__ - Initializes base engine.
                | get_bundle - Gets current configuration bundle.
                | update_bundle - Updates configuration bundle.
                | _apply_bundle - Applies bundle configuration to instance attributes.
                | get_context - Returns the context.
                | is_initialized - Checks if base engine is initialized.
                | process - Processes and runs application/tool/script.
                | __str__ - Returns base engine as string representation.
    '''

    _is_initialized: bool
    _context: ContextBundle
    _info_manager: IInfoManager
    _splash_manager: ISplashManager
    _option_manager: IOptionManager
    _generation_manager: IGeneratorManager

    def __init__(self, own: BaseBundle) -> None:
        '''
            Initializes base engine.

            :param own: Base bundle containing core components for base package.
            :exceptions:
                | ATSValueError: Base bundle must be provided and have proper values.
                | ATSTypeError:  Base bundle must be an instance of BaseBundle
                |                and its attributes must be instances of their
                |                respective interfaces and types.
        '''
        self._is_initialized = False
        BaseValidator.validate(own)
        self._apply_bundle(own)

        components: list[object] = [self._info_manager, self._splash_manager, self._option_manager]
        self._is_initialized = all(
            component is not None and component.is_initialized() for component in components
        )

    def get_bundle(self) -> BaseBundle:
        '''
            Gets current base configuration bundle.

            :return: Base configuration bundle.
            :exceptions: None.
        '''
        return BaseBundle(
            context_bundle=self._context,
            info_manager=self._info_manager,
            splash_manager=self._splash_manager,
            option_manager=self._option_manager,
            generation_manager=self._generation_manager
        )

    def update_bundle(self, bundle: BaseBundle) -> bool:
        '''
            Updates base configuration bundle.

            :param bundle: Base configuration bundle.
            :return: True if configuration was successfully updated, False otherwise.
            :exceptions: None.
        '''
        try:
            BaseValidator.validate(bundle)
            self._apply_bundle(bundle)

            components: list[object] = [self._info_manager, self._splash_manager, self._option_manager]
            self._is_initialized = all(
                component is not None and component.is_initialized() for component in components
            )

            return self._is_initialized

        except (ATSValueError, ATSTypeError):
            return False

    def _apply_bundle(self, bundle: BaseBundle) -> None:
        '''
            Applies bundle configuration to instance attributes.

            :param bundle: Base bundle with components.
            :exceptions: None.
        '''
        self._context = bundle.context_bundle
        self._info_manager = bundle.info_manager
        self._splash_manager = bundle.splash_manager
        self._option_manager = bundle.option_manager
        self._generation_manager = bundle.generation_manager

    def get_context(self) -> ContextBundle:
        '''
            Returns current context.

            :return: Current context.
            :exceptions: None.
        '''
        return self._context

    def is_initialized(self) -> bool:
        '''
            Checks if base engine is initialized.

            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        return self._is_initialized

    def process(self, verbose: bool = False) -> bool:
        '''
            Processes and runs App/Tool/Script.

            :param verbose: Enable/Disable verbose option (default False).
            :return: True if successfully, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns base engine as string representation.

            :return: Base engine as string representation.
            :exceptions: None.
        '''
        return to_str(self)
