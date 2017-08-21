# encoding: utf-8

from ats_utilities.ats_name import ATSName
from ats_utilities.ats_version import ATSVersion
from ats_utilities.ats_build_date import ATSBuildDate
from ats_utilities.ats_license import ATSLicense
from ats_utilities.config.check_base_config import CheckBaseConfig
from ats_utilities.error.ats_value_error import ATSValueError
from ats_utilities.text.stdout_text import ATS, DBG, ERR, RST

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
    Keep App/Tool/Script information in one container object.
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
        method:
            __init__ - Initial constructor
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = '[ATS_INFO]'

    def __init__(self, info, verbose=False):
        """
        Setting container info for App/Tool/Script.
        :param info: App/Tool/Script basic information
        :type info: dict
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2}{3}".format(
                cls.VERBOSE, DBG, 'Setting info structure', RST
            )
            print(msg)
        check_config = CheckBaseConfig.is_correct(info, verbose)
        is_dict = isinstance(info, dict)
        if check_config and is_dict:
            app_name = info.get('app_name')
            ATSName.__init__(self, app_name, verbose)
            app_version = info.get('app_version')
            ATSVersion.__init__(self, app_version, verbose)
            app_build_date = info.get('app_build_date')
            ATSBuildDate.__init__(self, app_build_date, verbose)
            app_license = info.get('app_license')
            ATSLicense.__init__(self, app_license, verbose)
        else:
            msg = "{0} {1}{2} {3} [{4}]{5}".format(
                cls.VERBOSE, ERR, ATS, 'wrong info structure', type(info), RST
            )
            raise ATSValueError(msg)

    def __str__(self):
        """
        Return human readable string (ATSInfo).
        :return: String representation of ATSInfo
        :rtype: str
        """
        ats_name = self.get_ats_name()
        ats_version = self.get_ats_version()
        ats_build_date = self.get_ats_build_date()
        ats_license = self.get_ats_license()
        return "{0} info \n{1} \n{2} \n{3} \n{4}".format(
            ATS, ats_name, ats_version, ats_build_date, ats_license
        )

    def __repr__(self):
        """
        Return unambiguous string (ATSInfo).
        :return: String representation of ATSInfo
        :rtype: str
        """
        return "{0}(info)".format(type(self).__name__)
