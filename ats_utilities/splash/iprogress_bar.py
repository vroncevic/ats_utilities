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
    Defines interface IProgressBar with attribute(s) and method(s).
    Interface for progress bar component.
'''

from abc import ABC, abstractmethod
from typing import List

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IProgressBar(ABC):
    '''
        Defines interface IProgressBar with attribute(s) and method(s).
        Interface for progress bar component.

        It defines:

            :attributes: None
            :methods:
                | set_level - Sets level of progress (abstract).
                | plot_progress - Plots progress (abstract).
                | set_and_plot - Sets and plots progress (abstract).
    '''

    @abstractmethod
    def set_level(self, level: int) -> None:
        '''
            Sets level of progress.

            :param level: Level of progress
            :type level: <int>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement set_level method")

    @abstractmethod
    def plot_progress(self, columns: int) -> None:
        '''
            Plots progress.

            :param columns: Colums for open console session
            :type columns: <int>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement plot_progress method")

    @abstractmethod
    def set_and_plot(self, level: int, columns: int) -> None:
        '''
            Sets and plots progress.

            :param level: Level of progress
            :type level: <int>
            :param columns: colums for open console session
            :type columns: <int>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement set_and_plot method")
