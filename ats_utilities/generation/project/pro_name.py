# -*- coding: UTF-8 -*-

'''
Module
    pro_name.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    ats_utilities is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    ats_utilities is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines the ProName class with attribute(s) and method(s).
    Defines project name container.
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
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ProName:
    '''
        Defines the ProName class with attribute(s) and method(s).
        Defines project name container.
        Mechanism for project configuration.

        It defines:

            :attributes:
                | _pro_name - The project name.
            :methods:
                | __init__ - Initializes the project name.
                | pro_name - Property methods for setting and getting the respective property value.
                | not_none - Checks if the project name is not None.
                | __str__ - Returns the ATS project name as a string representation.
    '''

    _pro_name: str | None
    _context: ContextBundle

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes the project name.

            :param context_bundle: The context bundle for project name.
            :exceptions:
                | ATSValueError: The context bundle must be provided and have proper values.
                | ATSTypeError:  The context bundle must be an instance of ContextBundle and
                |                its attributes must be instances of their respective types.
        '''
        ContextBundleValidator.validate(context_bundle)
        self._context = context_bundle
        self._pro_name = None

    @property
    @vreport('getting pro name {pro_name}')
    def pro_name(self) -> str:
        '''
            Property method for getting the project name in string format.

            :return: The formatted project name in string format.
            :exceptions:
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._pro_name

    @pro_name.setter
    @mcheck([('str:name', None)])
    @vreport('getting pro name {pro_name}')
    def pro_name(self, name: str) -> None:
        '''
            Property method for setting the project name.

            :param name: The project name in string format.
            :exceptions:
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError:      Parameter type validation failed.
                | ATSValueError:     Parameter format validation failed.
                | ATSRuntimeError:   The decorator is used on a non-class method.
                | ATSAttributeError: The class does not provide a '_checker' object.
        '''
        self._pro_name = name

    @vreport('checking pro name {pro_name}')
    def not_none(self) -> bool:
        '''
            Checks if the project name is not None.

            :return: True if successful, otherwise False.
            :exceptions:
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._pro_name is not None

    def __str__(self) -> str:
        '''
            Returns the ATS project name as a string representation.

            :return: The ATS project name as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
