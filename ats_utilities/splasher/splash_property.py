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

from typing import Any, override
from ats_utilities.splasher.isplash_property import ISplashProperty
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import require_attributes, format_instance_to_string
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.proxy_reporter import vreporter
from ats_utilities.factory_dict_utils import require_keys, cherry_pick_dict, has_required_keys

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class SplashProperty(ISplashProperty):
    '''
        Defines class SplashProperty with attribute(s) and method(s).
        Creates an API for checking splash screen property.

        It defines:

            :attributes:
                | _required_keys - Required splash screen keys (default frozenset).
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _splash_property - Splash screen property in dict format (default None).
            :methods:
                | __init__ - Initials SplashProperty constructor.
                | splash_property - Property method for get/set splash property.  
                | validates - Validates splash screen property.
                | __str__ - Returns the string representation of SplashProperty.
    '''

    _required_keys: frozenset[str] = frozenset([
        SplashKeys.ATS_ORGANIZATION,
        SplashKeys.ATS_REPOSITORY,
        SplashKeys.ATS_NAME,
        SplashKeys.ATS_LOGO_PATH,
        SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE
    ])

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(self, context_bundle: ContextBundle | None = None) -> None:
        '''
            Initials SplashProperty constructor.

            :param context_bundle: Context bundle for splash screen property | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        factory_context_bundle(self, context_bundle)
        self._splash_property: dict[Any, Any] | None = None

    @property
    @vreporter('get splash property {splash_property}')
    @override
    def splash_property(self) -> dict[Any, Any] | None:
        '''
            Property method for getting splash screen property.

            :return: Formatted splash screen property in dict format | None.
            :rtype: <dict[Any, Any] | None>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @verboser decorator.
        '''
        return self._splash_property

    @splash_property.setter
    @validator([('dict:splash_property_setup', None)])
    @vreporter('set splash property {splash_property}')
    @override
    def splash_property(self, splash_property_setup: dict[Any, Any] | None) -> None:
        '''
            Property method for setting project splash screen property.

            :param splash_property_setup: Project splash property in dict format | None.
            :type splash_property_setup: <dict[Any, Any] | None>
            :exceptions:
                | ATSTypeError: splash property setup is not a dict | None.
                | ATSValueError: splash property setup is missing required keys.
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @verboser decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        require_keys(splash_property_setup, self._required_keys)
        self._splash_property = cherry_pick_dict(splash_property_setup, self._required_keys)

    @vreporter('validation or splash property {splash_property}')
    @require_attributes('_splash_property')
    @override
    def validates(self) -> bool:
        '''
            Validates splash screen property.

            :return: True (success) else False (fail).
            :rtype: <bool>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_splash_property'.
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @verboser decorator.
        '''
        return has_required_keys(self._splash_property, self._required_keys)

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of SplashProperty.

            :return: The SplashProperty as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
