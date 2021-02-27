# -*- coding: UTF-8 -*-

'''
 Module
     ats_build_date.py
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
     Define class ATSBuildDate with attribute(s) and method(s).
     Keep App/Tool/Script build date in one property object.
'''

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSBuildDate(object):
    '''
        Define class ATSBuildDate with attribute(s) and method(s).
        Keep App/Tool/Script build date in one property object.
        It defines:

            :attributes:
                | __build_date - App/Tool/Script build date.
            :methods:
                | __init__ - Initial constructor.
                | build_date - Property methods for set/get operations.
    '''

    def __init__(self):
        '''
            Initial constructor.

            :exceptions: None
        '''
        self.__build_date = None

    @property
    def build_date(self):
        '''
            Property method for getting App/Tool/Script build date.

            :return: App/Tool/Script build date | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.__build_date

    @build_date.setter
    def build_date(self, build_date):
        '''
            Property method for setting App/Tool/Script build date.

            :param build_date: App/Tool/Script build date.
            :type build_date: <str>
            :exceptions: None
        '''
        self.__build_date = build_date
