# -*- coding: UTF-8 -*-

'''
Module
    test_imanager.py
Info
    Unit tests for IOptionManager protocol interface using unittest.
'''

from __future__ import annotations

import unittest
from collections.abc import Sequence

from ats_utilities.option.ioption_configurator import IOptionConfigurator
from ats_utilities.option.ioption_parser import IOptionParser
from ats_utilities.option.imanager import IOptionManager


class MockNamespace:
    '''Helper class for representing parsed options.'''
    def __init__(self, **kwargs: object) -> None:
        self.__dict__.update(kwargs)


class ConcreteOptionManager:
    '''Mock implementacija IOptionManager protokola koja satisfies oba roditeljska protokola.'''

    def __init__(self, bundle: object = None, context: object = None, strategy: str = "argparse") -> None:
        self._bundle: object = bundle or {}
        self._context: object = context or {}
        self._strategy: str = strategy
        self.operations: list[tuple[tuple[str, ...], dict[str, object]]] = []
        self.version: str | None = None
        self.registered_commands: list[object] = []

    # IOptionConfigurator metode
    def add_operation(self, *args: str, **kwargs: object) -> None:
        self.operations.append((args, kwargs))

    def add_version_operation(self, version: str | None) -> None:
        self.version = version

    def register_commands(self, commands: Sequence[object]) -> None:
        self.registered_commands.extend(commands)

    # IOptionParser metode
    def parse_input_args(self, arguments: list[str]) -> MockNamespace:
        return MockNamespace(args=arguments, type="input")

    def parse_args(self, arguments: list[str]) -> MockNamespace:
        return MockNamespace(args=arguments, type="standard")

    def parse_command(self, arguments: list[str] | None = None) -> dict[str, object]:
        return {"parsed_command": "build", "args": arguments or []}

    # IOptionManager sopstvene metode i property
    def get_bundle(self) -> object:
        return self._bundle

    def update_bundle(self, bundle: object) -> bool:
        if isinstance(bundle, dict):
            self._bundle = bundle
            return True
        return False

    def get_context(self) -> object:
        return self._context

    @property
    def strategy(self) -> str:
        return self._strategy

    def is_initialized(self) -> bool:
        return bool(self._bundle) and bool(self._context)

    def __str__(self) -> str:
        return "ConcreteOptionManager"


class IncompleteOptionManager:
    '''Incomplete class that is missing the IOptionConfigurator part of the protocol.'''

    def get_bundle(self) -> object:
        return {}

    def is_initialized(self) -> bool:
        return False


class TestIOptionManager(unittest.TestCase):
    '''Test suite for the IOptionManager protocol using the unittest framework.'''

    def setUp(self) -> None:
        '''Prepares test environment and instance before each test.'''
        self.mock_bundle = {"cli_name": "ats_cli", "default_env": "prod"}
        self.mock_context = {"sys_argv": ["script.py", "--help"]}
        self.manager = ConcreteOptionManager(
            bundle=self.mock_bundle,
            context=self.mock_context,
            strategy="click"
        )

    def test_protocol_conformance(self) -> None:
        '''Tests that the class passes the conformance check for IOptionManager, IOptionConfigurator and IOptionParser.'''
        self.assertTrue(isinstance(self.manager, IOptionManager))
        self.assertTrue(isinstance(self.manager, IOptionConfigurator))
        self.assertTrue(isinstance(self.manager, IOptionParser))

    def test_protocol_non_conformance(self) -> None:
        '''Tests that the incomplete class fails the isinstance check for IOptionManager.'''
        incomplete = IncompleteOptionManager()
        self.assertFalse(isinstance(incomplete, IOptionManager))

    def test_get_bundle(self) -> None:
        '''Tests the get_bundle method.'''
        self.assertEqual(self.manager.get_bundle(), self.mock_bundle)

    def test_update_bundle(self) -> None:
        '''Tests the update_bundle method with valid and invalid input.'''
        new_bundle = {"cli_name": "ats_cli_v2"}
        self.assertTrue(self.manager.update_bundle(new_bundle))
        self.assertEqual(self.manager.get_bundle(), new_bundle)

        self.assertFalse(self.manager.update_bundle("invalid_bundle"))

    def test_get_context(self) -> None:
        '''Tests the get_context method.'''
        self.assertEqual(self.manager.get_context(), self.mock_context)

    def test_strategy_property(self) -> None:
        '''Tests the strategy read-only property.'''
        self.assertEqual(self.manager.strategy, "click")

    def test_is_initialized(self) -> None:
        '''Tests the is_initialized method.'''
        self.assertTrue(self.manager.is_initialized())

        uninit_manager = ConcreteOptionManager()
        self.assertFalse(uninit_manager.is_initialized())

    def test_inherited_configurator_methods(self) -> None:
        '''Tests methods inherited from the IOptionConfigurator protocol.'''
        self.manager.add_operation("-p", "--port", type=int)
        self.assertEqual(len(self.manager.operations), 1)

        self.manager.add_version_operation("1.0.0")
        self.assertEqual(self.manager.version, "1.0.0")

        self.manager.register_commands(["init", "deploy"])
        self.assertEqual(self.manager.registered_commands, ["init", "deploy"])

    def test_inherited_parser_methods(self) -> None:
        '''Tests methods inherited from the IOptionParser protocol.'''
        ns_input = self.manager.parse_input_args(["--port", "8080"])
        self.assertEqual(ns_input.type, "input")

        ns_args = self.manager.parse_args(["--port", "8080"])
        self.assertEqual(ns_args.type, "standard")

        cmd = self.manager.parse_command(["deploy"])
        self.assertEqual(cmd["parsed_command"], "build")

    def test_string_representation(self) -> None:
        '''Tests the __str__ method.'''
        self.assertEqual(str(self.manager), "ConcreteOptionManager")


if __name__ == '__main__':
    unittest.main()
