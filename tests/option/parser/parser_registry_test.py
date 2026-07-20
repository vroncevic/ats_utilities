# -*- coding: UTF-8 -*-

'''
Module
    parser_registry_test.py
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
    Unit tests for ParserRegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.info.info_keys import InfoKeys
from ats_utilities.option.parser.parser_bundle import ParserBundle
from ats_utilities.option.parser.parser_registry import ParserRegistry
from ats_utilities.option.parser.parser_params import ParserParams

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ParserRegistryTest(unittest.TestCase):
    '''
        Defines class ParserRegistryTest with attribute(s) and method(s).
        Tests ParserRegistry static factory logic.

        It defines:

            :attributes: None.
            :methods:
                | test_create_parser_bundle_from_dict - Tests create_parser_bundle_from_dict.
    '''

    def test_create_parser_bundle_from_dict(self) -> None:
        '''
            Tests create_parser_bundle_from_dict.

            :exceptions: None.
        '''
        parameters = {
            InfoKeys.ATS_NAME: "mytool",
            InfoKeys.ATS_VERSION: "1.0.0",
            InfoKeys.ATS_LICENCE: "MIT",
            InfoKeys.ATS_BUILD_DATE: "2026-01-01"
        }
        mock_context = MagicMock(spec=ContextBundle)

        bundle = ParserRegistry.create_parser_bundle_from_dict(
            parameters=parameters,
            context_bundle=mock_context
        )

        self.assertIsInstance(bundle, ParserBundle)
        self.assertEqual(bundle.prog, "mytool 1.0.0")
        self.assertEqual(bundle.epilog, "mytool copyright (c) MIT")
        self.assertEqual(bundle.description, "mytool build date 2026-01-01")
        self.assertIs(bundle.context_bundle, mock_context)

    def test_create_bundle(self) -> None:
        """Tests create_bundle on ParserRegistry."""
        parameters = {
            InfoKeys.ATS_NAME: "mytool",
            InfoKeys.ATS_VERSION: "1.0.0",
            InfoKeys.ATS_LICENCE: "MIT",
            InfoKeys.ATS_BUILD_DATE: "2026-01-01"
        }
        mock_context = MagicMock(spec=ContextBundle)

        bundle = ParserRegistry.create_bundle(
            ParserParams(
                parameters=parameters,
                context_bundle=mock_context
            )
        )

        self.assertIsInstance(bundle, ParserBundle)
        self.assertEqual(bundle.prog, "mytool 1.0.0")
        self.assertEqual(bundle.epilog, "mytool copyright (c) MIT")
        self.assertEqual(bundle.description, "mytool build date 2026-01-01")
        self.assertIs(bundle.context_bundle, mock_context)


if __name__ == "__main__":
    unittest.main()
