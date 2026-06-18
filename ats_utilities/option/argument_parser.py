# -*- coding: UTF-8 -*-

'''
Module
    argument_parser.py
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
    Defines class ATSArgumentParser with attribute(s) and method(s).
    Custom ArgumentParser to route errors to IReporter.
'''

import sys
from typing import Any, List, Optional, NoReturn
from argparse import ArgumentParser
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import get_private_attr, format_instance_to_string
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.proxy_reporter import vreporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSArgumentParser(ArgumentParser):
    '''
        Defines class ATSArgumentParser with attribute(s) and method(s).
        Custom ArgumentParser to route errors to IReporter.

        It defines:

            :attributes:
                | __checker - Parameters checker (default ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
            :methods:
                | __init__ - Initials ATSArgumentParser constructor.
                | error - Overrides default error handling to use IReporter.
                | _reporter - Property method for getting the internal reporter instance.
                | __str__ - Returns the string representation of ATSArgumentParser.
    '''

    def __init__(
        self,
        *args: Any,
        option_bundle: Optional[ContextBundle] = None,
        **kwargs: Any
    ) -> None:
        '''
            Initials ATSArgumentParser constructor.

            :param args: Additional positional arguments
            :type args: <Any>
            :param option_bundle: Bundle with checker, reporter and verbose | None
            :type option_bundle: <Optional[ContextBundle]>
            :param kwargs: Additional keyword arguments
            :type kwargs: <Any>
            :exceptions: None
        '''
        super().__init__(*args, **kwargs)
        factory_context_bundle(self, option_bundle)

    @validator([('str:message', None)])
    @vreporter('argument error: {message}')
    def error(self, message: str) -> NoReturn:
        '''
            Overrides default error handling to use IReporter.

            :param message: Error message to report
            :type message: <str>
            :return: None
            :rtype: <NoReturn>
            :exceptions: None
        '''
        self._reporter.error([f'argument error: {message}'])
        sys.exit(2)

    @property
    def _reporter(self) -> IReporter:
        '''
            Property method for getting the internal reporter instance.

            :return: The reporter instance in IReporter format
            :rtype: <IReporter>
            :exceptions: None
        '''
        return get_private_attr(self, 'reporter')

    def __str__(self) -> str:
        '''
            Returns the string representation of ATSArgumentParser.

            :return: The ATSArgumentParser as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
