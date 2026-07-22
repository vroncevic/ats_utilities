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
    Unit tests for CheckerBundle class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.checker.bundle import CheckerBundle
from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.checker.format.iformat_validator import IFormatValidator
from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter
from ats_utilities.checker.type.itype_validator import ITypeValidator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class BundleTest(unittest.TestCase):
    '''
        Defines class BundleTest with attribute(s) and method(s).
        Tests CheckerBundle dataclass logic.
    '''

    def test_init_valid(self) -> None:
        mock_format = MagicMock(spec=IFormatValidator)
        mock_type = MagicMock(spec=ITypeValidator)
        mock_context = MagicMock(spec=IContextProvider)
        mock_reporter = MagicMock(spec=ICheckReporter)

        bundle = CheckerBundle(
            format_validator=mock_format,
            type_validator=mock_type,
            context_provider=mock_context,
            check_reporter=mock_reporter
        )
        self.assertIs(bundle.format_validator, mock_format)
        self.assertIs(bundle.type_validator, mock_type)
        self.assertIs(bundle.context_provider, mock_context)
        self.assertIs(bundle.check_reporter, mock_reporter)

    def test_to_dict(self) -> None:
        mock_format = MagicMock(spec=IFormatValidator)
        mock_type = MagicMock(spec=ITypeValidator)
        mock_context = MagicMock(spec=IContextProvider)
        mock_reporter = MagicMock(spec=ICheckReporter)

        bundle = CheckerBundle(
            format_validator=mock_format,
            type_validator=mock_type,
            context_provider=mock_context,
            check_reporter=mock_reporter
        )
        expected = {
            "format_validator": mock_format,
            "type_validator": mock_type,
            "context_provider": mock_context,
            "check_reporter": mock_reporter
        }
        self.assertEqual(bundle.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
