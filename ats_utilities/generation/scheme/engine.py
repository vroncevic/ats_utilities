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
    Defines the SchemeLoader class with attribute(s) and method(s).
    Provides an API for loading generation scheme from dict or file path using config_io.
'''

from __future__ import annotations

from os.path import exists
from collections.abc import Mapping

from ats_utilities.config_io.loader.engine import Loader
from ats_utilities.config_io.setup.factory import ConfigIOFactory
from ats_utilities.exceptions import ATSGeneratorError
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextValidator
from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_satisfied
from ats_utilities.exceptions.format_error import format_error_raw

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class SchemeLoader:
    '''
        Defines the SchemeLoader class with attribute(s) and method(s).
        Provides an API for loading generation scheme from dict or file path using config_io.

        It defines:

            :attributes:
                | _initialized - The indicates if loader is initialized.
                | _context - The context bundle for loader.
            :methods:
                | __init__ - Initializes scheme loader.
                | load - Loads and resolves the scheme from file path.
                | is_initialized - Checks if the scheme loader is initialized.
                | __str__ - Returns the scheme loader as a string representation.
    '''

    _initialized: bool
    _context: ContextBundle

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes scheme loader.

            :param context_bundle: The context bundle.
            :exceptions:
                | ATSValueError: Context bundle must be provided and have proper values.
                | ATSTypeError:  Context bundle must be an instance of ContextBundle and
                |                its attributes must be instances of their respective types.
        '''
        ContextValidator.validate(context_bundle)
        self._context = context_bundle
        self._initialized = True

    def load(self, scheme: str | Mapping[str, object]) -> dict[str, object]:
        '''
            Loads and resolves the scheme.

            :param scheme: The generation scheme file path or preloaded scheme.
            :return: The resolved scheme dictionary.
            :exceptions:
                | ATSTypeError:      Scheme is not a string or mapping.
                | ATSValueError:     Scheme file path does not exist.
                | ATSValueError:     Unsupported scheme file format.
                | ATSValueError:     Failed to setup config loader.
                | ATSGeneratorError: Loading scheme file fails.
        '''
        context: str = 'scheme_loader::load(...)'
        msg_scheme_istype: str = 'scheme must be of type str or Mapping'
        istype(scheme, (str, Mapping), context, msg_scheme_istype)

        if isinstance(scheme, str):
            msg_scheme_path: str = f'scheme file at the provided path does not exist: {scheme}'
            msg_scheme_format: str = f'unsupported scheme file format for: {scheme}. Only .json is supported.'
            msg_config_loader_none: str = f'failed to setup config loader for: {scheme}'

            not_satisfied(not exists(scheme), context, msg_scheme_path)
            not_satisfied(
                not scheme.endswith('.json'), context, msg_scheme_format
            )

            try:
                config_loader: Loader = Loader(
                    ConfigIOFactory.create_bundle(
                        {
                            'file_path': scheme,
                            'scheme': {},
                            'context_bundle': self._context
                        }
                    )
                )
                not_satisfied(config_loader is None, context, msg_config_loader_none)

                return config_loader.load_configuration()

            except Exception as exc:
                msg: str = format_error_raw(exc, self._context.verbose)
                msg_failed_to_load_scheme: str = f'failed to load scheme file {scheme}: {msg}'
                not_satisfied(True, context, msg_failed_to_load_scheme, ATSGeneratorError)

        return dict(scheme)

    def is_initialized(self) -> bool:
        '''
            Checks if scheme loader is initialized.

            :return: True if successful, otherwise False.
            :exceptions: None.
        '''
        return self._initialized

    def __str__(self) -> str:
        '''
            Returns the scheme loader as a string representation.

            :return: The Scheme loader as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
