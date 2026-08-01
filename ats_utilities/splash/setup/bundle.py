# -*- coding: UTF-8 -*-

'''
Module
    bundle.py
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
    Encapsulates splasher runtime components for simplification of splasher bundle creation.
'''

from __future__ import annotations

from dataclasses import dataclass

from ats_utilities.splash.property.isplash_property import ISplashProperty
from ats_utilities.splash.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.splash.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splash.progressbar.iprogress_bar import IProgressBar
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.utils.reflection import instance_to_dict

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class SplashBundle:
    '''
        Encapsulates splasher runtime components for simplification of splasher bundle creation.

        It defines:

            :attributes:
                | splash_property - The splash screen property instance.
                | terminal_property - The terminal properties instance.
                | ext - The generic external infrastructure instance.
                | pb - The progress bar component instance.
                | context_bundle - The context bundle instance.
            :methods:
                | to_dict - Converts splash bundle to a dictionary.
    '''

    splash_property: ISplashProperty
    terminal_property: ITerminalProperties
    ext: IExtInfrastructure
    pb: IProgressBar
    context_bundle: ContextBundle

    def to_dict(self) -> dict[str, object]:
        '''
            Converts splash bundle to a dictionary.

            :return: The dictionary representation of the splash bundle.
            :exceptions:
                | ATSValueError: Instance must be provided.
                | ATSValueError: Instance must be a dataclass instance.
        '''
        return instance_to_dict(self)
