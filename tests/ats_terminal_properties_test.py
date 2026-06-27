# -*- coding: UTF-8 -*-

'''
Module
    ats_terminal_properties_test.py
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
    Defines class ATSTerminalPropTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of termanl properties.
Execute
    python3 -m unittest -v ats_terminal_properties_test
'''

from unittest import TestCase, main, mock
from ats_utilities.splasher.terminal_properties import TerminalProperties
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSTerminalPropTestCase(TestCase):
    '''
        Defines class ATSTerminalPropTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of termanl properties.
        TerminalProperties unit tests.

        It defines:

            :attributes:
                | terminal - Terminal properties.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_create - Test for create.
                | test_size - Test for size.
                | test_wrong_descriptor - Test wrong descriptor.
                | test_str - Test string representation.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.terminal: TerminalProperties = TerminalProperties()

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_create(self) -> None:
        '''Test for create'''
        self.assertIsNotNone(self.terminal)

    def test_size(self) -> None:
        '''Test getting size'''
        self.assertIsNotNone(self.terminal.size())

    def test_wrong_descriptor(self) -> None:
        '''Test getting size'''
        with self.assertRaises(ATSTypeError):
            self.terminal.ioctl_get_window_size(None)  # type: ignore

    def test_str(self) -> None:
        '''Test string representation of TerminalProperties.'''
        self.assertIsInstance(str(self.terminal), str)

    @mock.patch('ats_utilities.splasher.terminal_properties.os.open')
    @mock.patch('ats_utilities.splasher.terminal_properties.os.close')
    @mock.patch('ats_utilities.splasher.terminal_properties.TerminalProperties.ioctl_get_window_size')
    @mock.patch('ats_utilities.splasher.terminal_properties.TerminalProperties.ioctl_for_all_descriptors')
    def test_size_with_controlling_terminal(self, mock_ioctl_all, mock_get_size, mock_close, mock_open) -> None:
        '''Test size() when ctermid open succeeds.'''
        mock_open.return_value = 999
        mock_get_size.return_value = (30, 100, 0, 0)
        
        terminal = TerminalProperties()
        size = terminal.size()
        
        self.assertEqual(size, (30, 100, 0, 0))
        mock_open.assert_called_once()
        mock_get_size.assert_called_once_with(999)
        mock_close.assert_called_once_with(999)

    @mock.patch('ats_utilities.splasher.terminal_properties.TerminalProperties.ioctl_for_all_descriptors')
    def test_size_ioctl_all_oserror(self, mock_ioctl_all) -> None:
        '''Test size() when ioctl_for_all_descriptors raises OSError.'''
        mock_ioctl_all.side_effect = OSError("No descriptors")
        terminal = TerminalProperties()
        size = terminal.size()
        self.assertIsNotNone(size)

    @mock.patch('ats_utilities.splasher.terminal_properties.os.open')
    @mock.patch('ats_utilities.splasher.terminal_properties.TerminalProperties.ioctl_for_all_descriptors')
    def test_size_fallback(self, mock_ioctl_all, mock_open) -> None:
        '''Test size() fallback to (24, 80, 0, 0) when all ioctls and open fail.'''
        mock_ioctl_all.side_effect = OSError("Mock error")
        mock_open.side_effect = OSError("Mock error")
        terminal = TerminalProperties()
        size = terminal.size()
        self.assertEqual(size, (24, 80, 0, 0))


if __name__ == '__main__':
    main()
