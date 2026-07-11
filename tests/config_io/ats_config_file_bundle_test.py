# -*- coding: UTF-8 -*-

'''
Module
    ats_config_file_bundle_test.py
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
    Creates test cases for checking ConfigFileBundle.
Execute
    python3 -m unittest -v tests/config_io/ats_config_file_bundle_test.py
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import MagicMock

from ats_utilities.config_io.config_file_bundle import ConfigFileBundle
from ats_utilities.config_io.ifile_check import IFileCheck
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


class ConfigFileBundleTestCase(TestCase):
    '''Test cases for ConfigFileBundle.'''

    def test_ats_config_file_bundle(self) -> None:
        '''Test ConfigFileBundle methods.'''
        mock_context = ContextBundle()
        mock_file_checker = MagicMock(spec=IFileCheck)
        mock_file_checker.__class__ = IFileCheck
        bundle1 = ConfigFileBundle()
        bundle2 = ConfigFileBundle(context=mock_context, file_checker=mock_file_checker)

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.context, mock_context)
        self.assertEqual(bundle1.file_checker, mock_file_checker)

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['context']['verbose'], mock_context.verbose)
        self.assertIsInstance(d['context']['checker'], type(mock_context.checker))
        self.assertIsInstance(d['context']['reporter'], type(mock_context.reporter))

    def test_ats_config_file_bundle_validation_errors(self) -> None:
        '''Test ConfigFileBundle validation exceptions.'''
        mock_context = ContextBundle()
        mock_file_checker = MagicMock(spec=IFileCheck)
        mock_file_checker.__class__ = IFileCheck
        fields = {
            'context': mock_context,
            'file_checker': mock_file_checker
        }
        for field in fields:
            kwargs = fields.copy()
            kwargs[field] = None
            bundle = ConfigFileBundle(**kwargs)
            with self.assertRaises(ATSValueError):
                bundle.validate()

    def test_ats_config_file_bundle_merge_type_check(self) -> None:
        '''Test that merge raises error if other is not a ConfigFileBundle.'''
        bundle = ConfigFileBundle()
        with self.assertRaises(ATSTypeError):
            bundle.merge("not_a_config_file_bundle")

    def test_ats_config_file_bundle_merge_with_none(self) -> None:
        '''Test ConfigFileBundle merge with None values.'''
        bundle1 = ConfigFileBundle()
        bundle2 = ConfigFileBundle()
        bundle2.context = None

        with self.assertRaises(ATSValueError):
            bundle1.merge(bundle2)


if __name__ == '__main__':
    main()
