# -*- coding: UTF-8 -*-

'''
Module
    story_factory_context_bundle.py.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class MyClass with attribute(s) and method(s).
    Creates an API for the ATS version in one property object.
'''

from abc import ABC, abstractmethod
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.registry import ContextRegistry
from ats_utilities.context.icontext_support import IContextSupport
from ats_utilities.context.context_support import ContextSupport
from ats_utilities.utils.reflection import to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IMyClass(IContextSupport, ABC):
    '''
        Defines class MyClass with attribute(s) and method(s).
        Creates an API for the instance.

        It defines:

            :methods:
                | not_none - Checks is attribute not None.
                | __str__ - Returns the string representation of instance.
    '''

    @abstractmethod
    def not_none(self) -> bool:
        '''
            Checks is attribute not None.

            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: TypeError
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of instance.

            :return: The instance as string representation
            :rtype: <str>
            :exceptions: TypeError
        '''
        pass


class MyClass(IMyClass, ContextSupport):
    '''
        Defines class MyClass with attribute(s) and method(s).
        Creates an API for the instance.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | my - Test attribute (default None).
            :methods:
                | __init__ - Initials MyClass constructor.
                | not_none - Checks is attribute not None.
                | __str__ - Returns the string representation of MyClass.
    '''

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initials MyClass constructor.

            :param context_bundle: Bundle with checker, reporter and verbose | None
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        ContextSupport.__init__(self, context_bundle)
        self.my: str | None = None

    def not_none(self) -> bool:
        '''
            Checks is attribute not None.

            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        return self.my is not None

    def __str__(self) -> str:
        '''
            Returns the string representation of the MyClass.

            :return: The MyClass instance as string representation
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)

obj: IMyClass | None = None

context_bundle: ContextBundle = ContextRegistry.create_default_context_bundle()
obj = MyClass(context_bundle=context_bundle)
print(obj)
print(obj.not_none())
obj.my = "myvalue"
print(obj.not_none())
print(50 * '=')
