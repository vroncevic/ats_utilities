# -*- coding: utf-8 -*-

try:
    from ats_utilities.text.stdout_text import ATS, DBG, RST
except ImportError as e:
    msg = "\n{0}\n".format(e)
    print(msg)
    exit(-1)  # Force close python module #####################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSBuildDate(object):
    """
    Define class ATSBuildDate with attribute(s) and method(s).
    Keep, set, get build date of App/Tool/Script.
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
            __build_date - Build date of App/Tool/Script
        method:
            __init__ - Initial constructor
            set_ats_build_date - Setting build date of App/Tool/Script
            get_ats_build_date - Getting build date of App/Tool/Script
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = '[ATS_BUILD_DATE]'

    def __init__(self, build_date=None, verbose=False):
        """
        Initial build date of App/Tool/Script.
        :param build_date: Build date of App/Tool/Script
        :type build_date: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2}{3}".format(
                cls.VERBOSE, DBG, 'Initial build date', RST
            )
            print(msg)
        self.__build_date = build_date

    def set_ats_build_date(self, build_date, verbose=False):
        """
        Setting build date of App/Tool/Script.
        :param build_date: Build date of App/Tool/Script
        :type build_date: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2} [{3}]{4}".format(
                cls.VERBOSE, DBG, 'Setting build date', build_date, RST
            )
            print(msg)
        self.__build_date = build_date

    def get_ats_build_date(self, verbose=False):
        """
        Getting build date of App/Tool/Script.
        :return: Build date of App/Tool/Script
        :rtype: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2} [{3}]{4}".format(
                cls.VERBOSE, DBG, 'Getting build date', self.__build_date, RST
            )
            print(msg)
        return self.__build_date

    def __str__(self):
        """
        Return human readable string (ATSBuildDate).
        :return: String representation of ATSBuildDate
        :rtype: str
        """
        return "{0} build date {1}".format(ATS, self.__build_date)

    def __repr__(self):
        """
        Return unambiguous string (ATSBuildDate).
        :return: String representation of ATSBuildDate
        :rtype: str
        """
        return "{0}(\'{1}\')".format(type(self).__name__, self.__build_date)
