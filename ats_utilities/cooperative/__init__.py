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
     Defined class CooperativeMeta with attribute(s) and method(s).
     Created cooperative mechanism for multi-inheritance.
'''

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.5.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CooperativeMeta(type):
    '''
        Defined class CooperativeMeta with attribute(s) and method(s).
        Created cooperative mechanism for multi-inheritance.
        It defines:

            :attributes:
                | combined_metas - combined metaclasses in form of dictionary.
            :methods:
                | __new__ - new constructor.
                | __init__ - initial constructor.
                | __str__ - str dunder method for CooperativeMeta.
    '''

    def __new__(cls, name, bases, members):
        '''
            New constructor.

            :param method_to_abstract: method object-reference.
            :type method_to_abstract: <function>
            :exceptions: None
        '''
        metas = [type(base) for base in bases]
        metas = [
            meta for index, meta in enumerate(metas)
            if not [later for later in metas[index+1:]
                    if issubclass(later, meta)]
        ]
        meta = type(name, tuple(metas), dict(combined_metas=metas))
        return meta(name, bases, members)

    def __init__(self, name, bases, members):
        '''
            Initial constructor.

            :param method_to_abstract: method object-reference.
            :type method_to_abstract: <function>
            :exceptions: None
        '''
        for meta in self.combined_metas:
            meta.__init__(self, name, bases, members)

    def __str__(cls):
        '''
            Dunder str method for CooperativeMeta.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ()'.format(cls.__name__)
