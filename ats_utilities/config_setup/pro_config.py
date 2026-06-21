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

from typing import Any
from ats_utilities.config_setup.ipro_config import IProConfig
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.proxy_reporter import vreporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


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
                | _checker - Factoriezed parameters checker (default Checker).
                | _reporter - Factoriezed reporter for messaging (default Reporter).
                | _verbose - Factoriezed Enable/Disable verbose option (default False).
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
    _reporter: IReporter
    _verbose: bool

    def __init__(self, context_bundle: ContextBundle | None = None) -> None:
        '''
            Initializes ProConfig constructor.

            :param context_bundle: Context bundle for project configuration | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None..
        '''
        factory_context_bundle(self, context_bundle)
        self._config: dict[Any, Any] | None = None

    @property
    @vreporter('get config {config}')
    def config(self) -> dict[Any, Any] | None:
        '''
            Property method for getting project configuration.

            :return: Formatted project configuration in dict format | None.
            :rtype: <dict[Any, Any] | None>
            :exceptions: ATSRuntimeError, ATSAttributeError.
        '''
        return self._config

    @config.setter
    @validator([('dict | None:pro_config', None)])
    @vreporter('get config {config}')
    def config(self, pro_config: dict[Any, Any] | None) -> None:
        '''
            Property method for setting project configuration.

            :param pro_config: Project configuration in dict format | None.
            :type pro_config: <dict[Any, Any] | None>
            :exceptions:
                | ATSTypeError, ATSValueError, RuntimeError, AttributeError.
                | RuntimeError, AttributeError.
        '''
        self._config = pro_config

    @vreporter('check config {config}')
    def not_none(self) -> bool:
        '''
            Checks project configuration is not None.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: ATSRuntimeError, ATSAttributeError.
        '''
        return self._config is not None

    def __str__(self) -> str:
        '''
            Returns the ATS project configuration as string representation.

            :return: The ATS project configuration as string representation.
            :rtype: <str>
            :exceptions: None..
        '''
        return format_instance_to_string(self)
