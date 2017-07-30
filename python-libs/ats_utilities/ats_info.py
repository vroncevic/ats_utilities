# encoding: utf-8

from ats_utilities.ats_name import ATSName
from ats_utilities.ats_version import ATSVersion
from ats_utilities.ats_build_date import ATSBuildDate
from ats_utilities.ats_license import ATSLicense
from ats_utilities.config.check_base_config import CheckBaseConfig
from ats_utilities.error.lookup_error import AppError

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSInfo(ATSName, ATSVersion, ATSBuildDate, ATSLicense):
    """
    Define class ATSInfo with attribute(s) and method(s).
    Keep App/Tool/Script information in one object.
    It defines:
        attribute:
            VERBOSE - Verbose prefix text
        method:
            __init__ - Initial constructor
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = '[ATS_INFO]'

    def __init__(self, info, verbose=False):
        """
        Setting container info for App/Tool/Script.
        :param info: App/Tool/Script basic info
        :type: dict
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        try:
            if CheckBaseConfig.now(info, verbose):
                ATSName.__init__(self, info['app_name'], verbose)
                ATSVersion.__init__(self, info['app_version'], verbose)
                ATSBuildDate.__init__(self, info['app_build_date'], verbose)
                ATSLicense.__init__(self, info['app_license'], verbose)
            else:
                msg = 'wrong App/Tool/Script info structure!'
                raise AppError(msg)
        except AppError as e:
            print("Error: ", e)

    def __str__(self):
        """
        Return human readable string (ATSInfo).
        :return: String representation of ATSInfo
        :rtype: str
        """
        ats_name = self.get_name()
        ats_version = self.get_version()
        ats_build_date = self.get_build_date()
        ats_license = self.get_license()
        return "App/Tool/Script info {0} {1} {2} {3}".format(
            ats_name, ats_version, ats_build_date, ats_license
        )

    def __repr__(self):
        """
        Return unambiguous string (ATSInfo).
        :return: String representation of ATSInfo
        :rtype: str
        """
        return "{0}(info)".format(type(self).__name__)
