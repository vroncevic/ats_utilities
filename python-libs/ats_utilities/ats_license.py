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

    VERBOSE = '[ATS_LICENSE]'

    def __init__(self, txt_license=None, verbose=False):
        """
        Initial text license of App/Tool/Script.
        :param txt_license: App/Tool/Script text license
        :type txt_license: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2}\n{3}{4}".format(
                cls.VERBOSE, DBG, 'Initial license', txt_license, RST
            )
            print(msg)
        self.__license = txt_license

    def set_ats_license(self, txt_license, verbose=False):
        """
        Setting text license of App/Tool/Script.
        :param txt_license: App/Tool/Script text license
        :type txt_license: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2}\n{3}{4}".format(
                cls.VERBOSE, DBG, 'Setting license', txt_license, RST
            )
            print(msg)
        self.__license = txt_license

    def get_ats_license(self, verbose=False):
        """
        Getting text license of App/Tool/Script.
        :return: App/Tool/Script text license
        :rtype: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return: License text
        :rtype: str
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2}\n{3}{4}".format(
                cls.VERBOSE, DBG, 'Getting license', self.__license, RST
            )
            print(msg)
        return self.__license

    def __str__(self):
        """
        Return human readable string (ATSLicense).
        :return: String representation of ATSLicense
        :rtype: str
        """
        return "{0} license {1}".format(ATS, self.__license)

    def __repr__(self):
        """
        Return unambiguous string (ATSLicense).
        :return: String representation of ATSLicense
        :rtype: str
        """
        return "{0}(\'{1}\')".format(type(self).__name__, self.__license)