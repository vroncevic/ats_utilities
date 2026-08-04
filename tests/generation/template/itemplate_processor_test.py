# -*- coding: UTF-8 -*-

'''
Module
    test_itemplate_processor.py
Info
    Unit tests for ITemplateProcessor protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.generation.template.itemplate_processor import ITemplateProcessor


class ConcreteTemplateProcessor:
    '''Mock implementation of ITemplateProcessor protocol for testing purposes.'''

    def __init__(self, initialized: bool = True) -> None:
        self._initialized = initialized

    def render(self, raw_content: bytes, vals: dict[str, str]) -> str | bytes:
        try:
            content_str = raw_content.decode('utf-8')
            for k, v in vals.items():
                content_str = content_str.replace(f"${{{k}}}", v)
            return content_str
        except UnicodeDecodeError:
            return raw_content

    def is_initialized(self) -> bool:
        return self._initialized

    def __str__(self) -> str:
        return "ConcreteTemplateProcessor"


class IncompleteTemplateProcessor:
    '''Incomplete class for negative test.'''

    def is_initialized(self) -> bool:
        return False


class TestITemplateProcessor(unittest.TestCase):
    '''Test suite for ITemplateProcessor protocol.'''

    def setUp(self) -> None:
        self.processor = ConcreteTemplateProcessor()

    def test_protocol_conformance(self) -> None:
        self.assertTrue(isinstance(self.processor, ITemplateProcessor))

    def test_protocol_non_conformance(self) -> None:
        incomplete = IncompleteTemplateProcessor()
        self.assertFalse(isinstance(incomplete, ITemplateProcessor))

    def test_render_text(self) -> None:
        raw = b"Hello ${NAME}, welcome to ${PROJECT}!"
        vals = {"NAME": "Vladimir", "PROJECT": "ats_utilities"}
        rendered = self.processor.render(raw, vals)
        self.assertEqual(rendered, "Hello Vladimir, welcome to ats_utilities!")

    def test_render_binary(self) -> None:
        raw_binary = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR"
        vals = {"NAME": "Test"}
        rendered = self.processor.render(raw_binary, vals)
        self.assertEqual(rendered, raw_binary)

    def test_is_initialized(self) -> None:
        self.assertTrue(self.processor.is_initialized())
        uninit = ConcreteTemplateProcessor(initialized=False)
        self.assertFalse(uninit.is_initialized())

    def test_string_representation(self) -> None:
        self.assertEqual(str(self.processor), "ConcreteTemplateProcessor")


if __name__ == '__main__':
    unittest.main()
