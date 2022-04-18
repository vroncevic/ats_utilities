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
     Defined class ATSRegister with attribute(s) and method(s).
     Created API for App/Tool/Script utilities, auto-register class.
'''

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.5.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSRegister(type):
    '''
        Defined class ATSRegister with attribute(s) and method(s).
        Created API for App/Tool/Script utilities, auto-register class.
        It defines:

            :attributes:
                | registry - set of classes.
            :methods:
                | __init__ - initial constructor.
                | __iter__ - getting iterator of set.
                | __str__ - str dunder method for ATSRegister.
    '''

    def __init__(cls, name, bases, namespace):
        '''
            Initial constructor.

            :param name: class name.
            :type name: <str>
            :param bases: class bases.
            :type bases: <tuple>
            :param namespace: class namespace.
            :type namespace: <dict>
            :exceptions: None
        '''
        super(ATSRegister, cls).__init__(name, bases, namespace)
        if not hasattr(cls, 'registry'):
            cls.registry = set()
        cls.registry.add(cls)
        cls.registry -= set(bases)

    def __iter__(cls):
        '''
            Getting iterator of set.

            :return: iterator of set.
            :rtype: <setiterator>
            :exceptions: None
        '''
        return iter(cls.registry)

    def __str__(cls):
        '''
            Dunder str method for ATSRegister.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        if cls in cls.registry:
            return cls.__name__
        return '{0} ({1})'.format(
            cls.__name__, ', '.join([
                reg_class.__name__ for reg_class in cls.registry
            ])
        )
