# -*- coding: UTF-8 -*-

'''
Module
    use_github.py
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
    Defines class UseGitHub with attribute(s) and method(s).
    Creates an API for the ATS use GitHub infrastructure in one property object.
'''

from typing import List, Optional
from ats_utilities.info.iuse_github import IUseGitHub
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.proxy_reporter import vreporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class UseGitHub(IUseGitHub):
    '''
        Defines class UseGitHub with attribute(s) and method(s).
        Creates an API for the ATS use GitHub infrastructure in one property object.

        It defines:

            :attributes:
                | __checker - Factoriezed parameters checker (default Checker).
                | __reporter - Factoriezed reporter for messaging (default Reporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __use_github - The ATS use GitHub infrastructure status (default None).
            :methods:
                | __init__ - Initializes UseGitHub constructor.
                | use_github - Property methods for set/get use_github.
                | not_none - Checks is ATS use GitHub infrastructure not None.
                | __str__ - Returns the ATS use GitHub infrastructure as string representation.
    '''

    def __init__(self, context_bundle: Optional[ContextBundle] = None) -> None:
        '''
            Initializes UseGitHub constructor.

            :param context_bundle: Context bundle for use_github | None.
            :type context_bundle: <Optional[ContextBundle]>
            :exceptions: None.
        '''
        factory_context_bundle(self, context_bundle)
        self.__use_github: Optional[bool] = None

    @property
    @vreporter('get use_github {use_github}')
    def use_github(self) -> Optional[bool]:
        '''
            Property method for getting ATS use GitHub infrastructure status.

            :return: The ATS use GitHub infrastructure status | None.
            :rtype: <Optional[bool]>
            :exceptions: RuntimeError, AttributeError.
        '''
        return self.__use_github

    @use_github.setter
    @validator([('Optional[bool]:use_github', None)])
    @vreporter('set use_github {use_github}')
    def use_github(self, use_github: Optional[bool]) -> None:
         '''
             Property method for setting ATS use GitHub infrastructure status.

             :param use_github: The ATS use GitHub infrastructure status | None.
             :type use_github: <Optional[bool]>
             :exceptions:
                 | ATSTypeError, ATSValueError, RuntimeError, AttributeError.
                 | RuntimeError, AttributeError.
         '''
         self.__use_github = use_github

    @vreporter('check use_github {use_github}')
    def not_none(self) -> bool:
        '''
            Checks is ATS use GitHub infrastructure not None.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError.
        '''
        return self.__use_github is not None

    def __str__(self) -> str:
        '''
            Returns the ATS use GitHub infrastructure as string representation.

            :return: The ATS use GitHub infrastructure as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
