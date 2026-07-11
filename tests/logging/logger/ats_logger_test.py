# -*- coding: UTF-8 -*-

'''
Module
    ats_logger_test.py
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
    Defines class ATSLoggerTestCase with attribute(s) and method(s).
    Creates test cases for checking StandardLogger component.
Execute
    python3 -m unittest -v tests/logging/logger/ats_logger_test.py
'''

from __future__ import annotations

from unittest import TestCase, main, mock
from os.path import dirname

from ats_utilities.logging.logger.logger import StandardLogger
from ats_utilities.logging.logger.logger_bundle import LoggerBundle
from ats_utilities.context_bundle import ContextBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSLoggerTestCase(TestCase):
    '''
        Defines class ATSLoggerTestCase with attribute(s) and method(s).
        Creates test cases for checking StandardLogger.

        It defines:

            :attributes:
                | LOG_FILE - Log file path template.
                | log_file - Log file path resolved.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_str - Test string representation of StandardLogger.
                | test_write_log - Test log writing directly.
                | test_logger_configure_stdout_and_file - Test stdout/file logger config.
                | test_write_log_invalid_level - Test write_log with unsupported level.
    '''

    LOG_FILE = '/log/simple_tool.log'

    def setUp(self) -> None:
        '''Call before test case.'''
        self.log_file: str = f'{dirname(dirname(dirname(__file__)))}/assets/log/simple_tool.log'

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_str(self) -> None:
        '''Test string representation of StandardLogger.'''
        logger = StandardLogger()
        self.assertIsInstance(str(logger), str)

    def test_write_log(self) -> None:
        '''Test log writing directly.'''
        bundle = LoggerBundle(name='logger_test', log_stdout=False, log_file=self.log_file)
        logger = StandardLogger(logger_bundle=bundle)
        self.assertTrue(logger.write_log('direct debug', logger.LOG_LEVELS.DEBUG))
        self.assertTrue(logger.write_log('direct info', logger.LOG_LEVELS.INFO))
        self.assertTrue(logger.write_log('direct warning', logger.LOG_LEVELS.WARNING))
        self.assertTrue(logger.write_log('direct error', logger.LOG_LEVELS.ERROR))
        self.assertTrue(logger.write_log('direct critical', logger.LOG_LEVELS.CRITICAL))

    @mock.patch('ats_utilities.logging.logger.logger.getLogger')
    @mock.patch('ats_utilities.logging.logger.logger.basicConfig')
    def test_logger_configure_stdout_and_file(self, mock_basicConfig, mock_getLogger) -> None:
        '''Test logger configure when both stdout and file log are enabled.'''
        mock_logger = mock.MagicMock()
        mock_logger.hasHandlers.return_value = False
        mock_getLogger.return_value = mock_logger

        bundle = LoggerBundle(
            name='test_config',
            log_stdout=True,
            log_file='test_log.log',
            configure_logging=True
        )
        logger = StandardLogger(bundle)
        mock_basicConfig.assert_called_once()
        kwargs = mock_basicConfig.call_args[1]
        self.assertEqual(kwargs['filename'], 'test_log.log')

    def test_write_log_invalid_level(self) -> None:
        '''Test write_log with unsupported level.'''
        logger = StandardLogger()
        self.assertFalse(logger.write_log('unsupported log', 999))


if __name__ == '__main__':
    main()
