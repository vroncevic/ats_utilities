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
    Creates test cases for checking SplashComponentBundle.
Execute
    python3 -m unittest -v tests/splasher/ats_component_bundle_test.py
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import MagicMock

from ats_utilities.splasher.component_bundle import SplashComponentBundle
from ats_utilities.splasher.property.isplash_property import ISplashProperty
from ats_utilities.splasher.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.splasher.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.progressbar.iprogress_bar import IProgressBar
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '1.0.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class SplashComponentBundleTestCase(TestCase):
    '''Test cases for SplashComponentBundle.'''

    def test_splash_component_bundle(self) -> None:
        '''Test SplashComponentBundle methods.'''
        mock_splash_prop = MagicMock(spec=ISplashProperty)
        mock_term_prop = MagicMock(spec=ITerminalProperties)
        mock_github = MagicMock(spec=IExtInfrastructure)
        mock_ext = MagicMock(spec=IExtInfrastructure)
        mock_pb = MagicMock(spec=IProgressBar)
        mock_context = ContextBundle()

        bundle1 = SplashComponentBundle()
        bundle2 = SplashComponentBundle(
            prop={'a': 'b'},
            splash_property=mock_splash_prop,
            terminal_property=mock_term_prop,
            github=mock_github,
            ext=mock_ext,
            pb=mock_pb,
            context_bundle=mock_context
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.prop, {'a': 'b'})

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['prop'], {'a': 'b'})

    def test_splash_component_bundle_validation_errors(self) -> None:
        '''Test SplashComponentBundle validation exceptions.'''
        mock_splash_prop = MagicMock(spec=ISplashProperty)
        mock_term_prop = MagicMock(spec=ITerminalProperties)
        mock_github = MagicMock(spec=IExtInfrastructure)
        mock_ext = MagicMock(spec=IExtInfrastructure)
        mock_pb = MagicMock(spec=IProgressBar)
        mock_context = ContextBundle()

        fields = {
            'prop': {'enabled': False},
            'splash_property': mock_splash_prop,
            'terminal_property': mock_term_prop,
            'github': mock_github,
            'ext': mock_ext,
            'pb': mock_pb,
            'context_bundle': mock_context
        }

        for field in fields:
            bundle = SplashComponentBundle(**fields)
            setattr(bundle, field, None)
            with self.assertRaises(ValueError):
                bundle.validate()

        with self.assertRaises(ATSTypeError):
            bundle.merge("not_a_splash_component_bundle")

    def test_splash_component_bundle_merge_with_none(self) -> None:
        '''Test SplashComponentBundle merge with None values.'''
        bundle1 = SplashComponentBundle()
        bundle2 = SplashComponentBundle()
        bundle2.splash_property = None

        with self.assertRaises(ATSValueError):
            bundle1.merge(bundle2)



if __name__ == '__main__':
    main()
