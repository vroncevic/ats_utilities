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
    Defineds class ProgressBar with attribute(s) and method(s).
    Implements a progressbar as part of splash screen.
'''

import sys
from typing import List
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.splasher.iprogress_bar import IProgressBar

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ProgressBar(IProgressBar):
    '''
        Defineds class ProgressBar with attribute(s) and method(s).
        Implements a progressbar as part of splash screen.

        It defines:

            :attributes:
                | DEFAULT_BAR_LENGTH - Length of progressbar.
                | DEFAULT_CHAR_ON - Loaded progress element.
                | DEFAULT_CHAR_OFF - Unloaded progress element.
                | __start - Start of level.
                | __end - End of level.
                | __bar_length - Progress length.
                | __level - Progress level.
                | __plotted - Plotted progress.
                | __level_chars - Level progress chars.
            :methods:
                | __init__ - Initials ProgressBar constructor.
                | set_level - Sets level for progress bar.
                | plot_progress - Plots progress bar.
                | set_and_plot - Sets and plots progress bar.
                | __del__ - Dunder del method for progress bar.
                | __str__ - Returns the string representation of ProgressBar.
    '''

    DEFAULT_BAR_LENGTH: int = 60
    DEFAULT_CHAR_ON: str = '█'
    DEFAULT_CHAR_OFF: str = ' '

    def __init__(self, end: int, start: int = 0) -> None:
        '''
            Initials ProgressBar constructor.

            :exceptions: None
        '''
        self.__end: int = end
        self.__start: int = start
        self.__bar_length: int = self.DEFAULT_BAR_LENGTH
        self.set_level(self.__start)
        self.__plotted: bool = False
        self.__level: int = 0
        self._ratio: float = 0.0
        self.__level_chars: int = 0

    def set_level(self, level: int) -> None:
        '''
            Sets level for progress bar.

            :param level: Level of progress
            :type level: <int>
            :exceptions: None
        '''
        self.__level = level
        if level < self.__start:
            self.__level = self.__start
        if level > self.__end:
            self.__level = self.__end
        self._ratio = (
            float(self.__level - self.__start) /
            float(self.__end - self.__start)
        )
        self.__level_chars = int(self._ratio * self.__bar_length)

    def plot_progress(self, columns: int) -> None:
        '''
            Plots progress bar.

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
                self.DEFAULT_CHAR_ON * int(self.__level_chars),
                self.DEFAULT_CHAR_OFF *
                int(self.__bar_length - self.__level_chars)
            )
        )
        sys.stdout.flush()
        self.__plotted = True

    def set_and_plot(self, level: int, columns: int) -> None:
        '''
            Sets and plots progress bar.

            :param level: Level of progress
            :type level: <int>
            :param columns: colums for open console session
            :type columns: <int>
            :exceptions: None
        '''
        old_chars: int = self.__level_chars
        self.set_level(level)
        if (not self.__plotted) or (old_chars != self.__level_chars):
            self.plot_progress(columns)

    def __del__(self) -> None:
        '''
            Dunder del method for ProgressBar.

            :exceptions: None
        '''
        sys.stdout.write("\n")

    def __str__(self) -> str:
        '''
            Returns the string representation of ProgressBar.

            :return: The ProgressBar as string representation
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        return format_instance_to_string(self)
