# -*- coding: UTF-8 -*-

'''
Module
    validator_test.py
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
    Unit tests for OptionValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.option.setup.bundle import OptionBundle
from ats_utilities.option.setup.validator import OptionValidator
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class OptionValidatorTest(unittest.TestCase):
    '''
        Defines class OptionValidatorTest with attribute(s) and method(s).
        Tests OptionValidator logic.
    '''

    def test_validate_valid(self) -> None:
        mock_strategy = MagicMock(spec=IParserStrategy)
        mock_context = MagicMock(spec=ContextBundle)
        params = {"name": "test_app"}

        bundle = OptionBundle(
            parameters=params,
            strategy=mock_strategy,
            context_bundle=mock_context
        )
        # Should validate successfully
        OptionValidator.validate(bundle)

    def test_validate_invalid_bundle(self) -> None:
        with self.assertRaises(ATSValueError):
            OptionValidator.validate(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            OptionValidator.validate(object())  # type: ignore

    def test_validate_invalid_none(self) -> None:
        mock_strategy = MagicMock(spec=IParserStrategy)
        mock_context = MagicMock(spec=ContextBundle)
        params = {"name": "test_app"}

        with self.assertRaises(ATSValueError):
            bundle = OptionBundle(parameters=None, strategy=mock_strategy, context_bundle=mock_context)  # type: ignore
            OptionValidator.validate(bundle)

        with self.assertRaises(ATSValueError):
            bundle = OptionBundle(parameters=params, strategy=None, context_bundle=mock_context)  # type: ignore
            OptionValidator.validate(bundle)

        with self.assertRaises(ATSValueError):
            bundle = OptionBundle(parameters=params, strategy=mock_strategy, context_bundle=None)  # type: ignore
            OptionValidator.validate(bundle)

    def test_validate_invalid_type(self) -> None:
        mock_strategy = MagicMock(spec=IParserStrategy)
        mock_context = MagicMock(spec=ContextBundle)
        params = {"name": "test_app"}

        with self.assertRaises(ATSTypeError):
            bundle = OptionBundle(parameters="not a dict", strategy=mock_strategy, context_bundle=mock_context)  # type: ignore
            OptionValidator.validate(bundle)

        with self.assertRaises(ATSTypeError):
            bundle = OptionBundle(parameters=params, strategy="not a strategy", context_bundle=mock_context)  # type: ignore
            OptionValidator.validate(bundle)

        with self.assertRaises(ATSTypeError):
            bundle = OptionBundle(parameters=params, strategy=mock_strategy, context_bundle="not a context")  # type: ignore
            OptionValidator.validate(bundle)


if __name__ == "__main__":
    unittest.main()
