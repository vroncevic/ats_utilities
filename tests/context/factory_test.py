# -*- coding: UTF-8 -*-

'''
Module
    context_factory_test.py
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
    Unit tests for ContextFactory class.
'''

from __future__ import annotations

import unittest

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextFactory
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ContextFactoryTest(unittest.TestCase):
    '''
        Defines class ContextFactoryTest with attribute(s) and method(s).
        Tests ContextFactory static factory logic.
    '''

    def test_create_default_context_bundle(self) -> None:
        '''
            Tests create_default_context_bundle.

            :exceptions: None.
        '''
        # Test with verbose=False
        bundle = ContextFactory.create_default_context_bundle(verbose=False)
        self.assertIsInstance(bundle, ContextBundle)
        self.assertIsInstance(bundle.checker, IChecker)
        self.assertIsInstance(bundle.logger, ILogger)
        self.assertIsInstance(bundle.reporter, IReporter)
        self.assertFalse(bundle.verbose)

        # Test with verbose=True
        bundle_verbose = ContextFactory.create_default_context_bundle(verbose=True)
        self.assertIsInstance(bundle_verbose, ContextBundle)
        self.assertTrue(bundle_verbose.verbose)


if __name__ == "__main__":
    unittest.main()
