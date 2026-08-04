# -*- coding: UTF-8 -*-

'''
Module
    test_ioption_parser.py
Info
    Unit tests for IOptionParser protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.option.ioption_parser import IOptionParser


class MockNamespace:
    '''Helper class for representing parsed options.'''
    def __init__(self, **kwargs: object) -> None:
        self.__dict__.update(kwargs)


class ConcreteOptionParser:
    '''Mock implementation of IOptionParser protocol for testing purposes.'''

    def parse_input_args(self, arguments: list[str]) -> MockNamespace:
        return MockNamespace(args=arguments, source="input")

    def parse_args(self, arguments: list[str]) -> MockNamespace:
        return MockNamespace(args=arguments, source="standard")

    def parse_command(self, arguments: list[str] | None = None) -> dict[str, object]:
        return {"command": "run", "raw_args": arguments or []}


class IncompleteOptionParser:
    '''Incomplete class missing parse_command method.'''

    def parse_args(self, arguments: list[str]) -> MockNamespace:
        return MockNamespace()


class TestIOptionParser(unittest.TestCase):
    '''Test suite for IOptionParser protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Setup test environment before each test.'''
        self.parser = ConcreteOptionParser()

    def test_protocol_conformance(self) -> None:
        '''Tests if a class with all methods passes the runtime_checkable check.'''
        self.assertTrue(isinstance(self.parser, IOptionParser))

    def test_protocol_non_conformance(self) -> None:
        '''Tests if an incomplete class fails the isinstance check.'''
        incomplete = IncompleteOptionParser()
        self.assertFalse(isinstance(incomplete, IOptionParser))

    def test_parse_input_args(self) -> None:
        '''Tests the parse_input_args method.'''
        res = self.parser.parse_input_args(["--config", "settings.json"])
        self.assertEqual(res.source, "input")
        self.assertEqual(res.args, ["--config", "settings.json"])

    def test_parse_args(self) -> None:
        '''Tests the parse_args method.'''
        res = self.parser.parse_args(["--debug"])
        self.assertEqual(res.source, "standard")
        self.assertEqual(res.args, ["--debug"])

    def test_parse_command(self) -> None:
        '''Tests the parse_command method with and without explicit arguments.'''
        res = self.parser.parse_command(["exec", "build"])
        self.assertEqual(res, {"command": "run", "raw_args": ["exec", "build"]})

        res_default = self.parser.parse_command()
        self.assertEqual(res_default, {"command": "run", "raw_args": []})


if __name__ == '__main__':
    unittest.main()
