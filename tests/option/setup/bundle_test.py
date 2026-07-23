# -*- coding: UTF-8 -*-

'''
Module
    bundle_test.py
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
    Unit tests for OptionBundle class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.setup.bundle import OptionBundle
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class OptionBundleTest(unittest.TestCase):
    '''
        Defines class OptionBundleTest with attribute(s) and method(s).
        Tests OptionBundle dataclass logic.
    '''

    def test_init_valid(self) -> None:
        mock_strategy = MagicMock(spec=IParserStrategy)
        mock_context = MagicMock(spec=ContextBundle)
        params = {"name": "test_app"}

        bundle = OptionBundle(
            parameters=params,
            strategy=mock_strategy,
            context_bundle=mock_context
        )
        self.assertEqual(bundle.parameters, params)
        self.assertIs(bundle.strategy, mock_strategy)
        self.assertIs(bundle.context_bundle, mock_context)

    def test_to_dict(self) -> None:
        mock_strategy = MagicMock(spec=IParserStrategy)
        mock_context = MagicMock(spec=ContextBundle)
        params = {"name": "test_app"}

        bundle = OptionBundle(
            parameters=params,
            strategy=mock_strategy,
            context_bundle=mock_context
        )

        expected = {
            "parameters": params,
            "strategy": mock_strategy,
            "context_bundle": mock_context
        }
        self.assertEqual(bundle.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
