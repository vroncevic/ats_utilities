# encoding: utf-8

from abc import ABCMeta, abstractmethod
from app.info import AppInfo
from app.cfg_settings import Settings
from app.option.option_parser import AppOptionParser
from app.configuration.check_base_config import CheckBaseConfig
from app.error.lookup_error import AppError

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CfgBase(AppInfo, Settings, AppOptionParser):
    """
    Define class CfgBase with attribute(s) and method(s).
    Load a settings, create a CL interface and run operation.
    It defines:
        attribute:
            __tool_operational - Control operational flag
        method:
            __init__ - Initial constructor
            add_new_option - Adding new option for CL interface
            get_tool_status - Getting tool status
            process - Process and run tool operation (Abstract method)
    """

    __metaclass__ = ABCMeta

    def __init__(self, base_config_file):
        """
        Setting version, build date, name and license of App/Tool/Script.
        :param base_config_file: Configuration file path
        :type: str
        """
        Settings.__init__(self, base_config_file)
        self.__tool_operational = False
        try:
            configuration = self.get_configuration()
            check_configuration = CheckBaseConfig.now(configuration)
            if configuration and check_configuration:
                AppInfo.__init__(self, configuration)
                tool_version = self.get_version()
                tool_build_date = self.get_build_date()
                tool_info = "{0} {1}".format(tool_version, tool_build_date)
                tool_name = self.get_name()
                tool_lic = self.get_license()
                AppOptionParser.__init__(self, tool_info, tool_name, tool_lic)
                self.__tool_operational = True
            else:
                msg = 'wrong configuration base structure!'
                raise AppError(msg)
        except AppError as e:
            print("Error: ", e)

    def add_new_option(self, *args, **kwargs):
        """
        Adding new option for CL interface.
        :param args: Arguments
        :type: Python object(s)
        :param kwargs: Options and texts
        :type: Python object(s)
        """
        self.add_operation(*args, **kwargs)

    def get_tool_status(self):
        """
        Getting tool status.
        :return: Operational boolean status
        :rtype: bool
        """
        return self.__tool_operational

    @abstractmethod
    def process(self):
        """
        Process and run tool operation (Abstract method).
        """
        pass
