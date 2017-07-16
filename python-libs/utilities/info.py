# encoding: utf-8

from utilities.name import AppName
from utilities.version import AppVersion
from utilities.build_date import BuildDate
from utilities.license import AppLicense
from utilities.config.check_base_config import CheckBaseConfig
from utilities.error.lookup_error import AppError

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class AppInfo(AppName, AppVersion, BuildDate, AppLicense):
    """
    Define class AppInfo with attribute(s) and method(s).
    Keep App/Tool/Script information in one object.
    It defines:
        attribute:
            None
        method:
            __init__ - Initial constructor
    """

    def __init__(self, info):
        """
        Setting container info for App/Tool/Script.
        :param info: App/Tool/Script basic info
        :type: dict
        """
        try:
            if CheckBaseConfig.now(info):
                AppName.__init__(self, info['app_name'])
                AppVersion.__init__(self, info['app_version'])
                BuildDate.__init__(self, info['app_build_date'])
                AppLicense.__init__(self, info['app_license'])
            else:
                msg = 'wrong App info structure!'
                raise AppError(msg)
        except AppError as e:
            print("Error: ", e)
