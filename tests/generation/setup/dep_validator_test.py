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
    Unit tests for GeneratorBundleDependenciesValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.generation.setup.dependencies import GeneratorBundleDependencies
from ats_utilities.generation.setup.dep_validator import GeneratorBundleDependenciesValidator
from ats_utilities.generation.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generation.tar.itar_processor import ITarProcessor
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class GeneratorDependenciesValidatorTest(unittest.TestCase):
    '''
        Defines class GeneratorDependenciesValidatorTest with attribute(s) and method(s).
        Tests GeneratorBundleDependenciesValidator component logic.
    '''

    def setUp(self) -> None:
        self.mock_context = MagicMock(spec=ContextBundle)
        self.mock_context.checker = MagicMock(spec=IChecker)
        self.mock_context.logger = MagicMock(spec=ILogger)
        self.mock_context.reporter = MagicMock(spec=IReporter)
        self.mock_context.verbose = True

    def _get_valid_deps(self) -> GeneratorBundleDependencies:
        return GeneratorBundleDependencies(
            scheme_loader=MagicMock(spec=ISchemeLoader),
            tar_processor=MagicMock(spec=ITarProcessor),
            context_bundle=self.mock_context
        )

    def test_validate_valid(self) -> None:
        deps = self._get_valid_deps()
        GeneratorBundleDependenciesValidator.validate(deps)

    def test_validate_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            GeneratorBundleDependenciesValidator.validate(None)  # type: ignore

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            GeneratorBundleDependenciesValidator.validate("invalid")  # type: ignore

    def test_validate_missing_attributes(self) -> None:
        deps = self._get_valid_deps()
        del deps['scheme_loader']  # type: ignore
        with self.assertRaises(ATSValueError):
            GeneratorBundleDependenciesValidator.validate(deps)


if __name__ == "__main__":
    unittest.main()
