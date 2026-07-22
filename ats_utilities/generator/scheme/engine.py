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
    Defines class SchemeLoader with method(s).
    Resolves generation scheme from dict or file path using config_io.
'''

from __future__ import annotations

from os.path import exists
from typing import Any, override
from collections.abc import Mapping

from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.config_io.loader.engine import Loader
from ats_utilities.config_io.config_io_registry import ConfigIORegistry
from ats_utilities.exceptions import ATSGeneratorError
from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_satisfied
from ats_utilities.exceptions.format_error import format_error_raw

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class SchemeLoader(ISchemeLoader):
    '''
        Defines class SchemeLoader with method(s).
        Resolves generation scheme from dict or file path using config_io.

        It defines:

            :attributes:
                | _initialized - Indicates if loader is initialized.
                | _context - Context bundle for loader.
            :methods:
                | __init__ - Initializes SchemeLoader constructor.
                | load - Loads and resolves the scheme from file path.
                | is_initialized - Checks if the loader is initialized.
                | __str__ - Returns the loader as string representation.
    '''

    _initialized: bool
    _context: ContextBundle

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes SchemeLoader constructor.

            :param context_bundle: Context bundle for scheme loader.
            :type context_bundle: <ContextBundle>
            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        self._context = context_bundle
        self._initialized = True

    @override
    def load(self, scheme: str | Mapping[str, Any]) -> dict[str, Any]:
        '''
            Loads and resolves the scheme.

            :param scheme: Generation scheme file path or preloaded scheme.
            :type scheme: <str | Mapping[str, Any]>
            :return: The resolved scheme dictionary.
            :rtype: <dict[str, Any]>
            :exceptions:
                | ATSTypeError: Scheme is not a string or mapping.
                | ATSValueError: Scheme file path does not exist.
                | ATSValueError: Unsupported scheme file format.
                | ATSValueError: Failed to setup config loader.
                | ATSGeneratorError: Loading scheme file fails.
        '''
        context: str = r'scheme_loader::load(...)'
        istype(scheme, (str, Mapping), context, r'scheme must be of type str or Mapping')

        if isinstance(scheme, str):
            not_satisfied(
                not exists(scheme), context, f'scheme file at the provided path does not exist: {scheme}'
            )
            not_satisfied(
                not scheme.endswith('.json'), context, f'unsupported scheme file format for: {scheme}. Only .json is supported.'
            )

            try:
                config_loader: Loader = Loader(
                    ConfigIORegistry.create_config_io_bundle_by_file_path_and_scheme(
                        file_path=scheme,
                        scheme={},
                        context_bundle=self._context
                    )
                )
                not_satisfied(config_loader is None, context, f'failed to setup config loader for: {scheme}')

                return config_loader.load_configuration()

            except Exception as exc:
                msg: str = format_error_raw(exc, self._context.verbose)
                not_satisfied(True, context, f'failed to load scheme file {scheme}: {msg}', ATSGeneratorError)

        return dict(scheme)

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if scheme loader component is initialized.

            :return: <True> if successful, <False> otherwise.
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
        return to_str(self)
