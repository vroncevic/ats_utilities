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

from ats_utilities.checker.reporter.checker_reporter_bundle import CheckerReporterBundle, ParamMetadata

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class CheckerReporterRegistry:
    '''
        Encapsulates core runtime components for simplification of CheckerReporterBundle creation.

        It defines:

            :methods:
                | create_checker_reporter_bundle - Creates a CheckerReporterBundle.
    '''

    @classmethod
    def create_checker_reporter_bundle(
        cls,
        context: str,
        parameters_meta: Sequence[ParamMetadata],
        err_indices: Sequence[int],
        is_fmt_err: bool
    ) -> CheckerReporterBundle:
        '''
            Creates a CheckerReporterBundle.

            :param context: Message context.
            :type context: <str>
            :param parameters_meta: Sequence of parameter name and parameter type tuples.
            :type parameters_meta: <Sequence[ParamMetadata]>
            :param err_indices: Sequence of error indices.
            :type err_indices: <Sequence[int]>
            :param is_fmt_err: Flag indicating if format error type has been found.
            :type is_fmt_err: <bool>
            :return: CheckerReporterBundle instance.
            :rtype: <CheckerReporterBundle>
            :exceptions:
                | ATSTypeError: Context must be a string.
                | ATSTypeError: Parameters metadata must be a sequence of ParamMetadata.
                | ATSTypeError: Error indices must be a sequence of integers.
                | ATSTypeError: Is format error must be a boolean.
        '''
        return CheckerReporterBundle(
            context=context,
            parameters_meta=parameters_meta,
            err_indices=err_indices,
            is_fmt_err=is_fmt_err
        )
