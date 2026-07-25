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

from ats_utilities.utils.setup.ifactory import IFactory
from ats_utilities.checker.setup.bundle import CheckerBundle
from ats_utilities.checker.setup.options import CheckerOptions
from ats_utilities.checker.setup.keys import CheckerKeys
from ats_utilities.checker.setup.registry import CheckerRegistry
from ats_utilities.checker.setup.dependencies import CheckerDependencies
from ats_utilities.checker.setup.opt_validator import CheckerOptionsValidator
from ats_utilities.checker.format.format_validator import FormatValidator
from ats_utilities.checker.type.type_validator import TypeValidator
from ats_utilities.checker.context.context_provider import ContextProvider
from ats_utilities.checker.reporter.check_reporter import CheckReporter

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class CheckerFactory(IFactory[CheckerBundle, CheckerOptions]):
    '''
        Factory for creating checker bundle instance.

        It defines:

            :methods:
                | create_bundle - Creates a checker bundle with optional pre-configured options.
    '''

    @classmethod
    @override
    def create_bundle(cls, options: CheckerOptions | None = None) -> CheckerBundle:
        '''
            Creates a checker bundle with optional pre-configured options.

            :param options: Creation options/parameters for the bundle (default None).
            :type options: CheckerOptions | None
            :return: Checker bundle instance.
            :rtype: CheckerBundle
            :exceptions:
                | ATSValueError: Options must be provided and have proper values.
                | ATSTypeError:  Options must be an instance of CheckerOptions
                |                and its attributes must be instances of their
                |                respective interfaces and types.
        '''
        if options is not None:
            CheckerOptionsValidator.validate(options)

        separator = options.get(CheckerKeys.SEPARATOR) if options else None
        abstract_types = options.get(CheckerKeys.ABSTRACT_TYPES) if options else None
        stack_index_caller = options.get(CheckerKeys.STACK_INDEX_CALLER) if options else None
        messages_provider = options.get(CheckerKeys.MESSAGES_PROVIDER) if options else None

        format_validator: FormatValidator = FormatValidator(separator=separator)
        type_validator: TypeValidator = TypeValidator(abstract_types=abstract_types)
        context_provider: ContextProvider = ContextProvider(stack_index_caller=stack_index_caller)
        check_reporter: CheckReporter = CheckReporter(message_provider=messages_provider)

        return CheckerRegistry.create_bundle(
            dependencies=CheckerDependencies(
                format_validator=format_validator,
                type_validator=type_validator,
                context_provider=context_provider,
                check_reporter=check_reporter
            )
        )
