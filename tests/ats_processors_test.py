# -*- coding: UTF-8 -*-

'''
Module
    ats_processors_test.py
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
    Defines class ATSProcessorsTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of config processors.
Execute
    python3 -m unittest -v ats_processors_test
'''

import io
from unittest import TestCase, main
from unittest.mock import patch
from ats_utilities.config_io.json.json_processor import JSONProcessor
from ats_utilities.config_io.yaml.yaml_processor import YAMLProcessor
from ats_utilities.config_io.xml.xml_processor import XMLProcessor
from ats_utilities.config_io.cfg.cfg_processor import CFGProcessor
from ats_utilities.config_io.ini.ini_processor import INIProcessor
from ats_utilities.exceptions.ats_error import ATSError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSProcessorsTestCase(TestCase):
    '''
        Defines class ATSProcessorsTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of config processors.
        Config processors unit tests.

        It defines:

            :attributes: None
            :methods:
                | test_json_processor - Tests JSONProcessor functionality.
                | test_yaml_processor - Tests YAMLProcessor functionality.
                | test_xml_processor - Tests XMLProcessor functionality.
                | test_cfg_processor - Tests CFGProcessor functionality.
                | test_ini_processor - Tests INIProcessor functionality.
    '''

    def test_json_processor(self) -> None:
        '''
            Tests JSONProcessor functionality.

            :exceptions: None.
        '''
        processor = JSONProcessor()
        valid_json = '{"ats_name": "Simple Tool", "ats_version": "1.0.0"}'
        invalid_json = '{invalid_json'

        # Decode valid
        self.assertTrue(processor.decode(valid_json))
        self.assertEqual(processor.to_dict(), {"ats_name": "Simple Tool", "ats_version": "1.0.0"})

        # Encode
        encoded = processor.encode()
        self.assertIn('"ats_name": "Simple Tool"', encoded)

        # Decode invalid
        self.assertFalse(processor.decode(invalid_json))

        # String representation
        self.assertIsInstance(str(processor), str)

    def test_yaml_processor(self) -> None:
        '''
            Tests YAMLProcessor functionality.

            :exceptions: None.
        '''
        processor = YAMLProcessor()
        valid_yaml = 'ats_name: Simple Tool\nats_version: 1.0.0\n'

        # Decode valid
        self.assertTrue(processor.decode(valid_yaml))
        self.assertEqual(processor.to_dict(), {"ats_name": "Simple Tool", "ats_version": "1.0.0"})

        # Encode
        encoded = processor.encode()
        self.assertIn('ats_name: Simple Tool', encoded)

        # String representation
        self.assertIsInstance(str(processor), str)

        # Decode invalid triggering ATSError via mock
        with patch('yaml.safe_load', side_effect=ATSError("Mock error")):
            self.assertFalse(processor.decode("invalid_yaml"))

    def test_xml_processor(self) -> None:
        '''
            Tests XMLProcessor functionality.

            :exceptions: None.
        '''
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

    def test_cfg_processor(self) -> None:
        '''
            Tests CFGProcessor functionality.

            :exceptions: None.
        '''
        processor = CFGProcessor()
        lines = [
            '# Comment line\n',
            '   \n',
            'ats_name = Simple Tool\n',
            'ats_version=1.0.0\n',
            'invalid_line_no_equals\n'
        ]

        self.assertTrue(processor.from_lines(lines))
        d = processor.to_dict()
        self.assertEqual(d.get('ats_name'), 'Simple Tool')
        self.assertEqual(d.get('ats_version'), '1.0.0')
        self.assertNotIn('invalid_line_no_equals', d)

        # to_string
        cfg_str = processor.to_string()
        self.assertIn('ats_name = Simple Tool', cfg_str)

        # String representation
        self.assertIsInstance(str(processor), str)

    def test_ini_processor(self) -> None:
        '''
            Tests INIProcessor functionality.

            :exceptions: None.
        '''
        processor = INIProcessor()

        # Before section load
        self.assertEqual(processor.to_dict(), {})

        ini_content = '[ats_info]\nats_name = Simple Tool\nats_version = 1.0.0\n'
        stream = io.StringIO(ini_content)

        # from_stream success
        self.assertTrue(processor.from_stream(stream))
        
        # to_dict
        d = processor.to_dict()
        self.assertEqual(d.get('ats_name'), 'Simple Tool')
        self.assertEqual(d.get('ats_version'), '1.0.0')

        # to_stream success
        out_stream = io.StringIO()
        self.assertTrue(processor.to_stream(out_stream))
        out_content = out_stream.getvalue()
        self.assertIn('[ats_info]', out_content)
        self.assertIn('ats_name = Simple Tool', out_content)

        class BadStream:
            def __iter__(self):
                raise OSError("Bad stream")

        self.assertFalse(processor.from_stream(BadStream()))

        # to_stream failure
        class BadOutStream:
            def write(self, *args, **kwargs):
                raise OSError("Bad write stream")

        self.assertFalse(processor.to_stream(BadOutStream()))

        # String representation
        self.assertIsInstance(str(processor), str)


if __name__ == '__main__':
    main()
