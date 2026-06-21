# -*- coding: UTF-8 -*-

'''
Module
    version.py
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
    Defines class Version with attribute(s) and method(s).
    Creates an API for the ATS version in one property object.
'''

from ats_utilities.info.iversion import IVersion
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
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Version(IVersion):
    '''
        Defines class Version with attribute(s) and method(s).
        Creates an API for the ATS version in one property object.

        It defines:

            :attributes:
                | _checker - Factoriezed parameters checker (default Checker).
                | _reporter - Factoriezed reporter for messaging (default Reporter).
                | _verbose - Factoriezed Enable/Disable verbose option (default False).
                | _version - The ATS version (default None).
            :methods:
                | __init__ - Initializes Version constructor.
                | version - Property methods for set/get version.
                | not_none - Checks is ATS version not None.
                | __str__ - Returns the ATS version as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(self, context_bundle: ContextBundle | None = None) -> None:
        '''
            Initializes Version constructor.

            :param context_bundle: Context bundle for version | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None..
        '''
        factory_context_bundle(self, context_bundle)
        self._version: str | None = None

    @property
    @vreporter('get version {version}')
    def version(self) -> str | None:
        '''
            Property method for getting ATS version.

            :return: The ATS version in string format | None.
            :rtype: <str | None>
            :exceptions: ATSRuntimeError, ATSAttributeError.
        '''
        return self._version

    @version.setter
    @validator([('str | None:version', None)])
    @vreporter('set version {version}')
    def version(self, version: str | None) -> None:
        '''
            Property method for setting ATS version.

            :param version: The ATS version in string format | None.
            :type version: <str | None>
            :exceptions:
                | ATSTypeError, ATSValueError, RuntimeError, AttributeError.
                | RuntimeError, AttributeError.
        '''
        self._version = version

    @vreporter('check version {version}')
    def not_none(self) -> bool:
        '''
            Checks is ATS version not None.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: ATSRuntimeError, ATSAttributeError.
        '''
        return self._version is not None

    def __str__(self) -> str:
        '''
            Returns the ATS version as string representation.

            :return: The ATS version as string representation.
            :rtype: <str>
            :exceptions: None..
        '''
        return format_instance_to_string(self)
