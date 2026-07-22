# -*- coding: UTF-8 -*-

'''
Module
    parser_bundle_test.py
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
    Unit tests for ParserBundle class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.option.parser.parser_bundle import ParserBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ParserBundleTest(unittest.TestCase):
    '''
        Defines class ParserBundleTest with attribute(s) and method(s).
        Tests ParserBundle dataclass logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init_valid - Tests successful ParserBundle initialization.
                | test_init_invalid_none - Tests ParserBundle initialization with None values.
                | test_init_invalid_type - Tests ParserBundle initialization with wrong types.
                | test_to_dict - Tests ParserBundle to_dict method.
    '''

    def test_init_valid(self) -> None:
        '''
            Tests successful ParserBundle initialization.

            :exceptions: None.
        '''
        mock_context = MagicMock(spec=ContextBundle)
        try:
            bundle = ParserBundle(
                prog="myprog",
                epilog="myepilog",
                description="mydesc",
                context_bundle=mock_context
            )
            self.assertEqual(bundle.prog, "myprog")
            self.assertEqual(bundle.epilog, "myepilog")
            self.assertEqual(bundle.description, "mydesc")
            self.assertIs(bundle.context_bundle, mock_context)
        except (ATSValueError, ATSTypeError):
            self.fail("Failed to instantiate ParserBundle with valid arguments.")

    def test_init_invalid_none(self) -> None:
        '''
            Tests ParserBundle initialization with None values.

            :exceptions: None.
        '''
        mock_context = MagicMock(spec=ContextBundle)

        with self.assertRaises(ATSValueError):
            ParserBundle(prog=None, epilog="myepilog", description="mydesc", context_bundle=mock_context)  # type: ignore

        with self.assertRaises(ATSValueError):
            ParserBundle(prog="myprog", epilog=None, description="mydesc", context_bundle=mock_context)  # type: ignore

        with self.assertRaises(ATSValueError):
            ParserBundle(prog="myprog", epilog="myepilog", description=None, context_bundle=mock_context)  # type: ignore

        with self.assertRaises(ATSValueError):
            ParserBundle(prog="myprog", epilog="myepilog", description="mydesc", context_bundle=None)  # type: ignore

    def test_init_invalid_type(self) -> None:
        '''
            Tests ParserBundle initialization with wrong types.

            :exceptions: None.
        '''
        mock_context = MagicMock(spec=ContextBundle)

        with self.assertRaises(ATSTypeError):
            ParserBundle(prog=123, epilog="myepilog", description="mydesc", context_bundle=mock_context)  # type: ignore

        with self.assertRaises(ATSTypeError):
            ParserBundle(prog="myprog", epilog=[], description="mydesc", context_bundle=mock_context)  # type: ignore

        with self.assertRaises(ATSTypeError):
            ParserBundle(prog="myprog", epilog="myepilog", description={}, context_bundle=mock_context)  # type: ignore

        with self.assertRaises(ATSTypeError):
            ParserBundle(prog="myprog", epilog="myepilog", description="mydesc", context_bundle="not context")  # type: ignore

    def test_to_dict(self) -> None:
        '''
            Tests ParserBundle to_dict method.

            :exceptions: None.
        '''
        mock_context = MagicMock(spec=ContextBundle)
        bundle = ParserBundle(
            prog="myprog",
            epilog="myepilog",
            description="mydesc",
            context_bundle=mock_context
        )
        expected = {
            "prog": "myprog",
            "epilog": "myepilog",
            "description": "mydesc",
            "context_bundle": mock_context
        }
        self.assertEqual(bundle.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
