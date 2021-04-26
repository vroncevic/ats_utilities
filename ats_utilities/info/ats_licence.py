# -*- coding: UTF-8 -*-

'''
 Module
     ats_licence.py
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
     Defined class ATSLicence with attribute(s) and method(s).
     Created API for App/Tool/Script licence in one property object.
'''

import sys

try:
    from ats_utilities import VerboseRoot
    from ats_utilities.checker import ATSChecker
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
__version__ = '1.7.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLicence:
    '''
        Defined class ATSLicence with attribute(s) and method(s).
        Created API for App/Tool/Script licence in one property object.
        It defines:

            :attributes:
                | __metaclass__ - Setting verbose root for ATSLicence.
                | __verbose - Enable/disable verbose option.
                | __licence - App/Tool/Script licence.
            :methods:
                | __init__ - Initial constructor.
                | name - Property methods for set/get operations.
                | is_not_none - Checking is App/Tool/Script licence None.
                | __str__ - Dunder method for ATSLicence.
    '''

    __metaclass__ = VerboseRoot

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__verbose = verbose
        self.__licence = None

    @property
    def licence(self):
        '''
            Property method for getting App/Tool/Script licence.

            :return: App/Tool/Script licence | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.__licence

    @licence.setter
    def licence(self, licence):
        '''
            Property method for setting App/Tool/Script licence.

            :param licence: App/Tool/Script licence.
            :type licence: <str>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('str:licence', licence)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        self.__licence = licence
        verbose_message(ATSLicence.VERBOSE, self.__verbose, licence)

    def is_not_none(self):
        '''
            Checking is App/Tool/Script licence None.

            :return: True | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return bool(self.__licence)

    def __str__(self):
        '''
            Dunder method for ATSLicence.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, str(self.__verbose), self.__licence
        )
