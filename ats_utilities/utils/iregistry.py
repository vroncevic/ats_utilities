# -*- coding: UTF-8 -*-

'''
Module
    iregistry.py
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
    Abstract interface for all component factories and registries.
    Encapsulates standard orchestration behavior across dynamic bundles.
'''

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IRegistry[T](ABC):
    '''
        Abstract interface for all component factories and registries.
        Encapsulates standard orchestration behavior across dynamic bundles.
    '''

    @classmethod
    @abstractmethod
    def create_bundle(cls, **kwargs: Any) -> T:
        '''
            Abstract factory method to orchestrate and build a component bundle.

            :param kwargs: Additional registry-specific orchestration parameters.
            :return: A fully constructed and validated bundle instance.
            :rtype: <T>
        '''
        pass
