# -*- coding: UTF-8 -*-

'''
Module
    progress_bar_test.py
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
    Unit tests for ProgressBar class.
'''

from __future__ import annotations

import unittest
from unittest.mock import patch, MagicMock

from ats_utilities.splasher.progressbar.progress_bar import ProgressBar

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ProgressBarTest(unittest.TestCase):
    '''
        Defines class ProgressBarTest with attribute(s) and method(s).
        Tests ProgressBar rendering and logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init - Tests initialization.
                | test_set_level_clamping - Tests level setting clamping logic.
                | test_plot_progress - Tests progressbar plotting to stdout.
                | test_set_and_plot - Tests plotting only on changes.
                | test_del - Tests dunder del method writing newline.
                | test_str - Tests __str__ method.
    '''

    def test_init(self) -> None:
        pb = ProgressBar(end=100, start=10)
        self.assertEqual(pb._end, 100)
        self.assertEqual(pb._start, 10)
        self.assertEqual(pb._bar_length, ProgressBar.DEFAULT_BAR_LENGTH)

    def test_set_level_clamping(self) -> None:
        pb = ProgressBar(end=100, start=10)

        # Under start
        pb.set_level(5)
        self.assertEqual(pb._level, 10)
        self.assertEqual(pb._ratio, 0.0)
        self.assertEqual(pb._level_chars, 0)

        # Over end
        pb.set_level(150)
        self.assertEqual(pb._level, 100)
        self.assertEqual(pb._ratio, 1.0)
        self.assertEqual(pb._level_chars, ProgressBar.DEFAULT_BAR_LENGTH)

        # Normal value
        pb.set_level(55)
        self.assertEqual(pb._level, 55)
        self.assertEqual(pb._ratio, 0.5)
        self.assertEqual(pb._level_chars, int(ProgressBar.DEFAULT_BAR_LENGTH * 0.5))

    @patch("sys.stdout.write")
    @patch("sys.stdout.flush")
    def test_plot_progress(self, mock_flush: MagicMock, mock_write: MagicMock) -> None:
        pb = ProgressBar(end=100, start=0)
        pb.set_level(50)
        pb.plot_progress(columns=80)

        mock_write.assert_called_once()
        mock_flush.assert_called_once()
        self.assertTrue(pb._plotted)

        # Verify bar elements inside printed string
        printed_str = mock_write.call_args[0][0]
        self.assertIn("50%", printed_str)
        self.assertIn(ProgressBar.DEFAULT_CHAR_ON, printed_str)

    @patch("sys.stdout.write")
    @patch("sys.stdout.flush")
    def test_set_and_plot(self, mock_flush: MagicMock, mock_write: MagicMock) -> None:
        pb = ProgressBar(end=100, start=0)
        pb.set_and_plot(50, 80)
        self.assertEqual(mock_write.call_count, 1)

        # Plotting the same level again should skip rewrite
        pb.set_and_plot(50, 80)
        self.assertEqual(mock_write.call_count, 1)

        # Plotting a different level should trigger rewrite
        pb.set_and_plot(70, 80)
        self.assertEqual(mock_write.call_count, 2)

    @patch("sys.stdout.write")
    def test_del(self, mock_write: MagicMock) -> None:
        pb = ProgressBar(end=100, start=0)
        del pb
        mock_write.assert_called_once_with('\n')

    def test_str(self) -> None:
        pb = ProgressBar(end=100, start=0)
        self.assertIn("ProgressBar", str(pb))


if __name__ == "__main__":
    unittest.main()
