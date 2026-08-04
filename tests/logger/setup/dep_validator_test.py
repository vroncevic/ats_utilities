# -*- coding: UTF-8 -*-

'''
Module
    dep_validator_test.py
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
    Unit tests for LoggerBundleDependenciesValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.logger.setup.dependencies import LoggerBundleDependencies
from ats_utilities.logger.setup.dep_validator import LoggerBundleDependenciesValidator
from ats_utilities.logger.underlying.iunderlying import IUnderlyingLogger
from ats_utilities.logger.formatter.iformatter import ILogFormatter
from ats_utilities.logger.buffer.ibuffer import ILogBuffer
from ats_utilities.logger.handler.ihandler_manager import ILogHandlerManager
from ats_utilities.logger.processor.imessage_processor import IMessageProcessor
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class LoggerDependenciesValidatorTest(unittest.TestCase):
    '''
        Defines class LoggerDependenciesValidatorTest with attribute(s) and method(s).
        Tests LoggerBundleDependenciesValidator component logic.
    '''

    def _get_valid_deps(self) -> LoggerBundleDependencies:
        return LoggerBundleDependencies(
            logger=MagicMock(spec=IUnderlyingLogger),
            has_file_handler=True,
            formatter=MagicMock(spec=ILogFormatter),
            buffer=MagicMock(spec=ILogBuffer),
            handler_manager=MagicMock(spec=ILogHandlerManager),
            message_processor=MagicMock(spec=IMessageProcessor)
        )

    def test_validate_valid(self) -> None:
        deps = self._get_valid_deps()
        LoggerBundleDependenciesValidator.validate(deps)

    def test_validate_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            LoggerBundleDependenciesValidator.validate(None)  # type: ignore

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            LoggerBundleDependenciesValidator.validate("invalid")  # type: ignore

    def test_validate_missing_attributes(self) -> None:
        deps = self._get_valid_deps()
        del deps['logger']  # type: ignore
        with self.assertRaises(ATSValueError):
            LoggerBundleDependenciesValidator.validate(deps)


if __name__ == "__main__":
    unittest.main()
