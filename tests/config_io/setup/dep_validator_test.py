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
    Unit tests for ConfigIODependenciesValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.config_io.setup.dependencies import ConfigIODependencies
from ats_utilities.config_io.setup.dep_validator import ConfigIODependenciesValidator
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class ConfigIODependenciesValidatorTest(unittest.TestCase):
    '''
        Defines class ConfigIODependenciesValidatorTest with attribute(s) and method(s).
        Tests ConfigIODependenciesValidator component logic.
    '''

    def setUp(self) -> None:
        self.mock_context = MagicMock(spec=ContextBundle)
        self.mock_context.checker = MagicMock(spec=IChecker)
        self.mock_context.logger = MagicMock(spec=ILogger)
        self.mock_context.reporter = MagicMock(spec=IReporter)
        self.mock_context.verbose = True

    def _get_valid_deps(self) -> ConfigIODependencies:
        return ConfigIODependencies(
            file_path="/path/to/file",
            processor=MagicMock(spec=IConfigProcessor),
            context_bundle=self.mock_context
        )

    def test_validate_valid(self) -> None:
        deps = self._get_valid_deps()
        ConfigIODependenciesValidator.validate(deps)

    def test_validate_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            ConfigIODependenciesValidator.validate(None)  # type: ignore

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            ConfigIODependenciesValidator.validate("invalid")  # type: ignore

    def test_validate_missing_attributes(self) -> None:
        deps = self._get_valid_deps()
        del deps['file_path']  # type: ignore
        with self.assertRaises(ATSValueError):
            ConfigIODependenciesValidator.validate(deps)

    def test_validate_invalid_attribute_types(self) -> None:
        deps = self._get_valid_deps()
        deps['file_path'] = 123  # type: ignore
        with self.assertRaises(ATSTypeError):
            ConfigIODependenciesValidator.validate(deps)


if __name__ == "__main__":
    unittest.main()
