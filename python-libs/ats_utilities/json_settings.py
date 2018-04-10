# -*- coding: UTF-8 -*-
# json_settings.py
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

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config.json.json2object import Json2Object
    from ats_utilities.config.json.object2json import Object2Json
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


class JsonSettings(Json2Object, Object2Json):
    """
        Define class JsonSettings with attribute(s) and method(s).
        JsonSettings class with json type of config.
        It defines:
            attribute:
                __CLASS_SLOTS__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
            method:
                __init__ - Initial constructor
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    __CLASS_SLOTS__ = (
        'VERBOSE'  # Read-Only
    )
    VERBOSE = 'ATS_UTILITIES::JSON_SETTINGS'

    def __init__(self, base_config_file, verbose=False):
        """
            Setting interfaces for json object.
            :param base_config_file: File config path
            :type base_config_file: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls = JsonSettings
        verbose_message(cls.VERBOSE, verbose, 'Initial ATS JSON settings')
        Json2Object.__init__(self, base_config_file, verbose=verbose)
        Object2Json.__init__(self, base_config_file, verbose=verbose)

    def __str__(self):
        """
            Return human readable string (JsonSettings).
            :return: String representation of JsonSettings
            :rtype: <str>
        """
        file_path = self.get_file_path()
        return "File path {0}".format(file_path)

    def __repr__(self):
        """
            Return unambiguous string (JsonSettings).
            :return: String representation of JsonSettings
            :rtype: <str>
        """
        cls, file_path = JsonSettings, self.get_file_path()
        return "{0}(\'{1}\')".format(cls.__name__, file_path)
