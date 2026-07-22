# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
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
    Unit tests for ArgParser class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.factory import ContextFactory
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.option.parser.engine import ArgParser
from ats_utilities.option.parser.parser_bundle import ParserBundle
from ats_utilities.reporter.ireporter import IReporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class EngineTest(unittest.TestCase):
    '''
        Defines class EngineTest with attribute(s) and method(s).
        Tests ArgParser engine logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init_valid - Tests successful initialization.
                | test_init_invalid - Tests initialization exceptions.
                | test_error - Tests error routing to reporter.
                | test_str - Tests __str__ representation.
    '''

    def test_init_valid(self) -> None:
        '''
            Tests successful initialization.

            :exceptions: None.
        '''
        context_bundle = ContextFactory.create_default_context_bundle()
        bundle = ParserBundle(
            prog="myprog",
            epilog="myepilog",
            description="mydesc",
            context_bundle=context_bundle
        )
        parser = ArgParser(bundle)
        self.assertEqual(parser.prog, "myprog")
        self.assertEqual(parser.epilog, "myepilog")
        self.assertEqual(parser.description, "mydesc")
        self.assertIs(parser._reporter, context_bundle.reporter)

    def test_init_invalid(self) -> None:
        '''
            Tests initialization exceptions.

            :exceptions: None.
        '''
        with self.assertRaises(ATSTypeError):
            ArgParser("not a bundle")  # type: ignore

    def test_error(self) -> None:
        '''
            Tests error routing to reporter.

            :exceptions: None.
        '''
        mock_reporter = MagicMock(spec=IReporter)
        custom_context = ContextFactory.create_default_context_bundle()
        custom_context = custom_context.__class__(
            checker=custom_context.checker,
            logger=custom_context.logger,
            reporter=mock_reporter,
            verbose=custom_context.verbose
        )

        bundle = ParserBundle(
            prog="myprog",
            epilog="myepilog",
            description="mydesc",
            context_bundle=custom_context
        )
        parser = ArgParser(bundle)

        with self.assertRaises(SystemExit) as cm:
            parser.error("failed parse")

        self.assertEqual(cm.exception.code, 2)
        mock_reporter.error.assert_called_once_with(["argument error: failed parse"])

    def test_str(self) -> None:
        '''
            Tests __str__ representation.

            :exceptions: None.
        '''
        context_bundle = ContextFactory.create_default_context_bundle()
        bundle = ParserBundle(
            prog="myprog",
            epilog="myepilog",
            description="mydesc",
            context_bundle=context_bundle
        )
        parser = ArgParser(bundle)
        self.assertIn("ArgParser", str(parser))

    def test_init_with_kwargs(self) -> None:
        '''
            Tests ArgParser initialization using kwargs.

            :exceptions: None.
        '''
        context_bundle = ContextFactory.create_default_context_bundle()
        parser = ArgParser(prog="testprog", context_bundle=context_bundle)
        self.assertEqual(parser.prog, "testprog")
        self.assertIs(parser._reporter, context_bundle.reporter)


if __name__ == "__main__":
    unittest.main()
