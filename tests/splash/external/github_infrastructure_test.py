# -*- coding: UTF-8 -*-

'''
Module
    github_infrastructure_test.py
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
    Unit tests for GitHubInfrastructure class.
'''

from __future__ import annotations

import unittest

from ats_utilities.context.factory import ContextFactory
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.splash.external.github_infrastructure import GitHubInfrastructure
from ats_utilities.splash.property.splash_property import SplashProperty


class GitHubInfrastructureTest(unittest.TestCase):
    '''
        Defines class GitHubInfrastructureTest with attribute(s) and method(s).
        Tests GitHubInfrastructure logic.
    '''

    def _get_valid_setup(self) -> dict[str, object]:
        return {
            SplashProperty.REPOSITORY_SETTING: "ats_utilities",
            SplashProperty.ORGANIZATION_SETTING: "vroncevic",
        }

    def test_init(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        gh = GitHubInfrastructure(context_bundle)
        self.assertEqual(gh.infrastructure_property, {})

    def test_getter_setter(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        gh = GitHubInfrastructure(context_bundle)
        setup = self._get_valid_setup()
        gh.infrastructure_property = setup
        self.assertEqual(gh.infrastructure_property, setup)

    def test_setter_invalid(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        gh = GitHubInfrastructure(context_bundle)

        # Invalid type
        with self.assertRaises(ATSTypeError):
            gh.infrastructure_property = "not a mapping"  # type: ignore

        # Missing required key
        invalid_setup = self._get_valid_setup()
        del invalid_setup[SplashProperty.ORGANIZATION_SETTING]
        with self.assertRaises(ATSValueError):
            gh.infrastructure_property = invalid_setup

    def test_hyperlinks_valid(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        gh = GitHubInfrastructure(context_bundle)
        gh.infrastructure_property = self._get_valid_setup()

        self.assertIn("github.io/ats_utilities", gh.get_info_text())
        self.assertIn("https://github.com/vroncevic/ats_utilities/issues/new/choose", gh.get_issue_text())
        self.assertIn("vroncevic.github.io", gh.get_author_text())

    def test_hyperlinks_uninitialized(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        gh = GitHubInfrastructure(context_bundle)

        with self.assertRaises(ATSValueError):
            gh.get_info_text()

        with self.assertRaises(ATSValueError):
            gh.get_issue_text()

        with self.assertRaises(ATSValueError):
            gh.get_author_text()

    def test_hyperlinks_missing_values(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        gh = GitHubInfrastructure(context_bundle)

        # Bypass setter check using private attribute
        gh._infrastructure_property = {
            SplashProperty.REPOSITORY_SETTING: None,
            SplashProperty.ORGANIZATION_SETTING: None,
        }

        self.assertIsNone(gh.get_info_text())
        self.assertIsNone(gh.get_issue_text())
        self.assertIsNone(gh.get_author_text())

    def test_str(self) -> None:
        context_bundle = ContextFactory.create_bundle()
        gh = GitHubInfrastructure(context_bundle)
        self.assertIn("GitHubInfrastructure", str(gh))


if __name__ == "__main__":
    unittest.main()
