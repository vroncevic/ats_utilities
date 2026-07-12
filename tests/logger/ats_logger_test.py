# -*- coding: UTF-8 -*-

'''
Module
    ats_logger_test.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
Info
    Creates test cases for checking Logger component.
'''

from __future__ import annotations

from unittest import TestCase, main, mock
from unittest.mock import MagicMock
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

from ats_utilities.logger.component_bundle import LoggerComponentBundle
from ats_utilities.logger.engine import Logger
from ats_utilities.logger.ilogger import ILogger


class LoggerTestCase(TestCase):
    '''Test cases for checking Logger component.'''

    def test_default_logger(self) -> None:
        '''Test Logger initialization with default bundle.'''
        logger = Logger()
        self.assertTrue(logger.is_initialized())
        self.assertIsInstance(str(logger), str)

    def test_custom_logger(self) -> None:
        '''Test Logger initialization with mock logger.'''
        mock_sys_logger = MagicMock()
        bundle = LoggerComponentBundle(logger=mock_sys_logger)
        logger = Logger(bundle)
        self.assertTrue(logger.is_initialized())

        # Test writing log
        logger.write_log("test message", INFO)
        mock_sys_logger.info.assert_called_once_with("test message")

    def test_write_log_non_standard_logger(self) -> None:
        '''Test Logger using a non-standard logger that has write_log method.'''
        mock_custom = MagicMock()
        del mock_custom.info  # Make sure it doesn't have standard info method
        mock_custom.write_log = MagicMock()

        bundle = LoggerComponentBundle(logger=mock_custom)
        logger = Logger(bundle)

        logger.write_log("custom log", WARNING)
        mock_custom.write_log.assert_called_once_with("custom log", WARNING)

    def test_set_level(self) -> None:
        '''Test set_level sets the log level on standard logger.'''
        mock_sys_logger = MagicMock()
        mock_sys_logger.setLevel = MagicMock()
        bundle = LoggerComponentBundle(logger=mock_sys_logger)
        logger = Logger(bundle)

        logger.set_level(DEBUG)
        mock_sys_logger.setLevel.assert_called_once_with(DEBUG)

    def test_no_color_environment(self) -> None:
        '''Test that ANSI color codes are stripped when NO_COLOR environment variable is set.'''
        mock_sys_logger = MagicMock()
        bundle = LoggerComponentBundle(logger=mock_sys_logger)
        logger = Logger(bundle)

        colored_message = "\x1b[31mError message\x1b[0m"
        with mock.patch.dict('os.environ', {'NO_COLOR': '1'}):
            logger.write_log(colored_message, ERROR)
            mock_sys_logger.error.assert_called_once_with("Error message")


if __name__ == '__main__':
    main()
