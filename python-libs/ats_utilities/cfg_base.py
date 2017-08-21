# encoding: utf-8

from abc import ABCMeta, abstractmethod

from ats_utilities.text.stdout_text import ATS, DBG, ERR, RST
from ats_utilities.ats_info import ATSInfo
from ats_utilities.cfg_settings import CfgSettings
from ats_utilities.option.ats_option_parser import ATSOptionParser
from ats_utilities.config.check_base_config import CheckBaseConfig
from ats_utilities.error.ats_value_error import ATSValueError

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CfgBase(ATSInfo, CfgSettings, ATSOptionParser):
    """
    Define class CfgBase with attribute(s) and method(s).
    Load a settings, create a CL interface and run operation.
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
            __tool_operational - Control operational flag
        method:
            __init__ - Initial constructor
            add_new_option - Adding new option for CL interface
            get_tool_status - Getting tool status
            process - Process and run tool operation (Abstract method)
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    __metaclass__ = ABCMeta
    VERBOSE = '[CFG_BASE]'

    def __init__(self, base_config_file, verbose=False):
        """
        Setting version, build date, name and license of App/Tool/Script.
        :param base_config_file: Configuration file path
        :type base_config_file: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2}{3}".format(
                cls.VERBOSE, DBG, 'Checking CFG configuration', RST
            )
            print(msg)
        self.__tool_operational = False
        CfgSettings.__init__(self, base_config_file, verbose)
        try:
            configuration = self.read_configuration(verbose)
            check_configuration = CheckBaseConfig.is_correct(
                configuration, verbose
            )
            if configuration and check_configuration:
                ATSInfo.__init__(self, configuration, verbose)
                statuses = []
                tool_version = self.get_ats_version()
                statuses.append(tool_version)
                tool_build_date = self.get_ats_build_date()
                statuses.append(tool_build_date)
                tool_name = self.get_ats_name()
                statuses.append(tool_name)
                tool_lic = self.get_ats_license()
                statuses.append(tool_lic)
                if all(status for status in statuses):
                    tool_info = "{0} {1}".format(tool_version, tool_build_date)
                    ATSOptionParser.__init__(
                        self, tool_info, tool_name, tool_lic, verbose
                    )
                    self.__tool_operational = True
                else:
                    msg = "{0} {1}{2} of {3} {4}".format(
                        cls.VERBOSE, ERR,
                        'Missing version/build_date/name or license', ATS, RST
                    )
                    raise ATSValueError(msg)
            else:
                msg = "{0} {1}{2} of {3}{4}".format(
                    cls.VERBOSE, ERR, 'Wrong configuration structure', ATS, RST
                )
                raise ATSValueError(msg)
        except ATSValueError as e:
            print(e)

    def add_new_option(self, *args, **kwargs):
        """
        Adding new option for CL interface.
        :param args: Arguments
        :type: Python object(s)
        :param kwargs: Options and texts
        :type: Python object(s)
        """
        self.add_operation(*args, **kwargs)

    def get_tool_status(self, verbose=False):
        """
        Getting tool status.
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return: True (tool ready) | False
        :rtype: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}[{2}]{3}".format(
                cls.VERBOSE, DBG, self.__tool_operational, RST
            )
            print(msg)
        return self.__tool_operational

    @abstractmethod
    def process(self, verbose=False):
        """
        Process and run tool operation (Abstract method).
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        pass

    def __str__(self):
        """
        Return human readable string (CfgBase).
        :return: String representation of CfgBase
        :rtype: str
        """
        file_path = self.get_file_path()
        return "File path {0}".format(file_path)

    def __repr__(self):
        """
        Return unambiguous string (CfgBase).
        :return: String representation of CfgBase
        :rtype: str
        """
        file_path = self.get_file_path()
        return "{0}(\'{1}\')".format(type(self).__name__, file_path)
