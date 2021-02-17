# -*- coding: UTF-8 -*-

"""
 Module
     ats_name.py
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
     Define class ATSName with attribute(s) and method(s).
     Keep App/Tool/Script name in one propery object.
"""

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSName(object):
    """
        Define class ATSName with attribute(s) and method(s).
        Keep App/Tool/Script name in one propery object.
        It defines:

            :attributes:
                | __name - App/Tool/Script name.
            :methods:
                | __init__ - Initial constructor.
                | name - Property methods for set/get operations.
    """

    def __init__(self):
        """
            Initial constructor.

            :exceptions: None
        """
        self.__name = None

    @property
    def name(self):
        """
            Property method for getting App/Tool/Script name.

            :return: App/Tool/Script name | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
            Property method for setting App/Tool/Script name.

            :param name: App/Tool/Script name.
            :type name: <str>
            :exceptions: None
        """
        self.__name = name
