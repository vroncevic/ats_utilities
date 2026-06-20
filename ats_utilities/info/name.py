# -*- coding: UTF-8 -*-

'''
Module
    name.py
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
    Defines class Name with attribute(s) and method(s).
    Creates an API for the ATS name in one property object.
'''

from typing import List, Optional
from ats_utilities.info.iname import IName
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


class Name(IName):
    '''
        Defines class Name with attribute(s) and method(s).
        Creates an API for the ATS name in one property object.

        It defines:

            :attributes:
                | __checker - Factoriezed parameters checker (default Checker).
                | __reporter - Factoriezed reporter for messaging (default Reporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __name - The ATS name (default None).
            :methods:
                | __init__ - Initializes Name constructor.
                | name - Property methods for set/get name.
                | not_none - Checks is ATS name not None.
                | __str__ - Returns the ATS name as string representation.
    '''

    def __init__(self, context_bundle: Optional[ContextBundle] = None) -> None:
        '''
            Initializes Name constructor.

            :param context_bundle: Context bundle for name | None.
            :type context_bundle: <Optional[ContextBundle]>
            :exceptions: None.
        '''
        factory_context_bundle(self, context_bundle)
        self.__name: Optional[str] = None

    @property
    @vreporter('get name {name}')
    def name(self) -> Optional[str]:
        '''
            Property method for getting ATS name.

            :return: The ATS name in string format | None.
            :rtype: <Optional[str]>
            :exceptions: RuntimeError, AttributeError.
        '''
        return self.__name

    @name.setter
    @validator([('Optional[str]:name', None)])
    @vreporter('set name {name}')
    def name(self, name: Optional[str]) -> None:
        '''
            Property method for setting ATS name.

            :param name: The ATS name in string format | None.
            :type name: <Optional[str]>
            :exceptions:
                | ATSTypeError, ATSValueError, RuntimeError, AttributeError.
                | RuntimeError, AttributeError.
        '''
        self.__name = name

    @vreporter('check name {name}')
    def not_none(self) -> bool:
        '''
            Checks is ATS name not None.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError.
        '''
        return self.__name is not None

    def __str__(self) -> str:
        '''
            Returns the ATS name as string representation.

            :return: The ATS name as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
