# -*- coding: UTF-8 -*-

'''
Module
    ext_infrastructure_test.py
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
    Unit tests for ExtInfrastructure class.
'''

from __future__ import annotations

import unittest

from ats_utilities.context.factory import ContextFactory
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.splash.external.ext_infrastructure import ExtInfrastructure
from ats_utilities.splash.property.splash_property import SplashProperty


class ExtInfrastructureTest(unittest.TestCase):
    '''
        Defines class ExtInfrastructureTest with attribute(s) and method(s).
        Tests ExtInfrastructure logic.
    '''

    def _get_valid_setup(self) -> dict[str, object]:
        return {
            SplashProperty.NAME_SETTING: "ats_utilities",
            SplashProperty.REPOSITORY_SETTING: "https://github.com/vroncevic/ats_utilities",
            SplashProperty.ORGANIZATION_SETTING: "vroncevic",
        }

    def test_init(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        ext = ExtInfrastructure(context_bundle)
        self.assertEqual(ext.infrastructure_property, {})

    def test_getter_setter(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        ext = ExtInfrastructure(context_bundle)
        setup = self._get_valid_setup()
        ext.infrastructure_property = setup
        self.assertEqual(ext.infrastructure_property, setup)

    def test_setter_invalid(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        ext = ExtInfrastructure(context_bundle)

        # Invalid type
        with self.assertRaises(ATSTypeError):
            ext.infrastructure_property = "not a mapping"  # type: ignore

        # Missing required key
        invalid_setup = self._get_valid_setup()
        del invalid_setup[SplashProperty.NAME_SETTING]
        with self.assertRaises(ATSValueError):
            ext.infrastructure_property = invalid_setup

    def test_hyperlinks_valid(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        ext = ExtInfrastructure(context_bundle)
        ext.infrastructure_property = self._get_valid_setup()

        self.assertIn("ats_utilities", ext.get_info_text())
        self.assertIn("https://github.com/vroncevic/ats_utilities", ext.get_issue_text())
        self.assertIn("vroncevic", ext.get_author_text())

    def test_hyperlinks_uninitialized(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        ext = ExtInfrastructure(context_bundle)

        with self.assertRaises(ATSValueError):
            ext.get_info_text()

        with self.assertRaises(ATSValueError):
            ext.get_issue_text()

        with self.assertRaises(ATSValueError):
            ext.get_author_text()

    def test_hyperlinks_missing_values(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        ext = ExtInfrastructure(context_bundle)

        # Bypass setter check using private attribute
        ext._infrastructure_property = {
            SplashProperty.NAME_SETTING: None,
            SplashProperty.REPOSITORY_SETTING: None,
            SplashProperty.ORGANIZATION_SETTING: None,
        }

        self.assertIsNone(ext.get_info_text())
        self.assertIsNone(ext.get_issue_text())
        self.assertIsNone(ext.get_author_text())

    def test_str(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        ext = ExtInfrastructure(context_bundle)
        self.assertIn("ExtInfrastructure", str(ext))


if __name__ == "__main__":
    unittest.main()
