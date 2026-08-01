# -*- coding: UTF-8 -*-

'''
Module
    progress_bar.py
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
    Defines the ProgressBar class with attribute(s) and method(s).
    Provides a API for progressbar as part of splash screen.
'''

from __future__ import annotations

import sys

from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ProgressBar:
    '''
        Defines the ProgressBar class with attribute(s) and method(s).
        Provides a API for progressbar as part of splash screen.

        It defines:

            :attributes:
                | DEFAULT_BAR_LENGTH - The length of progressbar.
                | DEFAULT_CHAR_ON - The loaded progress element.
                | DEFAULT_CHAR_OFF - The unloaded progress element.
                | _start - The start of level.
                | _end - The end of level.
                | _bar_length - The progress length.
                | _level - The progress level.
                | _plotted - The plotted progress.
                | _level_chars - The level progress chars.
            :methods:
                | __init__ - Initializes the ProgressBar instance.
                | set_level - Sets level for progress bar.
                | plot_progress - Plots progress bar.
                | set_and_plot - Sets and plots progress bar.
                | __del__ - Dunder del method for progress bar.
                | __str__ - Returns the progress bar as a string representation.
    '''

    DEFAULT_BAR_LENGTH: int = 60
    DEFAULT_CHAR_ON: str = '█'
    DEFAULT_CHAR_OFF: str = ' '
    _end: int
    _start: int
    _bar_length: int
    _plotted: bool
    _level: int
    _ratio: float
    _level_chars: int

    def __init__(self, end: int, start: int = 0) -> None:
        '''
            Initializes the ProgressBar instance.

            :param end: The end level of progress.
            :param start: The start level of progress (default 0).
            :exceptions: None.
        '''
        self._end = end
        self._start = start
        self._bar_length = self.DEFAULT_BAR_LENGTH
        self.set_level(self._start)
        self._plotted = False
        self._level = 0
        self._ratio = 0.0
        self._level_chars = 0

    def set_level(self, level: int) -> None:
        '''
            Sets level for progress bar.

            :param level: The level of progress.
            :exceptions: None.
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
            Plots progress bar.

            :param columns: The columns for open console session.
            :exceptions: None.
        '''
        start_position: float = (columns / 2) - (columns / 10)
        number_of_tabs: int = int((start_position/8) - 3)
        sys.stdout.write(
            '\r %s %3i%% %s%s'.expandtabs(4) % (
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
            Sets and plots progress bar.

            :param level: The level of progress.
            :param columns: The columns for open console session.
            :exceptions: None.
        '''
        old_chars: int = self._level_chars
        self.set_level(level)
        if (not self._plotted) or (old_chars != self._level_chars):
            self.plot_progress(columns)

    def __del__(self) -> None:
        '''
            Dunder del method for ProgressBar.

            :exceptions: None.
        '''
        sys.stdout.write('\n')

    def __str__(self) -> str:
        '''
            Returns the progress bar as a string representation.

            :return: The Progress bar as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
