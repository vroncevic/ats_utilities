# -*- coding: UTF-8 -*-

'''
Module
    ats_component_bundle_test.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Creates test cases for checking ReporterComponentBundle.
Execute
    python3 -m unittest -v tests/reporter/ats_component_bundle_test.py
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import MagicMock

from ats_utilities.reporter.component_bundle import ReporterComponentBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.exceptions import ATSValueError, ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '1.0.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ReporterComponentBundleTestCase(TestCase):
    '''Test cases for ReporterComponentBundle.'''

    def test_reporter_component_bundle(self) -> None:
        '''Test ReporterComponentBundle methods.'''
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)
        bundle1 = ReporterComponentBundle()
        bundle2 = ReporterComponentBundle(
            checker=mock_checker, theme=mock_theme, logger=mock_logger
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.checker, mock_checker)
        self.assertEqual(bundle1.theme, mock_theme)
        self.assertEqual(bundle1.logger, mock_logger)

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['checker'], mock_checker)
        self.assertEqual(d['logger'], mock_logger)

    def test_reporter_component_bundle_validation_errors(self) -> None:
        '''Test ReporterComponentBundle validation exceptions.'''
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)

        # Missing checker
        bundle = ReporterComponentBundle()
        bundle.checker = None
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # Missing theme
        bundle = ReporterComponentBundle()
        bundle.theme = None
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # Missing logger
        bundle = ReporterComponentBundle()
        bundle.logger = None
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # Type validation errors
        bundle = ReporterComponentBundle()
        bundle.checker = "not_a_checker"
        with self.assertRaises(ATSTypeError):
            bundle.validate()

        bundle = ReporterComponentBundle()
        bundle.theme = "not_a_theme"
        with self.assertRaises(ATSTypeError):
            bundle.validate()

        bundle = ReporterComponentBundle()
        bundle.logger = "not_a_logger"
        with self.assertRaises(ATSTypeError):
            bundle.validate()

        with self.assertRaises(ATSTypeError):
            bundle.merge("not_a_reporter_component_bundle")

    def test_reporter_component_bundle_merge_with_none(self) -> None:
        '''Test ReporterComponentBundle merge with None values.'''
        bundle1 = ReporterComponentBundle()
        bundle2 = ReporterComponentBundle()
        bundle2.theme = None
        bundle2.logger = None
        bundle1.merge(bundle2)
        self.assertIsNotNone(bundle1.theme)
        self.assertIsNotNone(bundle1.logger)



if __name__ == '__main__':
    main()
