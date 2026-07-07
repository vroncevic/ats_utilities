# -*- coding: UTF-8 -*-

'''
Module
    ats_context_bundle_test.py
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
    Creates test cases for checking ContextBundle.
Execute
    python3 -m unittest -v tests/ats_context_bundle_test.py
'''

from unittest import TestCase, main
from unittest.mock import MagicMock
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '1.0.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ContextBundleTestCase(TestCase):
    '''Test cases for ContextBundle.'''

    def test_context_bundle(self) -> None:
        '''Test ContextBundle methods.'''
        mock_checker = MagicMock(spec=IChecker)
        mock_reporter = MagicMock(spec=IReporter)

        bundle1 = ContextBundle()
        bundle2 = ContextBundle(checker=mock_checker, reporter=mock_reporter, verbose=True)

        # test merge
        bundle1.merge(bundle2)
        self.assertEqual(bundle1.checker, mock_checker)
        self.assertEqual(bundle1.reporter, mock_reporter)
        self.assertTrue(bundle1.verbose)

        # test validate
        bundle1.validate()

        # test to_dict
        d = bundle1.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d['checker'], mock_checker)
        self.assertEqual(d['reporter'], mock_reporter)
        self.assertTrue(d['verbose'])

    def test_context_bundle_validation_errors(self) -> None:
        '''Test ContextBundle validation exceptions.'''
        bundle = ContextBundle()
        bundle.checker = None
        with self.assertRaises(ATSValueError):
            bundle.validate()

        bundle = ContextBundle()
        bundle.reporter = None
        with self.assertRaises(ATSValueError):
            bundle.validate()

    def test_context_bundle_merge_type_check(self) -> None:
        '''Test that merge raises error if other is not a ContextBundle.'''
        bundle = ContextBundle()
        with self.assertRaises(ATSTypeError):
            bundle.merge("not_a_context_bundle")


if __name__ == '__main__':
    main()
