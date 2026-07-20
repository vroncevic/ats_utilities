# -*- coding: UTF-8 -*-

'''
Module
    checker_reporter_registry.py
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
    Encapsulates core runtime components for simplification of CheckerReporterBundle creation.
'''

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.checker.reporter.checker_reporter_bundle import CheckerReporterBundle, ParamMetadata

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class CheckerReporterRegistry(IRegistry[CheckerReporterBundle]):
    '''
        Encapsulates core runtime components for simplification of CheckerReporterBundle creation.

        It defines:

            :methods:
                | create_bundle - Creates a CheckerReporterBundle.
    '''

    @classmethod
    @override
    def create_bundle(cls, **kwargs: Any) -> CheckerReporterBundle:
        '''
            Creates a CheckerReporterBundle instance.

            :param kwargs: Additional registry-specific orchestration parameters.
            :return: CheckerReporterBundle instance.
            :rtype: <CheckerReporterBundle>
            :exceptions:
                | ATSValueError: Context must be provided.
                | ATSValueError: Parameters metadata must be provided.
                | ATSValueError: Error indices must be provided.
                | ATSValueError: Is format error must be provided.
                | ATSTypeError: Context must be a string.
                | ATSTypeError: Parameters metadata must be a sequence of ParamMetadata.
                | ATSTypeError: Error indices must be a sequence of integers.
                | ATSTypeError: Is format error must be a boolean.
        '''
        context: str | None = kwargs.get('context')
        parameters_meta: Sequence[ParamMetadata] | None = kwargs.get('parameters_meta')
        err_indices: Sequence[int] | None = kwargs.get('err_indices')
        is_fmt_err: bool | None = kwargs.get('is_fmt_err')

        return CheckerReporterBundle(
            context=context,
            parameters_meta=parameters_meta,
            err_indices=err_indices,
            is_fmt_err=is_fmt_err
        )
