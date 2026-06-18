# -*- coding: UTF-8 -*-

'''
Module
    licence.py
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
    Defines class ATSLicence with attribute(s) and method(s).
    Creates an API for the ATS licence in one property object.
'''

from typing import List, Optional
from ats_utilities.info.ilicence import ILicence
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.proxy_reporter import vreporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSLicence(ILicence):
    '''
        Defines class ATSLicence with attribute(s) and method(s).
        Creates an API for the ATS licence in one property object.

        It defines:

            :attributes:
                | __checker - Factoriezed parameters checker (default ATSChecker).
                | __reporter - Factoriezed reporter for messaging (default ATSReporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __licence - The ATS licence (default None).
            :methods:
                | __init__ - Initials ATSLicence constructor.
                | licence - Property methods for set/get operations.
                | not_none - Checks is ATS licence is not None.
                | __str__ - Returns the string representation of ATS licence.
    '''

    def __init__(self, info_bundle: Optional[ContextBundle] = None) -> None:
        '''
            Initials ATSLicence constructor.

            :param info_bundle: Bundle with checker, reporter and verbose | None
            :type info_bundle: <Optional[ContextBundle]>
            :exceptions: None
        '''
        factory_context_bundle(self, info_bundle)
        self.__licence: Optional[str] = None

    @property
    @vreporter('get licence {licence}')
    def licence(self) -> Optional[str]:
        '''
            Property method for getting ATS licence.

            :return: The ATS licence in string format | None
            :rtype: <Optional[str]>
            :exceptions: RuntimeError, AttributeError
        '''
        return self.__licence

    @licence.setter
    @validator([('Optional[str]:licence', None)])
    @vreporter('set licence {licence}')
    def licence(self, licence: Optional[str]) -> None:
        '''
            Property method for setting ATS licence.

            :param licence: The ATS licence in string format | None
            :type licence: <Optional[str]>
            :exceptions:
                | ATSTypeError, ATSValueError, RuntimeError, AttributeError
                | RuntimeError, AttributeError
        '''
        self.__licence = licence

    @vreporter('check licence {licence}')
    def not_none(self) -> bool:
        '''
            Checks is ATS licence not None.

            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError
        '''
        return self.__licence is not None

    def __str__(self) -> str:
        '''
            Returns the string representation of ATS licence.

            :return: The ATS licence instance as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
