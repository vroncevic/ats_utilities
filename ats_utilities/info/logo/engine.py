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
    Defines class Logo with attribute(s) and method(s).
    Creates an API for the logo path in one property object.
'''

from __future__ import annotations

from typing import override

from ats_utilities.info.logo.ilogo import ILogo
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.context.context_bundle_inject import inject_context_bundle
from ats_utilities.utils.reflection import to_str
from ats_utilities.checker.proxy_validator import vcheck
from ats_utilities.reporter.proxy_reporter import vreport

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Logo(ILogo):
    '''
        Defines class Logo with attribute(s) and method(s).
        Creates an API for the logo path in one property object.
        Note: Logo path is only prepared when it is set by user (not None).

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger for logging (default Logger).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _logo - The logo path for App/Tool/Script (default None).
            :methods:
                | __init__ - Initializes Logo constructor.
                | logo - Property methods for set/get logo.
                | not_none - Checks is logo path not None.
                | __str__ - Returns the Logo as string representation.
    '''

    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _logo: str | None

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes Logo constructor.

            :param context_bundle: Context bundle for logo.
            :type context_bundle: <ContextBundle>
            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        inject_context_bundle(self, context_bundle)
        self._logo = None

    @property
    @vreport('getting logo {logo}')
    @override
    def logo(self) -> str | None:
        '''
            Property method for getting logo path.
            Note: Logo path is only prepared when it is set by user (not None).

            :return: The logo path in string format | None.
            :rtype: <str | None>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._logo

    @logo.setter
    @vcheck([('str:logo', None)])
    @vreport('setting logo {logo}')
    @override
    def logo(self, logo: str) -> None:
        '''
            Property method for setting logo path.
            Note: Logo path is only prepared when it is set by user (not None).

            :param logo: The logo path in string format.
            :type logo: <str>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._logo = logo

    @vreport('checking logo {logo}')
    @override
    def not_none(self) -> bool:
        '''
            Checks is logo path not None.
            Note: Logo path is only prepared when it is set by user (not None).

            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._logo is not None

    @override
    def __str__(self) -> str:
        '''
            Returns the Logo as string representation.

            :return: The Logo as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
