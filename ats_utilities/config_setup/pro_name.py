# -*- coding: UTF-8 -*-

'''
Module
    pro_name.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    ats_utilities is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    ats_utilities is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class ProName with attribute(s) and method(s).
    Defines project name container.
'''

from ats_utilities.config_setup.ipro_name import IProName
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


class ProName(IProName):
    '''
        Defines class ProName with attribute(s) and method(s).
        Defines project name container.
        Mechanism for project configuration.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _pro_name - Project name.
            :methods:
                | __init__ - Initializes ProName constructor.
                | pro_name - Property methods for set/get operations.
                | not_none - Checks project name is not None.
                | __str__ - Returns the ATS project name as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(self, context_bundle: ContextBundle | None = None) -> None:
        '''
            Initializes ProName constructor.

            :param context_bundle: Contex bundle for project name | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None..
        '''
        factory_context_bundle(self, context_bundle)
        self._pro_name: str | None = None

    @property
    @vreporter('get pro name {pro_name}')
    def pro_name(self) -> str | None:
        '''
            Property method for getting project name in string format.

            :return: Formatted project name in string format | None.
            :rtype: <str | None>
            :exceptions: ATSRuntimeError, ATSAttributeError.
        '''
        return self._pro_name

    @pro_name.setter
    @validator([('str | None:name', None)])
    @vreporter('get pro name {pro_name}')
    def pro_name(self, name: str | None) -> None:
        '''
            Property method for setting project name.

            :param name: Project name in string format | None.
            :type name: <str | None>
            :exceptions:
                | ATSTypeError, ATSValueError, RuntimeError, AttributeError.
                | RuntimeError, AttributeError.
        '''
        self._pro_name = name

    @vreporter('check pro name {pro_name}')
    def not_none(self) -> bool:
        '''
            Checks project name is not None.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: ATSRuntimeError, ATSAttributeError.
        '''
        return self._pro_name is not None

    def __str__(self) -> str:
        '''
            Returns the ATS project name as string representation.

            :return: The ATS project name as string representation.
            :rtype: <str>
            :exceptions: None..
        '''
        return format_instance_to_string(self)
