# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
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
    Unit tests for OptionManager class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.context_registry import ContextRegistry
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.option.command.ioption_command import IOptionCommand
from ats_utilities.option.engine import OptionManager
from ats_utilities.option.option_bundle import OptionBundle
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class EngineTest(unittest.TestCase):
    '''
        Defines class EngineTest with attribute(s) and method(s).
        Tests OptionManager engine logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init_valid - Tests option manager successful initialization.
                | test_init_invalid - Tests option manager initialization exceptions.
                | test_get_shared_context - Tests get_shared_context.
                | test_add_operation - Tests add_operation.
                | test_add_version_operation - Tests add_version_operation.
                | test_parse_input_args - Tests parse_input_args.
                | test_parse_args - Tests parse_args.
                | test_register_commands - Tests register_commands.
                | test_parse_command - Tests parse_command.
                | test_is_initialized - Tests is_initialized.
                | test_str - Tests __str__ representation.
    '''

    def test_init_valid(self) -> None:
        '''
            Tests option manager successful initialization.

            :exceptions: None.
        '''
        mock_strategy = MagicMock(spec=IParserStrategy)
        context_bundle = ContextRegistry.create_default_context_bundle()
        bundle = OptionBundle(
            parameters={"name": "test"},
            strategy=mock_strategy,
            context_bundle=context_bundle
        )

        manager = OptionManager(bundle)
        self.assertTrue(manager._is_initialized)
        self.assertIs(manager._strategy, mock_strategy)
        self.assertIs(manager.get_shared_context(), context_bundle)

    def test_init_invalid(self) -> None:
        '''
            Tests option manager initialization exceptions.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError):
            OptionManager(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            OptionManager("not a bundle")  # type: ignore

    def test_get_shared_context(self) -> None:
        '''
            Tests get_shared_context.

            :exceptions: None.
        '''
        mock_strategy = MagicMock(spec=IParserStrategy)
        context_bundle = ContextRegistry.create_default_context_bundle()
        bundle = OptionBundle(
            parameters={"name": "test"},
            strategy=mock_strategy,
            context_bundle=context_bundle
        )
        manager = OptionManager(bundle)
        self.assertIs(manager.get_shared_context(), context_bundle)

    def test_add_operation(self) -> None:
        '''
            Tests add_operation.

            :exceptions: None.
        '''
        mock_strategy = MagicMock(spec=IParserStrategy)
        context_bundle = ContextRegistry.create_default_context_bundle()
        bundle = OptionBundle(
            parameters={"name": "test"},
            strategy=mock_strategy,
            context_bundle=context_bundle
        )
        manager = OptionManager(bundle)
        manager.add_operation("-f", "--flag", dest="flag", help="test flag")
        mock_strategy.add_argument.assert_called_once_with("-f", "--flag", dest="flag", help="test flag")

    def test_add_version_operation(self) -> None:
        '''
            Tests add_version_operation.

            :exceptions: None.
        '''
        mock_strategy = MagicMock(spec=IParserStrategy)
        context_bundle = ContextRegistry.create_default_context_bundle()
        bundle = OptionBundle(
            parameters={"name": "test"},
            strategy=mock_strategy,
            context_bundle=context_bundle
        )
        manager = OptionManager(bundle)

        # Test with version value
        manager.add_version_operation("1.2.3")
        mock_strategy.add_version.assert_called_once_with("1.2.3")

        # Test with None or empty (should not call add_version)
        mock_strategy.reset_mock()
        manager.add_version_operation(None)
        mock_strategy.add_version.assert_not_called()

    def test_parse_input_args(self) -> None:
        '''
            Tests parse_input_args.

            :exceptions: None.
        '''
        mock_strategy = MagicMock(spec=IParserStrategy)
        mock_ns = MagicMock(spec=OptionNamespace)
        mock_strategy.parse.return_value = mock_ns

        context_bundle = ContextRegistry.create_default_context_bundle()
        bundle = OptionBundle(
            parameters={"name": "test"},
            strategy=mock_strategy,
            context_bundle=context_bundle
        )
        manager = OptionManager(bundle)
        res = manager.parse_input_args(["-f", "val"])
        mock_strategy.parse.assert_called_once_with(["-f", "val"], known_only=False)
        self.assertIs(res, mock_ns)

    def test_parse_args(self) -> None:
        '''
            Tests parse_args.

            :exceptions: None.
        '''
        mock_strategy = MagicMock(spec=IParserStrategy)
        mock_ns = MagicMock(spec=OptionNamespace)
        mock_strategy.parse.return_value = mock_ns

        context_bundle = ContextRegistry.create_default_context_bundle()
        bundle = OptionBundle(
            parameters={"name": "test"},
            strategy=mock_strategy,
            context_bundle=context_bundle
        )
        manager = OptionManager(bundle)
        res = manager.parse_args(["-f", "val"])
        mock_strategy.parse.assert_called_once_with(["-f", "val"], known_only=True)
        self.assertIs(res, mock_ns)

    def test_register_commands(self) -> None:
        '''
            Tests register_commands.

            :exceptions: None.
        '''
        mock_strategy = MagicMock(spec=IParserStrategy)
        context_bundle = ContextRegistry.create_default_context_bundle()
        bundle = OptionBundle(
            parameters={"name": "test"},
            strategy=mock_strategy,
            context_bundle=context_bundle
        )
        manager = OptionManager(bundle)
        mock_cmd = MagicMock(spec=IOptionCommand)
        manager.register_commands([mock_cmd])
        mock_strategy.register_commands.assert_called_once_with([mock_cmd])

    def test_parse_command(self) -> None:
        '''
            Tests parse_command.

            :exceptions: None.
        '''
        mock_strategy = MagicMock(spec=IParserStrategy)
        mock_strategy.parse_command.return_value = ("cmd", {"arg": "val"})

        context_bundle = ContextRegistry.create_default_context_bundle()
        bundle = OptionBundle(
            parameters={"name": "test"},
            strategy=mock_strategy,
            context_bundle=context_bundle
        )
        manager = OptionManager(bundle)
        res = manager.parse_command(["cmd", "arg"])
        mock_strategy.parse_command.assert_called_once_with(["cmd", "arg"])
        self.assertEqual(res, ("cmd", {"arg": "val"}))

    def test_is_initialized(self) -> None:
        '''
            Tests is_initialized.

            :exceptions: None.
        '''
        mock_strategy = MagicMock(spec=IParserStrategy)
        mock_strategy.is_initialized.return_value = True

        context_bundle = ContextRegistry.create_default_context_bundle()
        bundle = OptionBundle(
            parameters={"name": "test"},
            strategy=mock_strategy,
            context_bundle=context_bundle
        )
        manager = OptionManager(bundle)
        self.assertTrue(manager.is_initialized())

        # When strategy is not initialized
        mock_strategy.is_initialized.return_value = False
        self.assertFalse(manager.is_initialized())

    def test_str(self) -> None:
        '''
            Tests __str__ representation.

            :exceptions: None.
        '''
        mock_strategy = MagicMock(spec=IParserStrategy)
        context_bundle = ContextRegistry.create_default_context_bundle()
        bundle = OptionBundle(
            parameters={"name": "test"},
            strategy=mock_strategy,
            context_bundle=context_bundle
        )
        manager = OptionManager(bundle)
        self.assertIn("OptionManager", str(manager))


if __name__ == "__main__":
    unittest.main()
