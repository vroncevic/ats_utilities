# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

class CheckBaseConfig(object):
    """
    Define class GenPyModule with attribute(s) and method(s).
    Checking basic configuration structure.
    It defines:
        attribute:
            __BASE_CONFIG - Basic configuration keys
        method:
            now - Check basic configuration
    """

    __BASE_CONFIG = {
        1 : "app_name",
        2 : "app_version",
        3 : "app_build_date",
        4 : "app_license"
    }

    @classmethod
    def now(cls, configuration):
        """
        :param configuration: Base configuration
        :type: dict
        :return: Boolean status
        :rtype: bool
        """
        for config_key in configuration.keys():
            if config_key not in CheckBaseConfig.__BASE_CONFIG.values():
                return False
        return True
