# -*- coding: UTF-8 -*-

'''
Module
    test_iprogress_bar.py
Info
    Unit tests for IProgressBar protocol interface using unittest.
'''

from __future__ import annotations

import unittest

from ats_utilities.splash.progressbar.iprogress_bar import IProgressBar


class ConcreteProgressBar:
    '''Mock implementation of IProgressBar protocol for testing purposes.'''

    def __init__(self) -> None:
        self._level: int = 0
        self._last_plotted_columns: int | None = None

    def set_level(self, level: int) -> None:
        self._level = max(0, min(100, level))

    def plot_progress(self, columns: int) -> None:
        self._last_plotted_columns = columns

    def set_and_plot(self, level: int, columns: int) -> None:
        self.set_level(level)
        self.plot_progress(columns)

    def __str__(self) -> str:
        return "ConcreteProgressBar"


class IncompleteProgressBar:
    '''Incomplete class lacking most methods from IProgressBar protocol.'''

    def set_level(self, level: int) -> None:
        pass


class TestIProgressBar(unittest.TestCase):
    '''Test suite for IProgressBar protocol using unittest framework.'''

    def setUp(self) -> None:
        '''Setup test environment and instance before each test.'''
        self.progress_bar = ConcreteProgressBar()

    def test_protocol_conformance(self) -> None:
        '''Tests whether the class with all methods passes the runtime_checkable check.'''
        self.assertTrue(isinstance(self.progress_bar, IProgressBar))

    def test_protocol_non_conformance(self) -> None:
        '''Tests whether the incomplete class fails the isinstance check.'''
        incomplete = IncompleteProgressBar()
        self.assertFalse(isinstance(incomplete, IProgressBar))

    def test_set_level(self) -> None:
        '''Tests set_level method.'''
        self.progress_bar.set_level(50)
        self.assertEqual(self.progress_bar._level, 50)

    def test_plot_progress(self) -> None:
        '''Tests plot_progress method for displaying progress bar.'''
        self.progress_bar.plot_progress(80)
        self.assertEqual(self.progress_bar._last_plotted_columns, 80)

    def test_set_and_plot(self) -> None:
        '''Tests combined set_and_plot method.'''
        self.progress_bar.set_and_plot(75, 120)
        self.assertEqual(self.progress_bar._level, 75)
        self.assertEqual(self.progress_bar._last_plotted_columns, 120)

    def test_string_representation(self) -> None:
        '''Tests __str__ method.'''
        self.assertEqual(str(self.progress_bar), "ConcreteProgressBar")


if __name__ == '__main__':
    unittest.main()
