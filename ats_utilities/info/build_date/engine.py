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
    Defines the BuildDate class with attribute(s) and method(s).
    Provides an API for the build date in one property object.
'''

from __future__ import annotations

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextValidator
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


class BuildDate:
    '''
        Defines the BuildDate class with attribute(s) and method(s).
        Provides an API for the build date in one property object.
        Note: The build date is only prepared when it is set by the user (not None).

        It defines:

            :attributes:
                | _build_date - The build date for the App/Tool/Script (default: None).
            :methods:
                | __init__ - Initializes the BuildDate instance.
                | build_date - Property methods for setting and getting the build date.
                | not_none - Checks if the build date is not None.
                | __str__ - Returns the BuildDate as a string representation.
    '''

    _build_date: str | None
    _context: ContextBundle

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes the BuildDate instance.

            :param context_bundle: The context bundle for build date.
            :exceptions:
                | ATSValueError:  Context bundle must be provided and have proper values.
                | ATSTypeError:   Context bundle must be an instance of ContextBundle
                |                 and its attributes must be instances of their
                |                 respective types.
        '''
        ContextValidator.validate(context_bundle)
        self._context = context_bundle
        self._build_date = None

    @property
    @vreport('getting build_date {build_date}')
    def build_date(self) -> str | None:
        '''
            Property method for getting the build date.
            Note: The build date is only prepared when it is set by the user (not None).

            :return: The build date in string format | None.
            :exceptions:
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._build_date

    @build_date.setter
    @mcheck([('str:build_date', None)])
    @vreport('setting build_date {build_date}')
    def build_date(self, build_date: str) -> None:
        '''
            Property method for setting the build date.
            Note: The build date is only prepared when it is set by the user (not None).

            :param build_date: The build date in string format.
            :exceptions:
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError:      Parameter type validation failed.
                | ATSValueError:     Parameter format validation failed.
                | ATSRuntimeError:   The decorator is used on a non-class method.
                | ATSAttributeError: The class does not provide a '_checker' object.
        '''
        self._build_date = build_date

    @vreport('checking build_date {build_date}')
    def not_none(self) -> bool:
        '''
            Checks if the build date is not None.
            Note: The build date is only prepared when it is set by the user (not None).

            :return: True if successful, otherwise False.
            :exceptions:
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._build_date is not None

    def __str__(self) -> str:
        '''
            Returns the BuildDate as a string representation.

            :return: The BuildDate as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
