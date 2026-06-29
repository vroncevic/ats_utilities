# -*- coding: UTF-8 -*-

'''
Module
    scheme_loader.py
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
    Defines class SchemeLoader with method(s).
    Resolves generation scheme from dict or file path using config_io.
'''

import os
from typing import Any, override
from ats_utilities.generator.ischeme_loader import ISchemeLoader
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.config_io.config_loader_bundle import ATSConfigLoaderBundle
from ats_utilities.config_io.config_loader import ConfigLoader
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.exceptions.ats_generator_error import ATSGeneratorError
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class SchemeLoader(ISchemeLoader):
    '''
        Defines class SchemeLoader with method(s).
        Resolves generation scheme from dict or file path using config_io.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
            :methods:
                | __init__ - Initializes SchemeLoader constructor.
                | load - Loads and resolves the scheme from dict or path.
                | is_initialized - Checks if the loader is initialized.
                | __str__ - Returns the loader as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(self, context_bundle: ContextBundle | None = None) -> None:
        '''
            Initializes SchemeLoader constructor.

            :param context_bundle: Context bundle for scheme loader | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        factory_context_bundle(self, context_bundle)
        self._initialized: bool = True

    @override
    def load(self, scheme: dict[str, Any] | str) -> dict[str, Any]:
        '''
            Loads and resolves the scheme.

            :param scheme: Generation scheme mapping or file path.
            :type scheme: <dict[str, Any] | str>
            :return: The resolved scheme dictionary.
            :rtype: <dict[str, Any]>
            :exceptions:
                | ATSTypeError - Scheme is not a dict or a string.
                | ATSValueError - Scheme file path does not exist.
                | ATSGeneratorError - Loading scheme file fails.
        '''
        if not isinstance(scheme, (dict, str)):
            raise ATSTypeError("scheme must be of type dict or str")

        if isinstance(scheme, str):
            if not os.path.exists(scheme):
                raise ATSValueError(f"scheme file does not exist: '{scheme}'")

            if not scheme.endswith('.json'):
                raise ATSValueError(f"unsupported scheme file format for: '{scheme}'. Only .json is supported.")

            try:
                loader_bundle: ATSConfigLoaderBundle = ATSConfigLoaderBundle(info_file=scheme)
                config_loader: ConfigLoader = ConfigLoader(loader_bundle)
                loader = config_loader.setup_config_loader()

                if loader is None:
                    raise ATSGeneratorError(f"failed to setup config loader for: '{scheme}'")

                return loader.load_configuration()

            except Exception as exc:
                raise ATSGeneratorError(f"failed to load scheme file '{scheme}': {exc}")

        return scheme

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if scheme loader component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        return self._initialized

    @override
    def __str__(self) -> str:
        '''
            Returns the SchemeLoader as string representation.

            :return: The SchemeLoader as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
