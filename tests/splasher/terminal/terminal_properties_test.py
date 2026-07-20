# -*- coding: UTF-8 -*-

'''
Module
    terminal_properties_test.py
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
    Unit tests for TerminalProperties class.
'''

from __future__ import annotations

import unittest
from unittest.mock import patch, MagicMock

from ats_utilities.context.context_factory import ContextFactory
from ats_utilities.exceptions import ATSTypeError
from ats_utilities.splasher.terminal.terminal_properties import TerminalProperties

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class TerminalPropertiesTest(unittest.TestCase):
    '''
        Defines class TerminalPropertiesTest with attribute(s) and method(s).
        Tests TerminalProperties logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init - Tests initialization.
                | test_ioctl_get_window_size_valid - Tests getting window size with a mock ioctl.
                | test_ioctl_get_window_size_invalid_type - Tests type error with wrong argument.
                | test_size_standard_descriptors - Tests size querying with standard descriptors.
                | test_size_ctermid - Tests size querying using ctermid.
                | test_size_fallback - Tests fallback to default size on failure.
                | test_str - Tests __str__ method.
    '''

    def test_init(self) -> None:
        context_bundle = ContextFactory.create_default_context_bundle()
        tp = TerminalProperties(context_bundle)
        self.assertIsNone(tp._window_size)

    @patch("ats_utilities.splasher.terminal.terminal_properties.ioctl")
    @patch("ats_utilities.splasher.terminal.terminal_properties.unpack")
    def test_ioctl_get_window_size_valid(self, mock_unpack: MagicMock, mock_ioctl: MagicMock) -> None:
        mock_unpack.return_value = (40, 100, 0, 0)
        context_bundle = ContextFactory.create_default_context_bundle()
        tp = TerminalProperties(context_bundle)
        res = tp.ioctl_get_window_size(1)
        self.assertEqual(res, (40, 100, 0, 0))
        mock_ioctl.assert_called_once()

    def test_ioctl_get_window_size_invalid_type(self) -> None:
        context_bundle = ContextFactory.create_default_context_bundle()
        tp = TerminalProperties(context_bundle)
        with self.assertRaises(ATSTypeError):
            tp.ioctl_get_window_size("not an int")  # type: ignore

    @patch("ats_utilities.splasher.terminal.terminal_properties.ioctl")
    @patch("ats_utilities.splasher.terminal.terminal_properties.unpack")
    def test_size_standard_descriptors(self, mock_unpack: MagicMock, mock_ioctl: MagicMock) -> None:
        mock_unpack.return_value = (30, 90, 0, 0)
        context_bundle = ContextFactory.create_default_context_bundle()
        tp = TerminalProperties(context_bundle)
        res = tp.size()
        self.assertEqual(res, (30, 90, 0, 0))

    @patch("ats_utilities.splasher.terminal.terminal_properties.ioctl")
    @patch("ats_utilities.splasher.terminal.terminal_properties.open")
    @patch("ats_utilities.splasher.terminal.terminal_properties.close")
    @patch("ats_utilities.splasher.terminal.terminal_properties.unpack")
    def test_size_ctermid(self, mock_unpack: MagicMock, mock_close: MagicMock, mock_open: MagicMock, mock_ioctl: MagicMock) -> None:
        # Standard descriptors fail (raise OSError), but ctermid works
        mock_ioctl.side_effect = [
            OSError("fd 0 failed"), OSError("fd 1 failed"), OSError("fd 2 failed"), b"packed_data"
        ]
        mock_unpack.return_value = (35, 95, 0, 0)
        mock_open.return_value = 10

        context_bundle = ContextFactory.create_default_context_bundle()
        tp = TerminalProperties(context_bundle)
        res = tp.size()
        self.assertEqual(res, (35, 95, 0, 0))
        mock_open.assert_called_once()
        mock_close.assert_called_once_with(10)

    @patch("ats_utilities.splasher.terminal.terminal_properties.ioctl")
    @patch("ats_utilities.splasher.terminal.terminal_properties.open")
    def test_size_fallback(self, mock_open: MagicMock, mock_ioctl: MagicMock) -> None:
        # Everything fails
        mock_ioctl.side_effect = OSError("ioctl failed")
        mock_open.side_effect = OSError("open failed")

        context_bundle = ContextFactory.create_default_context_bundle()
        tp = TerminalProperties(context_bundle)
        res = tp.size()
        self.assertEqual(res, (24, 80, 0, 0))

    @patch("ats_utilities.splasher.terminal.terminal_properties.ioctl")
    @patch("ats_utilities.splasher.terminal.terminal_properties.unpack")
    def test_ioctl_for_all_descriptors_loops(self, mock_unpack: MagicMock, mock_ioctl: MagicMock) -> None:
        mock_unpack.side_effect = [None, (30, 90, 0, 0)]
        context_bundle = ContextFactory.create_default_context_bundle()
        tp = TerminalProperties(context_bundle)
        tp.ioctl_for_all_descriptors()
        self.assertEqual(tp._window_size, (30, 90, 0, 0))

    @patch("ats_utilities.splasher.terminal.terminal_properties.TerminalProperties.ioctl_for_all_descriptors")
    @patch("ats_utilities.splasher.terminal.terminal_properties.open")
    def test_size_ioctl_all_raises_oserror(self, mock_open: MagicMock, mock_ioctl_all: MagicMock) -> None:
        mock_ioctl_all.side_effect = OSError("mocked oserror")
        mock_open.side_effect = OSError("open failed")
        context_bundle = ContextFactory.create_default_context_bundle()
        tp = TerminalProperties(context_bundle)
        res = tp.size()
        self.assertEqual(res, (24, 80, 0, 0))

    @patch("ats_utilities.splasher.terminal.terminal_properties.TerminalProperties.ioctl_for_all_descriptors")
    @patch("ats_utilities.splasher.terminal.terminal_properties.open")
    def test_size_open_ctermid_raises_oserror_with_preexisting_window_size(self, mock_open: MagicMock, mock_ioctl_all: MagicMock) -> None:
        context_bundle = ContextFactory.create_default_context_bundle()
        tp = TerminalProperties(context_bundle)
        tp._window_size = (30, 90, 0, 0)
        mock_open.side_effect = OSError("open failed")
        res = tp.size()
        self.assertEqual(res, (30, 90, 0, 0))

    def test_str(self) -> None:
        context_bundle = ContextFactory.create_default_context_bundle()
        tp = TerminalProperties(context_bundle)
        self.assertIn("TerminalProperties", str(tp))


if __name__ == "__main__":
    unittest.main()
