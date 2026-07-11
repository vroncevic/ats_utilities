# -*- coding: UTF-8 -*-

'''
Module
    ats_xml_processor_test.py
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
    Creates test cases for checking XMLProcessor.
Execute
    python3 -m unittest -v tests/config_io/xml/ats_xml_processor_test.py
'''

from __future__ import annotations

from unittest import TestCase, main
from ats_utilities.config_io.xml.xml_processor import XMLProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class XMLProcessorTestCase(TestCase):
    '''Test cases for XMLProcessor.'''

    def test_xml_processor(self) -> None:
        '''Tests XMLProcessor functionality.'''
        processor = XMLProcessor()
        
        # Test to_dict and to_string before load
        self.assertEqual(processor.to_dict(), {})
        self.assertEqual(processor.to_string(), "")
        self.assertEqual(processor._get_val("ats_name"), "")

        valid_xml = '<ats_info><ats_name>Simple Tool</ats_name><ats_version>1.0.0</ats_version></ats_info>'
        self.assertTrue(processor.from_string(valid_xml))

        # to_dict
        d = processor.to_dict()
        self.assertEqual(d['ats_name'], 'Simple Tool')
        self.assertEqual(d['ats_version'], '1.0.0')

        # to_string
        xml_str = processor.to_string()
        self.assertIn('<ats_name>Simple Tool</ats_name>', xml_str)

        # String representation
        self.assertIsInstance(str(processor), str)

        # Test node is None and node.text is None
        processor2 = XMLProcessor()
        processor2.from_string('<ats_info><ats_name>Test</ats_name></ats_info>')
        self.assertEqual(processor2._get_val('nonexistent'), '')

        processor3 = XMLProcessor()
        processor3.from_string('<ats_info><ats_name/></ats_info>')
        self.assertEqual(processor3._get_val('ats_name'), '')


if __name__ == '__main__':
    main()
