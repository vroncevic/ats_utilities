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
from typing import Any, NoReturn, override

from ats_utilities.option.parser.iarg_parser import IArgParser
from ats_utilities.option.parser.data import ParserData
from ats_utilities.option.parser.data_validator import ParserDataValidator
from ats_utilities.context.factory import ContextFactory
from ats_utilities.utils.reflection import to_str
from ats_utilities.checker.proxy_validator import mcheck
from ats_utilities.reporter.proxy_reporter import vreport
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ArgParser(ArgumentParser, IArgParser):
    '''
        Defines class ArgParser with attribute(s) and method(s).
        Custom ArgumentParser to route errors to IReporter.

        It defines:

            :methods:
                | __init__ - Initials ArgParser constructor.
                | error - Overrides default error handling to use IReporter.
                | __str__ - Returns the string representation of ArgParser.
    '''

    def __init__(self, own: ParserData | None = None, **kwargs: Any) -> None:
        '''
            Initializes ArgParser constructor.

            :param own: Data with components for argument parser.
            :type own: <ParserData | None>
            :param kwargs: Additional keyword arguments.
            :type kwargs: Any
            :exceptions: None.
        '''
        if own is None:
            own = kwargs.pop('own', None)

        if own is not None:
            ParserDataValidator.validate(own)

        if own is None:
            ctx_bundle = kwargs.pop('context_bundle', None)

            if ctx_bundle is None:
                ctx_bundle = ContextFactory.create_default_bundle()

            own = ParserData(
                prog=kwargs.get('prog', ''),
                epilog=kwargs.get('epilog', ''),
                description=kwargs.get('description', ''),
                context_bundle=ctx_bundle
            )

        self._context = own.context_bundle
        for name in ('prog', 'epilog', 'description'):
            if name not in kwargs:
                kwargs[name] = getattr(own, name)

        ArgumentParser.__init__(self, **kwargs)

    @mcheck([('str:message', None)])
    @vreport('argument error: {message}')
    @override
    def error(self, message: str) -> NoReturn:
        '''
            Overrides default error handling to use IReporter.

            :param message: Error message to report.
            :type message: str
            :rtype: NoReturn
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._context.reporter.error([f'argument error: {message}'])
        sys.exit(2)

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of ArgParser.

            :return: The ArgParser as string representation.
            :rtype: str
            :exceptions: None.
        '''
        return to_str(self)
