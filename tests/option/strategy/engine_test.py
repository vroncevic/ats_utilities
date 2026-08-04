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
    Unit tests for ParserStrategy class.
'''

from __future__ import annotations

import sys
import unittest
from argparse import ArgumentParser
from collections.abc import Sequence
from unittest.mock import MagicMock

from ats_utilities.context.factory import ContextBundleFactory
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.option.command.data import OptionData
from ats_utilities.option.command.ioption_command import IOptionCommand
from ats_utilities.option.underlying.engine import ParserAdapter
from ats_utilities.option.strategy.data import StrategyData
from ats_utilities.option.strategy.engine import ParserStrategy

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class DummyCommand(IOptionCommand):
    '''
        Dummy command to test parser strategy register commands.
    '''
    @property
    def name(self) -> str:
        return "dummy"

    @property
    def help_text(self) -> str:
        return "dummy help"

    @property
    def options(self) -> Sequence[OptionData]:
        return [
            OptionData(name="--flag", help_text="flag help", action="store_true", default=None, required=False, choices=None, nargs=None),
            OptionData(name="--choice", help_text="choice help", choices=["1", "2"], default="1", required=False, action=None, nargs=None),
            OptionData(name="--num", help_text="num help", nargs=2, action=None, default=None, required=False, choices=None),
            OptionData(name="--req", help_text="req help", required=True, action=None, default=None, choices=None, nargs=None)
        ]

    def __str__(self) -> str:
        return "DummyCommand"


class EngineTest(unittest.TestCase):
    '''
        Defines class EngineTest with attribute(s) and method(s).
        Tests ParserStrategy engine logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init_valid - Tests successful ParserStrategy initialization.
                | test_init_invalid - Tests ParserStrategy initialization exceptions.
                | test_add_argument - Tests add_argument delegation.
                | test_add_version - Tests add_version delegation.
                | test_parse - Tests parsing arguments.
                | test_register_commands - Tests registering and parsing commands.
                | test_parse_command_sys_argv - Tests parse_command defaults to sys.argv.
                | test_is_initialized - Tests is_initialized method.
                | test_str - Tests __str__ representation.
    '''

    def test_init_valid(self) -> None:
        '''
            Tests successful ParserStrategy initialization.

            :exceptions: None.
        '''
        context_bundle = ContextBundleFactory.create_bundle()
        parser = ParserAdapter(ArgumentParser(prog="mytool 1.0.0"))

        bundle = StrategyData(
            context_bundle=context_bundle,
            parser=parser
        )
        strategy = ParserStrategy(bundle)
        self.assertIs(strategy._context, context_bundle)
        self.assertTrue(strategy.is_initialized())

    def test_init_invalid(self) -> None:
        '''
            Tests ParserStrategy initialization exceptions.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError):
            ParserStrategy(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            ParserStrategy("not a bundle")  # type: ignore

    def test_add_argument(self) -> None:
        '''
            Tests add_argument delegation.

            :exceptions: None.
        '''
        context_bundle = ContextBundleFactory.create_bundle()
        parser = ParserAdapter(ArgumentParser())

        bundle = StrategyData(
            context_bundle=context_bundle,
            parser=parser
        )
        strategy = ParserStrategy(bundle)
        strategy.add_argument("-f", "--file", dest="file")
        
        # Test parsing it
        ns = strategy.parse(["-f", "test.txt"])
        self.assertEqual(getattr(ns, "file"), "test.txt")

    def test_add_version(self) -> None:
        '''
            Tests add_version delegation.

            :exceptions: None.
        '''
        context_bundle = ContextBundleFactory.create_bundle()
        parser = ParserAdapter(ArgumentParser())

        bundle = StrategyData(
            context_bundle=context_bundle,
            parser=parser
        )
        strategy = ParserStrategy(bundle)
        strategy.add_version("1.2.3")

        # When --version is parsed, it prints version and exits
        with self.assertRaises(SystemExit):
            strategy.parse(["--version"])

    def test_parse(self) -> None:
        '''
            Tests parsing arguments.

            :exceptions: None.
        '''
        context_bundle = ContextBundleFactory.create_bundle()
        parser = ParserAdapter(ArgumentParser())

        bundle = StrategyData(
            context_bundle=context_bundle,
            parser=parser
        )
        strategy = ParserStrategy(bundle)
        strategy.add_argument("-v", "--verbose", action="store_true")

        # Test normal parse (known_only=False)
        ns1 = strategy.parse(["-v"])
        self.assertTrue(getattr(ns1, "verbose"))

        # Test parse known args (known_only=True)
        ns2 = strategy.parse(["-v", "extra_arg"], known_only=True)
        self.assertTrue(getattr(ns2, "verbose"))

    def test_register_commands(self) -> None:
        '''
            Tests registering and parsing commands.

            :exceptions: None.
        '''
        context_bundle = ContextBundleFactory.create_bundle()
        parser = ParserAdapter(ArgumentParser())
        bundle = StrategyData(
            context_bundle=context_bundle,
            parser=parser
        )
        strategy = ParserStrategy(bundle)
        cmd = DummyCommand()
        strategy.register_commands([cmd])

        class DummyCommand2(DummyCommand):
            @property
            def name(self) -> str:
                return "dummy2"

        cmd2 = DummyCommand2()
        # Register a second time to hit the "subparsers already exist" branch
        strategy.register_commands([cmd2])

        # Test parsing the command
        cmd_name, params = strategy.parse_command(["dummy", "--flag", "--choice", "2", "--num", "1", "2", "--req", "req_val"])
        self.assertEqual(cmd_name, "dummy")
        self.assertTrue(params["flag"])
        self.assertEqual(params["choice"], "2")
        self.assertEqual(params["num"], ["1", "2"])
        self.assertEqual(params["req"], "req_val")

    def test_parse_command_sys_argv(self) -> None:
        '''
            Tests parse_command defaults to sys.argv.

            :exceptions: None.
        '''
        context_bundle = ContextBundleFactory.create_bundle()
        parser = ParserAdapter(ArgumentParser())

        bundle = StrategyData(
            context_bundle=context_bundle,
            parser=parser
        )
        strategy = ParserStrategy(bundle)
        cmd = DummyCommand()
        strategy.register_commands([cmd])

        test_args = ["mytool", "dummy", "--flag", "--req", "req_val"]

        with unittest.mock.patch("ats_utilities.option.strategy.engine.argv", test_args):
            cmd_name, params = strategy.parse_command(None)
            self.assertEqual(cmd_name, "dummy")
            self.assertTrue(params["flag"])

    def test_is_initialized(self) -> None:
        '''
            Tests is_initialized method.

            :exceptions: None.
        '''
        context_bundle = ContextBundleFactory.create_bundle()
        parser = ParserAdapter(ArgumentParser())
        bundle = StrategyData(
            context_bundle=context_bundle,
            parser=parser
        )
        strategy = ParserStrategy(bundle)
        self.assertTrue(strategy.is_initialized())

    def test_str(self) -> None:
        '''
            Tests __str__ representation.

            :exceptions: None.
        '''
        context_bundle = ContextBundleFactory.create_bundle()
        parser = ParserAdapter(ArgumentParser())
        bundle = StrategyData(
            context_bundle=context_bundle,
            parser=parser
        )
        strategy = ParserStrategy(bundle)
        self.assertIn("ParserStrategy", str(strategy))


if __name__ == "__main__":
    unittest.main()
