# -*- coding: UTF-8 -*-
# ats_version_test.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# ats_utilities is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ats_utilities is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys

try:
    from unittest import TestCase, main

    from ats_utilities.ats_version import ATSVersion
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python Test Case #############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestATSVersion(TestCase):

    def test_initial(self):
        al = ATSVersion('1.0')
        self.assertTrue(type(al.get_ats_version()) is str)
        self.assertTrue(issubclass(ATSVersion, object))

    def test_getter(self):
        al = ATSVersion('ver.1.0')
        self.assertTrue(al.get_ats_version() == 'ver.1.0')

    def test_setter(self):
        al = ATSVersion('')
        self.assertFalse(al.get_ats_version() == '123')
        al.set_ats_version('Apache 2.0')
        self.assertTrue(al.get_ats_version() == 'Apache 2.0')


if __name__ == '__main__':
    main()
