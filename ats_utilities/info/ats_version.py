# -*- coding: UTF-8 -*-

'''
Module
    ats_version.py
Copyright
    Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class ATSVersion with attribute(s) and method(s).
    Creates API for ATS version in one property object.
'''

import sys

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.9.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSVersion(ATSChecker):
    '''
        Defines class ATSVersion with attribute(s) and method(s).
        Creates API for ATS version in one property object.
        ATS version container.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | _version - ATS version.
            :methods:
                | __init__ - Initial ATSVersion constructor.
                | version - Property methods for set/get operations.
                | is_not_none - Check is ATS version not None.
    '''

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initial ATSVersion constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__()
        self._verbose: bool = verbose
        self._version: str | None = None

    @property
    def version(self) -> str | None:
        '''
            Property method for getting ATS version.

            :return: ATS version | None
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self._version

    @version.setter
    def version(self, version: str | None) -> None:
        '''
            Property method for setting ATS version.

            :param version: ATS version | None
            :type version: <str> | <NoneType>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([('str:version', version)])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if error_id == self.VALUE_ERROR:
            raise ATSBadCallError(error_msg)
        self._version = version
        verbose_message(self._verbose, [f'version {version}'])

    def is_not_none(self) -> bool:
        '''
            Checking is ATS version None.

            :return: True (ATS version is not None) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return self._version is not None
