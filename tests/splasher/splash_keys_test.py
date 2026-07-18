# -*- coding: UTF-8 -*-

'''
Module
    splash_keys_test.py
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
    Unit tests for SplashKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from ats_utilities.splasher.splash_keys import SplashKeys

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class SplashKeysTest(unittest.TestCase):
    '''
        Defines class SplashKeysTest with attribute(s) and method(s).
        Tests SplashKeys configuration model.

        It defines:

            :attributes: None.
            :methods:
                | test_default_init - Tests instantiation with defaults.
                | test_disabled_init - Tests instantiation when enabled=False.
                | test_get_key_to_attr - Tests key mapping helpers.
                | test_from_dict - Tests factory parsing.
                | test_get_all_keys - Tests retrieving list of all keys.
                | test_to_dict - Tests converting to dictionary.
    '''

    def test_default_init(self) -> None:
        keys = SplashKeys()
        self.assertIsNone(keys.name)
        self.assertIsNone(keys.repository)
        self.assertIsNone(keys.organization)
        self.assertIsNone(keys.logo_path)
        self.assertIsNone(keys.use_github_infrastructure)
        self.assertTrue(keys.enabled)

    def test_disabled_init(self) -> None:
        keys = SplashKeys(
            name="test_app",
            repository="test_repo",
            organization="test_org",
            logo_path="/path/to/logo",
            use_github_infrastructure=True,
            enabled=False
        )
        self.assertIsNone(keys.name)
        self.assertIsNone(keys.repository)
        self.assertIsNone(keys.organization)
        self.assertIsNone(keys.logo_path)
        self.assertIsNone(keys.use_github_infrastructure)
        self.assertFalse(keys.enabled)

    def test_get_key_to_attr(self) -> None:
        mapping = SplashKeys.get_key_to_attr()
        self.assertIsInstance(mapping, MappingProxyType)
        self.assertEqual(mapping[SplashKeys.ATS_NAME], "name")
        self.assertEqual(mapping[SplashKeys.ATS_REPOSITORY], "repository")
        self.assertEqual(mapping[SplashKeys.ATS_ORGANIZATION], "organization")
        self.assertEqual(mapping[SplashKeys.ATS_LOGO_PATH], "logo_path")
        self.assertEqual(mapping[SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE], "use_github_infrastructure")

    def test_from_dict(self) -> None:
        config = {
            "enabled": True,
            "ats_name": "app",
            "ats_repository": "repo",
            "ats_organization": "org",
            "ats_logo_path": "/logo.png",
            "ats_use_github_infrastructure": True,
        }
        keys = SplashKeys.from_dict(config)
        self.assertEqual(keys.name, "app")
        self.assertEqual(keys.repository, "repo")
        self.assertEqual(keys.organization, "org")
        self.assertEqual(keys.logo_path, "/logo.png")
        self.assertTrue(keys.use_github_infrastructure)
        self.assertTrue(keys.enabled)

        # From dict when disabled
        config_disabled = {"enabled": False}
        keys_disabled = SplashKeys.from_dict(config_disabled)
        self.assertFalse(keys_disabled.enabled)
        self.assertIsNone(keys_disabled.name)

    def test_get_all_keys(self) -> None:
        all_keys = SplashKeys.get_all_keys()
        self.assertIsInstance(all_keys, tuple)
        self.assertIn("ats_name", all_keys)
        self.assertIn("ats_repository", all_keys)

    def test_to_dict(self) -> None:
        config = {
            "enabled": True,
            "ats_name": "app",
            "ats_repository": "repo",
            "ats_organization": "org",
            "ats_logo_path": "/logo.png",
            "ats_use_github_infrastructure": True,
        }
        keys = SplashKeys.from_dict(config)
        expected = {
            "ats_name": "app",
            "ats_repository": "repo",
            "ats_organization": "org",
            "ats_logo_path": "/logo.png",
            "ats_use_github_infrastructure": True,
        }
        self.assertEqual(keys.to_dict(), expected)

        # To dict when disabled
        keys_disabled = SplashKeys(enabled=False)
        self.assertEqual(keys_disabled.to_dict(), {"enabled": False})


if __name__ == "__main__":
    unittest.main()
