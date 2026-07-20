# -*- coding: UTF-8 -*-

'''
Module
    checker_factory.py
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
    Factory for creating CheckerBundle components.
'''

from __future__ import annotations

from ats_utilities.checker.checker_bundle import CheckerBundle
from ats_utilities.checker.format.format_validator import FormatValidator
from ats_utilities.checker.type.type_validator import TypeValidator
from ats_utilities.checker.context.context_provider import ContextProvider
from ats_utilities.checker.reporter.check_reporter import CheckReporter

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class CheckerFactory:
    '''
        Factory for creating CheckerBundle components.
    '''

    @classmethod
    def create_default_checker_bundle(cls) -> CheckerBundle:
        '''
            Creates a default CheckerBundle with pre-configured components.

            :return: Default CheckerBundle instance.
            :rtype: <CheckerBundle>
            :exceptions: None.
        '''
        format_validator: FormatValidator = FormatValidator()
        type_validator: TypeValidator = TypeValidator()
        context_provider: ContextProvider = ContextProvider()
        check_reporter: CheckReporter = CheckReporter()

        return CheckerBundle(
            format_validator=format_validator,
            type_validator=type_validator,
            context_provider=context_provider,
            check_reporter=check_reporter
        )
