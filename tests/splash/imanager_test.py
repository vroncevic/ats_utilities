# -*- coding: UTF-8 -*-

'''
Module
    test_imanager.py
Info
    Unit tests for ISplashManager protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.splash.imanager import ISplashManager


class ConcreteSplashManager:
    '''Mock implementation of ISplashManager protocol for testing purposes.'''

    def __init__(self, bundle: object = None, context: object = None) -> None:
        self._bundle: object = bundle or {}
        self._context: object = context or {"env": "cli"}
        self._visible: bool = False
        self._centered_lines: list[tuple[object, str]] = []

    def get_bundle(self) -> object:
        return self._bundle

    def update_bundle(self, bundle: object) -> bool:
        if isinstance(bundle, dict):
            self._bundle = bundle
            return True
        return False

    def get_context(self) -> object:
        return self._context

    def show(self) -> None:
        self._visible = True

    def center(self, position: object, text: str) -> None:
        self._centered_lines.append((position, text))

    def is_initialized(self) -> bool:
        return bool(self._bundle) and bool(self._context)

    def __str__(self) -> str:
        return "ConcreteSplashManager"


class IncompleteSplashManager:
    '''Incomplete class lacking most methods from ISplashManager protocol.'''

    def show(self) -> None:
        pass


class TestISplashManager(unittest.TestCase):
    '''Test suite for ISplashManager protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Setup test environment and instance before each test.'''
        self.mock_bundle = {"title": "ATS Utilities", "version": "3.4.4"}
        self.mock_context = {"width": 80, "height": 24}
        self.splash_manager = ConcreteSplashManager(
            bundle=self.mock_bundle,
            context=self.mock_context
        )

    def test_protocol_conformance(self) -> None:
        '''Tests whether the class with all methods passes the runtime_checkable check.'''
        self.assertTrue(isinstance(self.splash_manager, ISplashManager))

    def test_protocol_non_conformance(self) -> None:
        '''Tests whether the incomplete class fails the isinstance check.'''
        incomplete = IncompleteSplashManager()
        self.assertFalse(isinstance(incomplete, ISplashManager))

    def test_get_bundle(self) -> None:
        '''Tests the get_bundle method.'''
        self.assertEqual(self.splash_manager.get_bundle(), self.mock_bundle)

    def test_update_bundle(self) -> None:
        '''Tests the update_bundle method with valid and invalid input.'''
        new_bundle = {"title": "ATS CLI Suite", "version": "4.0.0"}
        self.assertTrue(self.splash_manager.update_bundle(new_bundle))
        self.assertEqual(self.splash_manager.get_bundle(), new_bundle)

        self.assertFalse(self.splash_manager.update_bundle("invalid_bundle"))

    def test_get_context(self) -> None:
        '''Tests the get_context method.'''
        self.assertEqual(self.splash_manager.get_context(), self.mock_context)

    def test_show(self) -> None:
        '''Tests the show method for displaying the splash screen.'''
        self.assertFalse(self.splash_manager._visible)
        self.splash_manager.show()
        self.assertTrue(self.splash_manager._visible)

    def test_center(self) -> None:
        '''Tests the center method for positioning and centering text.'''
        self.splash_manager.center(10, "Welcome to ATS Utilities")
        self.assertIn((10, "Welcome to ATS Utilities"), self.splash_manager._centered_lines)

    def test_is_initialized(self) -> None:
        '''Tests the is_initialized method.'''
        self.assertTrue(self.splash_manager.is_initialized())

        uninit_manager = ConcreteSplashManager()
        self.assertFalse(uninit_manager.is_initialized())

    def test_string_representation(self) -> None:
        '''Tests the __str__ method.'''
        self.assertEqual(str(self.splash_manager), "ConcreteSplashManager")


if __name__ == '__main__':
    unittest.main()
