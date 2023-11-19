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
    Defines class VerboseRoot with attribute(s) and method(s).
    Creates API for setup verbose class path from metaclass.
'''

from typing import Any, Dict, Tuple

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


def auto_str(mcs: Any) -> Any:
    '''
        Auto define class dunder method __str__.

        :return: Updated class for __str__ definition
        :rtype: <Any>
        :exceptions: None
    '''

    def __str__(self: Any) -> str:
        '''
            Return string representation of instance with members.

            :return: String representation of instance with members
            :rtype: <str>
            :exceptions: None
        '''
        return (
            f'{type(self).__name__}('
            f'{", ".join(f"{k}={v}" for k, v in self.__dict__.items())}'
            ')'
        )
    mcs.__str__ = __str__
    return mcs


@auto_str
class VerboseRoot(type):
    '''
        Defines class VerboseRoot with attribute(s) and method(s).
        Creates API for setup verbose class path with metaclass.
        This metaclass is designed to set a verbose attribute on
        classes; it creates based on the module path and a specified
        root package name. It conditionally formats this attribute
        to reflect the class's module path or a specified root
        package name.

        It defines:

            :attributes:
                | package_name - root package name of framework.
            :methods:
                | __new__ - New VerboseRoot constructor.
    '''

    package_name: str = 'ATS_UTILITIES'

    def __new__(
        mcs,
        name: str,
        bases: Tuple[type, ...],
        dct: Dict[Any, Any]
    ) -> type:
        '''
            New VerboseRoot constructor.

            :param mcs: Represents metaclass
            :type mcs: <Type[type]>
            :param name: Represents the name of the class being created
            :type name: <str>
            :param bases: Represents a tupple of base classes
            :type bases: <Tuple[Any, ...]>
            :param dct: Represents attributes and methods of class
            :type dct: <Dict[Any, Any]>
            :return: Created class type
            :rtype: <type>
            :exceptions: None
        '''
        module_path: str | None = dct.get('__module__')
        if module_path and module_path.startswith(mcs.package_name):
            dct['verbose'] = module_path.replace('.', '::')
        else:
            dct['verbose'] = mcs.package_name
        return super().__new__(mcs, name, bases, dct)
