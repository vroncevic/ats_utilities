# -*- coding: UTF-8 -*-

'''
Module
    test_iinfo_manager.py
Info
    Unit tests for IInfoManager protocol interface using unittest.
'''

from __future__ import annotations

import unittest
from typing import Any

from ats_utilities.info.imanager import IInfoManager


class ConcreteInfoManager:
    '''Mock implementation of IInfoManager protocol for testing purposes.'''

    def __init__(self, bundle: Any = None, context: Any = None, info: Any = None) -> None:
        self._bundle: Any = bundle or {}
        self._context: Any = context or {}
        self._info: Any = info or {}
        self.refreshed: bool = False

    def get_bundle(self) -> Any:
        return self._bundle

    def update_bundle(self, bundle: Any) -> bool:
        if isinstance(bundle, dict):
            self._bundle = bundle
            return True
        return False

    def get_context(self) -> Any:
        return self._context

    def set_info(self, info: Any) -> None:
        self._info = info

    def get_info(self) -> Any:
        return self._info

    def is_initialized(self) -> bool:
        return bool(self._bundle) and bool(self._context) and bool(self._info)

    def refresh_status(self) -> None:
        self.refreshed = True

    def __str__(self) -> str:
        return "ConcreteInfoManager"


class IncompleteInfoManager:
    '''Incomplete class that is missing key protocol methods.'''

    def get_info(self) -> Any:
        return {}


class TestIInfoManager(unittest.TestCase):
    '''Test suite for IInfoManager protocol using the unittest framework.'''

    def setUp(self) -> None:
        '''Prepares test environment and instance before each test.'''
        self.mock_bundle = {"info_file": "config/info.yaml", "format": "yaml"}
        self.mock_context = {"env": "production"}
        self.mock_info = {"app_name": "ats_utilities", "version": "3.4.6"}

        self.info_manager = ConcreteInfoManager(
            bundle=self.mock_bundle,
            context=self.mock_context,
            info=self.mock_info
        )

    def test_protocol_conformance(self) -> None:
        '''Tests that the class with all methods passes the runtime_checkable check.'''
        self.assertTrue(isinstance(self.info_manager, IInfoManager))

    def test_protocol_non_conformance(self) -> None:
        '''Tests that the incomplete class fails the isinstance check.'''
        incomplete = IncompleteInfoManager()
        self.assertFalse(isinstance(incomplete, IInfoManager))

    def test_get_bundle(self) -> None:
        '''Tests the get_bundle method.'''
        self.assertEqual(self.info_manager.get_bundle(), self.mock_bundle)

    def test_update_bundle(self) -> None:
        '''Tests the update_bundle method with valid and invalid input.'''
        new_bundle = {"info_file": "config/new_info.yaml", "format": "yaml"}
        self.assertTrue(self.info_manager.update_bundle(new_bundle))
        self.assertEqual(self.info_manager.get_bundle(), new_bundle)

        self.assertFalse(self.info_manager.update_bundle("invalid_bundle"))

    def test_get_context(self) -> None:
        '''Tests the get_context method.'''
        self.assertEqual(self.info_manager.get_context(), self.mock_context)

    def test_set_and_get_info(self) -> None:
        '''Tests the set_info and get_info methods for handling the info structure.'''
        self.assertEqual(self.info_manager.get_info(), self.mock_info)

        updated_info = {"app_name": "ats_utilities", "version": "3.5.0"}
        self.info_manager.set_info(updated_info)
        self.assertEqual(self.info_manager.get_info(), updated_info)

    def test_is_initialized(self) -> None:
        '''Tests the is_initialized method.'''
        self.assertTrue(self.info_manager.is_initialized())

        uninit_manager = ConcreteInfoManager()
        self.assertFalse(uninit_manager.is_initialized())

    def test_refresh_status(self) -> None:
        '''Tests the refresh_status method.'''
        self.assertFalse(self.info_manager.refreshed)
        self.info_manager.refresh_status()
        self.assertTrue(self.info_manager.refreshed)

    def test_string_representation(self) -> None:
        '''Tests the __str__ method.'''
        self.assertEqual(str(self.info_manager), "ConcreteInfoManager")


if __name__ == '__main__':
    unittest.main()
