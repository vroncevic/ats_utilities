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
    Unit tests for SplashValidator class.
'''

from __future__ import annotations

import unittest
from typing import Any
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.splasher.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.progressbar.iprogress_bar import IProgressBar
from ats_utilities.splasher.property.isplash_property import ISplashProperty
from ats_utilities.splasher.setup.bundle import SplashBundle
from ats_utilities.splasher.setup.validator import SplashValidator
from ats_utilities.splasher.terminal.iterminal_properties import ITerminalProperties

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class SplashValidatorTest(unittest.TestCase):
    '''
        Defines class SplashValidatorTest with attribute(s) and method(s).
        Tests SplashValidator logic.
    '''

    def _get_mocks(self) -> dict[str, Any]:
        return {
            "prop": {"enabled": True},
            "splash_property": MagicMock(spec=ISplashProperty),
            "property_validated": True,
            "terminal_property": MagicMock(spec=ITerminalProperties),
            "ext": MagicMock(spec=IExtInfrastructure),
            "pb": MagicMock(spec=IProgressBar),
            "context_bundle": MagicMock(spec=ContextBundle),
        }

    def test_validate_valid(self) -> None:
        mocks = self._get_mocks()
        bundle = SplashBundle(**mocks)
        # Should validate successfully
        SplashValidator.validate(bundle)

    def test_validate_invalid_bundle(self) -> None:
        with self.assertRaises(ATSValueError):
            SplashValidator.validate(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            SplashValidator.validate(object())  # type: ignore

    def test_validate_invalid_none(self) -> None:
        for key in self._get_mocks().keys():
            # property_validated is a bool, so setting it to None should raise an error
            mocks = self._get_mocks()
            mocks[key] = None  # type: ignore
            bundle = SplashBundle.__new__(SplashBundle)
            for k, v in mocks.items():
                object.__setattr__(bundle, k, v)
            with self.assertRaises(ATSValueError):
                SplashValidator.validate(bundle)

    def test_validate_invalid_type(self) -> None:
        type_mismatches = {
            "prop": object(),
            "splash_property": MagicMock(spec=ContextBundle),
            "property_validated": object(),
            "terminal_property": MagicMock(spec=IProgressBar),
            "ext": MagicMock(spec=ISplashProperty),
            "pb": MagicMock(spec=ITerminalProperties),
            "context_bundle": MagicMock(spec=IExtInfrastructure)
        }

        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                mocks = self._get_mocks()
                mocks[field] = bad_value
                bundle = SplashBundle.__new__(SplashBundle)
                for k, v in mocks.items():
                    object.__setattr__(bundle, k, v)
                with self.assertRaises(ATSTypeError):
                    SplashValidator.validate(bundle)


if __name__ == "__main__":
    unittest.main()
