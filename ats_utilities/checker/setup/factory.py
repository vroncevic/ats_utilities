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
    Factory for creating the checker bundle.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.checker.setup.bundle import CheckerBundle
from ats_utilities.checker.setup.options import CheckerBundleOptions
from ats_utilities.checker.setup.keys import CheckerBundleKeys
from ats_utilities.checker.setup.registry import CheckerBundleRegistry
from ats_utilities.checker.setup.dependencies import CheckerBundleDependencies
from ats_utilities.checker.setup.opt_validator import CheckerBundleOptionsValidator
from ats_utilities.checker.format.engine import FormatValidator
from ats_utilities.checker.type.engine import TypeValidator
from ats_utilities.checker.context.engine import ContextProvider
from ats_utilities.checker.reporter.engine import CheckReporter

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class CheckerBundleFactory:
    '''
        Factory for creating the checker bundle.

        It defines:

            :methods:
                | create_bundle - Creates the checker bundle with optional pre-configured options.
    '''

    @classmethod
    def create_bundle(cls, options: CheckerBundleOptions | None = None) -> CheckerBundle:
        '''
            Creates the checker bundle with optional pre-configured options.

            :param options: The creation options/parameters for the checker bundle (default: None).
            :return: The checker bundle.
            :exceptions:
                | ATSValueError: The checker bundle options must be provided and have proper values.
                | ATSTypeError:  The checker bundle options must be an instance of Mapping and its attributes
                |                must be instances of their respective interfaces and types.
                | ATSValueError: The checker bundle dependencies must be provided and have proper attributes.
                | ATSTypeError:  The checker bundle dependencies must be an instance of Mapping and its attributes
                |                must be instances of their respective types.
                | ATSValueError: The checker bundle must be provided and have proper values.
                | ATSTypeError:  The checker bundle must be an instance of CheckerBundle
                |                and its attributes must be instances of their respective types.
        '''
        if options is not None:
            CheckerBundleOptionsValidator.validate(options)

        separator: str | None = options.get(CheckerBundleKeys.OPTION_SEPARATOR) if options else None
        abstract_types: Mapping | None = options.get(CheckerBundleKeys.OPTION_ABSTRACT_TYPES) if options else None
        stack_index_caller: int | None = options.get(CheckerBundleKeys.OPTION_STACK_INDEX_CALLER) if options else None
        messages_provider: Mapping | None = options.get(CheckerBundleKeys.OPTION_MESSAGES_PROVIDER) if options else None

        format_validator: FormatValidator = FormatValidator(separator=separator)
        type_validator: TypeValidator = TypeValidator(abstract_types=abstract_types)
        context_provider: ContextProvider = ContextProvider(stack_index_caller=stack_index_caller)
        check_reporter: CheckReporter = CheckReporter(message_provider=messages_provider)

        return CheckerBundleRegistry.create_bundle(
            dependencies=CheckerBundleDependencies(
                format_validator=format_validator,
                type_validator=type_validator,
                context_provider=context_provider,
                check_reporter=check_reporter
            )
        )
