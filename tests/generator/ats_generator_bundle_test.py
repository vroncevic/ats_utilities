# -*- coding: UTF-8 -*-

'''
Module
    ats_generator_bundle_test.py
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
    Creates test cases for checking GeneratorBundle.
Execute
    python3 -m unittest -v tests/generator/ats_generator_bundle_test.py
'''

from __future__ import annotations

from unittest import TestCase, main

from ats_utilities.generator.generator_bundle import GeneratorBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '1.0.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class GeneratorBundleTestCase(TestCase):
    '''Test cases for GeneratorBundle.'''

    def test_generator_bundle_methods(self) -> None:
        '''Test GeneratorBundle methods.'''
        bundle1 = GeneratorBundle(
            archive_path='a.tgz',
            target_dir='tmp',
            template_key='key',
            scheme={},
            template_values={}
        )
        bundle2 = GeneratorBundle(
            archive_path='b.tgz',
            target_dir='out',
            template_key='key2',
            scheme={'a': 'b'},
            template_values={'x': 'y'}
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.archive_path, 'b.tgz')
        self.assertEqual(bundle1.target_dir, 'out')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['archive_path'], 'b.tgz')

    def test_generator_bundle_validation_errors(self) -> None:
        '''Test GeneratorBundle validation exceptions.'''
        # Missing values (None)
        fields = {
            'archive_path': 'a.tgz',
            'target_dir': 'tmp',
            'template_key': 'key',
            'scheme': {},
            'template_values': {}
        }
        for field in fields:
            kwargs = fields.copy()
            kwargs[field] = None
            bundle = GeneratorBundle(**kwargs)
            with self.assertRaises(ATSValueError):
                bundle.validate()

        # Type errors
        type_checks = {
            'archive_path': 123,
            'target_dir': 123,
            'template_key': 123,
            'scheme': 123,
            'template_values': 123
        }
        for field, invalid_val in type_checks.items():
            kwargs = fields.copy()
            kwargs[field] = invalid_val
            bundle = GeneratorBundle(**kwargs)
            with self.assertRaises(ATSTypeError):
                bundle.validate()

    def test_generator_bundle_merge_type_check(self) -> None:
        '''Test that merge raises error if other is not a GeneratorBundle.'''
        bundle = GeneratorBundle(
            archive_path='a.tgz',
            target_dir='tmp',
            template_key='key',
            scheme={},
            template_values={}
        )
        with self.assertRaises(ATSTypeError):
            bundle.merge("not_a_generator_bundle")

    def test_generator_bundle_merge_with_none(self) -> None:
        '''Test GeneratorBundle merge with None values.'''
        bundle1 = GeneratorBundle(
            archive_path='a.tgz',
            target_dir='tmp',
            template_key='key',
            scheme={},
            template_values={}
        )
        bundle2 = GeneratorBundle(
            archive_path='b.tgz',
            target_dir='tmp2',
            template_key='key2',
            scheme={},
            template_values={}
        )
        bundle2.archive_path = None
        bundle1.merge(bundle2)
        self.assertEqual(bundle1.archive_path, 'a.tgz')



if __name__ == '__main__':
    main()
