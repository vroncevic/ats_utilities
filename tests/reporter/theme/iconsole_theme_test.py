# -*- coding: UTF-8 -*-

'''
Module
    test_iconsole_theme.py
Info
    Unit tests for IConsoleTheme protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme


class ConcreteConsoleTheme:
    '''Mock implementation of IConsoleTheme protocol for testing purposes.'''

    def __init__(self) -> None:
        self._colors: dict[str, str] = {
            "error": "\033[91m",
            "success": "\033[92m",
            "warning": "\033[93m",
            "reset": "\033[0m",
        }

    def get_color(self, color_type: str) -> str:
        return self._colors.get(color_type.lower(), self._colors["reset"])

    def __str__(self) -> str:
        return "ConcreteConsoleTheme"


class IncompleteConsoleTheme:
    '''Incomplete class lacking get_color method from IConsoleTheme protocol.'''

    def reset_theme(self) -> None:
        pass


class TestIConsoleTheme(unittest.TestCase):
    '''Unit tests for IConsoleTheme protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Preparing test environment and instance before each test.'''
        self.theme = ConcreteConsoleTheme()

    def test_protocol_conformance(self) -> None:
        '''Tests if the class with all methods passes the runtime_checkable check.'''
        self.assertTrue(isinstance(self.theme, IConsoleTheme))

    def test_protocol_non_conformance(self) -> None:
        '''Tests if the incomplete class fails the isinstance check.'''
        incomplete = IncompleteConsoleTheme()
        self.assertFalse(isinstance(incomplete, IConsoleTheme))

    def test_get_color_valid_type(self) -> None:
        '''Tests the get_color method with defined color types.'''
        self.assertEqual(self.theme.get_color("error"), "\033[91m")
        self.assertEqual(self.theme.get_color("success"), "\033[92m")
        self.assertEqual(self.theme.get_color("warning"), "\033[93m")

    def test_get_color_unknown_type(self) -> None:
        '''Tests the get_color method when an unknown type is provided.'''
        self.assertEqual(self.theme.get_color("unknown"), "\033[0m")

    def test_string_representation(self) -> None:
        '''Tests the __str__ method.'''
        self.assertEqual(str(self.theme), "ConcreteConsoleTheme")


if __name__ == '__main__':
    unittest.main()
