# -*- coding: utf-8 -*-

'''
Module
    context_bundle.py
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
    Defines parameter bundle dataclass for component dependency management.
    Encapsulates core runtime components for simplifcation.
'''

from dataclasses import dataclass
from typing import List, Optional
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class ContextBundle:
    '''
        Encapsulates core runtime components for simplifcation.
        Enables passing dependencies to other components.

        It defines:

            :attributes:
                | checker - Checker for parameters (default None).
                | reporter - Reporter for providing all types of messages (default None).
                | verbose - Flag for enabling verbose output (default False).
            :methods: None
    '''

    checker: Optional[IChecker] = None
    reporter: Optional[IReporter] = None
    verbose: bool = False
