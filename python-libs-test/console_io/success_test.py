# -*- coding: UTF-8 -*-

"""
 Module
     success_test.py
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
     Define class TestATSSuccess with attribute(s) and method(s).
     Test TestATSSuccess attributes.
"""

import sys

try:
    from unittest import TestCase, main
    from colorama import Fore

    from ats_utilities import ATSRegister
    from ats_utilities.console_io import ATSConsoleIO
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.console_io.success import ATSSuccess, success_message
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE) # Force close python ATS ###############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestATSSuccess(TestCase):
    """
        Define class TestATSSuccess with attribute(s) and method(s).
        Test TestATSSuccess attributes.
        It defines:
            attribute:
                None
            method:
                test_initial - Initial test
                test_success_message_bad_call - Test bad call
                test_success_message_type_error - Test error message
    """

    def test_initial(self):
        atss = ATSSuccess()
        atss.message = "Simple success message"
        clone_of_message = "{0}{1}{2}".format(
            Fore.GREEN, "Simple success message", Fore.RESET
        )
        self.assertTrue(type(atss.message) is str)
        self.assertFalse(issubclass(ATSSuccess, ATSRegister))
        self.assertTrue(issubclass(ATSSuccess, ATSConsoleIO))
        self.assertTrue(ATSSuccess in ATSConsoleIO)
        self.assertFalse(atss.message == "Simple success message")
        self.assertTrue(atss.message == clone_of_message)

    def test_success_message_bad_call(self):
        with self.assertRaises(ATSBadCallError):
            # Missing second argument
            success_message('[SIMPLE_TOOL]')

    def test_success_message_type_error(self):
        with self.assertRaises(ATSTypeError):
            # Wrong type of first argument
            success_message(1200, 1, 2, 3)


if __name__ == '__main__':
    main()
