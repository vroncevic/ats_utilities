# -*- coding: UTF-8 -*-

'''
Module
    pro_config.py
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
    Defines class ProConfig with attribute(s) and method(s).
    Defines project configuration container.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, override

from ats_utilities.config_setup.ipro_config import IProConfig
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import to_str
from ats_utilities.checker.proxy_validator import vcheck
from ats_utilities.reporter.proxy_reporter import vreport

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ProConfig(IProConfig):
    '''
        Defines class ProConfig with attribute(s) and method(s).
        Defines project configuration container.
        Mechanism for project configuration.

        It defines:

            :attributes:
                | TEMPLATES - Templates key used for processing template files.
                | MODULES - Modules key used for processing template files.
                | FORMAT - Format for template file extension.
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger for logging (default Logger).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _config - Tool configuration in dictionary format (default None).
            :methods:
                | __init__ - Initializes ProConfig constructor.
                | config - Property methods for set/get operations.
                | not_none - Checks project configuration is not None.
                | __str__ - Returns the ATS project configuration as string representation.
    '''

    TEMPLATES: str = 'templates'
    MODULES: str = 'modules'
    FORMAT: str = 'template'
    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _config: Mapping[str, Any] | None

    def __init__(self, context_bundle: ContextBundle | None = None) -> None:
        '''
            Initializes ProConfig constructor.

            :param context_bundle: Context bundle for project configuration | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        factory_context_bundle(self, context_bundle)
        self._config = None

    @property
    @vreport('getting config {config}')
    @override
    def config(self) -> Mapping[str, Any]:
        '''
            Property method for getting project configuration.

            :return: Formatted project configuration in dict format.
            :rtype: <Mapping[str, Any]>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._config

    @config.setter
    @vcheck([('Mapping | None:pro_config', None)])
    @vreport('getting config {config}')
    @override
    def config(self, pro_config: Mapping[str, Any]) -> None:
        '''
            Property method for setting project configuration.

            :param pro_config: Project configuration in Mapping format.
            :type pro_config: <Mapping[str, Any]>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._config = pro_config

    @vreport('checking config {config}')
    @override
    def not_none(self) -> bool:
        '''
            Checks project configuration is not None.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._config is not None

    @override
    def __str__(self) -> str:
        '''
            Returns the ATS project configuration as string representation.

            :return: The ATS project configuration as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
