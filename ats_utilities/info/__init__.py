# -*- coding: utf-8 -*-

'''
 Module
     __init__.py
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
     Defined class ATSInfo with attribute(s) and method(s).
     Created API for App/Tool/Script informations in one container object.
'''

import sys
from datetime import datetime

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.info.ats_name import ATSName
    from ats_utilities.info.ats_info_ok import ATSInfoOk
    from ats_utilities.info.ats_version import ATSVersion
    from ats_utilities.info.ats_licence import ATSLicence
    from ats_utilities.console_io.error import error_message
    from ats_utilities.info.ats_build_date import ATSBuildDate
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSInfo(ATSName, ATSVersion, ATSLicence, ATSBuildDate, ATSInfoOk):
    '''
        Defined class ATSInfo with attribute(s) and method(s).
        Created API for App/Tool/Script informations in one container object.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | ATS_NAME - ATS name key.
                | ATS_VERSION - ATS version key.
                | ATS_LICENCE - ATS licence key.
                | ATS_BUILD_DATE - ATS build date key.
                | ATS_BASE_INFO - ATS base information dict.
            :methods:
                | __init__ - Initial constructor.
                | show_base_info - Show ATS informations.
                | is_correct - Check information structure.
                | __str__ - Dunder method for ATSInfo.
    '''

    __slots__ = (
        'VERBOSE', 'ATS_NAME', 'ATS_VERSION', 'ATS_LICENCE',
        'ATS_BUILD_DATE', 'ATS_BASE_INFO', 'name', 'version',
        'licence', 'build_date', 'ats_info_ok'
    )
    VERBOSE = 'ATS_UTILITIES::INFO::ATS_INFO'
    ATS_NAME = 'ats_name'
    ATS_VERSION = 'ats_version'
    ATS_LICENCE = 'ats_licence'
    ATS_BUILD_DATE = 'ats_build_date'
    ATS_BASE_INFO = {
        1: ATS_NAME,
        2: ATS_VERSION,
        3: ATS_LICENCE,
        4: ATS_BUILD_DATE,
    }

    def __init__(self, info, verbose=False):
        '''
            Initial constructor.

            :param info: App/Tool/Script basic informations.
            :type info: <dict>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('dict:info', info)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        ATSName.__init__(self)
        ATSVersion.__init__(self)
        ATSLicence.__init__(self)
        ATSBuildDate.__init__(self)
        ATSInfoOk.__init__(self)
        if ATSInfo.is_correct(info, verbose=verbose):
            verbose_message(ATSInfo.VERBOSE, verbose, 'load ATS informations')
            self.name = info.get(ATSInfo.ATS_NAME)
            self.version = info.get(ATSInfo.ATS_VERSION)
            self.licence = info.get(ATSInfo.ATS_LICENCE)
            self.build_date = info.get(ATSInfo.ATS_BUILD_DATE)
            self.ats_info_ok = True

    def show_base_info(self):
        '''
            Show ATS informations.

            :exceptions: None
        '''
        if self.ats_info_ok:
            print(
                '\n{0} version {1} {2}'.format(
                    '[{0}]'.format(self.__name), self.__version,
                    datetime.now().date()
                )
            )

    @classmethod
    def is_correct(cls, informations, verbose=False):
        '''
            Check information structure.

            :param informations: ATS base informations.
            :type informations: <dict>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: True (correct information structure) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status, statuses = ATSChecker(), None, False, []
        error, status = checker.check_params(
            [('dict:informations', informations)]
        )
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        verbose_message(cls.VERBOSE, verbose, 'check ATS informations')
        for info_key in informations.keys():
            if info_key not in cls.ATS_BASE_INFO.values():
                message = '{0} [{1}]'.format('key not expected', info_key)
                error_message(cls.VERBOSE, message)
                statuses.append(False)
            else:
                statuses.append(True)
        status = all(statuses)
        return True if status else False

    def __str__(self):
        '''
            Dunder method for ATSInfo.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4}, {5})'.format(
            self.__class__.__name__, ATSName.__str__(self),
            ATSVersion.__str__(self), ATSLicence.__str__(self),
            ATSBuildDate.__str__(self), ATSInfoOk.__str__(self)
        )
