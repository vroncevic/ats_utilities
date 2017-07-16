# encoding: utf-8

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class AbstractSetConfig(object):
    """
    Define class AbstractSetConfig with attribute(s) and method(s).
    It defines:
        attribute:
            None
        method:
            set_configuration - Setting config (Abstract method)
    """

    def set_configuration(self, configuration):
        """
        Setting config.
        :param configuration: Configuration object
        :type configuration: dict
        """
        msg = 'Not implemented'
        raise NotImplementedError(msg)
