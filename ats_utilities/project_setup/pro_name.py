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

from __future__ import annotations

from typing import override

from ats_utilities.project_setup.ipro_name import IProName
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


class ProName(IProName):
    '''
        Defines class ProName with attribute(s) and method(s).
        Defines project name container.
        Mechanism for project configuration.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger for logging (default Logger).
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
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _pro_name: str | None

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes ProName constructor.

            :param context_bundle: Contex bundle for project name.
            :type context_bundle: <ContextBundle>
            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        inject_context_bundle(self, context_bundle)
        self._pro_name = None

    @property
    @vreport('getting pro name {pro_name}')
    @override
    def pro_name(self) -> str:
        '''
            Property method for getting project name in string format.

            :return: Formatted project name in string format.
            :rtype: <str>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._pro_name

    @pro_name.setter
    @vcheck([('str:name', None)])
    @vreport('getting pro name {pro_name}')
    @override
    def pro_name(self, name: str) -> None:
        '''
            Property method for setting project name.

            :param name: Project name in string format.
            :type name: <str>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._pro_name = name

    @vreport('checking pro name {pro_name}')
    @override
    def not_none(self) -> bool:
        '''
            Checks project name is not None.

            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._pro_name is not None

    @override
    def __str__(self) -> str:
        '''
            Returns the ATS project name as string representation.

            :return: The ATS project name as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
