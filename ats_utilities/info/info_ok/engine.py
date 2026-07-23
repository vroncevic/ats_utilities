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
    Defines class InfoOk with attribute(s) and method(s).
    Creates an API for the info status in one property object.
'''

from __future__ import annotations

from typing import override

from ats_utilities.info.info_ok.iinfo_ok import IInfoOk
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.utils.reflection import to_str
from ats_utilities.checker.proxy_validator import mcheck
from ats_utilities.reporter.proxy_reporter import vreport

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class InfoOk(IInfoOk):
    '''
        Defines class InfoOk with attribute(s) and method(s).
        Creates an API for the info status in one property object.
        Note: Info status is only prepared when it is set by user (not None).

        It defines:

            :attributes:
                | _info_ok - The info status App/Tool/Script is OK (default False).
            :methods:
                | __init__ - Initializes InfoOk constructor.
                | info_ok - Property methods for set/get information status.
                | not_none - Checks if info status is not None.
                | __str__ - Returns the InfoOk as string representation.
    '''

    _info_ok: bool
    _context: ContextBundle

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes InfoOk constructor.

            :param context_bundle: Context bundle for info ok status.
            :type context_bundle: ContextBundle
            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        self._context = context_bundle
        self._info_ok = False

    @property
    @vreport('getting info_ok {info_ok}')
    @override
    def info_ok(self) -> bool:
        '''
            Property method for getting information status.
            Note: Info status is only prepared when it is set by user (not None).

            :return: The information status in bool format.
            :rtype: bool
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._info_ok

    @info_ok.setter
    @mcheck([('bool:info_ok', None)])
    @vreport('setting info_ok {info_ok}')
    @override
    def info_ok(self, info_ok: bool) -> None:
        '''
            Property method for setting information status.
            Note: Info status is only prepared when it is set by user (not None).

            :param info_ok: The information status in bool format.
            :type info_ok: bool
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._info_ok = info_ok

    @vreport('checking info_ok {info_ok}')
    @override
    def not_none(self) -> bool:
        '''
            Checks if info status is not None.
            Note: Info status is only prepared when it is set by user (not None).

            :return: True if successful, otherwise False.
            :rtype: bool
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._info_ok is not None

    @override
    def __str__(self) -> str:
        '''
            Returns the InfoOk as string representation.

            :return: The InfoOk as string representation.
            :rtype: str
            :exceptions: None.
        '''
        return to_str(self)
