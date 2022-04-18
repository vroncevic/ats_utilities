# -*- coding: UTF-8 -*-

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
     Defined class Singleton with attribute(s) and method(s).
     Created API for auto-register singleton object.
'''

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.5.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Singleton:
    '''
        Defined class Singleton with attribute(s) and method(s).
        Created API for auto-register singleton object.
        It defines:

            :attributes:
                | __INSTANCES - class dictionary for collecting instances.
            :methods:
                | __new__ - set class instance.
                | __str__ - str dunder method for Singleton.
    '''

    __INSTANCE = None

    def __new__(class_, *args, **kwargs):
        '''
            Set class instance.

            :param *args: iteration object.
            :type *args: <iter>
            :param **kwargs: iteration object.
            :type **kwargs: <dict>
            :return: python object instance.
            :rtype: <Python Object>
            :exceptions: None
        '''
        if not isinstance(class_.__INSTANCE, class_):
            class_.__INSTANCE = object.__new__(class_, *args, **kwargs)
        return class_.__INSTANCE

    def __str__(self):
        '''
            Dunder str method for Singleton.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ()'.format(self.__name__)
