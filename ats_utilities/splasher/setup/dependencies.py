# -*- coding: UTF-8 -*-

'''
Module
    dependencies.py
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
    Splash dependencies and options for splash bundle creation.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypedDict

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.splasher.property.isplash_property import ISplashProperty
from ats_utilities.splasher.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.splasher.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.progressbar.iprogress_bar import IProgressBar

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class SplashDependencies(TypedDict):
    '''
        Splash dependencies for splash bundle creation.

        It defines:

            :attributes:
                | prop: Splash screen properties in dict format.
                | splash_property: Splash screen property instance.
                | property_validated: Property validated flag.
                | terminal_property: Terminal properties instance.
                | ext: Generic external infrastructure instance.
                | pb: Progress bar component instance.
                | context_bundle: Context bundle instance.
    '''
    prop: Mapping[str, Any]
    splash_property: ISplashProperty
    property_validated: bool
    terminal_property: ITerminalProperties
    ext: IExtInfrastructure
    pb: IProgressBar
    context_bundle: ContextBundle


class SplashOptions(TypedDict):
    '''
        Splash options for splash bundle creation.

        It defines:

            :attributes:
                | prop: Splash screen properties in dict format.
                | context_bundle: Context bundle instance.
    '''
    prop: Mapping[str, Any]
    context_bundle: ContextBundle
