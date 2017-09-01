# -*- coding: utf-8 -*-

try:
    from ats_utilities.config.cfg.cfg2object import Cfg2Object
    from ats_utilities.config.cfg.object2cfg import Object2Cfg
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


class CfgSettings(Cfg2Object, Object2Cfg):
    """
    Define class CfgSettings with attribute(s) and method(s).
    CfgSettings class with cfg type of configuration.
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
        method:
            __init__ - Initial constructor
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = '[CFG_SETTINGS]'

    def __init__(self, base_config_file, verbose=False):
        """
        Setting interfaces for cfg object.
        :param base_config_file: File config path
        :type base_config_file: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        cls = self.__class__
        if verbose:
            msg = "{0} {1}{2} for {3}{4}".format(
                cls.VERBOSE, DBG, 'Setting CFG interface', ATS, RST
            )
            print(msg)
        Cfg2Object.__init__(self, base_config_file, verbose)
        Object2Cfg.__init__(self, base_config_file, verbose)

    def __str__(self):
        """
        Return human readable string (CfgSettings).
        :return: String representation of CfgSettings
        :rtype: str
        """
        file_path = self.get_file_path()
        return "File path {0}".format(file_path)

    def __repr__(self):
        """
        Return unambiguous string (CfgSettings).
        :return: String representation of CfgSettings
        :rtype: str
        """
        file_path = self.get_file_path()
        return "{0}(\'{1}\')".format(type(self).__name__, file_path)
