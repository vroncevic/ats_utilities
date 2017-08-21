# encoding: utf-8

from ats_utilities.text.stdout_text import ATS, DBG, RST

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

    VERBOSE = '[ATS_VERSION]'

    def __init__(self, version=None, verbose=False):
        """
        Initial version number of App/Tool/Script.
        :param version: App/Tool/Script version
        :type version: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2} [{3}]{4}".format(
                cls.VERBOSE, DBG, 'Initial version', version, RST
            )
            print(msg)
        self.__version = version

    def set_ats_version(self, version, verbose=False):
        """
        Setting version number of App/Tool/Script.
        :param version: App/Tool/Script version
        :type version: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2} [{3}]{4}".format(
                cls.VERBOSE, DBG, 'Setting version', version, RST
            )
            print(msg)
        self.__version = version

    def get_ats_version(self, verbose=False):
        """
        Getting version number of App/Tool/Script.
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return: App/Tool/Script version
        :rtype: str
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2} [{3}]{4}".format(
                cls.VERBOSE, DBG, 'Getting version', self.__version, RST
            )
            print(msg)
        return self.__version

    def __str__(self):
        """
        Return human readable string (ATSVersion).
        :return: String representation of ATSVersion
        :rtype: str
        """
        return "{0} version {1}".format(ATS, self.__version)

    def __repr__(self):
        """
        Return unambiguous string (ATSVersion).
        :return: String representation of ATSVersion
        :rtype: str
        """
        return "{0}(\'{1}\')".format(type(self).__name__, self.__version)
