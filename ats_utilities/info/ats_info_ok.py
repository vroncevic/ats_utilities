# -*- coding: UTF-8 -*-

"""
 Module
     ats_info_ok.py
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
     Define class ATSInfoOk with attribute(s) and method(s).
     Keep App/Tool/Script information status in one property object.
"""

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSInfoOk(object):
    """
        Define class ATSInfoOk with attribute(s) and method(s).
        Keep App/Tool/Script information status in one property object.
        It defines:

            :attributes:
                | __ats_info_ok - App/Tool/Script information status.
            :methods:
                | __init__ - Initial constructor.
                | ats_info_ok - Property methods for set/get operations.
    """

    def __init__(self):
       """
            Initial constructor.

            :exceptions: None
       """
       self.__ats_info_ok = True

    @property
    def ats_info_ok(self):
        """
            Property method for getting App/Tool/Script information status.

            :return: App/Tool/Script information status | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        """
        return self.__ats_info_ok

    @ats_info_ok.setter
    def ats_info_ok(self, ats_info_ok):
        """
            Property method for setting App/Tool/Script information status.

            :param ats_info_ok: App/Tool/Script information status.
            :type ats_info_ok: <str>
            :exceptions: None
        """
        self.__ats_info_ok = ats_info_ok
