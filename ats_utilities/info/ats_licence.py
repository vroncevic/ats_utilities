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

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/master/LICENSE'
__version__ = '1.5.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLicence(object):
    '''
        Defined class ATSLicence with attribute(s) and method(s).
        Created API for App/Tool/Script licence in one property object.
        It defines:

            :attributes:
                | __licence - App/Tool/Script licence.
            :methods:
                | __init__ - Initial constructor.
                | name - Property methods for set/get operations.
                | is_not_none - Checking is App/Tool/Script licence None.
                | __str__ - Dunder method for ATSLicence.
    '''

    def __init__(self):
        '''
            Initial constructor.

            :exceptions: None
        '''
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
            :exceptions: None
        '''
        self.__licence = licence

    def is_not_none(self):
        '''
            Checking is App/Tool/Script licence None.

            :return: True | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return True if self.__licence is not None else False

    def __str__(self):
        '''
            Dunder method for ATSLicence.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(self.__class__.__name__, self.__licence)
