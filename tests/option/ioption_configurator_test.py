# -*- coding: UTF-8 -*-

'''
Module
    test_ioption_configurator.py
Info
    Unit tests for IOptionConfigurator protocol interface using unittest.
'''

from __future__ import annotations

import unittest
from collections.abc import Sequence

from ats_utilities.option.ioption_configurator import IOptionConfigurator


class ConcreteOptionConfigurator:
    '''Mock implementation of IOptionConfigurator protocol for testing purposes.'''

    def __init__(self) -> None:
        self.operations: list[tuple[tuple[str, ...], dict[str, object]]] = []
        self.version: str | None = None
        self.registered_commands: list[object] = []

    def add_operation(self, *args: str, **kwargs: object) -> None:
        self.operations.append((args, kwargs))

    def add_version_operation(self, version: str | None) -> None:
        self.version = version

    def register_commands(self, commands: Sequence[object]) -> None:
        self.registered_commands.extend(commands)


class IncompleteOptionConfigurator:
    '''Incomplete class lacking methods from IOptionConfigurator protocol.'''

    def add_version_operation(self, version: str | None) -> None:
        pass


class TestIOptionConfigurator(unittest.TestCase):
    '''Test suite for IOptionConfigurator protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Setup test environment and instance before each test.'''
        self.configurator = ConcreteOptionConfigurator()

    def test_protocol_conformance(self) -> None:
        '''Tests whether the class with all methods passes the runtime_checkable check.'''
        self.assertTrue(isinstance(self.configurator, IOptionConfigurator))

    def test_protocol_non_conformance(self) -> None:
        '''Tests whether the incomplete class fails the isinstance check.'''
        incomplete = IncompleteOptionConfigurator()
        self.assertFalse(isinstance(incomplete, IOptionConfigurator))

    def test_add_operation(self) -> None:
        '''Tests add_operation method with positional and keyword arguments.'''
        self.configurator.add_operation("-v", "--verbose", action="store_true", help="Verbose mode")
        self.assertEqual(len(self.configurator.operations), 1)
        args, kwargs = self.configurator.operations[0]
        self.assertEqual(args, ("-v", "--verbose"))
        self.assertEqual(kwargs, {"action": "store_true", "help": "Verbose mode"})

    def test_add_version_operation(self) -> None:
        '''Tests add_version_operation method.'''
        self.configurator.add_version_operation("3.4.6")
        self.assertEqual(self.configurator.version, "3.4.6")

        self.configurator.add_version_operation(None)
        self.assertIsNone(self.configurator.version)

    def test_register_commands(self) -> None:
        '''Tests register_commands method for registering a sequence of commands.'''
        commands = ["start", "stop", "restart"]
        self.configurator.register_commands(commands)
        self.assertEqual(self.configurator.registered_commands, commands)


if __name__ == '__main__':
    unittest.main()
