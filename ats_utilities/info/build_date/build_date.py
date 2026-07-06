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

from __future__ import annotations

from typing import override

from ats_utilities.info.build_date.ibuild_date import IBuildDate
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


class BuildDate(IBuildDate):
    '''
        Defines class BuildDate with attribute(s) and method(s).
        Creates an API for the ATS build date in one property object.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _build_date - The ATS build date (default None).
            :methods:
                | __init__ - Initializes BuildDate constructor.
                | build_date - Property methods for set/get build date.
                | not_none - Checks is ATS build date not None.
                | __str__ - Returns the ATS build date as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool
    _build_date: str | None

    def __init__(self, context_bundle: ContextBundle | None = None) -> None:
        '''
            Initializes BuildDate constructor.

            :param context_bundle: Context bundle for build date | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        factory_context_bundle(self, context_bundle)
        self._build_date = None

    @property
    @vreport('get build_date {build_date}')
    @override
    def build_date(self) -> str:
        '''
            Property method for getting ATS build date.

            :return: The ATS build date in string format.
            :rtype: <str>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._build_date

    @build_date.setter
    @vcheck([('str:build_date', None)])
    @vreport('set build_date {build_date}')
    @override
    def build_date(self, build_date: str) -> None:
        '''
            Property method for setting ATS build date.

            :param build_date: The ATS build date in string format.
            :type build_date: <str>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._build_date = build_date

    @vreport('check build_date {build_date}')
    @override
    def not_none(self) -> bool:
        '''
            Checks is ATS build date not None.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._build_date is not None

    @override
    def __str__(self) -> str:
        '''
            Returns the ATS build date as string representation.

            :return: The ATS build date as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
