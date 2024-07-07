# -*- coding: UTF-8 -*-

'''
Module
    progress_bar.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defineds class ProgressBar with attribute(s) and method(s).
    Loads a progressbar as part of splash screen.
'''

import sys
from typing import List

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ProgressBar:
    '''
        Defineds class ProgressBar with attribute(s) and method(s).
        Loads a progressbar as part of splash screen.
        Progress bar component.

        It defines:

            :attributes:
                | DEFAULT_BAR_LENGTH - Length of progressbar.
                | DEFAULT_CHAR_ON - Loaded progress element.
                | DEFAULT_CHAR_OFF - Unloaded progress element.
                | _start - Start of level.
                | _end - End of level.
                | _bar_length - Progress length.
                | _level - Progress level.
                | _plotted - Plotted progress.
                | _level_chars - Level progress chars.
            :methods:
                | __init__ - Initials ProgressBar constructor.
                | set_level - Sets level of progress.
                | plot_progress - Plots progress.
                | set_and_plot - Sets and plots progress.
                | __del__ - Dunder del method for ProgressBar.
    '''

    DEFAULT_BAR_LENGTH: int = 60
    DEFAULT_CHAR_ON: str = '█'
    DEFAULT_CHAR_OFF: str = ' '

    def __init__(self, end: int, start: int = 0) -> None:
        '''
            Initials ProgressBar constructor.

            :exceptions: None
        '''
        self._end: int = end
        self._start: int = start
        self._bar_length: int = self.DEFAULT_BAR_LENGTH
        self.set_level(self._start)
        self._plotted: bool = False
        self._level: int = 0
        self._ratio: float = 0.0
        self._level_chars: int = 0

    def set_level(self, level: int) -> None:
        '''
            Sets level.

            :param level: Level of progress
            :type level: <int>
            :exceptions: None
        '''
        self._level = level
        if level < self._start:
            self._level = self._start
        if level > self._end:
            self._level = self._end
        self._ratio = (
            float(self._level - self._start) /
            float(self._end - self._start)
        )
        self._level_chars = int(self._ratio * self._bar_length)

    def plot_progress(self, columns: int) -> None:
        '''
            Plots progress.

            :param columns: Colums for open console session
            :type columns: <int>
            :exceptions: None
        '''
        start_position: float = (columns / 2) - (columns / 10)
        number_of_tabs: int = int((start_position/8) - 3)
        sys.stdout.write(
            "\r %s %3i%% %s%s".expandtabs(4) % (
                '\011' * number_of_tabs,
                int(self._ratio * 100.0),
                self.DEFAULT_CHAR_ON * int(self._level_chars),
                self.DEFAULT_CHAR_OFF *
                int(self._bar_length - self._level_chars)
            )
        )
        sys.stdout.flush()
        self._plotted = True

    def set_and_plot(self, level: int, columns: int) -> None:
        '''
            Sets and plots progress.

            :param level: Level of progress
            :type level: <int>
            :param columns: colums for open console session
            :type columns: <int>
            :exceptions: None
        '''
        old_chars: int = self._level_chars
        self.set_level(level)
        if (not self._plotted) or (old_chars != self._level_chars):
            self.plot_progress(columns)

    def __del__(self) -> None:
        '''
            Dunder del method for ProgressBar.

            :exceptions: None
        '''
        sys.stdout.write("\n")
