# -*- coding: UTF-8 -*-

'''
Module
    ats_build_date.py
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
    Defines class ATSBuildDate with attribute(s) and method(s).
    Creates API for ATS build date in one property object.
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


class ATSBuildDate(ATSChecker):
    '''
        Defines class ATSBuildDate with attribute(s) and method(s).
        Creates API for ATS build date in one property object.
        ATS build date container.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | _build_date - ATS build date.
            :methods:
                | __init__ - Initial ATSBuildDate constructor.
                | build_date - Property methods for set/get operations.
                | is_not_none - Check is ATS build date not None.
    '''

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initial ATSBuildDate constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__()
        self._verbose: bool = verbose
        self._build_date: str | None = None

    @property
    def build_date(self) -> str | None:
        '''
            Property method for getting ATS build date.

            :return: ATS build date | None
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self._build_date

    @build_date.setter
    def build_date(self, build_date: str | None) -> None:
        '''
            Property method for setting ATS build date.

            :param build_date: ATS build date | None
            :type build_date: <str> | <NoneType>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('str:build_date', build_date)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if error_id == self.VALUE_ERROR:
            raise ATSBadCallError(error_msg)
        self._build_date = build_date
        verbose_message(self._verbose, [f'build date {build_date}'])

    def is_not_none(self) -> bool:
        '''
            Check is ATS build date not None.

            :return: True (ATS build date is not None) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return self._build_date is not None
