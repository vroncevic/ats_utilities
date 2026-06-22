# -*- coding: UTF-8 -*-

'''
Module
    ats_factory_component_test.py
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
    Defines class ATSFactoryComponentTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of factory_component functions.
Execute
    python3 -m unittest -v ats_factory_component_test
'''

from unittest import TestCase, main
from unittest.mock import MagicMock
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class DummyComponent:
    '''
        Simple dummy class for component testing.

        It defines:

            :attributes: None
            :methods: None
    '''

    def __init__(self, val: str = 'default') -> None:
        '''
            Initial constructor.

            :param val: Dummy value
            :type val: <str>
            :exceptions: None
        '''
        self.val = val


class ATSFactoryComponentTestCase(TestCase):
    '''
        Defines class ATSFactoryComponentTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of factory_component functions.
        Factory component functions unit tests.

        It defines:

            :attributes: None
            :methods:
                | test_make_component_existing - Test make_component with existing instance.
                | test_make_component_new - Test make_component instantiating default class.
                | test_make_component_args - Test make_component instantiating default class with args.
                | test_validate_component_success - Test validate_component with valid type.
                | test_validate_component_failure - Test validate_component with invalid type.
                | test_validate_component_mock_success - Test validate_component with mock object.
    '''

    def test_make_component_existing(self) -> None:
        '''
            Test make_component with existing instance.

            :return: None.
            :rtype: <None>
            :exceptions: None.
        '''
        existing = DummyComponent('existing')
        res = make_component(existing, DummyComponent)
        self.assertIs(res, existing)
        self.assertEqual(res.val, 'existing')

    def test_make_component_new(self) -> None:
        '''
            Test make_component instantiating default class.

            :return: None.
            :rtype: <None>
            :exceptions: None.
        '''
        res = make_component(None, DummyComponent)
        self.assertIsInstance(res, DummyComponent)
        self.assertEqual(res.val, 'default')

    def test_make_component_args(self) -> None:
        '''
            Test make_component instantiating default class with args.

            :return: None.
            :rtype: <None>
            :exceptions: None.
        '''
        res = make_component(None, DummyComponent, {'val': 'custom'})
        self.assertIsInstance(res, DummyComponent)
        self.assertEqual(res.val, 'custom')

    def test_validate_component_success(self) -> None:
        '''
            Test validate_component with valid type.

            :return: None.
            :rtype: <None>
            :exceptions: None.
        '''
        instance = DummyComponent()
        validate_component(instance, DummyComponent)

    def test_validate_component_mock_success(self) -> None:
        '''
            Test validate_component with mock object.

            :return: None.
            :rtype: <None>
            :exceptions: None.
        '''
        instance = MagicMock(spec=DummyComponent)
        validate_component(instance, DummyComponent)

    def test_validate_component_failure(self) -> None:
        '''
            Test validate_component with invalid type.

            :return: None.
            :rtype: <None>
            :exceptions: None.
        '''
        instance = "not a dummy component"
        with self.assertRaises(ATSTypeError):
            validate_component(instance, DummyComponent)


if __name__ == '__main__':
    main()

