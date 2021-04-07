# -*- coding: UTF-8 -*-

'''
 Module
     ats_name.py
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
     Defined class ATSName with attribute(s) and method(s).
     Created API for App/Tool/Script name in one propery object.
'''

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSName(object):
    '''
        Defined class ATSName with attribute(s) and method(s).
        Created API for App/Tool/Script name in one propery object.
        It defines:

            :attributes:
                | __name - App/Tool/Script name.
            :methods:
                | __init__ - Initial constructor.
                | name - Property methods for set/get operations.
                | is_not_none - Checking is App/Tool/Script name None.
                | __str__ - Dunder method for ATSName.
    '''

    def __init__(self):
        '''
            Initial constructor.

            :exceptions: None
        '''
        self.__name = None

    @property
    def name(self):
        '''
            Property method for getting App/Tool/Script name.

            :return: App/Tool/Script name | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.__name

    @name.setter
    def name(self, name):
        '''
            Property method for setting App/Tool/Script name.

            :param name: App/Tool/Script name.
            :type name: <str>
            :exceptions: None
        '''
        self.__name = name

    def is_not_none(self):
        '''
            Checking is App/Tool/Script name None.

            :return: True | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return True if self.__name is not None else False

    def __str__(self):
        '''
            Dunder method for ATSName.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(self.__class__.__name__, self.__name)
