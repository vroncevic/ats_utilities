# -*- coding: UTF-8 -*-

'''
Module
    ats_scheme_loader_test.py
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
    Creates test cases for checking SchemeLoader.
Execute
    python3 -m unittest -v tests/generator/scheme/ats_scheme_loader_test.py
'''

from __future__ import annotations

import tempfile
from unittest import TestCase, main, mock

from ats_utilities.generator.scheme.scheme_loader import SchemeLoader
from ats_utilities.exceptions import ATSGeneratorError, ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class SchemeLoaderTestCase(TestCase):
    '''Test cases for SchemeLoader.'''

    def test_scheme_loader_failures(self) -> None:
        '''Test SchemeLoader error handling and edge cases.'''
        loader = SchemeLoader()

        # Wrong type
        with self.assertRaises(ATSTypeError):
            loader.load(123)  # type: ignore

        # Non-existent path
        with self.assertRaises(ATSValueError):
            loader.load('non_existent.json')

        # Unsupported format (suffix not .json)
        with tempfile.NamedTemporaryFile(suffix='.txt') as tmp:
            with self.assertRaises(ATSValueError):
                loader.load(tmp.name)

        # Failed setup config loader (returns None)
        with tempfile.NamedTemporaryFile(suffix='.json') as tmp:
            with mock.patch('ats_utilities.generator.scheme.scheme_loader.ConfigLoader.setup_loader', return_value=None):
                with self.assertRaises(ATSGeneratorError):
                    loader.load(tmp.name)

        # Failed setup config loader (raises Exception)
        with tempfile.NamedTemporaryFile(suffix='.json') as tmp:
            with mock.patch('ats_utilities.generator.scheme.scheme_loader.ConfigLoader.setup_loader', side_effect=Exception('Load failed')):
                with self.assertRaises(ATSGeneratorError):
                    loader.load(tmp.name)

        # Return dict when dict is passed
        self.assertEqual(loader.load({'a': 'b'}), {'a': 'b'})


if __name__ == '__main__':
    main()
