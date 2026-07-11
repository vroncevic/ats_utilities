# -*- coding: UTF-8 -*-

'''
Module
    ats_file_bundle_test.py
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
    Creates test cases for checking FileBundle.
Execute
    python3 -m unittest -v tests/config_io/ats_file_bundle_test.py
'''

from __future__ import annotations

from unittest import TestCase, main
from ats_utilities.config_io.file_bundle import FileBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '1.0.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class FileBundleTestCase(TestCase):
    '''Test cases for FileBundle.'''

    def test_ats_file_bundle(self) -> None:
        '''Test FileBundle methods.'''
        bundle1 = FileBundle()
        bundle2 = FileBundle(file_path='a.txt', file_mode='w', file_format='txt')

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.file_path, 'a.txt')
        self.assertEqual(bundle1.file_mode, 'w')
        self.assertEqual(bundle1.file_format, 'txt')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['file_path'], 'a.txt')

    def test_ats_file_bundle_validation_errors(self) -> None:
        '''Test FileBundle validation exceptions.'''
        fields = {
            'file_path': 'a.txt',
            'file_mode': 'w',
            'file_format': 'txt'
        }
        for field in fields:
            kwargs = fields.copy()
            kwargs[field] = None
            bundle = FileBundle(**kwargs)
            with self.assertRaises(ATSValueError):
                bundle.validate()

    def test_ats_file_bundle_merge_type_check(self) -> None:
        '''Test that merge raises error if other is not a FileBundle.'''
        bundle = FileBundle()
        with self.assertRaises(ATSTypeError):
            bundle.merge("not_a_file_bundle")

    def test_ats_file_bundle_merge_with_none(self) -> None:
        '''Test FileBundle merge with None values.'''
        bundle1 = FileBundle()
        bundle2 = FileBundle()
        bundle2.file_path = None
        with self.assertRaises(ATSValueError):
            bundle1.merge(bundle2)

if __name__ == '__main__':
    main()
