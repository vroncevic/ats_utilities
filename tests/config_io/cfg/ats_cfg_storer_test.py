# -*- coding: UTF-8 -*-

'''
Module
    ats_cfg_storer_test.py
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
    Defines class CFGStorerTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of CFGStorer.
Execute
    python3 -m unittest -v ats_cfg_storer_test
'''

from unittest import TestCase, main
from unittest.mock import MagicMock
from ats_utilities.config_io.cfg.cfg_storer import CFGStorer
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.cfg.icfg_processor import ICFGProcessor
from ats_utilities.config_io.cfg.object2cfg import Object2Cfg
from ats_utilities.config_io.cfg.cfg_processor import CFGProcessor

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class CFGStorerTestCase(TestCase):
    '''
        Defines class CFGStorerTestCase with attribute(s) and method(s).
        Creates test cases for checking CFGStorer interfaces.
        CFGStorer unit tests.

        It defines:

            :methods:
                | test_not_none - Test is CFGStorer not None.
                | test_store_configuration_success - Test storing configuration successfully.
                | test_str - Test string representation of CFGStorer.
    '''

    def test_not_none(self) -> None:
        '''Test is CFGStorer not None.'''
        storer = CFGStorer(info_file='dummy.cfg')
        self.assertIsNotNone(storer)

    def test_store_configuration_success(self) -> None:
        '''Test storing configuration successfully.'''
        mock_obj2cfg = MagicMock(spec=Object2Cfg)
        mock_processor = MagicMock(spec=CFGProcessor)
        
        mock_obj2cfg.write_configuration.return_value = True
        
        storer = CFGStorer(
            info_file='dummy.cfg',
            object2cfg=mock_obj2cfg,
            cfg_processor=mock_processor
        )
        
        config = {'key': 'value'}
        result = storer.store_configuration(config)
        self.assertTrue(result)
        mock_processor.from_lines.assert_called_once_with(["key = value\n"])
        mock_obj2cfg.write_configuration.assert_called_once_with(mock_processor)

    def test_str(self) -> None:
        '''Test string representation of CFGStorer.'''
        storer = CFGStorer(info_file='dummy.cfg')
        self.assertIsInstance(str(storer), str)


if __name__ == '__main__':
    main()

