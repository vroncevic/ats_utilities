# -*- coding: UTF-8 -*-

'''
Module
    checker_registry.py
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
    Encapsulates core runtime components for simplification of CheckerBundle creation.
'''

from __future__ import annotations

from typing import Any, override

from ats_utilities.utils.iregistry import IRegistry
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


class CheckerRegistry(IRegistry[CheckerBundle]):
    '''
        Encapsulates core runtime components for simplification of CheckerBundle creation.

        It defines:

            :methods:
                | create_bundle - Creates a CheckerBundle instance using either file path and scheme or injected processor.
                | create_checker_bundle_by_file_path_and_scheme - Creates a CheckerBundle based on file path and scheme.
                | create_checker_bundle_by_processor - Creates a CheckerBundle based on an injected processor.
    '''

    @classmethod
    @override
    def create_bundle(cls, **kwargs: Any) -> CheckerBundle:
        '''
            Creates a CheckerBundle instance using either file path and scheme or injected processor.

            :param kwargs: Additional registry-specific orchestration parameters.
            :return: CheckerBundle instance.
            :rtype: <CheckerBundle>
            :exceptions:
                | ATSValueError: File path must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: Scheme must be an instance of Mapping interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle interface.
        '''
        return cls.create_default_checker_bundle()

    @classmethod
    def create_default_checker_bundle(cls) -> CheckerBundle:
        '''
            Creates a default CheckerBundle with pre-configured components.

            :return: Default CheckerBundle instance.
            :rtype: <CheckerBundle>
            :exceptions: None.
        '''
        return CheckerBundle(
            format_validator=FormatValidator(),
            type_validator=TypeValidator(),
            context_provider=ContextProvider(),
            check_reporter=CheckReporter()
        )
