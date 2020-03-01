# -*- coding: UTF-8 -*-

"""
 Module
     warning_test.py
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
     Define class TestATSWarning with attribute(s) and method(s).
     Test TestATSWarning attributes.
"""

import sys

try:
    from unittest import TestCase, main
    from colorama import Fore

    from ats_utilities import ATSRegister
    from ats_utilities.console_io import ATSConsoleIO
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.console_io.warning import ATSWarning, warning_message
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


class TestATSWarning(TestCase):
    """
        Define class TestATSWarning with attribute(s) and method(s).
        Test TestATSWarning attributes.
        It defines:
            attribute:
                None
            method:
                test_initial - Initial test
                test_warning_message_bad_call - Test bad call
                test_warning_message_type_error - Test error message
    """

    def test_initial(self):
        atsw = ATSWarning()
        atsw.message = "Simple warning message"
        clone_of_message = "{0}{1}{2}".format(
            Fore.YELLOW, "Simple warning message", Fore.RESET
        )
        self.assertTrue(type(atsw.message) is str)
        self.assertFalse(issubclass(ATSWarning, ATSRegister))
        self.assertTrue(issubclass(ATSWarning, ATSConsoleIO))
        self.assertTrue(ATSWarning in ATSConsoleIO)
        self.assertFalse(atsw.message == "Simple warning message")
        self.assertTrue(atsw.message == clone_of_message)

    def test_warning_message_bad_call(self):
        with self.assertRaises(ATSBadCallError):
            warning_message('[SIMPLE_TOOL]')

    def test_warning_message_type_error(self):
        with self.assertRaises(ATSTypeError):
            warning_message(2, 1, 12212, 1212, 143134)


if __name__ == '__main__':
    main()
