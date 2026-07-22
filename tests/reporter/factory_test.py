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
    Unit tests for ReporterFactory class.
'''

from __future__ import annotations

import unittest

from ats_utilities.checker.engine import Checker
from ats_utilities.logger.engine import Logger
from ats_utilities.reporter.bundle import ReporterBundle
from ats_utilities.reporter.factory import ReporterFactory
from ats_utilities.reporter.theme.engine import ConsoleTheme

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class FactoryTest(unittest.TestCase):
    '''
        Defines class FactoryTest with attribute(s) and method(s).
        Tests ReporterFactory static factory logic.
    '''

    def test_create_default_bundle(self) -> None:
        bundle = ReporterFactory.create_default_bundle()
        self.assertIsInstance(bundle, ReporterBundle)
        self.assertIsInstance(bundle.checker, Checker)
        self.assertIsInstance(bundle.theme, ConsoleTheme)
        self.assertIsInstance(bundle.logger, Logger)


if __name__ == "__main__":
    unittest.main()
