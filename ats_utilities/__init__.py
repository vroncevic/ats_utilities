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
     Defined class VerboseRoot with attribute(s) and method(s).
     Created API for setup verbose class path from metaclass.
'''

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.5.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class VerboseRoot(type):
    '''
        Defined class VerboseRoot with attribute(s) and method(s).
        Created API for setup verbose class path from metaclass.
        It defines:

            :attributes:
                | ROOT_PACKAGE_NAME - root package name of framework.
            :methods:
                | __new__ - new constructor.
                | __str__ - str dunder method for VerboseRoot.
    '''

    ROOT_PACKAGE_NAME = 'ATS_UTILITIES'

    def __new__(cls, name, bases, dct):
        '''
            New constructor.

            :param name: class name.
            :type name: <str>
            :param bases: class bases.
            :type bases: <tuple>
            :param namespace: class namespace.
            :type namespace: <dict>
            :return: root class type.
            :rtype: <type>
            :exceptions: None
        '''
        root_type = type.__new__(cls, name, bases, dct)
        root_type_path = root_type.__module__.replace('.', '::')
        root_package = root_type_path.split('::')[0]
        if root_package.upper() == cls.ROOT_PACKAGE_NAME:
            root_type.VERBOSE = '{0}'.format(root_type_path)
        else:
            root_type.VERBOSE = cls.ROOT_PACKAGE_NAME
        return root_type

    def __str__(cls):
        '''
            Dunder str method for VerboseRoot.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ()'.format(cls.__name__)
