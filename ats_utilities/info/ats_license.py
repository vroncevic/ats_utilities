# -*- coding: UTF-8 -*-

"""
 Module
     ats_license.py
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
     Define class ATSLicense with attribute(s) and method(s).
     Keep App/Tool/Script license in one property object.
"""

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.2.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLicense(object):
    """
        Define class ATSLicense with attribute(s) and method(s).
        Keep App/Tool/Script license in one property object.
        It defines:

            :attributes:
                | __license - App/Tool/Script license.
            :methods:
                | __init__ - Initial constructor.
                | name - Property methods for set/get operations.
    """

    def __init__(self):
        """
            Initial constructor.

            :exceptions: None
        """
        self.__license = None

    @property
    def license(self):
        """
            Property method for getting App/Tool/Script license.

            :return: App/Tool/Script license | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        """
        return self.__license

    @license.setter
    def license(self, license):
        """
            Property method for setting App/Tool/Script license.

            :param license: App/Tool/Script license.
            :type license: <str>
            :exceptions: None
        """
        self.__license = license
