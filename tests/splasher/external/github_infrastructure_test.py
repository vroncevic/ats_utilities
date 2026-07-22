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
from typing import Any

from ats_utilities.context.factory import ContextFactory
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.splasher.external.github_infrastructure import GitHubInfrastructure
from ats_utilities.splasher.splash_keys import SplashKeys

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class GitHubInfrastructureTest(unittest.TestCase):
    '''
        Defines class GitHubInfrastructureTest with attribute(s) and method(s).
        Tests GitHubInfrastructure logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init - Tests constructor.
                | test_getter_setter - Tests property getter and setter.
                | test_setter_invalid - Tests setter error assertions.
                | test_hyperlinks_valid - Tests info, issue, and author hyperlink text outputs.
                | test_hyperlinks_uninitialized - Tests error cases for uninitialized attributes.
                | test_hyperlinks_missing_values - Tests error cases for missing values.
                | test_str - Tests __str__ method.
    '''

    def _get_valid_setup(self) -> dict[str, Any]:
        return {
            SplashKeys.ATS_REPOSITORY: "ats_utilities",
            SplashKeys.ATS_ORGANIZATION: "vroncevic",
        }

    def test_init(self) -> None:
        context_bundle = ContextFactory.create_default_context_bundle()
        gh = GitHubInfrastructure(context_bundle)
        self.assertEqual(gh.infrastructure_property, {})

    def test_getter_setter(self) -> None:
        context_bundle = ContextFactory.create_default_context_bundle()
        gh = GitHubInfrastructure(context_bundle)
        setup = self._get_valid_setup()
        gh.infrastructure_property = setup
        self.assertEqual(gh.infrastructure_property, setup)

    def test_setter_invalid(self) -> None:
        context_bundle = ContextFactory.create_default_context_bundle()
        gh = GitHubInfrastructure(context_bundle)

        # Invalid type
        with self.assertRaises(ATSTypeError):
            gh.infrastructure_property = "not a mapping"  # type: ignore

        # Missing required key
        invalid_setup = self._get_valid_setup()
        del invalid_setup[SplashKeys.ATS_ORGANIZATION]
        with self.assertRaises(ATSValueError):
            gh.infrastructure_property = invalid_setup

    def test_hyperlinks_valid(self) -> None:
        context_bundle = ContextFactory.create_default_context_bundle()
        gh = GitHubInfrastructure(context_bundle)
        gh.infrastructure_property = self._get_valid_setup()

        self.assertIn("github.io/ats_utilities", gh.get_info_text())
        self.assertIn("https://github.com/vroncevic/ats_utilities/issues/new/choose", gh.get_issue_text())
        self.assertIn("vroncevic.github.io", gh.get_author_text())

    def test_hyperlinks_uninitialized(self) -> None:
        context_bundle = ContextFactory.create_default_context_bundle()
        gh = GitHubInfrastructure(context_bundle)

        with self.assertRaises(ATSValueError):
            gh.get_info_text()

        with self.assertRaises(ATSValueError):
            gh.get_issue_text()

        with self.assertRaises(ATSValueError):
            gh.get_author_text()

    def test_hyperlinks_missing_values(self) -> None:
        context_bundle = ContextFactory.create_default_context_bundle()
        gh = GitHubInfrastructure(context_bundle)

        # Bypass setter check using private attribute
        gh._infrastructure_property = {
            SplashKeys.ATS_REPOSITORY: "",
            SplashKeys.ATS_ORGANIZATION: "",
        }

        with self.assertRaises(ATSValueError):
            gh.get_info_text()

        with self.assertRaises(ATSValueError):
            gh.get_issue_text()

        with self.assertRaises(ATSValueError):
            gh.get_author_text()

    def test_str(self) -> None:
        context_bundle = ContextFactory.create_default_context_bundle()
        gh = GitHubInfrastructure(context_bundle)
        self.assertIn("GitHubInfrastructure", str(gh))


if __name__ == "__main__":
    unittest.main()
