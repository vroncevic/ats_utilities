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
    Defines class UseGitHub with attribute(s) and method(s).
    Creates an API for the use GitHub infrastructure in one property object.
'''

from __future__ import annotations

from typing import override

from ats_utilities.info.use_github.iuse_github import IUseGitHub
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


class UseGitHub(IUseGitHub):
    '''
        Defines class UseGitHub with attribute(s) and method(s).
        Creates an API for the use GitHub infrastructure in one property object.
        Note: Use GitHub is only prepared when it is set by user (not None).

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _use_github - The use GitHub infrastructure for App/Tool/Script (default False).
            :methods:
                | __init__ - Initializes UseGitHub constructor.
                | use_github - Property methods for set/get use_github.
                | not_none - Checks is use GitHub infrastructure not None.
                | __str__ - Returns the use GitHub infrastructure as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool
    _use_github: bool

    def __init__(self, context_bundle: ContextBundle | None = None) -> None:
        '''
            Initializes UseGitHub constructor.

            :param context_bundle: Context bundle for use_github | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        factory_context_bundle(self, context_bundle)
        self._use_github = False

    @property
    @vreport('getting use_github {use_github}')
    @override
    def use_github(self) -> bool:
        '''
            Property method for getting use GitHub infrastructure.
            Note: Use GitHub is only prepared when it is set by user (not None).

            :return: The use GitHub infrastructure.
            :rtype: <bool>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._use_github

    @use_github.setter
    @vcheck([('bool:use_github', None)])
    @vreport('setting use_github {use_github}')
    @override
    def use_github(self, use_github: bool) -> None:
         '''
             Property method for setting use GitHub infrastructure.
             Note: Use GitHub is only prepared when it is set by user (not None).

             :param use_github: The use GitHub infrastructure.
             :type use_github: <bool>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
         '''
         self._use_github = use_github

    @vreport('checking use_github {use_github}')
    @override
    def not_none(self) -> bool:
        '''
            Checks is use GitHub infrastructure not None.
            Note: Use GitHub is only prepared when it is set by user (not None).

            :return: True (not None) | False (None).
            :rtype: <bool>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._use_github is not None

    @override
    def __str__(self) -> str:
        '''
            Returns the UseGitHub infrastructure as string representation.

            :return: The UseGitHub infrastructure as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
