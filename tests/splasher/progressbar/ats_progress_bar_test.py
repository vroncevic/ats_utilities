# -*- coding: UTF-8 -*-

'''
Module
    ats_progress_bar_test.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Creates test cases for checking ProgressBar.
Execute
    python3 -m unittest -v tests/splasher/progressbar/ats_progress_bar_test.py
'''

from __future__ import annotations

from unittest import TestCase, main

from ats_utilities.splasher.progressbar.progress_bar import ProgressBar

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '1.0.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ProgressBarTestCase(TestCase):
    '''Test cases for ProgressBar.'''

    def test_progress_bar_bounds(self) -> None:
        '''Test progress bar set_level under start and over end.'''
        pb = ProgressBar(end=90, start=10)
        
        # Test setting level below start
        pb.set_level(5)
        self.assertEqual(pb._level, 10)
        
        # Test setting level above end
        pb.set_level(100)
        self.assertEqual(pb._level, 90)

    def test_progress_bar_str_representation(self) -> None:
        '''Test progress bar string representation.'''
        pb = ProgressBar(50)
        self.assertIsInstance(str(pb), str)

    def test_progress_bar_set_and_plot(self) -> None:
        '''Test progress bar set_and_plot with same and different levels.'''
        pb = ProgressBar(end=100, start=0)
        
        pb.set_and_plot(50, 80)
        self.assertTrue(pb._plotted)
        
        pb.set_and_plot(50, 80)
        self.assertTrue(pb._plotted)
        
        pb.set_and_plot(60, 80)
        self.assertTrue(pb._plotted)



if __name__ == '__main__':
    main()
