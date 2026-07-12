# -*- coding: UTF-8 -*-

'''
Module
    ats_component_bundle_test.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
Info
    Creates test cases for checking LoggerComponentBundle.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import MagicMock

from ats_utilities.logger.component_bundle import LoggerComponentBundle
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.exceptions import ATSValueError, ATSTypeError


class LoggerComponentBundleTestCase(TestCase):
    '''Test cases for checking LoggerComponentBundle.'''

    def test_default_initialization(self) -> None:
        '''Test default initialization of LoggerComponentBundle.'''
        bundle = LoggerComponentBundle()
        self.assertIsNotNone(bundle.logger)
        self.assertIsNone(bundle.log_file)

    def test_custom_initialization(self) -> None:
        '''Test custom initialization of LoggerComponentBundle.'''
        mock_logger = MagicMock(spec=ILogger)
        mock_logger.__class__ = ILogger
        bundle = LoggerComponentBundle(logger=mock_logger, log_file='test.log')
        self.assertEqual(bundle.logger, mock_logger)
        self.assertEqual(bundle.log_file, 'test.log')

    def test_invalid_logger_type(self) -> None:
        '''Test LoggerComponentBundle raises ATSTypeError for invalid logger type.'''
        with self.assertRaises(ATSTypeError):
            LoggerComponentBundle(logger="not_a_logger")

    def test_validate_success(self) -> None:
        '''Test validate success with valid values.'''
        mock_logger = MagicMock(spec=ILogger)
        mock_logger.__class__ = ILogger
        bundle = LoggerComponentBundle(logger=mock_logger, log_file='test.log')
        bundle.validate()  # Should not raise

    def test_validate_missing_logger(self) -> None:
        '''Test validate raises ValueError when logger is missing.'''
        bundle = LoggerComponentBundle()
        bundle.logger = None
        bundle.log_file = 'test.log'
        with self.assertRaises(ValueError):
            bundle.validate()

    def test_validate_missing_log_file(self) -> None:
        '''Test validate raises ValueError when log_file is missing.'''
        mock_logger = MagicMock(spec=ILogger)
        mock_logger.__class__ = ILogger
        bundle = LoggerComponentBundle(logger=mock_logger)
        with self.assertRaises(ValueError):
            bundle.validate()

    def test_validate_invalid_log_file_type(self) -> None:
        '''Test validate raises ATSTypeError when log_file type is invalid.'''
        mock_logger = MagicMock(spec=ILogger)
        mock_logger.__class__ = ILogger
        bundle = LoggerComponentBundle(logger=mock_logger, log_file=123)
        with self.assertRaises(ATSTypeError):
            bundle.validate()

    def test_merge(self) -> None:
        '''Test merging LoggerComponentBundle.'''
        mock_logger1 = MagicMock(spec=ILogger)
        mock_logger1.__class__ = ILogger
        bundle1 = LoggerComponentBundle(logger=mock_logger1, log_file='first.log')

        mock_logger2 = MagicMock(spec=ILogger)
        mock_logger2.__class__ = ILogger
        bundle2 = LoggerComponentBundle(logger=mock_logger2, log_file='second.log')

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.logger, mock_logger2)
        self.assertEqual(bundle1.log_file, 'second.log')

    def test_to_dict(self) -> None:
        '''Test to_dict method.'''
        mock_logger = MagicMock(spec=ILogger)
        mock_logger.__class__ = ILogger
        bundle = LoggerComponentBundle(logger=mock_logger, log_file='test.log')
        d = bundle.to_dict()
        self.assertEqual(d['logger'], mock_logger)
        self.assertEqual(d['log_file'], 'test.log')


if __name__ == '__main__':
    main()
