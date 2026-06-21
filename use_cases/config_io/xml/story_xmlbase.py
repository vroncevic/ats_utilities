# -*- coding: utf-8 -*-

'''
Module
    story_xmlbase.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Use cases for ATS XmlBase.
'''

import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from ats_utilities.config_io.xml.xmlbase import XmlBase

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

info_file: str = "/data/dev/python/ats_utilities/github/ats_utilities/tests/config/ats_cli_xml_api.xml"
framework_core = XmlBase(info_file, verbose=True)

#
# 3rd party [BeautifulSoup]
# ==========================


#class BeautifulSoupAdapter(IXMLProcessor):
#    '''
#        ...
#    '''
#    def __init__(self):
#        '''
#            ...
#        '''
#        self.soup = None
#
#    def from_string(self, xml_content: str) -> bool:
#        '''
#            ...
#        '''
#        self.soup = BeautifulSoup(xml_content, 'xml')
#        return True
#
#    def to_string(self) -> str:
#        '''
#            ...
#        '''
#        return str(self.soup) if self.soup else ""
#
#    def get_ats_info(self) -> dict[str, str]:
#        '''
#            ...
#        '''
#
#        if not self.soup:
#            return {}
#
#        return {
#            'ats_name': self.soup.find('ats_name').get_text() if self.soup.find('ats_name') else "",
#            'ats_version': self.soup.find('ats_version').get_text() if self.soup.find('ats_version') else "",
#            'ats_build_date': self.soup.find('ats_build_date').get_text() if self.soup.find('ats_build_date') else "",
#            'ats_licence': self.soup.find('ats_licence').get_text() if self.soup.find('ats_licence') else ""
#        }
#
### Korisnik bira parser na nivou aplikacije:
###odabrani_parser = ElementTreeAdapter()
#info_file: str = "/data/dev/python/ats_utilities/github/ats_utilities/tests/config/ats_cli_xml_api.xml"
#odabrani_parser = BeautifulSoupAdapter()
#reader = Xml2Object(config_file=info_file, xml_processor=odabrani_parser)
#writer = Object2Xml(config_file=info_file)
#framework_core = XmlBase(info_file=info_file, xml2obj=reader, obj2xml=writer, verbose=True)