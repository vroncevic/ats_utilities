# -*- coding: UTF-8 -*-

"""
 Module
     __init__.py
 Copyright
     Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
     ats_utilities is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     ats_utilities is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class XmlBase with attribute(s) and method(s).
     Load ATS informations, setup ATS CL interface.
"""

import sys

try:
    from ats_utilities.info import ATSInfo
    from ats_utilities.option import ATSOptionParser
    from ats_utilities.config_io.xml.xml2object import Xml2Object
    from ats_utilities.config_io.xml.object2xml import Object2Xml
except ImportError as error_message:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class XmlBase(ATSInfo):
    """
        Define class XmlBase with attribute(s) and method(s).
        Load ATS informations, setup ATS CL interface.
        It defines:

            :attributes:
                | tool_operational - Control ATS operational functionality.
                | xml2obj - In API for informations.
                | obj2xml - Out API for informations.
                | option_parser - Option parser for ATS.
            :methods:
                | __init__ - Initial constructor.
    """

    def __init__(self, informations_file, verbose=False):
        """
            Initial constructor.

            :param informations_file: Informations file path.
            :type informations_file: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        """
        informations, tool_info = None, None
        self.tool_operational = False  # App/Tool/Script not operational
        self.xml2obj = Xml2Object(informations_file)
        self.obj2xml = Object2Xml(informations_file)
        if all([self.xml2obj, self.obj2xml]):
            informations = self.xml2obj.read_configuration()
        if informations:
            ATSInfo.__init__(self, informations, verbose=verbose)
            if self.ats_info_ok:
                tool_info = "{0} {1}".format(self.name, self.build_date)
                self.option_parser = ATSOptionParser(
                    tool_info, self.version, self.license, verbose=verbose
                )
                self.tool_operational = True  # App/Tool/Script operational
