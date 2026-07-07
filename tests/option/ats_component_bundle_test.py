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
    Creates test cases for checking OptionComponentBundle.
Execute
    python3 -m unittest -v tests/option/ats_component_bundle_test.py
'''

from unittest import TestCase, main
from unittest.mock import MagicMock
from ats_utilities.option.component_bundle import OptionComponentBundle
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.exceptions import ATSValueError, ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '1.0.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class OptionComponentBundleTestCase(TestCase):
    '''Test cases for OptionComponentBundle.'''

    def test_option_component_bundle(self) -> None:
        '''Test OptionComponentBundle methods.'''
        mock_strategy = MagicMock(spec=IParserStrategy)
        mock_context = ContextBundle()

        bundle1 = OptionComponentBundle()
        bundle2 = OptionComponentBundle(parameters={'a': 'b'}, strategy=mock_strategy, context_bundle=mock_context)

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.parameters, {'a': 'b'})
        self.assertEqual(bundle1.strategy, mock_strategy)
        self.assertEqual(bundle1.context_bundle, mock_context)

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['parameters'], {'a': 'b'})

    def test_option_component_bundle_validation_errors(self) -> None:
        '''Test OptionComponentBundle validation exceptions.'''
        mock_strategy = MagicMock(spec=IParserStrategy)
        mock_context = ContextBundle()

        # Missing parameters
        bundle = OptionComponentBundle(parameters={'a': 'b'}, strategy=mock_strategy, context_bundle=mock_context)
        bundle.parameters = None
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # Missing strategy
        bundle = OptionComponentBundle(parameters={'a': 'b'}, strategy=mock_strategy, context_bundle=mock_context)
        bundle.strategy = None
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # Missing context_bundle
        bundle = OptionComponentBundle(parameters={'a': 'b'}, strategy=mock_strategy, context_bundle=mock_context)
        bundle.context_bundle = None
        with self.assertRaises(ATSValueError):
            bundle.validate()

    def test_option_component_bundle_merge_type_check(self) -> None:
        '''Test that merge raises error if other is not an OptionComponentBundle.'''
        bundle = OptionComponentBundle()
        with self.assertRaises(ATSTypeError):
            bundle.merge("not_an_option_component_bundle")


if __name__ == '__main__':
    main()
