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
    Defines class ArgParser with attribute(s) and method(s).
    Custom ArgumentParser to route errors to IReporter.
'''

from __future__ import annotations

import sys
from typing import Any, NoReturn, override
from argparse import ArgumentParser

from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
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


class ArgParser(ArgumentParser):
    '''
        Defines class ArgParser with attribute(s) and method(s).
        Custom ArgumentParser to route errors to IReporter.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
            :methods:
                | __init__ - Initials ArgParser constructor.
                | error - Overrides default error handling to use IReporter.
                | _reporter - Returns the reporter instance.
                | __str__ - Returns the string representation of ArgParser.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(
        self,
        *args: Any,
        context_bundle: ContextBundle | None = None,
        **kwargs: Any
    ) -> None:
        '''
            Initializes ArgParser constructor.

            :param args: Additional positional arguments.
            :type args: <Any>
            :param context_bundle: Context bundle for argument parser | None.
            :type context_bundle: <ContextBundle | None>
            :param kwargs: Additional keyword arguments.
            :type kwargs: <Any>
            :exceptions: None.
        '''
        super().__init__(*args, **kwargs)
        factory_context_bundle(self, context_bundle)

    @vcheck([('str:message', None)])
    @vreport('argument error: {message}')
    @override
    def error(self, message: str) -> NoReturn:
        '''
            Overrides default error handling to use IReporter.

            :param message: Error message to report.
            :type message: <str>
            :rtype: <NoReturn>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._reporter.error([f'argument error: {message}'])
        sys.exit(2)

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of ArgParser.

            :return: The ArgParser as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
