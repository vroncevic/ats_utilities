# -*- coding: UTF-8 -*-

'''
Module
    template_dir.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class TemplateDir with attribute(s) and method(s).
    Defines project template directory container.
'''

import sys
from typing import List, Optional

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TemplateDir:
    '''
        Defines class TemplateDir with attribute(s) and method(s).
        Defines project template directory container.
        Mechanism for project configuration.

        It defines:

            :attributes:
                | _template_dir - Project template dir.
            :methods:
                | __init__ - Initials TemplateDir constructor.
                | template_dir - Property methods for set/get operations.
                | is_template_dir_ok - Checks is template dir ok.
    '''

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials TemplateDir constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self._template_dir: Optional[str] = None
        verbose_message(verbose, ['init template dir'])

    @property
    def template_dir(self) -> Optional[str]:
        '''
            Property method for getting template dir.

            :return: Formatted template dir | None.
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self._template_dir

    @template_dir.setter
    def template_dir(self, path: Optional[str]) -> None:
        '''
            Property method for setting project template dir.

            :param path: Project template dir | None
            :type path: <Optional[str]>
            :exceptions: ATSTypeError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = checker.check_params([('str:path', path)])
        if error_id == checker.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        self._template_dir = path

    def is_template_dir_ok(self) -> bool:
        '''
            Checks is project template dir ok.

            :return: True (tempalte dir is ok) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return bool(self._template_dir)
