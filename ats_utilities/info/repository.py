# -*- coding: UTF-8 -*-

'''
Module
    repository.py
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
    Defines class Repository with attribute(s) and method(s).
    Creates an API for the ATS repository in one property object.
'''

from typing import override
from ats_utilities.info.irepository import IRepository
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.proxy_reporter import vreporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Repository(IRepository):
    '''
        Defines class Repository with attribute(s) and method(s).
        Creates an API for the ATS repository in one property object.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _repository - The ATS repository (default None).
            :methods:
                | __init__ - Initializes Repository constructor.
                | repository - Property methods for set/get repository.
                | not_none - Checks is ATS repository not None.
                | __str__ - Returns the ATS repository as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(self, context_bundle: ContextBundle | None = None) -> None:
        '''
            Initializes Repository constructor.

            :param context_bundle: Context bundle for repository | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        factory_context_bundle(self, context_bundle)
        self._repository: str | None = None

    @property
    @vreporter('get repository {repository}')
    @override
    def repository(self) -> str | None:
        '''
            Property method for getting ATS repository.

            :return: The ATS repository in string format | None.
            :rtype: <str | None>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @verboser decorator.
        '''
        return self._repository

    @repository.setter
    @validator([('str | None:repository', None)])
    @vreporter('set repository {repository}')
    @override
    def repository(self, repository: str | None) -> None:
        '''
            Property method for setting ATS repository.

            :param repository: The ATS repository in string format | None.
            :type repository: <str | None>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @verboser decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._repository = repository

    @vreporter('check repository {repository}')
    @override
    def not_none(self) -> bool:
        '''
            Checks is ATS repository not None.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @verboser decorator.
        '''
        return self._repository is not None

    @override
    def __str__(self) -> str:
        '''
            Returns the ATS repository as string representation.

            :return: The ATS repository as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
