# -*- coding: utf-8 -*-

'''
Module
    config_bundle.py
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
    Defines parameter bundle data classes for dependency group simplification.
    Encapsulates core configuration and processor utilities to minimize constructor overhead.
'''

from dataclasses import dataclass
from typing import List, Optional
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.config_io.ifile_check import IFileCheck

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class ATSConfigBundle:
    '''
        Encapsulates the core system tracking, verification, and infrastructure components.
        Acts as a Parameter Object to clean up highly repetitive logger and validator arguments.

        :param checker: Parameters checker implementation | None
        :type checker: <Optional[IChecker]>
        :param reporter: Console messaging reporter implementation | None
        :type reporter: <Optional[IReporter]>
        :param file_checker: File and path structure verification tool | None
        :type file_checker: <Optional[IFileCheck]>
        :param verbose: Global operational flag to enable/disable verbose output
        :type verbose: <bool>
    '''
    checker: Optional[IChecker] = None
    reporter: Optional[IReporter] = None
    file_checker: Optional[IFileCheck] = None
    verbose: bool = False
