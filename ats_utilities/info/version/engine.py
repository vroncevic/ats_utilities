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
    Defines class Version with attribute(s) and method(s).
    Creates an API for the version in one property object.
'''

from __future__ import annotations

from typing import override

from ats_utilities.info.version.iversion import IVersion
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


class Version(IVersion):
    '''
        Defines class Version with attribute(s) and method(s).
        Creates an API for the version in one property object.
        Note: Version is only prepared when it is set by user (not None).

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger (default Logger).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _version - The version for App/Tool/Script (default None).
            :methods:
                | __init__ - Initializes Version constructor.
                | version - Property methods for set/get version.
                | not_none - Checks is version not None.
                | __str__ - Returns the version as string representation.
    '''

    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _version: str | None

    def __init__(self, context_bundle: ContextBundle | None = None) -> None:
        '''
            Initializes Version constructor.

            :param context_bundle: Context bundle for version | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        factory_context_bundle(self, context_bundle)
        self._version = None

    @property
    @vreport('getting version {version}')
    @override
    def version(self) -> str | None:
        '''
            Property method for getting version.
            Note: Version is only prepared when it is set by user (not None).

            :return: The version in string format | None.
            :rtype: <str | None>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._version

    @version.setter
    @vcheck([('str:version', None)])
    @vreport('setting version {version}')
    @override
    def version(self, version: str) -> None:
        '''
            Property method for setting version.
            Note: Version is only prepared when it is set by user (not None).

            :param version: The version in string format.
            :type version: <str>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._version = version

    @vreport('checking version {version}')
    @override
    def not_none(self) -> bool:
        '''
            Checks is version not None.
            Note: Version is only prepared when it is set by user (not None).

            :return: True (not None) | False (None).
            :rtype: <bool>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._version is not None

    @override
    def __str__(self) -> str:
        '''
            Returns the Version as string representation.

            :return: The Version as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
