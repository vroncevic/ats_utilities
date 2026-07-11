# -*- coding: UTF-8 -*-

'''
Module
    ats_cfg_processor_test.py
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
    Creates test cases for checking CFGProcessor.
Execute
    python3 -m unittest -v tests/config_io/cfg/ats_cfg_processor_test.py
'''

from __future__ import annotations

from unittest import TestCase, main
from ats_utilities.config_io.cfg.cfg_processor import CFGProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class CFGProcessorTestCase(TestCase):
    '''Test cases for CFGProcessor.'''

    def test_cfg_processor(self) -> None:
        '''Tests CFGProcessor functionality.'''
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


if __name__ == '__main__':
    main()
