# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
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
    Defines class ProConfig with attribute(s) and method(s).
    Defines project configuration container.
'''

import sys
from typing import Any, Dict, List, Optional

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as ats_error_message:  # pragma: no cover
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')  # pragma: no cover

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ProConfig:
    '''
        Defines class ProConfig with attribute(s) and method(s).
        Defines project configuration container.
        Mechanism for project configuration.

        It defines:

            :attributes:
                | TEMPLATES - Templates key.
                | MODULES - Modules key.
                | FORMAT - Format for template file.
                | _config - Tool configuration in dictionary format.
            :methods:
                | __init__ - Initials ProConfig constructor.
                | pro_name - Property methods for set/get operations.
                | is_config_ok - Checks is project configuration ok.
    '''

    TEMPLATES: str = 'templates'
    MODULES: str = 'modules'
    FORMAT: str = 'template'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials ProConfig constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self._config: Optional[Dict[Any, Any]]
        verbose_message(verbose, ['init project configuration'])

    @property
    def config(self) -> Optional[Dict[Any, Any]]:
        '''
            Property method for getting project configuration.

            :return: Formatted project configuration | None
            :rtype: <Optional[Dict[Any, Any]]>
            :exceptions: None
        '''
        return self._config

    @config.setter
    def config(self, pro: Optional[Dict[Any, Any]]) -> None:
        '''
            Property method for setting project configuration.

            :param pro: Project configuration in dict format | None
            :type pro: <Optional[Dict[Any, Any]]>
            :exceptions: ATSTypeError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = checker.check_params([('dict:pro', pro)])
        if error_id == checker.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        self._config = pro

    def is_config_ok(self) -> bool:
        '''
            Checks is project configuration ok.

            :return: True (configuration is ok) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return bool(self._config)
