# -*- coding: UTF-8 -*-

'''
Module
    iprogress_bar.py
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
    Defines abstract class IProgressBar with method(s).
    Interface for progress bar component.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IProgressBar(ABC):
    '''
        Defines abstract class IProgressBar with method(s).
        Interface for progress bar component.

        It defines:

            :methods:
                | set_level - Sets level of progress.
                | plot_progress - Plots progress.
                | set_and_plot - Sets and plots progress.
                | __str__ - Returns the progress bar as string representation.
    '''

    @abstractmethod
    def set_level(self, level: int) -> None:
        '''
            Sets level of progress.

            :param level: Level of progress.
            :type level: int
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def plot_progress(self, columns: int) -> None:
        '''
            Plots progress.

            :param columns: Columns for open console session.
            :type columns: int
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def set_and_plot(self, level: int, columns: int) -> None:
        '''
            Sets and plots progress.

            :param level: Level of progress.
            :type level: int
            :param columns: Columns for open console session.
            :type columns: int
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the progress bar as string representation.

            :return: The progress bar as string representation.
            :rtype: str
            :exceptions: None.
        '''
        pass
