# -*- coding: UTF-8 -*-

"""
 Module
     ats_info_test.py
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
     Define class TestATSInfo with attribute(s) and method(s).
     Test ATSInfo attributes.
"""

import sys

try:
    from unittest import TestCase, main

    from ats_utilities.ats_info import ATSInfo
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestATSInfo(TestCase):
    """
        Define class TestATSInfo with attribute(s) and method(s).
        Test ATSInfo attributes.
        It defines:
            attribute:
                None
            method:
                test_initial - Initial test
    """

    def test_initial(self):
        info = {
            'ats_name': 'Simple Test',
            'ats_version': 'ver.1.0',
            'ats_build_date': '10-Apr-2018',
            'ats_license': 'GPLv3'
        }
        ats = ATSInfo(info)
        self.assertTrue(ats.is_ats_info_ok())


if __name__ == '__main__':
    main()
