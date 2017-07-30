# encoding: utf-8

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSName(object):
    """
    Define class ATSName with attribute(s) and method(s).
    Keep, set, get App/Tool/Script name.
    It defines:
        attribute:
            VERBOSE - Verbose prefix text
            __program_name - Name of App/Tool/Script
        method:
            __init__ - Initial constructor
            set_name - Setting program name of App/Tool/Script
            get_name - Getting program name of App/Tool/Script
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = '[ATS_NAME]'

    def __init__(self, program_name=None, verbose=False):
        """
        Initial program name of App/Tool/Script.
        :param program_name: App/Tool/Script name
        :type: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        if verbose:
            msg = ATSName.VERBOSE
            print(msg)
        self.__program_name = program_name

    def set_name(self, program_name):
        """
        Setting program name of App/Tool/Script.
        :param program_name: App/Tool/Script name
        :type: str
        """
        self.__program_name = program_name

    def get_name(self):
        """
        Getting program name of App/Tool/Script.
        :return: App/Tool/Script name
        :rtype: str
        """
        return self.__program_name

    def __str__(self):
        """
        Return human readable string (ATSName).
        :return: String representation of ATSName
        :rtype: str
        """
        ats_name = self.get_name()
        return "App/Tool/Script name {0}".format(ats_name)

    def __repr__(self):
        """
        Return unambiguous string (ATSName).
        :return: String representation of ATSName
        :rtype: str
        """
        ats_name = self.get_name()
        return "{0}(\'{1}\')".format(type(self).__name__, ats_name)
