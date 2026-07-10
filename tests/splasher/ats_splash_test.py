# -*- coding: UTF-8 -*-

'''
Module
    ats_splash_test.py
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
    Defines class ATSSplashTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of termanl properties.
Execute
    python3 -m unittest -v ats_splash_test
'''

from os.path import dirname
from unittest import TestCase, main, mock
from ats_utilities.splasher.engine import Splasher
from ats_utilities.splasher.progressbar.progress_bar import ProgressBar
from ats_utilities.splasher.component_bundle import SplashComponentBundle
from ats_utilities.splasher.splash_center_bundle import SplashCenterBundle
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from unittest.mock import MagicMock
from ats_utilities.splasher.property.isplash_property import ISplashProperty
from ats_utilities.splasher.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.splasher.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.progressbar.iprogress_bar import IProgressBar

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class ATSSplashTestCase(TestCase):
    '''
        Defines class ATSSplashTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of termanl properties.
        Splasher unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_splash_with_none_property - Test splash with None.
                | test_create - Test for create (not None).
                | test_create_with_ext - Test for create with external.
                | test_wrong_parameter_center - Test for wrong center param.
                | test_empty_parameter_center - Test for empty center param.
                | test_str - Test string representation.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_splash_with_none_property(self) -> None:
        '''Test splash with None'''
        splash: Splasher = Splasher(None)  # type: ignore
        self.assertFalse(splash.is_initialized())

    @mock.patch('ats_utilities.splasher.component_bundle.make_component')
    def test_splasher_initialization_failures(self, mock_make_component) -> None:
        '''Test Splasher initialization with errors.'''
        mock_make_component.side_effect = Exception('Unexpected')
        try:
            bundle: SplashComponentBundle | None = SplashComponentBundle(
                prop={
                    SplashKeys.ATS_ORGANIZATION: 'App Example',
                    SplashKeys.ATS_REPOSITORY: 'app_example',
                    SplashKeys.ATS_NAME: 'appexample',
                    SplashKeys.ATS_LOGO_PATH: f'{dirname(__file__)}/config/app.logo',
                    SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE: True
                }
            )
        except Exception:
            bundle = None

        splash: Splasher = Splasher(bundle)
        self.assertFalse(splash.is_initialized())

    @mock.patch('sys.stdout')
    @mock.patch('builtins.print')
    def test_splasher_initialization_ats_error(self, mock_print, mock_stdout) -> None:
        '''Test Splasher initialization ATS error (non-existent logo).'''
        bundle = SplashComponentBundle(
            prop={
                SplashKeys.ATS_ORGANIZATION: 'App Example',
                SplashKeys.ATS_REPOSITORY: 'app_example',
                SplashKeys.ATS_NAME: 'appexample',
                SplashKeys.ATS_LOGO_PATH: '/non_existent_logo_12345.logo',
                SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE: True
            }
        )
        splash = Splasher(bundle)
        self.assertFalse(splash.is_initialized())

    @mock.patch('sys.stdout')
    @mock.patch('builtins.print')
    @mock.patch('ats_utilities.splasher.engine.sleep')
    def test_create(self, mock_sleep, mock_print, mock_stdout) -> None:
        '''Test for create (not None)'''
        bundle = SplashComponentBundle(
            prop={
                SplashKeys.ATS_ORGANIZATION: 'App Example',
                SplashKeys.ATS_REPOSITORY: 'app_example',
                SplashKeys.ATS_NAME: 'appexample',
                SplashKeys.ATS_LOGO_PATH: f'{dirname(__file__)}/config/app.logo',
                SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE: True
            }
        )
        splash: Splasher = Splasher(bundle)
        self.assertIsNotNone(splash)

    @mock.patch('sys.stdout')
    @mock.patch('builtins.print')
    @mock.patch('ats_utilities.splasher.engine.sleep')
    def test_create_with_ext(self, mock_sleep, mock_print, mock_stdout) -> None:
        '''Test for create with external'''
        bundle = SplashComponentBundle(
            prop={
                SplashKeys.ATS_ORGANIZATION: 'App Example',
                SplashKeys.ATS_REPOSITORY: 'app_example',
                SplashKeys.ATS_NAME: 'appexample',
                SplashKeys.ATS_LOGO_PATH: f'{dirname(__file__)}/config/app.logo',
                SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE: False
            }
        )
        splash: Splasher = Splasher(bundle)
        self.assertIsNotNone(splash)

    @mock.patch('sys.stdout')
    @mock.patch('builtins.print')
    @mock.patch('ats_utilities.splasher.engine.sleep')
    def test_wrong_parameter_center(self, mock_sleep, mock_print, mock_stdout) -> None:
        '''Test for wrong center param'''
        bundle = SplashComponentBundle(
            prop={
                SplashKeys.ATS_ORGANIZATION: 'App Example',
                SplashKeys.ATS_REPOSITORY: 'app_example',
                SplashKeys.ATS_NAME: 'appexample',
                SplashKeys.ATS_LOGO_PATH: f'{dirname(__file__)}/config/app.logo',
                SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE: False
            }
        )
        splash: Splasher = Splasher(bundle)
        with self.assertRaises(ATSTypeError):
            splash.center(SplashCenterBundle(columns='wrong_type', text='test'))

    @mock.patch('sys.stdout')
    @mock.patch('builtins.print')
    @mock.patch('ats_utilities.splasher.engine.sleep')
    def test_empty_parameter_center(self, mock_sleep, mock_print, mock_stdout) -> None:
        '''Test for empty center param'''
        bundle = SplashComponentBundle(
            prop={
                SplashKeys.ATS_ORGANIZATION: 'App Example',
                SplashKeys.ATS_REPOSITORY: 'app_example',
                SplashKeys.ATS_NAME: 'appexample',
                SplashKeys.ATS_LOGO_PATH: f'{dirname(__file__)}/config/app.logo',
                SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE: False
            }
        )
        splash: Splasher = Splasher(bundle)
        with self.assertRaises(ATSValueError):
            splash.center(SplashCenterBundle(columns=120, additional_shifter=20, text=''))

    @mock.patch('sys.stdout')
    @mock.patch('builtins.print')
    @mock.patch('ats_utilities.splasher.engine.sleep')
    def test_str(self, mock_sleep, mock_print, mock_stdout) -> None:
        '''Test string representation of Splasher and ProgressBar.'''
        bundle = SplashComponentBundle(
            prop={
                SplashKeys.ATS_ORGANIZATION: 'App Example',
                SplashKeys.ATS_REPOSITORY: 'app_example',
                SplashKeys.ATS_NAME: 'appexample',
                SplashKeys.ATS_LOGO_PATH: f'{dirname(__file__)}/config/app.logo',
                SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE: False
            }
        )
        splash: Splasher = Splasher(bundle)
        self.assertIsInstance(str(splash), str)
        pb = ProgressBar(50)
        self.assertIsInstance(str(pb), str)

    def test_progress_bar_bounds(self) -> None:
        '''Test progress bar set_level under start and over end.'''
        pb = ProgressBar(end=90, start=10)
        
        # Test setting level below start
        pb.set_level(5)
        self.assertEqual(pb._level, 10)
        
        # Test setting level above end
        pb.set_level(100)
        self.assertEqual(pb._level, 90)

    def test_get_shared_context(self) -> None:
        '''Test get_shared_context returns ContextBundle.'''
        from ats_utilities.context_bundle import ContextBundle
        bundle = SplashComponentBundle(
            prop={
                SplashKeys.ATS_ORGANIZATION: 'App Example',
                SplashKeys.ATS_REPOSITORY: 'app_example',
                SplashKeys.ATS_NAME: 'appexample',
                SplashKeys.ATS_LOGO_PATH: f'{dirname(__file__)}/config/app.logo',
                SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE: True
            }
        )
        splash: Splasher = Splasher(bundle)
        context = splash.get_shared_context()
        self.assertIsInstance(context, ContextBundle)
    def test_splash_disabled(self) -> None:
        '''Test that splasher initializes but does nothing when disabled'''
        bundle = SplashComponentBundle(
            prop={
                'enabled': False
            }
        )
        splash: Splasher = Splasher(bundle)
        self.assertTrue(splash.is_initialized())


    def test_splash_center_bundle(self) -> None:
        '''Test SplashCenterBundle methods.'''
        bundle1 = SplashCenterBundle()
        bundle2 = SplashCenterBundle(columns=80, additional_shifter=2, text='Welcome')

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.columns, 80)
        self.assertEqual(bundle1.additional_shifter, 2)
        self.assertEqual(bundle1.text, 'Welcome')

        # Test merge when other fields are None (covers 123->120 branch)
        bundle3 = SplashCenterBundle()
        bundle3.columns = None
        bundle3.additional_shifter = None
        bundle3.text = None
        bundle2.merge(bundle3)
        self.assertEqual(bundle2.columns, 80) # should remain unchanged

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['text'], 'Welcome')

    def test_splash_center_bundle_validation_errors(self) -> None:
        '''Test SplashCenterBundle validation exceptions.'''
        # columns negative value in post init gets set to 0
        b_neg_cols = SplashCenterBundle(columns=-1)
        self.assertEqual(b_neg_cols.columns, 0)

        # additional_shifter negative value in post init gets set to 0
        b_neg_shift = SplashCenterBundle(additional_shifter=-1)
        self.assertEqual(b_neg_shift.additional_shifter, 0)

        # columns type error
        with self.assertRaises(ATSTypeError):
            SplashCenterBundle(columns='not_int', additional_shifter=2, text='ok')

        # columns value error
        bundle = SplashCenterBundle(columns=80, additional_shifter=2, text='ok')
        bundle.columns = -1
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # additional_shifter type error
        with self.assertRaises(ATSTypeError):
            SplashCenterBundle(columns=80, additional_shifter='not_int', text='ok')

        # additional_shifter value error
        bundle = SplashCenterBundle(columns=80, additional_shifter=2, text='ok')
        bundle.additional_shifter = -1
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # text type error
        bundle = SplashCenterBundle(columns=80, additional_shifter=2, text=123)  # type: ignore
        with self.assertRaises(ATSTypeError):
            bundle.validate()

        # text value error (empty string)
        bundle = SplashCenterBundle(columns=80, additional_shifter=2, text='   ')
        with self.assertRaises(ATSValueError):
            bundle.validate()

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

if __name__ == '__main__':
    main()
