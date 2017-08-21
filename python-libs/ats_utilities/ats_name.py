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


class ATSName(object):
    """
    Define class ATSName with attribute(s) and method(s).
    Keep, set, get App/Tool/Script name.
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
            __program_name - Name of App/Tool/Script
        method:
            __init__ - Initial constructor
            set_ats_name - Setting name of App/Tool/Script
            get_ats_name - Getting name of App/Tool/Script
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = '[ATS_NAME]'

    def __init__(self, program_name=None, verbose=False):
        """
        Initial name of App/Tool/Script.
        :param program_name: App/Tool/Script name
        :type program_name: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2} [{2}]{4}".format(
                cls.VERBOSE, DBG, 'Initial program name', program_name, RST
            )
            print(msg)
        self.__program_name = program_name

    def set_ats_name(self, program_name, verbose=False):
        """
        Setting name of App/Tool/Script.
        :param program_name: App/Tool/Script name
        :type program_name: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2} [{3}]{4}".format(
                cls.VERBOSE, DBG, 'Setting program name', program_name, RST
            )
            print(msg)
        self.__program_name = program_name

    def get_ats_name(self, verbose=False):
        """
        Getting name of App/Tool/Script.
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return: App/Tool/Script name
        :rtype: str
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2} [{3}]{4}".format(
                cls.VERBOSE, DBG, 'Getting program name',
                self.__program_name, RST
            )
            print(msg)
        return self.__program_name

    def __str__(self):
        """
        Return human readable string (ATSName).
        :return: String representation of ATSName
        :rtype: str
        """
        return "{0} name {1}".format(ATS, self.__program_name)

    def __repr__(self):
        """
        Return unambiguous string (ATSName).
        :return: String representation of ATSName
        :rtype: str
        """
        return "{0}(\'{1}\')".format(type(self).__name__, self.__program_name)
