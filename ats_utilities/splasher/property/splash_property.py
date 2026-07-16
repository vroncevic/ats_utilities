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

from __future__ import annotations

from typing import Any, override
from collections.abc import Mapping

from ats_utilities.splasher.property.isplash_property import ISplashProperty
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.context.context_bundle_inject import inject_context_bundle
from ats_utilities.utils.reflection import has_attrs, to_str
from ats_utilities.checker.proxy_validator import vcheck
from ats_utilities.reporter.proxy_reporter import vreport
from ats_utilities.utils.dicts import require_keys, has_required_keys

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class SplashProperty(ISplashProperty):
    '''
        Defines class SplashProperty with attribute(s) and method(s).
        Creates an API for checking splash screen property.
        Note: Splash screen property comes from info configuration file as read only data.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger (default Logger).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _splash_keys - Splash keys for App/Tool/Script splash screen (default None).
            :methods:
                | __init__ - Initials SplashProperty constructor.
                | splash_keys - Property method for get/set splash keys.  
                | validates - Validates splash keys.
                | __str__ - Returns the string representation of SplashProperty.
    '''

    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _splash_keys: SplashKeys | None

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initials SplashProperty constructor.

            :param context_bundle: Context bundle for splash screen property | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        inject_context_bundle(self, context_bundle)
        self._splash_keys = None

    @property
    @vreport('getting splash property {splash_keys}')
    @override
    def splash_keys(self) -> Mapping[str, Any]:
        '''
            Property method for getting splash screen property.
            Note: Splash screen property comes from info configuration file as read only data.

            :return: Formatted splash screen property in Mapping format (read only data).
            :rtype: <Mapping[str, Any]>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._splash_keys.to_dict() if self._splash_keys is not None else {}

    @splash_keys.setter
    @vcheck([('Mapping:setup', None)])
    @vreport('setting splash property {splash_keys}')
    @override
    def splash_keys(self, setup: Mapping[str, Any]) -> None:
        '''
            Property method for setting project splash screen property.
            Note: Splash screen property comes from info configuration file as read only data.

            :param setup: Project splash property in Mapping format (read only data).
            :type setup: <Mapping[str, Any]>
            :exceptions:
                | ATSTypeError: splash property setup is not a Mapping.
                | ATSValueError: splash property setup is missing required keys.
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        is_enabled = bool(setup.get('enabled', True))

        if is_enabled:
            require_keys(setup, frozenset(SplashKeys.get_all_keys()))

        self._splash_keys = SplashKeys.from_dict(setup)

    @vreport('validation or splash property {splash_keys}')
    @has_attrs('_splash_keys')
    @override
    def validates(self) -> bool:
        '''
            Validates splash screen property.
            Note: Splash screen property comes from info configuration file as read only data.

            :return: True (success) else False (fail).
            :rtype: <bool>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_splash_keys'.
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        if not self._splash_keys.enabled:
            return True

        return has_required_keys(self.splash_keys, frozenset(SplashKeys.get_all_keys()))

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of SplashProperty.

            :return: The SplashProperty as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
