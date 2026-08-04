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
    Unit tests for GeneratorBundleValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.generation.setup.bundle import GeneratorBundle
from ats_utilities.generation.setup.validator import GeneratorBundleValidator
from ats_utilities.generation.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generation.tar.itar_processor import ITarProcessor


class GeneratorValidatorTest(unittest.TestCase):
    '''
        Defines class GeneratorValidatorTest with attribute(s) and method(s).
        Tests GeneratorBundleValidator logic.
    '''

    def setUp(self) -> None:
        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        self.mock_context_bundle.checker = MagicMock(spec=IChecker)
        self.mock_context_bundle.logger = MagicMock(spec=ILogger)
        self.mock_context_bundle.reporter = MagicMock(spec=IReporter)
        self.mock_context_bundle.verbose = True

        self.mock_scheme_loader = MagicMock(spec=ISchemeLoader)
        self.mock_tar_processor = MagicMock(spec=ITarProcessor)

        self.valid_params = {
            "context_bundle": self.mock_context_bundle,
            "scheme_loader": self.mock_scheme_loader,
            "tar_processor": self.mock_tar_processor
        }

    def test_validate_valid(self) -> None:
        bundle = GeneratorBundle(**self.valid_params)
        GeneratorBundleValidator.validate(bundle)

    def test_validate_invalid_bundle(self) -> None:
        with self.assertRaises(ATSValueError):
            GeneratorBundleValidator.validate(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            GeneratorBundleValidator.validate(object())  # type: ignore

    def test_validate_invalid_none(self) -> None:
        fields = ["context_bundle", "scheme_loader", "tar_processor"]

        for field in fields:
            with self.subTest(field=field):
                invalid_params = self.valid_params.copy()
                invalid_params[field] = None  # type: ignore
                bundle = GeneratorBundle(**invalid_params)
                with self.assertRaises(ATSValueError):
                    GeneratorBundleValidator.validate(bundle)

    def test_validate_invalid_type(self) -> None:
        type_mismatches = {
            "context_bundle": MagicMock(spec=ISchemeLoader),
            "scheme_loader": MagicMock(spec=ContextBundle),
            "tar_processor": MagicMock(spec=ContextBundle)
        }

        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                invalid_params = self.valid_params.copy()
                invalid_params[field] = bad_value
                bundle = GeneratorBundle(**invalid_params)
                with self.assertRaises(ATSTypeError):
                    GeneratorBundleValidator.validate(bundle)


if __name__ == "__main__":
    unittest.main()
