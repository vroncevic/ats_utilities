# -*- coding: UTF-8 -*-

'''
Module
    test_isplash_property.py
Info
    Unit tests for ISplashProperty protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.splash.property.isplash_property import ISplashProperty


class ConcreteSplashProperty:
    '''Mock implementation of ISplashProperty protocol for testing purposes.'''

    def __init__(self, initial_settings: dict[str, object] | None = None) -> None:
        self._settings: dict[str, object] = initial_settings or {
            "name": "ats_utilities",
            "repository": "https://github.com/vroncevic/ats_utilities",
            "organization": "vroncevic",
            "logo": "/assets/logo.png",
            "use_github": True,
            "enabled": True,
        }

    @property
    def settings(self) -> dict[str, object]:
        return self._settings

    @settings.setter
    def settings(self, setup: dict[str, object]) -> None:
        if isinstance(setup, dict):
            self._settings = setup

    def is_settings_enabled(self) -> bool:
        return bool(self._settings.get("enabled", False))

    def get_name(self) -> str | None:
        return self._settings.get("name")

    def get_repository(self) -> str | None:
        return self._settings.get("repository")

    def get_organization(self) -> str | None:
        return self._settings.get("organization")

    def get_logo(self) -> str | None:
        return self._settings.get("logo")

    def get_use_github_infrastructure(self) -> bool:
        return bool(self._settings.get("use_github", False))

    def __str__(self) -> str:
        return "ConcreteSplashProperty"


class IncompleteSplashProperty:
    '''Incomplete class lacking most getter methods and settings property.'''

    def get_name(self) -> str | None:
        return "Incomplete"


class TestISplashProperty(unittest.TestCase):
    '''Test suite for ISplashProperty protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Setup test environment and instance before each test.'''
        self.splash_prop = ConcreteSplashProperty()

    def test_protocol_conformance(self) -> None:
        '''Tests whether the class with all methods passes the runtime_checkable check.'''
        self.assertTrue(isinstance(self.splash_prop, ISplashProperty))

    def test_protocol_non_conformance(self) -> None:
        '''Tests whether the incomplete class fails the isinstance check.'''
        incomplete = IncompleteSplashProperty()
        self.assertFalse(isinstance(incomplete, ISplashProperty))

    def test_settings_property_getter_and_setter(self) -> None:
        '''Tests getter and setter for settings property.'''
        current_settings = self.splash_prop.settings
        self.assertEqual(current_settings["name"], "ats_utilities")

        new_settings = {
            "name": "new_tool",
            "repository": "https://github.com/vroncevic/new_tool",
            "organization": "vroncevic",
            "logo": "/assets/new_logo.png",
            "use_github": False,
            "enabled": False,
        }
        self.splash_prop.settings = new_settings
        self.assertEqual(self.splash_prop.settings, new_settings)

    def test_is_settings_enabled(self) -> None:
        '''Tests is_settings_enabled method.'''
        self.assertTrue(self.splash_prop.is_settings_enabled())

        disabled_prop = ConcreteSplashProperty(initial_settings={"enabled": False})
        self.assertFalse(disabled_prop.is_settings_enabled())

    def test_getters_metadata(self) -> None:
        '''Tests get_name, get_repository, get_organization, get_logo and get_use_github_infrastructure.'''
        self.assertEqual(self.splash_prop.get_name(), "ats_utilities")
        self.assertEqual(
            self.splash_prop.get_repository(),
            "https://github.com/vroncevic/ats_utilities"
        )
        self.assertEqual(self.splash_prop.get_organization(), "vroncevic")
        self.assertEqual(self.splash_prop.get_logo(), "/assets/logo.png")
        self.assertTrue(self.splash_prop.get_use_github_infrastructure())

    def test_getters_returns_none(self) -> None:
        '''Tests getters when values are not set in settings.'''
        empty_prop = ConcreteSplashProperty(initial_settings={})
        self.assertIsNotNone(empty_prop.get_name())
        self.assertIsNotNone(empty_prop.get_repository())
        self.assertIsNotNone(empty_prop.get_organization())
        self.assertIsNotNone(empty_prop.get_logo())
        self.assertTrue(empty_prop.get_use_github_infrastructure())

    def test_string_representation(self) -> None:
        '''Tests __str__ method.'''
        self.assertEqual(str(self.splash_prop), "ConcreteSplashProperty")


if __name__ == '__main__':
    unittest.main()
