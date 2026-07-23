# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating checker bundle instance.
'''

from typing import override

from ats_utilities.utils.ifactory import IFactory
from ats_utilities.checker.setup.bundle import CheckerBundle
from ats_utilities.checker.setup.registry import CheckerRegistry
from ats_utilities.checker.format.format_validator import FormatValidator
from ats_utilities.checker.type.type_validator import TypeValidator
from ats_utilities.checker.context.context_provider import ContextProvider
from ats_utilities.checker.reporter.check_reporter import CheckReporter

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class CheckerFactory(IFactory[CheckerBundle, None]):
    '''
        Factory for creating checker bundle instance.

        It defines:

            :methods:
                | create_default_bundle - Creates a default checker bundle with pre-configured options.
    '''

    @classmethod
    @override
    def create_default_bundle(cls, options: None = None) -> CheckerBundle:
        '''
            Creates a default checker bundle with pre-configured options.

            :param options: Creation options/parameters for the bundle (default None).
            :type options: None
            :return: Default checker bundle instance.
            :rtype: CheckerBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Context provider must be provided.
                | ATSValueError: Check reporter must be provided.
                | ATSValueError: Format validator must be provided.
                | ATSValueError: Type validator must be provided.
                | ATSTypeError: Bundle must be an instance of CheckerBundle.
                | ATSTypeError: Context provider must be an instance of IContextProvider.
                | ATSTypeError: Check reporter must be an instance of ICheckReporter.
                | ATSTypeError: Format validator must be an instance of IFormatValidator.
                | ATSTypeError: Type validator must be an instance of ITypeValidator.
        '''
        format_validator: FormatValidator = FormatValidator()
        type_validator: TypeValidator = TypeValidator()
        context_provider: ContextProvider = ContextProvider()
        check_reporter: CheckReporter = CheckReporter()

        bundle: CheckerBundle = CheckerRegistry.create_bundle({
            'format_validator': format_validator,
            'type_validator': type_validator,
            'context_provider': context_provider,
            'check_reporter': check_reporter
        })

        return bundle
