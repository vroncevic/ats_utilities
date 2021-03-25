# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
 Copyright
     Copyright (C) 2019 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class ATSConsoleIO with attribute(s) and method(s).
     Created glue-metaclass API console log mechanism.
'''

import sys

try:
    from ats_utilities.register import ATSRegister
except ImportError as ATS_ERROR_MESSAGE:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ATS_ERROR_MESSAGE)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/master/LICENSE'
__version__ = '1.5.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSConsoleIO(object):
    '''
        Defined class ATSConsoleIO with attribute(s) and method(s).
        Created glue-metaclass API console log mechanism.

            | * Success messages (Colorize text to green).
            | * Verbose messages (Colorize text to blue).
            | * Warning messages (Colorize text to yellow).
            | * Error messages (Colorize text to red).

        It defines:

            :attributes:
                | __metaclass__ - Setting metaclass.
            :methods:
                | __str__ - Dunder method for object ATSConsoleIO.
    '''
    __metaclass__ = ATSRegister

    def __str__(self):
        '''
            Dunder method for object ATSConsoleIO.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0}'.format(self.__class__.__name__)
