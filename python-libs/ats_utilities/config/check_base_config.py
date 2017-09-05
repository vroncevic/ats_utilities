# -*- coding: utf-8 -*-

import sys

try:
    from ats_utilities.text.stdout_text import DBG, ERR, RST
    from ats_utilities.text import COut
except ImportError as e:
    msg = "\n{0}\n".format(e)
    sys.exit(msg)  # Force close python ATS ###################################

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
    Define class CheckBaseConfig with attribute(s) and method(s).
    Checking basic configuration structure.
    It defines:
        attribute:
            __BASE_CONFIG - Basic config keys
                1: 'ats_name'
                2: 'ats_version'
                3: 'ats_build_date'
                4: 'ats_license'
            VERBOSE - Verbose prefix console text
        method:
            is_correct - Check basic configuration keys
    """

    __BASE_CONFIG = {
        1: 'ats_name',
        2: 'ats_version',
        3: 'ats_build_date',
        4: 'ats_license'
    }

    VERBOSE = 'CHECK_BASE_CONFIG'

    @classmethod
    def is_correct(cls, configuration, verbose=False):
        """
        Check basic configuration structure.
        :param configuration: Base configuration
        :type configuration: <dict>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: True (correct) | False
        :rtype: <bool>
        """
        cout = COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}".format('Checking configuration parameters')
        COut.print_console_msg(msg, verbose=verbose)
        configuration_is_dict, status = isinstance(configuration, dict), False
        if configuration_is_dict:
            statuses, config_keys = [], configuration.keys()
            config_values = cls.__BASE_CONFIG.values()
            for cfg_key in config_keys:
                if cfg_key not in config_values:
                    msg = "\n{0} [{1}]\n".format('Key not expected', cfg_key)
                    COut.print_console_msg(msg, error=True)
                    statuses.append(False)
                else:
                    statuses.append(True)
            status = all(status for status in statuses)
        return True if status else False
