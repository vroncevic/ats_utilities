# -*- coding: UTF-8 -*-

'''
Module
    test_iterminal_properties.py
Info
    Unit tests for ITerminalProperties protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.splash.terminal.iterminal_properties import ITerminalProperties


class ConcreteTerminalProperties:
    '''Mock implementation of ITerminalProperties protocol for testing purposes.'''

    def __init__(self, default_size: tuple[int, int] = (80, 24)) -> None:
        self._default_size = default_size
        self._all_descriptors_configured = False

    def ioctl_get_window_size(self, file_descriptor: int) -> tuple[int, int]:
        if isinstance(file_descriptor, int) and file_descriptor >= 0:
            return self._default_size
        return (0, 0)

    def ioctl_for_all_descriptors(self) -> None:
        self._all_descriptors_configured = True

    def size(self) -> tuple[int, int]:
        return self._default_size

    def __str__(self) -> str:
        return "ConcreteTerminalProperties"


class IncompleteTerminalProperties:
    '''Incomplete class lacking most methods from ITerminalProperties protocol.'''

    def size(self) -> tuple[int, int]:
        return (80, 24)


class TestITerminalProperties(unittest.TestCase):
    '''Test suite for ITerminalProperties protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Setup test environment and instance before each test.'''
        self.term_props = ConcreteTerminalProperties(default_size=(120, 40))

    def test_protocol_conformance(self) -> None:
        '''Tests whether the class with all methods passes the runtime_checkable check.'''
        self.assertTrue(isinstance(self.term_props, ITerminalProperties))

    def test_protocol_non_conformance(self) -> None:
        '''Tests whether the incomplete class fails the isinstance check.'''
        incomplete = IncompleteTerminalProperties()
        self.assertFalse(isinstance(incomplete, ITerminalProperties))

    def test_ioctl_get_window_size(self) -> None:
        '''Tests the ioctl_get_window_size method with valid and invalid descriptor.'''
        self.assertEqual(self.term_props.ioctl_get_window_size(1), (120, 40))
        # Invalid descriptor
        self.assertEqual(self.term_props.ioctl_get_window_size(-1), (0, 0))

    def test_ioctl_for_all_descriptors(self) -> None:
        '''Tests the ioctl_for_all_descriptors method.'''
        self.assertFalse(self.term_props._all_descriptors_configured)
        self.term_props.ioctl_for_all_descriptors()
        self.assertTrue(self.term_props._all_descriptors_configured)

    def test_size(self) -> None:
        '''Tests the size method for getting window size.'''
        self.assertEqual(self.term_props.size(), (120, 40))

    def test_string_representation(self) -> None:
        '''Tests the __str__ method.'''
        self.assertEqual(str(self.term_props), "ConcreteTerminalProperties")


if __name__ == '__main__':
    unittest.main()
