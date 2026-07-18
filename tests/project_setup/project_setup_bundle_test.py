# -*- coding: UTF-8 -*-

'''
Module
    project_setup_bundle_test.py
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
    Unit tests for ProjectSetupBundle class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.project_setup.ipro_config import IProConfig
from ats_utilities.project_setup.ipro_name import IProName
from ats_utilities.project_setup.itemplate_dir import ITemplateDir
from ats_utilities.project_setup.project_setup_bundle import ProjectSetupBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ProjectSetupBundleTest(unittest.TestCase):
    '''
        Defines class ProjectSetupBundleTest with attribute(s) and method(s).
        Tests ProjectSetupBundle dataclass logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init_valid - Tests successful ProjectSetupBundle initialization.
                | test_init_invalid_none - Tests ProjectSetupBundle initialization with None values.
                | test_init_invalid_type - Tests ProjectSetupBundle initialization with wrong types.
                | test_to_dict - Tests ProjectSetupBundle to_dict method.
    '''

    def test_init_valid(self) -> None:
        '''
            Tests successful ProjectSetupBundle initialization.

            :exceptions: None.
        '''
        mock_pro_name = MagicMock(spec=IProName)
        mock_pro_config = MagicMock(spec=IProConfig)
        mock_template_dir = MagicMock(spec=ITemplateDir)
        mock_context = MagicMock(spec=ContextBundle)

        try:
            bundle = ProjectSetupBundle(
                pro_name=mock_pro_name,
                pro_config=mock_pro_config,
                template_dir=mock_template_dir,
                context_bundle=mock_context
            )
            self.assertIs(bundle.pro_name, mock_pro_name)
            self.assertIs(bundle.pro_config, mock_pro_config)
            self.assertIs(bundle.template_dir, mock_template_dir)
            self.assertIs(bundle.context_bundle, mock_context)
        except (ATSValueError, ATSTypeError):
            self.fail("Failed to instantiate ProjectSetupBundle with valid arguments.")

    def test_init_invalid_none(self) -> None:
        '''
            Tests ProjectSetupBundle initialization with None values.

            :exceptions: None.
        '''
        mock_pro_name = MagicMock(spec=IProName)
        mock_pro_config = MagicMock(spec=IProConfig)
        mock_template_dir = MagicMock(spec=ITemplateDir)
        mock_context = MagicMock(spec=ContextBundle)

        with self.assertRaises(ATSValueError):
            ProjectSetupBundle(pro_name=None, pro_config=mock_pro_config, template_dir=mock_template_dir, context_bundle=mock_context)  # type: ignore

        with self.assertRaises(ATSValueError):
            ProjectSetupBundle(pro_name=mock_pro_name, pro_config=None, template_dir=mock_template_dir, context_bundle=mock_context)  # type: ignore

        with self.assertRaises(ATSValueError):
            ProjectSetupBundle(pro_name=mock_pro_name, pro_config=mock_pro_config, template_dir=None, context_bundle=mock_context)  # type: ignore

        with self.assertRaises(ATSValueError):
            ProjectSetupBundle(pro_name=mock_pro_name, pro_config=mock_pro_config, template_dir=mock_template_dir, context_bundle=None)  # type: ignore

    def test_init_invalid_type(self) -> None:
        '''
            Tests ProjectSetupBundle initialization with wrong types.

            :exceptions: None.
        '''
        mock_pro_name = MagicMock(spec=IProName)
        mock_pro_config = MagicMock(spec=IProConfig)
        mock_template_dir = MagicMock(spec=ITemplateDir)
        mock_context = MagicMock(spec=ContextBundle)

        with self.assertRaises(ATSTypeError):
            ProjectSetupBundle(pro_name="not IProName", pro_config=mock_pro_config, template_dir=mock_template_dir, context_bundle=mock_context)  # type: ignore

        with self.assertRaises(ATSTypeError):
            ProjectSetupBundle(pro_name=mock_pro_name, pro_config="not IProConfig", template_dir=mock_template_dir, context_bundle=mock_context)  # type: ignore

        with self.assertRaises(ATSTypeError):
            ProjectSetupBundle(pro_name=mock_pro_name, pro_config=mock_pro_config, template_dir="not ITemplateDir", context_bundle=mock_context)  # type: ignore

        with self.assertRaises(ATSTypeError):
            ProjectSetupBundle(pro_name=mock_pro_name, pro_config=mock_pro_config, template_dir=mock_template_dir, context_bundle="not ContextBundle")  # type: ignore

    def test_to_dict(self) -> None:
        '''
            Tests ProjectSetupBundle to_dict method.

            :exceptions: None.
        '''
        mock_pro_name = MagicMock(spec=IProName)
        mock_pro_config = MagicMock(spec=IProConfig)
        mock_template_dir = MagicMock(spec=ITemplateDir)
        mock_context = MagicMock(spec=ContextBundle)

        bundle = ProjectSetupBundle(
            pro_name=mock_pro_name,
            pro_config=mock_pro_config,
            template_dir=mock_template_dir,
            context_bundle=mock_context
        )
        expected = {
            "pro_name": mock_pro_name,
            "pro_config": mock_pro_config,
            "template_dir": mock_template_dir,
            "context_bundle": mock_context
        }
        self.assertEqual(bundle.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
