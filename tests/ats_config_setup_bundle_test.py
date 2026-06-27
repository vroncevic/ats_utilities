# -*- coding: UTF-8 -*-

'''
Module
    ats_config_setup_bundle_test.py
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
    Defines class ConfigSetupComponentBundleTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ConfigSetupComponentBundle.
Execute
    python3 -m unittest -v ats_config_setup_bundle_test
'''

from unittest import TestCase, main
from unittest.mock import MagicMock
from ats_utilities.config_setup.component_bundle import ConfigSetupComponentBundle
from ats_utilities.config_setup.ipro_config import IProConfig
from ats_utilities.config_setup.pro_config import ProConfig
from ats_utilities.config_setup.ipro_name import IProName
from ats_utilities.config_setup.pro_name import ProName
from ats_utilities.config_setup.itemplate_dir import ITemplateDir
from ats_utilities.config_setup.template_dir import TemplateDir
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ConfigSetupComponentBundleTestCase(TestCase):
    '''
        Defines class ConfigSetupComponentBundleTestCase with attribute(s) and method(s).
        Creates test cases for checking ConfigSetupComponentBundle interfaces.
        ConfigSetupComponentBundle unit tests.

        It defines:

            :attributes: None
            :methods:
                | test_init - Test is ConfigSetupComponentBundle initialized correctly.
                | test_validate - Test validate method.
                | test_merge - Test merge method.
                | test_to_dict - Test to_dict method.
    '''

    def test_init(self) -> None:
        '''Test is ConfigSetupComponentBundle initialized correctly.'''
        bundle = ConfigSetupComponentBundle()
        self.assertIsNone(bundle.pro_config)
        self.assertIsNone(bundle.pro_name)
        self.assertIsNone(bundle.template_dir)
        self.assertIsNone(bundle.context_bundle)

    def test_validate(self) -> None:
        '''Test validate method.'''
        context_bundle: ContextBundle = ContextBundle()
        bundle = ConfigSetupComponentBundle(
            pro_config=ProConfig(context_bundle),
            pro_name=ProName(context_bundle),
            template_dir=TemplateDir(context_bundle),
            context_bundle=context_bundle
        )
        # Should not raise any exception as it is currently pass
        try:
            bundle.validate()
        except Exception as e:
            self.fail(f"validate() raised {type(e).__name__} unexpectedly!")

    def test_validate_with_missing_pro_config(self) -> None:
        context_bundle: ContextBundle = ContextBundle()
        bundle = ConfigSetupComponentBundle(
            pro_name=ProName(context_bundle),
            template_dir=TemplateDir(context_bundle),
            context_bundle=context_bundle
        )
        with self.assertRaisesRegex(ATSValueError, r'project configuration must be provided\.'):
            bundle.validate()

    def test_validate_with_missing_pro_name(self) -> None:
        context_bundle: ContextBundle = ContextBundle()
        bundle = ConfigSetupComponentBundle(
            pro_config=ProConfig(context_bundle),
            template_dir=TemplateDir(context_bundle),
            context_bundle=context_bundle
        )
        with self.assertRaisesRegex(ATSValueError, r'project name must be provided\.'):
            bundle.validate()

    def test_validate_with_missing_template_dir(self) -> None:
        context_bundle: ContextBundle = ContextBundle()
        bundle = ConfigSetupComponentBundle(
            pro_config=ProConfig(context_bundle),
            pro_name=ProName(context_bundle)
        )
        with self.assertRaisesRegex(ATSValueError, r'template directory must be provided\.'):
            bundle.validate()

    def test_validate_with_missing_context_bundle(self) -> None:
        context_bundle: ContextBundle = ContextBundle()
        bundle = ConfigSetupComponentBundle(
            pro_config=ProConfig(context_bundle),
            pro_name=ProName(context_bundle),
            template_dir=TemplateDir(context_bundle)
        )
        with self.assertRaisesRegex(ATSValueError, r'context bundle must be provided\.'):
            bundle.validate()

    def test_merge(self) -> None:
        '''Test merge method.'''
        mock_pro_config = MagicMock(spec=IProConfig)
        mock_pro_name = MagicMock(spec=IProName)
        mock_template_dir = MagicMock(spec=ITemplateDir)
        mock_context_bundle = MagicMock(spec=ContextBundle)

        bundle1 = ConfigSetupComponentBundle()
        bundle2 = ConfigSetupComponentBundle(
            pro_config=mock_pro_config,
            pro_name=mock_pro_name,
            template_dir=mock_template_dir,
            context_bundle=mock_context_bundle
        )

        bundle1.merge(bundle2)

        self.assertEqual(bundle1.pro_config, mock_pro_config)
        self.assertEqual(bundle1.pro_name, mock_pro_name)
        self.assertEqual(bundle1.template_dir, mock_template_dir)
        self.assertEqual(bundle1.context_bundle, mock_context_bundle)

    def test_to_dict(self) -> None:
        '''Test to_dict method.'''
        mock_pro_config = MagicMock(spec=IProConfig)
        bundle = ConfigSetupComponentBundle(pro_config=mock_pro_config)
        
        bundle_dict = bundle.to_dict()
        self.assertIsInstance(bundle_dict, dict)
        self.assertEqual(bundle_dict['pro_config'], mock_pro_config)
        self.assertIsNone(bundle_dict['pro_name'])


if __name__ == '__main__':
    main()
