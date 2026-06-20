# -*- coding: UTF-8 -*-

'''
Module
    build_date.py
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
    Defines class BuildDate with attribute(s) and method(s).
    Creates an API for the ATS build date in one property object.
'''

from typing import List, Optional
from ats_utilities.info.ibuild_date import IBuildDate
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


class BuildDate(IBuildDate):
    '''
        Defines class BuildDate with attribute(s) and method(s).
        Creates an API for the ATS build date in one property object.

        It defines:

            :attributes:
                | __checker - Factoriezed parameters checker (default Checker).
                | __reporter - Factoriezed reporter for messaging (default Reporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __build_date - The ATS build date (default None).
            :methods:
                | __init__ - Initializes BuildDate constructor.
                | build_date - Property methods for set/get build date.
                | not_none - Checks is ATS build date not None.
                | __str__ - Returns the ATS build date as string representation.
    '''

    def __init__(self, context_bundle: Optional[ContextBundle] = None) -> None:
        '''
            Initializes BuildDate constructor.

            :param context_bundle: Context bundle for build date | None.
            :type context_bundle: <Optional[ContextBundle]>
            :exceptions: None.
        '''
        factory_context_bundle(self, context_bundle)
        self.__build_date: Optional[str] = None

    @property
    @vreporter('get build_date {build_date}')
    def build_date(self) -> Optional[str]:
        '''
            Property method for getting ATS build date.

            :return: The ATS build date in string format | None.
            :rtype: <Optional[str]>
            :exceptions: RuntimeError, AttributeError.
        '''
        return self.__build_date

    @build_date.setter
    @validator([('Optional[str]:build_date', None)])
    @vreporter('set build_date {build_date}')
    def build_date(self, build_date: Optional[str]) -> None:
        '''
            Property method for setting ATS build date.

            :param build_date: The ATS build date in string format | None.
            :type build_date: <Optional[str]>
            :exceptions:
                | ATSTypeError, ATSValueError, RuntimeError, AttributeError.
                | RuntimeError, AttributeError.
        '''
        self.__build_date = build_date

    @vreporter('check build_date {build_date}')
    def not_none(self) -> bool:
        '''
            Checks is ATS build date not None.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError.
        '''
        return self.__build_date is not None

    def __str__(self) -> str:
        '''
            Returns the ATS build date as string representation.

            :return: The ATS build date as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
