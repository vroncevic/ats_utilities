# -*- coding: UTF-8 -*-

'''
Module
    ats_config_loader_bundle_test.py
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
    Creates test cases for checking ConfigLoaderBundle.
Execute
    python3 -m unittest -v tests/config_io/ats_config_loader_bundle_test.py
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import MagicMock

from ats_utilities.config_io.config_loader_bundle import ConfigLoaderBundle
from ats_utilities.config_io.config_file_bundle import ConfigFileBundle
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.json.ijson_processor import IJSONProcessor
from ats_utilities.exceptions import ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '1.0.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ConfigLoaderBundleTestCase(TestCase):
    '''Test cases for ConfigLoaderBundle.'''

    def test_ats_config_loader_bundle(self) -> None:
        '''Test ConfigLoaderBundle methods.'''
        mock_config2object = MagicMock(spec=IRead)
        mock_config2object.__class__ = IRead
        mock_config_bundle = MagicMock(spec=ConfigFileBundle)
        mock_config_bundle.__class__ = ConfigFileBundle
        mock_processor = MagicMock(spec=IJSONProcessor)
        mock_processor.__class__ = IJSONProcessor
        bundle1 = ConfigLoaderBundle()
        bundle2 = ConfigLoaderBundle(
            info_file='config.json',
            config2object=mock_config2object,
            config_bundle=mock_config_bundle,
            processor=mock_processor
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.info_file, 'config.json')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['info_file'], 'config.json')

    def test_ats_config_loader_bundle_validation_errors(self) -> None:
        '''Test ConfigLoaderBundle validation exceptions.'''
        mock_config2object = MagicMock(spec=IRead)
        mock_config2object.__class__ = IRead
        mock_config_bundle = MagicMock(spec=ConfigFileBundle)
        mock_config_bundle.__class__ = ConfigFileBundle
        mock_processor = MagicMock(spec=IJSONProcessor)
        mock_processor.__class__ = IJSONProcessor
        fields = {
            'info_file': 'config.json',
            'config2object': mock_config2object,
            'config_bundle': mock_config_bundle,
            'processor': mock_processor
        }
        for field in fields:
            kwargs = fields.copy()
            kwargs[field] = None
            bundle = ConfigLoaderBundle(**kwargs)
            with self.assertRaises(ATSValueError):
                bundle.validate()

    def test_ats_config_loader_bundle_merge_type_check(self) -> None:
        '''Test that merge raises error if other is not a ConfigLoaderBundle.'''
        bundle = ConfigLoaderBundle()
        with self.assertRaises(ATSTypeError):
            bundle.merge("not_a_config_loader_bundle")

    def test_ats_config_loader_bundle_merge_with_none(self) -> None:
        '''Test ConfigLoaderBundle merge with None values.'''
        bundle1 = ConfigLoaderBundle()
        bundle2 = ConfigLoaderBundle()
        bundle2.info_file = None

        with self.assertRaises(ATSValueError):
            bundle1.merge(bundle2)


if __name__ == '__main__':
    main()
