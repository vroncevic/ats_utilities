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
    Unit tests for InfoFactory class.
'''

from __future__ import annotations

import unittest

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextFactory
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.info.setup.bundle import InfoBundle
from ats_utilities.info.info_keys import InfoKeys
from ats_utilities.info.setup.factory import InfoFactory

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class InfoFactoryTest(unittest.TestCase):
    '''
        Defines class InfoFactoryTest with attribute(s) and method(s).
        Tests InfoFactory logic.
    '''

    def test_create_info_bundle_from_dict(self) -> None:
        context_bundle = ContextFactory.create_default_bundle()
        info_data = {
            InfoKeys.ATS_NAME: "ats_utilities",
            InfoKeys.ATS_VERSION: "3.4.4",
            InfoKeys.ATS_BUILD_DATE: "2026-07-18",
            InfoKeys.ATS_LICENCE: "GPLv3",
            InfoKeys.ATS_REPOSITORY: "https://github.com/vroncevic/ats_utilities",
            InfoKeys.ATS_ORGANIZATION: "vroncevic",
            InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE: "True",  # String "True" gets parsed to bool
            InfoKeys.ATS_LOGO_PATH: "/path/to/logo.png",
            InfoKeys.ATS_LOG_FILE: "/path/to/run.log",
            InfoKeys.ATS_INFO_OK: True
        }
        bundle = InfoFactory.create_default_bundle({
            'info': info_data,
            'context_bundle': context_bundle
        })
        self.assertIsInstance(bundle, InfoBundle)
        self.assertEqual(bundle.name.name, "ats_utilities")
        self.assertEqual(bundle.version.version, "3.4.4")
        self.assertEqual(bundle.build_date.build_date, "2026-07-18")
        self.assertEqual(bundle.licence.licence, "GPLv3")
        self.assertEqual(bundle.repository.repository, "https://github.com/vroncevic/ats_utilities")
        self.assertEqual(bundle.organization.organization, "vroncevic")
        self.assertTrue(bundle.use_github.use_github)
        self.assertEqual(bundle.logo.logo, "/path/to/logo.png")
        self.assertEqual(bundle.log_file.log_file, "/path/to/run.log")
        self.assertTrue(bundle.info_ok.info_ok)

        # test backward compatibility method
        bundle_compat = InfoFactory.create_info_bundle_from_dict(info_data, context_bundle)
        self.assertIsInstance(bundle_compat, InfoBundle)

    def test_create_info_bundle_from_dict_invalid(self) -> None:
        context_bundle = ContextFactory.create_default_bundle()
        info_data = {}

        # Context bundle None
        with self.assertRaises(ATSValueError):
            InfoFactory.create_default_bundle({
                'info': info_data,
                'context_bundle': None  # type: ignore
            })

        # Info dict None
        with self.assertRaises(ATSValueError):
            InfoFactory.create_default_bundle({
                'info': None,  # type: ignore
                'context_bundle': context_bundle
            })

        # Invalid types
        with self.assertRaises(ATSTypeError):
            InfoFactory.create_default_bundle({
                'info': info_data,
                'context_bundle': object()  # type: ignore
            })

        with self.assertRaises(ATSTypeError):
            InfoFactory.create_default_bundle({
                'info': "not a dict",  # type: ignore
                'context_bundle': context_bundle
            })

    def test_create_info_bundle_from_dict_edge_cases(self) -> None:
        context_bundle = ContextFactory.create_default_bundle()

        # 1. Use Github infrastructure is boolean False
        info_data_bool = {
            InfoKeys.ATS_NAME: "ats_utilities",
            InfoKeys.ATS_VERSION: "3.4.4",
            InfoKeys.ATS_BUILD_DATE: "2026-07-18",
            InfoKeys.ATS_LICENCE: "GPLv3",
            InfoKeys.ATS_REPOSITORY: "https://github.com/vroncevic/ats_utilities",
            InfoKeys.ATS_ORGANIZATION: "vroncevic",
            InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE: False,  # actual bool
            InfoKeys.ATS_LOGO_PATH: "/path/to/logo.png",
            InfoKeys.ATS_LOG_FILE: "/path/to/run.log",
            InfoKeys.ATS_INFO_OK: True
        }
        bundle = InfoFactory.create_info_bundle_from_dict(info_data_bool, context_bundle)
        self.assertFalse(bundle.use_github.use_github)

        # 2. Use Github infrastructure is string "False"
        info_data_str_false = info_data_bool.copy()
        info_data_str_false[InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE] = "False"
        bundle_str_false = InfoFactory.create_info_bundle_from_dict(info_data_str_false, context_bundle)
        self.assertFalse(bundle_str_false.use_github.use_github)

        # 3. Patch _ATTR_TO_CLASS to return None for a key to hit line 109
        original_attr_to_class = InfoFactory._ATTR_TO_CLASS
        try:
            InfoFactory._ATTR_TO_CLASS = dict(original_attr_to_class)
            InfoFactory._ATTR_TO_CLASS[InfoKeys.ATS_NAME] = None
            with self.assertRaises(TypeError):
                InfoFactory.create_info_bundle_from_dict(info_data_bool, context_bundle)
        finally:
            InfoFactory._ATTR_TO_CLASS = original_attr_to_class


if __name__ == "__main__":
    unittest.main()
