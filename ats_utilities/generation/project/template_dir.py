# -*- coding: UTF-8 -*-

'''
Module
    template_dir.py
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
    Defines the TemplateDir class with attribute(s) and method(s).
    Defines project template directory container.
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


class TemplateDir:
    '''
        Defines the TemplateDir class with attribute(s) and method(s).
        Defines project template directory container.
        Mechanism for project configuration.

        It defines:

            :attributes:
                | _template_dir - The project template dir path (default: None).
            :methods:
                | __init__ - Initializes the template dir.
                | template_dir - Property methods for setting and getting the respective property value.
                | not_none - Checks if the template dir is not None.
                | __str__ - Returns the ATS project template directory as a string representation.
    '''

    _template_dir: str | None
    _context: ContextBundle

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes the template dir.

            :param context_bundle: The context bundle for template dir.
            :exceptions:
                | ATSValueError: The context bundle must be provided and have proper values.
                | ATSTypeError:  The context bundle must be an instance of ContextBundle and
                |                its attributes must be instances of their respective types.
        '''
        ContextBundleValidator.validate(context_bundle)
        self._context = context_bundle
        self._template_dir = None

    @property
    @vreport('getting template dir {template_dir}')
    def template_dir(self) -> str:
        '''
            Property method for getting the template dir.

            :return: The formatted template dir in string format.
            :exceptions:
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._template_dir

    @template_dir.setter
    @mcheck([('str:dir_path', None)])
    @vreport('getting template dir {template_dir}')
    def template_dir(self, dir_path: str) -> None:
        '''
            Property method for setting the project template dir.

            :param dir_path: The project template dir path in string format.
            :exceptions:
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError:      Parameter type validation failed.
                | ATSValueError:     Parameter format validation failed.
                | ATSRuntimeError:   The decorator is used on a non-class method.
                | ATSAttributeError: The class does not provide a '_checker' object.
        '''
        self._template_dir = dir_path

    @vreport('checking template dir {template_dir}')
    def not_none(self) -> bool:
        '''
            Checks if the project template dir is not None.

            :return: True if successful, otherwise False.
            :exceptions:
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._template_dir is not None

    def __str__(self) -> str:
        '''
            Returns the ATS project template directory as a string representation.

            :return: The ATS project template directory as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
