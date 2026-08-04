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
    Defines the UseGitHub class with attribute(s) and method(s).
    Provides an API for the use GitHub infrastructure in one property object.
'''

from __future__ import annotations

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextBundleValidator
from ats_utilities.utils.reflection import to_str
from ats_utilities.checker.proxy_validator import mcheck
from ats_utilities.reporter.proxy_reporter import vreport

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class UseGitHub:
    '''
        Defines the UseGitHub class with attribute(s) and method(s).
        Provides an API for the use GitHub infrastructure in one property object.
        Note: The use github is only prepared when it is set by the user (not None).

        It defines:

            :attributes:
                | _use_github - The use GitHub infrastructure for the App/Tool/Script (default: False).
            :methods:
                | __init__ - Initializes the UseGitHub.
                | use_github - Property methods for setting and getting the use_github.
                | not_none - Checks if the use GitHub infrastructure is not None.
                | __str__ - Returns the use GitHub infrastructure as a string representation.
    '''

    _use_github: bool
    _context: ContextBundle

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes the UseGitHub.

            :param context_bundle: The context bundle for use_github.
            :exceptions:
                | ATSValueError: The context bundle must be provided and have proper values.
                | ATSTypeError:  The context bundle must be an instance of ContextBundle
                |                and its attributes must be instances of their respective types.
        '''
        ContextBundleValidator.validate(context_bundle)
        self._context = context_bundle
        self._use_github = False

    @property
    @vreport('getting use_github {use_github}')
    def use_github(self) -> bool | None:
        '''
            Property method for getting the use GitHub infrastructure.
            Note: The use github is only prepared when it is set by the user (not None).

            :return: The use GitHub infrastructure | None.
            :exceptions:
                | ATSRuntimeError: The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._use_github

    @use_github.setter
    @mcheck([('bool:use_github', None)])
    @vreport('setting use_github {use_github}')
    def use_github(self, use_github: bool) -> None:
        '''
            Property method for setting the use GitHub infrastructure.
            Note: The use github is only prepared when it is set by the user (not None).

            :param use_github: The use GitHub infrastructure.
            :exceptions:
                | ATSRuntimeError: The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: The decorator is used on a non-class method.
                | ATSAttributeError: The class does not provide a '_checker' object.
        '''
        self._use_github = use_github

    @vreport('checking use_github {use_github}')
    def not_none(self) -> bool:
        '''
            Checks if the use GitHub infrastructure is not None.
            Note: The use github is only prepared when it is set by the user (not None).

            :return: True if successful, otherwise False.
            :exceptions:
                | ATSRuntimeError: The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._use_github is not None

    def __str__(self) -> str:
        '''
            Returns the UseGitHub infrastructure as a string representation.

            :return: The UseGitHub infrastructure as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
