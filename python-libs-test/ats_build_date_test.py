# -*- coding: UTF-8 -*-
# ats_build_date_test.py
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

    from ats_utilities.ats_build_date import ATSBuildDate
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


class TestATSBuildDate(TestCase):

    def test_initial(self):
        abd = ATSBuildDate('02-Apr-2018')
        self.assertTrue(type(abd.get_ats_build_date()) is str)
        self.assertTrue(issubclass(ATSBuildDate, object))

    def test_getter(self):
        abd = ATSBuildDate('01-Apr-2018')
        self.assertTrue(abd.get_ats_build_date() == '01-Apr-2018')

    def test_setter(self):
        abd = ATSBuildDate('')
        self.assertFalse(abd.get_ats_build_date() == '123')
        abd.set_ats_build_date('03-Apr-2018')
        self.assertTrue(abd.get_ats_build_date() == '03-Apr-2018')


if __name__ == '__main__':
    main()
