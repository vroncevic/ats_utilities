# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
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
    Unit tests for ReporterBundleFactory class.
'''

from __future__ import annotations

import unittest

from ats_utilities.checker.engine import Checker
from ats_utilities.logger.engine import Logger
from ats_utilities.reporter.setup.bundle import ReporterBundle
from ats_utilities.reporter.setup.factory import ReporterBundleFactory
from ats_utilities.reporter.theme.engine import ConsoleTheme

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class FactoryTest(unittest.TestCase):
    '''
        Defines class FactoryTest with attribute(s) and method(s).
        Tests ReporterBundleFactory static factory logic.
    '''

    def test_create_default_bundle(self) -> None:
        bundle = ReporterBundleFactory.create_bundle()
        self.assertIsInstance(bundle, ReporterBundle)
        self.assertIsInstance(bundle.checker, Checker)
        self.assertIsInstance(bundle.theme, ConsoleTheme)
        self.assertIsInstance(bundle.logger, Logger)

    def test_create_bundle_with_options(self) -> None:
        from ats_utilities.reporter.setup.options import ReporterBundleOptions
        options: ReporterBundleOptions = {
            "checker": {},
            "logger": {"log_level": 20},
            "theme": {"success": "green"}
        }
        bundle = ReporterBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, ReporterBundle)


if __name__ == "__main__":
    unittest.main()
