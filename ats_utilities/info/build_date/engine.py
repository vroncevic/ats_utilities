# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Creates an API for the build date in one property object.
'''

from __future__ import annotations

from typing import override

from ats_utilities.info.build_date.ibuild_date import IBuildDate
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.context.context_support import ContextSupport
from ats_utilities.utils.reflection import to_str
from ats_utilities.checker.proxy_validator import mcheck
from ats_utilities.reporter.proxy_reporter import vreport

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class BuildDate(ContextSupport, IBuildDate):
    '''
        Defines class BuildDate with attribute(s) and method(s).
        Creates an API for the build date in one property object.
        Note: Build date is only prepared when it is set by user (not None).

        It defines:

            :attributes:
                | _build_date - The build date for App/Tool/Script (default None).
            :methods:
                | __init__ - Initializes BuildDate constructor.
                | build_date - Property methods for set/get build date.
                | not_none - Checks is build date not None.
                | __str__ - Returns the BuildDate as string representation.
    '''

    _build_date: str | None

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes BuildDate constructor.

            :param context_bundle: Context bundle for build date.
            :type context_bundle: <ContextBundle>
            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        ContextSupport.__init__(self, context_bundle)
        self._build_date = None

    @property
    @vreport('getting build_date {build_date}')
    @override
    def build_date(self) -> str | None:
        '''
            Property method for getting build date.
            Note: Build date is only prepared when it is set by user (not None).

            :return: The build date in string format | None.
            :rtype: <str | None>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._build_date

    @build_date.setter
    @mcheck([('str:build_date', None)])
    @vreport('setting build_date {build_date}')
    @override
    def build_date(self, build_date: str) -> None:
        '''
            Property method for setting build date.
            Note: Build date is only prepared when it is set by user (not None).

            :param build_date: The build date in string format.
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

    @vreport('checking build_date {build_date}')
    @override
    def not_none(self) -> bool:
        '''
            Checks is build date not None.
            Note: Build date is only prepared when it is set by user (not None).

            :return: <True> if successful, <False> otherwise.
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
            Returns the BuildDate as string representation.

            :return: The BuildDate as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
