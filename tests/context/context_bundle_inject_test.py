# -*- coding: UTF-8 -*-

'''
Module
    context_bundle_inject_test.py
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
    Unit tests for Context Bundle injection utilities.
'''

from __future__ import annotations

from typing import Any
import unittest
from unittest.mock import MagicMock

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.context.context_bundle_inject import inject, inject_context_bundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class FallbackClassNoDeps:
    '''
        Dummy fallback class with no dependencies.
    '''
    pass


class FallbackClassWithDeps:
    '''
        Dummy fallback class with dependencies.
    '''
    def __init__(self, **kwargs: Any) -> None:
        self.dependencies = kwargs


class ContextBundleInjectTest(unittest.TestCase):
    '''
        Defines class ContextBundleInjectTest with attribute(s) and method(s).
        Tests context bundle dependency injection logic.

        It defines:

            :attributes: None.
            :methods:
                | test_inject_passed_value - Tests inject with a direct passed value.
                | test_inject_fallback_type_no_deps - Tests inject with a class fallback and no dependencies.
                | test_inject_fallback_type_with_single_dep - Tests inject with class fallback and single dependency.
                | test_inject_fallback_type_with_multiple_deps - Tests inject with class fallback and multiple dependencies.
                | test_inject_fallback_value - Tests inject with a raw value fallback.
                | test_inject_context_bundle_valid - Tests inject_context_bundle with valid bundle.
                | test_inject_context_bundle_invalid - Tests inject_context_bundle error conditions.
    '''

    def test_inject_passed_value(self) -> None:
        '''
            Tests inject with a direct passed value.

            :exceptions: None.
        '''
        class Target:
            pass

        target = Target()
        inject(target, ('my_attr', 'passed_value', 'fallback_value', None))
        self.assertEqual(getattr(target, '_my_attr'), 'passed_value')

    def test_inject_fallback_type_no_deps(self) -> None:
        '''
            Tests inject with a class fallback and no dependencies.

            :exceptions: None.
        '''
        class Target:
            pass

        target = Target()
        inject(target, ('my_attr', None, FallbackClassNoDeps, None))
        self.assertIsInstance(getattr(target, '_my_attr'), FallbackClassNoDeps)

    def test_inject_fallback_type_with_single_dep(self) -> None:
        '''
            Tests inject with class fallback and single dependency.

            :exceptions: None.
        '''
        class Target:
            def __init__(self) -> None:
                self._dep1 = "dependency_1"

        target = Target()
        inject(target, ('my_attr', None, FallbackClassWithDeps, 'dep1'))
        resolved = getattr(target, '_my_attr')
        self.assertIsInstance(resolved, FallbackClassWithDeps)
        self.assertEqual(resolved.dependencies, {"dep1": "dependency_1"})

    def test_inject_fallback_type_with_multiple_deps(self) -> None:
        '''
            Tests inject with class fallback and multiple dependencies.

            :exceptions: None.
        '''
        class Target:
            def __init__(self) -> None:
                self._dep1 = "dependency_1"
                self._dep2 = "dependency_2"

        target = Target()
        inject(target, ('my_attr', None, FallbackClassWithDeps, ['dep1', 'dep2']))
        resolved = getattr(target, '_my_attr')
        self.assertIsInstance(resolved, FallbackClassWithDeps)
        self.assertEqual(resolved.dependencies, {"dep1": "dependency_1", "dep2": "dependency_2"})

        # Case when a dependency is missing (dependency_obj is None)
        class TargetMissingDep:
            def __init__(self) -> None:
                self._dep1 = "dependency_1"

        target_missing = TargetMissingDep()
        inject(target_missing, ('my_attr', None, FallbackClassWithDeps, ['dep1', 'dep2']))
        resolved_missing = getattr(target_missing, '_my_attr')
        self.assertIsInstance(resolved_missing, FallbackClassWithDeps)
        self.assertEqual(resolved_missing.dependencies, {"dep1": "dependency_1"})

    def test_inject_fallback_value(self) -> None:
        '''
            Tests inject with a raw value fallback.

            :exceptions: None.
        '''
        class Target:
            pass

        target = Target()
        inject(target, ('my_attr', None, 'fallback_raw_val', None))
        self.assertEqual(getattr(target, '_my_attr'), 'fallback_raw_val')

    def test_inject_context_bundle_valid(self) -> None:
        '''
            Tests inject_context_bundle with valid bundle.

            :exceptions: None.
        '''
        class Target:
            pass

        mock_checker = MagicMock(spec=IChecker)
        mock_logger = MagicMock(spec=ILogger)
        mock_reporter = MagicMock(spec=IReporter)

        ctx = ContextBundle(
            checker=mock_checker,
            logger=mock_logger,
            reporter=mock_reporter,
            verbose=True
        )

        target = Target()
        inject_context_bundle(target, ctx)

        self.assertIs(getattr(target, '_checker'), mock_checker)
        self.assertIs(getattr(target, '_logger'), mock_logger)
        self.assertIs(getattr(target, '_reporter'), mock_reporter)
        self.assertTrue(getattr(target, '_verbose'))

    def test_inject_context_bundle_invalid(self) -> None:
        '''
            Tests inject_context_bundle error conditions.

            :exceptions: None.
        '''
        class Target:
            pass

        target = Target()

        with self.assertRaises(ATSValueError):
            inject_context_bundle(target, None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            inject_context_bundle(target, "not a bundle")  # type: ignore


if __name__ == "__main__":
    unittest.main()
