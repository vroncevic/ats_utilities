# -*- coding: UTF-8 -*-

'''
Module
    validator_test.py
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
    Unit tests for LoggerBundleValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.logger.setup.bundle import LoggerBundle
from ats_utilities.logger.setup.validator import LoggerBundleValidator
from ats_utilities.logger.underlying.iunderlying import IUnderlyingLogger
from ats_utilities.logger.formatter.iformatter import ILogFormatter
from ats_utilities.logger.buffer.ibuffer import ILogBuffer
from ats_utilities.logger.handler.ihandler_manager import ILogHandlerManager
from ats_utilities.logger.processor.imessage_processor import IMessageProcessor
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class ValidatorTest(unittest.TestCase):
    '''
        Defines class ValidatorTest with attribute(s) and method(s).
        Tests LoggerBundleValidator logic.
    '''

    def _get_bundle_args(self) -> dict[str, object]:
        return {
            "logger": MagicMock(spec=IUnderlyingLogger),
            "has_file_handler": True,
            "formatter": MagicMock(spec=ILogFormatter),
            "buffer": MagicMock(spec=ILogBuffer),
            "handler_manager": MagicMock(spec=ILogHandlerManager),
            "message_processor": MagicMock(spec=IMessageProcessor)
        }

    def test_validation_valid(self) -> None:
        bundle = LoggerBundle(**self._get_bundle_args())
        LoggerBundleValidator.validate(bundle)

    def test_validation_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            LoggerBundleValidator.validate(None)  # type: ignore

    def test_validation_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            LoggerBundleValidator.validate("invalid")  # type: ignore

    def test_validation_missing_attributes(self) -> None:
        fields = ["logger", "has_file_handler", "formatter", "buffer", "handler_manager", "message_processor"]
        for field in fields:
            with self.subTest(field=field):
                invalid_params = self._get_bundle_args()
                invalid_params[field] = None  # type: ignore
                bundle = LoggerBundle(**invalid_params)
                with self.assertRaises(ATSValueError):
                    LoggerBundleValidator.validate(bundle)

    def test_validation_invalid_types(self) -> None:
        type_mismatches = {
            "logger": "not_logger",
            "has_file_handler": "not_bool",
            "formatter": "not_formatter",
            "buffer": "not_buffer",
            "handler_manager": "not_handler",
            "message_processor": "not_processor"
        }
        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                invalid_params = self._get_bundle_args()
                invalid_params[field] = bad_value
                bundle = LoggerBundle(**invalid_params)
                with self.assertRaises(ATSTypeError):
                    LoggerBundleValidator.validate(bundle)


if __name__ == "__main__":
    unittest.main()
