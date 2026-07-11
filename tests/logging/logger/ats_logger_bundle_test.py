# -*- coding: UTF-8 -*-

'''
Module
    ats_logger_bundle_test.py
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
    Creates test cases for checking LoggerBundle.
'''

from __future__ import annotations

from unittest import TestCase, main

from ats_utilities.logging.logger.logger_bundle import LoggerBundle
from ats_utilities.exceptions import ATSValueError, ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '1.0.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class LoggerBundleTestCase(TestCase):
    '''Test cases for LoggerBundle.'''

    def test_logger_bundle(self) -> None:
        '''Test LoggerBundle methods.'''
        bundle1 = LoggerBundle()
        bundle2 = LoggerBundle(name='test_logger', configure_logging=False, log_stdout=False, log_file='test.log')

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.name, 'test_logger')
        self.assertFalse(bundle1.configure_logging)
        self.assertFalse(bundle1.log_stdout)
        self.assertEqual(bundle1.log_file, 'test.log')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['name'], 'test_logger')

    def test_logger_bundle_validation_errors(self) -> None:
        '''Test LoggerBundle validation exceptions.'''
        fields = {
            'name': 'test_logger',
            'configure_logging': True,
            'log_stdout': True,
            'log_file': 'test.log'
        }
        for field in fields:
            kwargs = fields.copy()
            kwargs[field] = None
            bundle = LoggerBundle(**kwargs)
            with self.assertRaises(ATSValueError):
                bundle.validate()

        # Type validation errors
        bundle = LoggerBundle(name='test_logger', configure_logging='not_bool', log_file='test.log')
        with self.assertRaises(ATSTypeError):
            bundle.validate()

        bundle = LoggerBundle(name='test_logger', log_stdout='not_bool', log_file='test.log')
        with self.assertRaises(ATSTypeError):
            bundle.validate()

        bundle = LoggerBundle(name=123, log_stdout=True, log_file='test.log')
        with self.assertRaises(ATSTypeError):
            bundle.validate()

        bundle = LoggerBundle(name='test_logger', log_stdout=True, log_file=123)
        with self.assertRaises(ATSTypeError):
            bundle.validate()

        with self.assertRaises(ATSTypeError):
            bundle.merge("not_a_logger_bundle")

    def test_logger_bundle_merge_with_none(self) -> None:
        '''Test LoggerBundle merge with None values.'''
        bundle1 = LoggerBundle(name='test_logger', log_file='test.log')
        bundle2 = LoggerBundle(name='test_logger2', log_file='test2.log')
        bundle2.name = None
        bundle1.merge(bundle2)
        self.assertEqual(bundle1.name, 'test_logger')



if __name__ == '__main__':
    main()
