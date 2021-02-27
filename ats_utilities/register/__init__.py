# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define class ATSRegister with attribute(s) and method(s).
     App/Tool/Script settings utilities, auto-register class.
'''

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSRegister(type):
    '''
        Define class ATSRegister with attribute(s) and method(s).
        App/Tool/Script settings utilities, auto-register class.
        It defines:

            :attributes:
                | registry - List of classes.
            :methods:
                | __init__ - Initial constructor.
                | __iter__ - Getting iterator of set.
                | __str__ - String representation of LogRegister.
    '''

    def __init__(cls, name, bases, nmspc):
        '''
            Initial constructor, register class.

            :param name: class name.
            :type name: <str>
            :param bases: Class bases.
            :type bases: <tuple>
            :param nmspc: Class namespace.
            :type nmspc: <dict>
            :exceptions: None
        '''
        super(ATSRegister, cls).__init__(name, bases, nmspc)
        if not hasattr(cls, 'registry'):
            cls.registry = set()
        cls.registry.add(cls)
        cls.registry -= set(bases)

    def __iter__(cls):
        '''
            Getting iterator of set.

            :return: Iterator of set.
            :rtype: <setiterator>
            :exceptions: None
        '''
        return iter(cls.registry)

    def __str__(cls):
        '''
            String representation of LogRegister.

            :return: Return human readable string (LogRegister).
            :rtype: <str>
            :exceptions: None
        '''
        if cls in cls.registry:
            return cls.__name__
        return '{0}{1}{2}'.format(
            cls.__name__, ': ', ', '.join([sc.__name__ for sc in cls])
        )
