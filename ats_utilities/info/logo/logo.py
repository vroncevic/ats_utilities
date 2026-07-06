# -*- coding: UTF-8 -*-

'''
Module
    logo.py
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
    Defines class Logo with attribute(s) and method(s).
    Creates an API for the ATS logo path in one property object.
'''

from __future__ import annotations

from typing import override

from ats_utilities.info.logo.ilogo_path import ILogoPath
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import to_str
from ats_utilities.checker.proxy_validator import vcheck
from ats_utilities.reporter.proxy_reporter import vreport

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Logo(ILogoPath):
    '''
        Defines class Logo with attribute(s) and method(s).
        Creates an API for the ATS logo path in one property object.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _logo_path - The ATS logo path (default None).
            :methods:
                | __init__ - Initializes Logo constructor.
                | logo_path - Property methods for set/get logo_path.
                | not_none - Checks is ATS logo path not None.
                | __str__ - Returns the ATS logo path as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool
    _logo_path: str | None

    def __init__(self, context_bundle: ContextBundle | None = None) -> None:
        '''
            Initializes Logo constructor.

            :param context_bundle: Context bundle for logo_path | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        factory_context_bundle(self, context_bundle)
        self._logo_path = None

    @property
    @vreport('get logo_path {logo_path}')
    @override
    def logo_path(self) -> str:
        '''
            Property method for getting ATS logo path.

            :return: The ATS logo path in string format.
            :rtype: <str>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._logo_path

    @logo_path.setter
    @vcheck([('str:logo_path', None)])
    @vreport('set logo_path {logo_path}')
    @override
    def logo_path(self, logo_path: str) -> None:
        '''
            Property method for setting ATS logo path.

            :param logo_path: The ATS logo path in string format.
            :type logo_path: <str>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._logo_path = logo_path

    @vreport('check logo_path {logo_path}')
    @override
    def not_none(self) -> bool:
        '''
            Checks is ATS logo path not None.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._logo_path is not None

    @override
    def __str__(self) -> str:
        '''
            Returns the ATS logo path as string representation.

            :return: The ATS logo path as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
