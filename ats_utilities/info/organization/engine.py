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
    Defines class Organization with attribute(s) and method(s).
    Creates an API for the organization in one property object.
'''

from __future__ import annotations

from typing import override

from ats_utilities.info.organization.iorganization import IOrganization
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.utils.reflection import to_str
from ats_utilities.checker.proxy_validator import mcheck
from ats_utilities.reporter.proxy_reporter import vreport

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Organization(IOrganization):
    '''
        Defines class Organization with attribute(s) and method(s).
        Creates an API for the organization in one property object.
        Note: Organization is only prepared when it is set by user (not None).

        It defines:

            :attributes:
                | _organization - The organization for App/Tool/Script (default None).
            :methods:
                | __init__ - Initializes Organization constructor.
                | organization - Property methods for set/get organization.
                | not_none - Checks is organization not None.
                | __str__ - Returns the organization as string representation.
    '''

    _organization: str | None
    _context: ContextBundle

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes Organization constructor.

            :param context_bundle: Context bundle for organization.
            :type context_bundle: ContextBundle
            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        self._context = context_bundle
        self._organization = None

    @property
    @vreport('getting organization {organization}')
    @override
    def organization(self) -> str | None:
        '''
            Property method for getting organization.
            Note: Organization is only prepared when it is set by user (not None).

            :return: The organization in string format | None.
            :rtype: str | None
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._organization

    @organization.setter
    @mcheck([('str:organization', None)])
    @vreport('setting organization {organization}')
    @override
    def organization(self, organization: str) -> None:
        '''
            Property method for setting organization.
            Note: Organization is only prepared when it is set by user (not None).

            :param organization: The organization in string format.
            :type organization: str
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._organization = organization

    @vreport('checking organization {organization}')
    @override
    def not_none(self) -> bool:
        '''
            Checks is organization not None.
            Note: Organization is only prepared when it is set by user (not None).

            :return: True if successful, otherwise False.
            :rtype: bool
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._organization is not None

    @override
    def __str__(self) -> str:
        '''
            Returns the Organization as string representation.

            :return: The Organization as string representation.
            :rtype: str
            :exceptions: None.
        '''
        return to_str(self)
