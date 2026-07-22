# -*- coding: UTF-8 -*-

'''
Module
    option_registry_test.py
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
    Unit tests for OptionRegistry class.
'''

from __future__ import annotations

import unittest
from typing import Any

from ats_utilities.context.factory import ContextFactory
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.option_bundle import OptionBundle
from ats_utilities.option.option_registry import OptionRegistry
from ats_utilities.option.option_params import OptionParams
from ats_utilities.option.parser.iarg_parser import IArgParser
from ats_utilities.option.option_factory import OptionFactory

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class DummyParser(IArgParser):
    '''
        Dummy parser class for registry tests.
    '''
    _context: ContextBundle

    def __init__(self, own: Any) -> None:
        if own and hasattr(own, 'context_bundle'):
            self._context = own.context_bundle
        else:
            self._context = ContextFactory.create_default_context_bundle()

    def get_context(self) -> ContextBundle:
        return self._context

    def error(self, message: str) -> Any:
        pass

    def add_argument(self, *args: Any, **kwargs: Any) -> None:
        pass

    def add_subparsers(self, *args: Any, **kwargs: Any) -> Any:
        pass

    def parse_args(self, *args: Any, **kwargs: Any) -> Any:
        pass

    def parse_known_args(self, *args: Any, **kwargs: Any) -> Any:
        pass

    def __str__(self) -> str:
        return "DummyParser"


class OptionRegistryTest(unittest.TestCase):
    '''
        Defines class OptionRegistryTest with attribute(s) and method(s).
        Tests OptionRegistry logic.
    '''

    def test_create_bundle(self) -> None:
        """Tests create_bundle on OptionRegistry."""
        parameters = {
            "name": "mytool",
            "version": "1.0.0",
            "description": "desc",
            "epilog": "epi"
        }
        context_bundle = ContextFactory.create_default_context_bundle()
        factory_bundle = OptionFactory.create_option_bundle_from_dict(
            parameters=parameters,
            context_bundle=context_bundle,
            parser_class=DummyParser
        )

        bundle = OptionRegistry.create_bundle(
            OptionParams(
                parameters=parameters,
                context_bundle=context_bundle,
                strategy=factory_bundle.strategy
            )
        )

        self.assertIsInstance(bundle, OptionBundle)
        self.assertEqual(bundle.parameters, parameters)
        self.assertIs(bundle.context_bundle, context_bundle)


if __name__ == "__main__":
    unittest.main()
