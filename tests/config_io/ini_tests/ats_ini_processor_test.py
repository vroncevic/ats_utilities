# -*- coding: UTF-8 -*-

'''
Module
    ats_ini_processor_test.py
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
    Creates test cases for checking INIProcessor.
Execute
    python3 -m unittest -v tests/config_io/ini/ats_ini_processor_test.py
'''

from __future__ import annotations

import io
from unittest import TestCase, main
from ats_utilities.config_io.processor.ini_processor import INIProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class INIProcessorTestCase(TestCase):
    '''Test cases for INIProcessor.'''

    def test_ini_processor(self) -> None:
        '''Tests INIProcessor functionality.'''
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
