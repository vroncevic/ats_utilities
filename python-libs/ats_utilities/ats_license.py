# encoding: utf-8

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
            VERBOSE - Verbose prefix text
            __license - Text with license
        method:
            __init__ - Initial constructor
            set_license - Setting App/Tool/Script text license
            get_license - Getting App/Tool/Script text license
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = '[ATS_LICENSE]'

    def __init__(self, txt_license=None, verbose=False):
        """
        Initial text license of App/Tool/Script.
        :param txt_license: App/Tool/Script text license
        :type: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        if verbose:
            msg = ATSLicense.VERBOSE
            print(msg)
        self.__license = txt_license

    def set_license(self, txt_license):
        """
        Setting text license of App/Tool/Script.
        :param txt_license: App/Tool/Script text license
        :type: str
        """
        self.__license = txt_license

    def get_license(self):
        """
        Getting text license of App/Tool/Script.
        :return: App/Tool/Script text license
        :rtype: str
        """
        return self.__license

    def __str__(self):
        """
        Return human readable string (ATSLicense).
        :return: String representation of ATSLicense
        :rtype: str
        """
        ats_license = self.get_license()
        return "App/Tool/Script license {0}".format(ats_license)

    def __repr__(self):
        """
        Return unambiguous string (ATSLicense).
        :return: String representation of ATSLicense
        :rtype: str
        """
        ats_license = self.get_license()
        return "{0}(\'{1}\')".format(type(self).__name__, ats_license)
