# -*- coding: UTF-8 -*-

'''
Module
    ats_yaml_processor_test.py
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
    Creates test cases for checking YAMLProcessor.
Execute
    python3 -m unittest -v tests/config_io/yaml/ats_yaml_processor_test.py
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import patch
from ats_utilities.config_io.processor.yaml_processor import YAMLProcessor
from ats_utilities.exceptions import ATSError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class YAMLProcessorTestCase(TestCase):
    '''Test cases for YAMLProcessor.'''

    def test_yaml_processor(self) -> None:
        '''Tests YAMLProcessor functionality.'''
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


if __name__ == '__main__':
    main()
