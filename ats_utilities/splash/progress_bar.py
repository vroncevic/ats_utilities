# -*- coding: UTF-8 -*-

'''
 Module
     progress_bar.py
 Copyright
     Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class ProgressBar with attribute(s) and method(s).
     Load a progressbar as part of splashscreen.
'''

import sys

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.0.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ProgressBar:
    '''
        Defined class ProgressBar with attribute(s) and method(s).
        Load a progressbar as part of splashscreen.
        It defines:

            :attributes:
                | DEFAULT_BAR_LENGTH - length of progressbar.
                | DEFAULT_CHAR_ON - loaded progress element.
                | DEFAULT_CHAR_OFF - unloaded progress element.
                | start - start of level.
                | end - end of level.
                | _bar_length - progress length.
                | _level - progress level.
                | _plotted - plotted progress.
                | _level_chars - level progress chars.
            :methods:
                | __init__ - initial constructor.
                | set_level - set level of progress.
                | plot_progress - plot progress.
                | set_and_plot - set and plot progress.
                | __del__ - dunder method for ProgressBar.
    '''
    DEFAULT_BAR_LENGTH = 60
    DEFAULT_CHAR_ON = '█'
    DEFAULT_CHAR_OFF = ' '

    def __init__(self, end, start=0):
        '''
            Initial constructor.

            :exceptions: None
        '''
        self.end = end
        self.start = start
        self._bar_length = self.__class__.DEFAULT_BAR_LENGTH
        self.set_level(self.start)
        self._plotted = False

    def set_level(self, level):
        '''
            Set level.

            :param level: level of progress.
            :type level: <int>
            :exceptions: None
        '''
        self._level = level
        if level < self.start:
            self._level = self.start
        if level > self.end:
            self._level = self.end
        self._ratio = float(self._level - self.start) / \
            float(self.end - self.start)
        self._level_chars = int(self._ratio * self._bar_length)

    def plot_progress(self, columns):
        '''
            Plot progress.

            :param columns: colums for open console session.
            :type columns: <int>
            :exceptions: None
        '''
        start_position = (columns/2) - (columns/10)
        number_of_tabs = int((start_position/8) - 3)
        sys.stdout.write(
            "\r %s %3i%% %s%s".expandtabs(4) % (
                '\011' * number_of_tabs,
                int(self._ratio * 100.0),
                self.__class__.DEFAULT_CHAR_ON * int(self._level_chars),
                self.__class__.DEFAULT_CHAR_OFF *
                int(self._bar_length - self._level_chars)
            )
        )
        sys.stdout.flush()
        self._plotted = True

    def set_and_plot(self, level, columns):
        '''
            Set and plot progress.

            :param level: level of progress.
            :type level: <int>
            :param columns: colums for open console session.
            :type columns: <int>
            :exceptions: None
        '''
        old_chars = self._level_chars
        self.set_level(level)
        if (not self._plotted) or (old_chars != self._level_chars):
            self.plot_progress(columns)

    def __del__(self):
        '''
            Dunder method for ProgressBar.

            :exceptions: None
        '''
        sys.stdout.write("\n")
