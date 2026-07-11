# -*- coding: UTF-8 -*-

'''
Module
    ats_logging_engine_test.py
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
    Defines class ATSLoggingEngineTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of LoggerManager.
Execute
    python3 -m unittest -v tests/logging/ats_logging_engine_test.py
'''

from __future__ import annotations

from unittest import TestCase, main, mock
from unittest.mock import MagicMock
from os.path import dirname

from ats_utilities.logging.engine import LoggerManager
from ats_utilities.logging.logger.ilogger import ILogger
from ats_utilities.logging.logger.logger import StandardLogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import Reporter
from ats_utilities.logging.component_bundle import LoggingComponentBundle
from ats_utilities.logging.logger.logger_bundle import LoggerBundle
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.exceptions import ATSAttributeError, ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
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


class ATSLoggingEngineTestCase(TestCase):
    '''
        Defines class ATSLoggingEngineTestCase with attribute(s) and method(s).
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
                | test_initialization_unexpected_exception - Test logger manager initialization unexpected exception.
                | test_str - Test string representation.
                | test_debug - Test debug log.
                | test_warning - Test warning log.
                | test_critical - Test critical log.
                | test_error - Test error log.
                | test_info - Test info log.
                | test_get_logger - Test get_logger returns logger component.
                | test_get_shared_context - Test get_shared_context returns ContextBundle.
                | test_init_with_custom_logger - Test logger manager initialization with custom logger.
                | test_log_levels_readonly - Test log level attributes are read-only after initialization.
    '''

    LOG_FILE = '/log/simple_tool.log'

    def setUp(self) -> None:
        '''Call before test case.'''
        self.log_file: str = f'{dirname(dirname(__file__))}/assets/log/simple_tool.log'
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

    @mock.patch('ats_utilities.logging.component_bundle.make_component')
    def test_initialization_failure(self, mock_make_component) -> None:
        '''Test logger manager initialization failure'''
        mock_make_component.side_effect = ATSTypeError('Failed to initialize component')
        invalid_manager = LoggerManager()
        with self.assertRaises(ATSValueError):
            invalid_manager.is_initialized()

    @mock.patch('ats_utilities.logging.component_bundle.make_component')
    def test_initialization_unexpected_exception(self, mock_make_component) -> None:
        '''Test logger manager initialization unexpected exception'''
        mock_make_component.side_effect = Exception('Unexpected')
        invalid_manager = LoggerManager()
        with self.assertRaises(ATSValueError):
            invalid_manager.is_initialized()
        self.assertFalse(invalid_manager._is_initialized)

    def test_str(self) -> None:
        '''Test string representation of LoggerManager.'''
        self.assertIsInstance(str(self.ats_base_logging), str)

    def test_debug(self) -> None:
        '''Test ATS debug log.'''
        self.assertTrue(
            self.ats_base_logging.write_log(
                'simple debug', self.ats_base_logging.DEBUG
            )
        )

    def test_warning(self) -> None:
        '''Test ATS warning log.'''
        self.assertTrue(
            self.ats_base_logging.write_log(
                'simple warning', self.ats_base_logging.WARNING
            )
        )

    def test_critical(self) -> None:
        '''Test ATS critical log.'''
        self.assertTrue(
            self.ats_base_logging.write_log(
                'simple critical', self.ats_base_logging.CRITICAL
            )
        )

    def test_error(self) -> None:
        '''Test ATS error log.'''
        self.assertTrue(
            self.ats_base_logging.write_log(
                'simple error', self.ats_base_logging.ERROR
            )
        )

    def test_info(self) -> None:
        '''Test ATS info log.'''
        self.assertTrue(
            self.ats_base_logging.write_log(
                'simple info', self.ats_base_logging.INFO
            )
        )

    def test_get_logger(self) -> None:
        '''Test get_logger returns logger component.'''
        logger = self.ats_base_logging.get_logger()
        self.assertIsNotNone(logger)

    def test_get_shared_context(self) -> None:
        '''Test get_shared_context returns ContextBundle.'''
        context = self.ats_base_logging.get_shared_context()
        self.assertIsInstance(context, ContextBundle)

    def test_init_with_custom_logger(self) -> None:
        '''Test logger manager initialization with custom logger.'''
        custom_logger = StandardLogger()
        component_bundle = LoggingComponentBundle(
            logger=custom_logger
        )
        manager = LoggerManager(component_bundle)
        self.assertTrue(manager.is_initialized())

    def test_log_levels_readonly(self) -> None:
        '''Test log level attributes are read-only after initialization.'''
        for level_attr in ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'):
            with self.assertRaises(ATSAttributeError):
                setattr(self.ats_base_logging, level_attr, 999)


if __name__ == '__main__':
    main()
