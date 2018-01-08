# -*- coding: UTF-8 -*-
# ats_license.py
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
    from ats_utilities.text import COut
    from ats_utilities.text.stdout_text import ATS
except ImportError as e:
    msg = "\n{0}\n".format(e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLicense(object):
    """
    Define class ATSLicense with attribute(s) and method(s).
    Keep, set, get text license of App/Tool/Script.
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
            __license - Text with license
        method:
            __init__ - Initial constructor
            set_ats_license - Setting App/Tool/Script text license
            get_ats_license - Getting App/Tool/Script text license
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = 'ATS_LICENSE'

    def __init__(self, txt_license=None, verbose=False):
        """
        Initial text license of App/Tool/Script.
        :param txt_license: App/Tool/Script text license | None
        :type txt_license: <str> | <NoneType>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        cls, cout = self.__class__, COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}\n{1}".format('Initial license', txt_license)
        COut.print_console_msg(msg, verbose=verbose)
        self.__license = txt_license

    def set_ats_license(self, txt_license, verbose=False):
        """
        Setting text license of App/Tool/Script.
        :param txt_license: App/Tool/Script text license
        :type txt_license: <str>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        msg = "{0}\n{1}".format('Setting license', txt_license)
        COut.print_console_msg(msg, verbose=verbose)
        self.__license = txt_license

    def get_ats_license(self, verbose=False):
        """
        Getting text license of App/Tool/Script.
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: App/Tool/Script license text | None
        :rtype: <str> | <NoneType>
        """
        msg = "{0}\n{1}".format('Getting license', self.__license)
        COut.print_console_msg(msg, verbose=verbose)
        return self.__license

    def __str__(self):
        """
        Return human readable string (ATSLicense).
        :return: String representation of ATSLicense
        :rtype: <str>
        """
        return "{0} license {1}".format(ATS, self.__license)

    def __repr__(self):
        """
        Return unambiguous string (ATSLicense).
        :return: String representation of ATSLicense
        :rtype: <str>
        """
        return "{0}(\'{1}\')".format(type(self).__name__, self.__license)
