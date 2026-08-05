# -*- coding: UTF-8 -*-

'''
Module
    test_iparser_strategy.py
Info
    Unit tests for IParserStrategy protocol interface using unittest.
'''

from __future__ import annotations

import unittest
from collections.abc import Sequence
from typing import Any

from ats_utilities.option.strategy.iparser_strategy import IParserStrategy


class MockNamespace:
    '''Helper class for representing parsed results.'''
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)


class ConcreteParserStrategy:
    '''Mock implementation of IParserStrategy protocol for testing purposes.'''

    def __init__(self) -> None:
        self.arguments: list[tuple[tuple[str, ...], dict[str, Any]]] = []
        self.version: str | None = None
        self.registered_commands: list[Any] = []
        self._initialized: bool = True

    def add_argument(self, *args: str, **kwargs: object) -> None:
        self.arguments.append((args, kwargs))

    def add_version(self, version: str | None) -> None:
        self.version = version

    def parse(self, arguments: list[str], known_only: bool = False) -> MockNamespace:
        return MockNamespace(raw_args=arguments, known_only=known_only)

    def register_commands(self, commands: Sequence[Any]) -> None:
        self.registered_commands.extend(commands)

    def parse_command(self, arguments: list[str] | None = None) -> dict[str, Any]:
        return {"command": "run", "parsed_args": arguments or []}

    def is_initialized(self) -> bool:
        return self._initialized

    def __str__(self) -> str:
        return "ConcreteParserStrategy"


class IncompleteParserStrategy:
    '''Incomplete class that is missing key protocol methods.'''

    def is_initialized(self) -> bool:
        return False


class TestIParserStrategy(unittest.TestCase):
    '''Test suite for IParserStrategy protocol using the unittest framework.'''

    def setUp(self) -> None:
        '''Prepares test environment and instance before each test.'''
        self.strategy = ConcreteParserStrategy()

    def test_protocol_conformance(self) -> None:
        '''Tests that the class with all methods passes the runtime_checkable check.'''
        self.assertTrue(isinstance(self.strategy, IParserStrategy))

    def test_protocol_non_conformance(self) -> None:
        '''Tests that the incomplete class fails the isinstance check.'''
        incomplete = IncompleteParserStrategy()
        self.assertFalse(isinstance(incomplete, IParserStrategy))

    def test_add_argument(self) -> None:
        '''Tests the add_argument method for adding options.'''
        self.strategy.add_argument("-f", "--file", type=str, required=True)
        self.assertEqual(len(self.strategy.arguments), 1)
        args, kwargs = self.strategy.arguments[0]
        self.assertEqual(args, ("-f", "--file"))
        self.assertEqual(kwargs, {"type": str, "required": True})

    def test_add_version(self) -> None:
        '''Tests the add_version method for setting version information.'''
        self.strategy.add_version("3.4.6")
        self.assertEqual(self.strategy.version, "3.4.6")

        self.strategy.add_version(None)
        self.assertIsNone(self.strategy.version)

    def test_parse(self) -> None:
        '''Tests the parse method with and without known_only flag.'''
        res = self.strategy.parse(["--file", "test.txt"], known_only=True)
        self.assertEqual(res.raw_args, ["--file", "test.txt"])
        self.assertTrue(res.known_only)

    def test_register_commands(self) -> None:
        '''Tests the register_commands method for registering subcommands.'''
        cmds = ["build", "test", "deploy"]
        self.strategy.register_commands(cmds)
        self.assertEqual(self.strategy.registered_commands, cmds)

    def test_parse_command(self) -> None:
        '''Tests the parse_command method for processing CLI subcommands.'''
        res = self.strategy.parse_command(["build", "--verbose"])
        self.assertEqual(res["command"], "run")
        self.assertEqual(res["parsed_args"], ["build", "--verbose"])

    def test_is_initialized(self) -> None:
        '''Tests the is_initialized method for verifying strategy state.'''
        self.assertTrue(self.strategy.is_initialized())
        self.strategy._initialized = False
        self.assertFalse(self.strategy.is_initialized())

    def test_string_representation(self) -> None:
        '''Tests the __str__ method.'''
        self.assertEqual(str(self.strategy), "ConcreteParserStrategy")


if __name__ == '__main__':
    unittest.main()
