# encoding: utf-8

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CheckBaseConfig(object):
    """
    Define class GenPyModule with attribute(s) and method(s).
    Checking basic config structure.
    It defines:
        attribute:
            __BASE_CONFIG - Basic config keys
        method:
            now - Check basic config
    """

    __BASE_CONFIG = {
        1: "app_name",
        2: "app_version",
        3: "app_build_date",
        4: "app_license"
    }

    @classmethod
    def now(cls, configuration):
        """
        Check basic config.
        :param configuration: Base config
        :type: dict
        :return: Boolean status
        :rtype: bool
        """
        statuses = []
        config_keys = configuration.keys()
        config_values = CheckBaseConfig.__BASE_CONFIG.values()
        for cfg_key in config_keys:
            if cfg_key not in config_values:
                statuses.append(False)
            else:
                statuses.append(True)
        return all(status for status in statuses)
