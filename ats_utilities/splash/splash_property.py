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
    Creates an API for checking splash property.
'''

from typing import Any, Dict, List, Optional
from ats_utilities.splash.isplash_property import ISplashProperty
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
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class SplashProperty(ISplashProperty):
    '''
        Defines class SplashProperty with attribute(s) and method(s).
        Creates an API for checking splash property.
        Splash screen property API.

        It defines:

            :attributes:
                | _EXPECTED_PROP_KEYS - Expected property names.
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
                | __splash_property - Splash property in dict format (default None).
            :methods:
                | __init__ - Initials SplashProperty constructor.
                | splash_property - Property method for get/set splash property.  
                | validation - Validates splash property.
                | _reporter - Property method for getting the internal reporter instance.
                | __str__ - Returns the string representation of splash property.
    '''

    _EXPECTED_PROP_KEYS: List[str] = [
        'ats_organization',
        'ats_repository',
        'ats_name',
        'ats_logo_path',
        'ats_use_github_infrastructure'
    ]

    def __init__(self, splash_bundle: Optional[ContextBundle] = None) -> None:
        '''
            Initials SplashProperty constructor.

            :param splash_bundle: Bundle with checker, reporter and verbose | None
            :type splash_bundle: <Optional[ContextBundle]>
            :exceptions: None
        '''
        factory_context_bundle(self, splash_bundle)
        self.__splash_property:  Optional[Dict[Any, Any]] = None

    @property
    @vreporter('get splash property {splash_property}')
    def splash_property(self) -> Optional[Dict[Any, Any]]:
        '''
            Property method for getting splash property.

            :return: Formatted splash property in dict format | None
            :rtype: <Optional[str]>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__splash_property

    @splash_property.setter
    @validator([('dict:splash_property_setup', None)])
    @vreporter('set splash property {splash_property}')
    def splash_property(self, splash_property_setup: Optional[Dict[Any, Any]]) -> None:
        '''
            Property method for setting project splash property.

            :param splash_property_setup: Project splash property in dict format | None
            :type splash_property_setup: <Optional[Dict[Any, Any]]>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        self.__splash_property = splash_property_setup

    @vreporter('validation or splash property {splash_property}')
    def validates(self) -> bool:
        '''
            Validates splash property.

            :return: True (splash property ok) else False (splash property not ok)
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        if not self.__splash_property:
            self._reporter.error(['missing splash property'])
            return False

        for key in self._EXPECTED_PROP_KEYS:
            if key not in self.__splash_property.keys():
                self._reporter.error([f'missing property {key}'])
                return False

        return True

    @property
    def _reporter(self) -> IReporter:
        '''
            Property method for getting the internal reporter instance.

            :return: The reporter instance in IReporter format
            :rtype: <IReporter>
            :exceptions: None
        '''
        return get_private_attr(self, 'reporter')

    def __str__(self) -> str:
        '''
            Returns the string representation of splash property.

            :return: The splash property as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
