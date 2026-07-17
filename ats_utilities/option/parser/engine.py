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
from argparse import ArgumentParser
from typing import NoReturn, override

from ats_utilities.option.parser.iarg_parser import IArgParser
from ats_utilities.option.parser.parser_bundle import ParserBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.context.context_bundle_inject import inject_context_bundle
from ats_utilities.utils.reflection import to_str
from ats_utilities.checker.proxy_validator import vcheck
from ats_utilities.reporter.proxy_reporter import vreport
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ArgParser(ArgumentParser, IArgParser):
    '''
        Defines class ArgParser with attribute(s) and method(s).
        Custom ArgumentParser to route errors to IReporter.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger (default Logger).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
            :methods:
                | __init__ - Initials ArgParser constructor.
                | error - Overrides default error handling to use IReporter.
                | __str__ - Returns the string representation of ArgParser.
    '''

    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool

    def __init__(self, component_bundle: ParserBundle) -> None:
        '''
            Initializes ArgParser constructor.

            :param args: Additional positional arguments.
            :type args: <Any>
            :param context_bundle: Context bundle for argument parser.
            :type context_bundle: <ContextBundle>
            :param kwargs: Additional keyword arguments.
            :type kwargs: <Any>
            :exceptions:
                | ATSValueError: Component bundle must be provided.
                | ATSTypeError: Component bundle must be a ParserBundle instance.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        not_none(component_bundle, r'component bundle must be provided')
        istype(component_bundle, ParserBundle, r'component bundle must be a ParserBundle instance')
        super().__init__(
            prog=component_bundle.prog,
            epilog=component_bundle.epilog,
            description=component_bundle.description
        )
        inject_context_bundle(self, component_bundle.context_bundle)

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
