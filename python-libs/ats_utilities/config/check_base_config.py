# -*- coding: UTF-8 -*-
# check_base_config.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# ats_utilities is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ats_utilities is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from inspect import stack

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
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
                VERBOSE - Console text indicator for current process-phase
            method:
                is_correct - Check basic configuration keys
    """

    __BASE_CONFIG = {
        1: 'ats_name',
        2: 'ats_version',
        3: 'ats_build_date',
        4: 'ats_license'
    }

    VERBOSE = '[ATS_UTILITIES::CONFIG::CHECK_BASE_CONFIG]'

    @classmethod
    def is_correct(cls, configuration, verbose=False):
        """
            Check basic configuration structure.
            :param configuration: Base configuration
            :type configuration: <dict>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (correct configuration structure) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, status, statuses = stack()[0][3], False, []
        configuration_txt = 'Argument: expected configuration <dict> object'
        configuration_msg = "{0} {1} {2}".format(
            cls.VERBOSE, func, configuration_txt
        )
        if configuration is None:
            raise ATSBadCallError(configuration_msg)
        if not isinstance(configuration, dict):
            raise ATSTypeError(configuration_msg)
        config_keys = configuration.keys()
        config_expected_keys = cls.__BASE_CONFIG.values()
        verbose_message(
            cls.VERBOSE, verbose, 'Checking configuration structure'
        )
        for cfg_key in config_keys:
            if cfg_key not in config_expected_keys:
                msg = "{0} [{1}]".format('Key not expected', cfg_key)
                error_message(cls.VERBOSE, msg)
                statuses.append(False)
            else:
                statuses.append(True)
        status = all(status for status in statuses)
        return True if status else False
