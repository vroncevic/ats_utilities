# -*- coding: UTF-8 -*-

'''
Module
    pro_config.py
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
    Defines the ProConfig class with attribute(s) and method(s).
    Defines project configuration container.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextBundleValidator
from ats_utilities.utils.reflection import to_str
from ats_utilities.checker.proxy_validator import mcheck
from ats_utilities.reporter.proxy_reporter import vreport

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ProConfig:
    '''
        Defines the ProConfig class with attribute(s) and method(s).
        Defines project configuration container.
        Mechanism for project configuration.

        It defines:

            :attributes:
                | TEMPLATES - The templates key used for processing template files.
                | MODULES - The modules key used for processing template files.
                | FORMAT - The format for template file extension.
                | _config - The tool configuration in dictionary format (default: None).
            :methods:
                | __init__ - Initializes project configuration.
                | config - Property methods for setting and getting the respective property value.
                | not_none - Checks if the project configuration is not None.
                | __str__ - Returns the ATS project configuration as a string representation.
    '''

    TEMPLATES: str = 'templates'
    MODULES: str = 'modules'
    FORMAT: str = 'template'
    _config: Mapping[str, object] | None
    _context: ContextBundle

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes project configuration.

            :param context_bundle: The context bundle for project configuration.
            :exceptions:
                | ATSValueError: The context bundle must be provided and have proper values.
                | ATSTypeError:  The context bundle must be an instance of ContextBundle and
                |                its attributes must be instances of their respective types.
        '''
        ContextBundleValidator.validate(context_bundle)
        self._context = context_bundle
        self._config = None

    @property
    @vreport('getting config {config}')
    def config(self) -> Mapping[str, object]:
        '''
            Property method for getting the project configuration.

            :return: The formatted project configuration in dict format.
            :exceptions:
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._config

    @config.setter
    @mcheck([('Mapping | None:pro_config', None)])
    @vreport('getting config {config}')
    def config(self, pro_config: Mapping[str, object]) -> None:
        '''
            Property method for setting the project configuration.

            :param pro_config: The project configuration in Mapping format.
            :exceptions:
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError:      Parameter type validation failed.
                | ATSValueError:     Parameter format validation failed.
                | ATSRuntimeError:   The decorator is used on a non-class method.
                | ATSAttributeError: The class does not provide a '_checker' object.
        '''
        self._config = pro_config

    @vreport('checking config {config}')
    def not_none(self) -> bool:
        '''
            Checks if the project configuration is not None.

            :return: True if successful, otherwise False.
            :exceptions:
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._config is not None

    def __str__(self) -> str:
        '''
            Returns the ATS project configuration as a string representation.

            :return: The ATS project configuration as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
