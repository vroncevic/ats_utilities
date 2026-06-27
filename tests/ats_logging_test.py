# -*- coding: UTF-8 -*-

'''
Module
    ats_logging_test.py
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
    Defines class ATSLoggingTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of LoggerManager.
Execute
    python3 -m unittest -v ats_logging_test
'''

from unittest import TestCase, main, mock
from os.path import dirname
from ats_utilities.logging.engine import LoggerManager
from ats_utilities.logging.logger import ATSLogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import Reporter
from ats_utilities.logging.component_bundle import LoggingComponentBundle
from ats_utilities.logging.logger_bundle import LoggerBundle
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSBaseLoggingFile(LoggerManager):
    '''Simple Class for checking LoggerManager.'''

    def __init__(self, log_file: str, reporter: IReporter = Reporter(), verbose: bool = False) -> None:
        '''Initial constructor.'''
        context = ContextBundle(reporter=reporter, verbose=verbose)
        logger_bundle = LoggerBundle(
            name='simple_test',
            log_stdout=False,
            log_file=log_file
        )
        component_bundle = LoggingComponentBundle(
            logger_bundle=logger_bundle,
            context_bundle=context
        )
        super().__init__(component_bundle)
        self._verbose = verbose
        if self.is_tool_ok():
            reporter.success(['init ATS logging'])

    def is_tool_ok(self) -> bool:
        '''
            Check is logger operational.

            :return: Is logger operational
            :rtype: <bool>
        '''
        return True


class ATSLoggingTestCase(TestCase):
    '''
        Defines class ATSLoggingTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of LoggerManager.
        LoggerManager unit tests.

        It defines:

            :attributes:
                | LOG_FILE - Log file path template.
                | ats_base_logging - API for checking base logging.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSBaseLoggingFile not None.
                | test_tool_operational - Test is logger operational.
                | test_is_initialized - Test is logger manager initialized.
                | test_initialization_failure - Test logger manager initialization failure.
                | test_debug - Test debug log.
                | test_warning - Test warning log.
                | test_critical - Test critical log.
                | test_error - Test error log.
                | test_info - Test info log.
                | test_str - Test string representation.
    '''

    LOG_FILE = '/log/simple_tool.log'

    def setUp(self) -> None:
        '''Call before test case.'''
        self.log_file: str = f'{dirname(__file__)}{self.LOG_FILE}'
        self.ats_base_logging: ATSBaseLoggingFile = ATSBaseLoggingFile(self.log_file)

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test not None'''
        self.assertIsNotNone(self.ats_base_logging)

    def test_tool_operational(self) -> None:
        '''Test is logger operational'''
        self.assertTrue(self.ats_base_logging.is_tool_ok())

    def test_is_initialized(self) -> None:
        '''Test is_initialized method'''
        self.assertTrue(self.ats_base_logging.is_initialized())

    @mock.patch('ats_utilities.logging.engine.make_component')
    def test_initialization_failure(self, mock_make_component) -> None:
        '''Test logger manager initialization failure'''
        mock_make_component.side_effect = ATSTypeError('Failed to initialize component')
        invalid_manager = LoggerManager()
        with self.assertRaises(ATSValueError):
            invalid_manager.is_initialized()

    @mock.patch('ats_utilities.logging.engine.make_component')
    def test_initialization_unexpected_exception(self, mock_make_component) -> None:
        '''Test logger manager initialization unexpected exception'''
        mock_make_component.side_effect = Exception('Unexpected')
        invalid_manager = LoggerManager()
        with self.assertRaises(ATSValueError):
            invalid_manager.is_initialized()
        self.assertFalse(invalid_manager._is_initialized)

    def test_str(self) -> None:
        '''Test string representation of LoggerManager and ATSLogger.'''
        self.assertIsInstance(str(self.ats_base_logging), str)
        logger = ATSLogger()
        self.assertIsInstance(str(logger), str)

    def test_debug(self) -> None:
        '''Test ATS debug log.'''
        self.assertTrue(
            self.ats_base_logging.write_log(
                'simple debug', self.ats_base_logging.ATS_DEBUG
            )
        )

    def test_warning(self) -> None:
        '''Test ATS warning log.'''
        self.assertTrue(
            self.ats_base_logging.write_log(
                'simple warning', self.ats_base_logging.ATS_WARNING
            )
        )

    def test_critical(self) -> None:
        '''Test ATS critical log.'''
        self.assertTrue(
            self.ats_base_logging.write_log(
                'simple critical', self.ats_base_logging.ATS_CRITICAL
            )
        )

    def test_error(self) -> None:
        '''Test ATS error log.'''
        self.assertTrue(
            self.ats_base_logging.write_log(
                'simple error', self.ats_base_logging.ATS_ERROR
            )
        )

    def test_info(self) -> None:
        '''Test ATS info log.'''
        self.assertTrue(
            self.ats_base_logging.write_log(
                'simple info', self.ats_base_logging.ATS_INFO
            )
        )

    def test_get_logger(self) -> None:
        '''Test get_logger returns logger component.'''
        logger = self.ats_base_logging.get_logger()
        self.assertIsNotNone(logger)

    @mock.patch('ats_utilities.logging.logger.getLogger')
    @mock.patch('ats_utilities.logging.logger.basicConfig')
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
        logger = ATSLogger(bundle)
        mock_basicConfig.assert_called_once()
        kwargs = mock_basicConfig.call_args[1]
        self.assertEqual(kwargs['filename'], 'test_log.log')

    def test_write_log_invalid_level(self) -> None:
        '''Test write_log with unsupported level.'''
        logger = ATSLogger()
        self.assertFalse(logger.write_log('unsupported log', 999))


if __name__ == '__main__':
    main()
