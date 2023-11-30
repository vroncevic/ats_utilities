# -*- coding: UTF-8 -*-

'''
Module
    ext_infrastructure.py
Copyright
    Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class ExtInfrastructure with attribute(s) and method(s).
    Creates API for processing hyperlinks for splash.
'''

import sys
from typing import Any, Dict

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.9.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ExtInfrastructure(ATSChecker):
    '''
        Defines class ExtInfrastructure with attribute(s) and method(s).
        Creates API for processing hyperlinks for splash.
        API for GitHub information.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | _property - Splash property in dict format.
            :methods:
                | __init__ - Initial ExtInfrastructure constructor.
                | get_info_text - Pre-processed info text.
                | get_issue_text - Pre-processed issue text.
                | get_author_text - Pre-processed author text.
    '''

    def __init__(self, prop: Dict[Any, Any], verbose: bool = False) -> None:
        '''
            Initial ExtInfrastructure constructor.

            :param property: Splash property in dict form
            :type property: <dict>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        super().__init__()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([('dict:prop', prop)])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if error_id == self.VALUE_ERROR:
            raise ATSBadCallError(error_msg)
        self._verbose: bool = verbose
        self._property: Dict[Any, Any] = prop
        verbose_message(self._verbose, [f'splash property {prop}'])

    def get_info_text(self) -> str:
        '''
            Pre-processed info text for splash.

            :return: Hyperlink with info text
            :rtype: <str>
            :exceptions: None
        '''
        name: str = self._property['ats_name']
        return f'\x1b]8;;{name}\a{name}\x1b]8;;\a'

    def get_issue_text(self) -> str:
        '''
            Pre-processed issue text for splash.

            :return: Hyperlink with issue info
            :rtype: <str>
            :exceptions: None
        '''
        repo: str = self._property['ats_repository']
        return f'\x1b]8;;{repo}\a{repo}\x1b]8;;\a'

    def get_author_text(self) -> str:
        '''
            Pre-processed author text for splash.

            :return: Hyperlink with author info
            :rtype: <str>
            :exceptions: None
        '''
        org: str = self._property['ats_organization']
        return f'\x1b]8;;{org}\a{org}\x1b]8;;\a'
