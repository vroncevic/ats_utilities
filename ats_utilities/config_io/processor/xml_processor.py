# -*- coding: UTF-8 -*-

'''
Module
    xml_processor.py
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
    Defines class XMLProcessor with attribute(s) and method(s).
    Creates an API to process configuration in XML format.
    1th level of configuration loader/storer implementation.
'''

from __future__ import annotations

from copy import deepcopy
from collections.abc import Mapping
from typing import Any, override
import xml.etree.ElementTree as ET

from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.factory_class import to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class XMLProcessor(IConfigProcessor):
    '''
        Defines class XMLProcessor with attribute(s) and method(s).
        Creates an API to process configuration in XML format.
        1th level of configuration loader/storer implementation.

        It defines:

            :attributes:
                | _root - Internal instance to store configuration data (default None).
                | _scheme - Mapping with configuration scheme (default None).
                | _root_tag - Resolved root element tag name (default 'configuration').
            :methods:
                | __init__ - Initializes XMLProcessor constructor.
                | deserialize - Loads and parses configuration from a raw source (string, stream, or lines).
                | serialize - Converts the internal configuration structure back to a formatted string representation.
                | update_data - Updates the internal configuration data and validates it against the scheme.
                | to_dict - Returns the parsed configuration as a flat or structured dictionary.
                | validate_by_scheme - Validates the internal parsed data structure against the provided scheme.
                | __str__ - Returns the XMLProcessor instance as string representation.

        XML Format Config Scheme
        ------------------------

        For XML configurations, the value in the ``scheme`` mapping **must** be 
        the parent element's tag name. The processor resolves the path using 
        XPath style (e.g., ``./parent/key``). If the tag is a direct child of 
        the root element, the value is an empty string (``""``).

        To configure a custom root element name, use the special reserve key ``"__root__"``.

        .. code-block:: python

            scheme = {
                "__root__": "ats_utility",    # Configures: <ats_utility>...</ats_utility> as root
                "ats_name": "ats_info",       # Maps to: <ats_info><ats_name>...</ats_name></ats_info>
                "hostname": "connection",     # Maps to: <connection><hostname>...</hostname></connection>
                "verbose": ""                 # Maps to: <root><verbose>...</verbose></root>
            }
    '''

    _root: ET.Element | None
    _scheme: Mapping[str, str] | None
    _root_tag: str

    def __init__(self, scheme: Mapping[str, str] | None = None) -> None:
        '''
            Initializes XMLProcessor constructor.

            :param scheme: Mapping with configuration scheme | None.
            :type scheme: <Mapping[str, str] | None>
            :exceptions: None.
        '''
        self._root = None
        self._scheme = scheme
        self._root_tag = 'configuration'

        if scheme is not None and '__root__' in scheme:
            self._root_tag = scheme['__root__']

    @override
    def deserialize(self, content: Any) -> bool:
        '''
            Loads and parses configuration from a raw source (string, stream, or lines).

            :param content: Raw configuration data (str, stream, or sequence).
            :type content: <Any>
            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        try:
            self._root = ET.fromstring(str(content))

            return self.validate_by_scheme()

        except ET.ParseError:
            return False

    @override
    def serialize(self) -> str:
        '''
            Converts the internal configuration structure back to a formatted string representation.

            :return: Configuration content as string.
            :rtype: <str>
            :exceptions: None.
        '''
        if self._root is not None:
            return ET.tostring(self._root, encoding='utf-8').decode('utf-8')

        return ''

    @override
    def update_data(self, new_data: Mapping[str, str]) -> bool:
        '''
            Updates the internal configuration data and validates it against the scheme.

            :param new_data: Mapping containing configuration keys and values.
            :type new_data: <Mapping[str, str]>
            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        old_root = deepcopy(self._root) if self._root is not None else None

        if self._root is None:
            self._root = ET.Element(self._root_tag)

        for key, value in new_data.items():
            if key == '__root__':
                continue

            parent_tag = self._scheme.get(key) if self._scheme is not None else None

            xpath_query = f'./{parent_tag}/{key}' if parent_tag else f'./{key}'
            node = self._root.find(xpath_query)

            if node is not None:
                node.text = str(value)
            else:
                if parent_tag:
                    parent_node = self._root.find(f'./{parent_tag}')
                    if parent_node is None:
                        parent_node = ET.SubElement(self._root, parent_tag)

                    child_node = ET.SubElement(parent_node, key)
                    child_node.text = str(value)
                else:
                    child_node = ET.SubElement(self._root, key)
                    child_node.text = str(value)

        if not self.validate_by_scheme():
            self._root = old_root

            return False

        return True

    @override
    def to_dict(self) -> dict[str, str]:
        '''
            Returns the parsed configuration as a flat or structured dictionary.

            :return: Dictionary with configuration information.
            :rtype: <dict[str, str]>
            :exceptions: None.
        '''
        if self._root is None:
            return {}

        if self._scheme is not None:
            result: dict[str, str] = {}

            for key, parent in self._scheme.items():
                if key == '__root__':
                    continue

                xpath_query = f'./{parent}/{key}' if parent else f'./{key}'
                node = self._root.find(xpath_query)

                if node is not None and node.text is not None:
                    result[key] = node.text.strip()
                else:
                    result[key] = ''

            return result

        return {child.tag: child.text.strip() for child in self._root if child.text is not None}

    @override
    def validate_by_scheme(self) -> bool:
        '''
            Validates the internal parsed data structure against the provided scheme.

            :return: <True> if data matches the scheme, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        if self._root is None:
            return False

        if self._scheme is None:
            return True

        for key, parent in self._scheme.items():
            if key == '__root__':
                continue

            xpath_query = f'./{parent}/{key}' if parent else f'./{key}'

            if self._root.find(xpath_query) is None:
                return False

        return True

    @override
    def __str__(self) -> str:
        '''
            Returns the XMLProcessor instance as string representation.

            :return: The XMLProcessor instance as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
