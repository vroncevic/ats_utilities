# -*- coding: utf-8 -*-

import sys

try:
    from ats_utilities.text import COut
    from ats_utilities.text.stdout_text import ATS
except ImportError as e:
    msg = "\n{0}\n".format(e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSVersion(object):
    """
    Define class ATSVersion with attribute(s) and method(s).
    Keep, set, get version number of App/Tool/Script.
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
            __version - Version number of App/Tool/Script
        method:
            __init__ - Initial constructor
            set_ats_version - Setting version number of App/Tool/Script
            get_ats_version - Getting version number of App/Tool/Script
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = 'ATS_VERSION'

    def __init__(self, version=None, verbose=False):
        """
        Initial version number of App/Tool/Script.
        :param version: App/Tool/Script version | None
        :type version: <str> | <NoneType>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        cls, cout = self.__class__, COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0} [{1}]".format('Initial version', version)
        COut.print_console_msg(msg, verbose=verbose)
        self.__version = version

    def set_ats_version(self, version, verbose=False):
        """
        Setting version number of App/Tool/Script.
        :param version: App/Tool/Script version
        :type version: <str>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        msg = "{0} [{1}]".format('Setting version', version)
        COut.print_console_msg(msg, verbose=verbose)
        self.__version = version

    def get_ats_version(self, verbose=False):
        """
        Getting version number of App/Tool/Script.
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: App/Tool/Script version | None
        :rtype: <str> | <NoneType>
        """
        msg = "{0} [{1}]".format('Getting version', self.__version)
        COut.print_console_msg(msg, verbose=verbose)
        return self.__version

    def __str__(self):
        """
        Return human readable string (ATSVersion).
        :return: String representation of ATSVersion
        :rtype: <str>
        """
        return "{0} version {1}".format(ATS, self.__version)

    def __repr__(self):
        """
        Return unambiguous string (ATSVersion).
        :return: String representation of ATSVersion
        :rtype: <str>
        """
        return "{0}(\'{1}\')".format(type(self).__name__, self.__version)
