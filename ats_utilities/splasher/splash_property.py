# -*- coding: UTF-8 -*-

'''
Module
    splash_property.py
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
    Defines class SplashProperty with attribute(s) and method(s).
    Creates an API for checking splash screen property.
'''

from typing import Any, Dict, List, Optional
from ats_utilities.splasher.isplash_property import ISplashProperty
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import get_private_attr, format_instance_to_string
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


class SplashProperty(ISplashProperty):
    '''
        Defines class SplashProperty with attribute(s) and method(s).
        Creates an API for checking splash screen property.

        It defines:

            :attributes:
                | _EXPECTED_PROP_KEYS - Expected property names.
                | __checker - Factoriezed parameters checker (default Checker).
                | __reporter - Factoriezed reporter for messaging (default Reporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __splash_property - Splash screen property in dict format (default None).
            :methods:
                | __init__ - Initials SplashProperty constructor.
                | splash_property - Property method for get/set splash property.  
                | validates - Validates splash screen property.
                | _reporter - Property method for getting the internal reporter instance.
                | __str__ - Returns the string representation of SplashProperty.
    '''

    _EXPECTED_PROP_KEYS: List[str] = [
        SplashKeys.ATS_ORGANIZATION,
        SplashKeys.ATS_REPOSITORY,
        SplashKeys.ATS_NAME,
        SplashKeys.ATS_LOGO_PATH,
        SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE
    ]

    def __init__(self, context_bundle: Optional[ContextBundle] = None) -> None:
        '''
            Initials SplashProperty constructor.

            :param context_bundle: Context bundle for splash screen property | None
            :type context_bundle: <Optional[ContextBundle]>
            :exceptions: None
        '''
        factory_context_bundle(self, context_bundle)
        self.__splash_property:  Optional[Dict[Any, Any]] = None

    @property
    @vreporter('get splash property {splash_property}')
    def splash_property(self) -> Optional[Dict[Any, Any]]:
        '''
            Property method for getting splash screen property.

            :return: Formatted splash screen property in dict format | None.
            :rtype: <Optional[Dict[Any, Any]]>
            :exceptions: RuntimeError, AttributeError
        '''
        return self.__splash_property

    @splash_property.setter
    @validator([('dict:splash_property_setup', None)])
    @vreporter('set splash property {splash_property}')
    def splash_property(self, splash_property_setup: Optional[Dict[Any, Any]]) -> None:
        '''
            Property method for setting project splash screen property.

            :param splash_property_setup: Project splash property in dict format | None.
            :type splash_property_setup: <Optional[Dict[Any, Any]]>
            :exceptions: ATSTypeError, ATSValueError, RuntimeError, AttributeError
        '''
        self.__splash_property = splash_property_setup

    @vreporter('validation or splash property {splash_property}')
    def validates(self) -> bool:
        '''
            Validates splash screen property.

            :return: True (success) else False (fail).
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError
        '''
        if not self.__splash_property:
            self._reporter.error(['missing complete splash screen property'])
            return False

        for key in self._EXPECTED_PROP_KEYS:
            if key not in self.__splash_property.keys():
                self._reporter.error([f'missing splash screen property [{key}]'])
                return False

        return True

    @property
    def _reporter(self) -> IReporter:
        '''
            Property method for getting the internal reporter instance.

            :return: The reporter instance in IReporter format.
            :rtype: <IReporter>
            :exceptions: None
        '''
        return get_private_attr(self, 'reporter')

    def __str__(self) -> str:
        '''
            Returns the string representation of SplashProperty.

            :return: The SplashProperty as string representation.
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
