# -*- coding: UTF-8 -*-

'''
Module
    check_reporter.py
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
    Defines class CheckReporter with attribute(s) and method(s).
    Creates an API for checking parameters for methods and functions.
'''

from __future__ import annotations

from typing import override

from ats_utilities.utils.reflection import to_str
from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter
from ats_utilities.checker.reporter.checker_reporter_bundle import CheckerReporterBundle
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class CheckReporter(ICheckReporter):
    '''
        Defines class CheckReporter with attribute(s) and method(s).
        Standard human-readable report formatter.
        Mechanism for checking function or method parameters (report).

        It defines:

            :methods:
                | build_message_format - Builds the final message report.
                | __str__ - Returns the check reporter as string representation.
    '''

    @override
    def build_message_format(self, report_bundle: CheckerReporterBundle) -> str:
        '''
            Builds the final message report for checker.

            :param report_bundle: Bundle with parameters.
            :type report_bundle: <CheckerReporterBundle>
            :return: Formatted message report.
            :rtype: <str>
            :exceptions:
                | ATSValueError: Report checker reporter bundle must be provided.
                | ATSTypeError: Report checker reporter bundle must be an instance of CheckerReporterBundle.
        '''
        not_none(
            report_bundle,
            r'check_reporter::build_message_format(...)',
            r'report checker reporter bundle must be provided'
        )
        istype(
            report_bundle, CheckerReporterBundle,
            r'check_reporter::build_message_format(...)',
            r'report bundle must be an instance of CheckerReporterBundle'
        )

        message = report_bundle.context
        err_set = set(report_bundle.err_indices)

        for i, (pname, ptype, inst) in enumerate(report_bundle.parameters_meta):
            message += f'\n    expected {pname} <{ptype}> object at {hex(id(inst))}'

            if i in err_set:
                message += ' wrong type'

        if report_bundle.is_fmt_err:
            message += ' format wrong during checking parameters_meta'

        return message

    @override
    def __str__(self) -> str:
        '''
            Returns the check reporter as string representation.

            :return: The check reporter as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
