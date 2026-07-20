# -*- coding: UTF-8 -*-

'''
Module
    option_factory_test.py
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
    Unit tests for OptionFactory class.
'''

from __future__ import annotations

import unittest
from typing import Any

from ats_utilities.context.context_factory import ContextFactory
from ats_utilities.context.context_support import ContextSupport
from ats_utilities.option.option_bundle import OptionBundle
from ats_utilities.option.option_factory import OptionFactory
from ats_utilities.option.parser.iarg_parser import IArgParser

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class DummyParser(IArgParser, ContextSupport):
    '''
        Dummy parser class for registry tests.
    '''
    def __init__(self, component_bundle: Any) -> None:
        if component_bundle and hasattr(component_bundle, 'context_bundle'):
            ContextSupport.__init__(self, component_bundle.context_bundle)
        else:
            ContextSupport.__init__(self, ContextFactory.create_default_context_bundle())

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


class OptionFactoryTest(unittest.TestCase):
    '''
        Defines class OptionFactoryTest with attribute(s) and method(s).
        Tests OptionFactory static factory logic.
    '''

    def test_create_option_bundle_from_dict(self) -> None:
        '''
            Tests create_option_bundle_from_dict.

            :exceptions: None.
        '''
        parameters = {
            "name": "mytool",
            "version": "1.0.0",
            "description": "desc",
            "epilog": "epi"
        }
        context_bundle = ContextFactory.create_default_context_bundle()

        bundle = OptionFactory.create_option_bundle_from_dict(
            parameters=parameters,
            context_bundle=context_bundle,
            parser_class=DummyParser
        )

        self.assertIsInstance(bundle, OptionBundle)
        self.assertEqual(bundle.parameters, parameters)
        self.assertIs(bundle.context_bundle, context_bundle)


if __name__ == "__main__":
    unittest.main()
