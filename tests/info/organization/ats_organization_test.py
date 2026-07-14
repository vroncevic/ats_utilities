# -*- coding: UTF-8 -*-

'''
Module
    ats_organization_test.py
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
    Defines classes OrganizationTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Organization.
Execute
    python3 -m unittest -v ats_organization_test
'''

from unittest import TestCase, main

from ats_utilities.info.organization.iorganization import IOrganization
from ats_utilities.info.organization.engine import Organization
from ats_utilities.exceptions import ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class OrganizationTestCase(TestCase):
    '''
        Defines classes OrganizationTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of Organization.
        Organization unit tests.

        It defines:

            :attributes:
                | instance - API for organization.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_instance_not_none - Test that Organization instance is not None.
                | test_organization_value_is_none_by_default - Test that organization value is None by default.
                | test_organization_try_to_set_none - Test setting organization to None.
                | test_organization_try_to_set_wrong_type - Test wrong type for organization.
                | test_organization_set_to_value - Test setting organization with value.
                | test_organization_set_twice - Test setting organization twice.
                | test_organization_set_then_changed - Test setting organization then changing it.
                | test_organization_not_none_after_set - Test that organization is not None after setting it.
                | test_organization_string_after_set - Test that organization is a string after setting it.
                | test_organization_str_representation - Test string representation of organization.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.instance = Organization()

    def tearDown(self) -> None:
        '''Call after test case.'''
        del self.instance

    def test_instance_not_none(self) -> None:
        '''By default Organization instance is not None.'''
        self.assertIsNotNone(self.instance)
        self.assertIsInstance(self.instance, IOrganization)

    def test_organization_value_is_none_by_default(self) -> None:
        '''Test organization value is None by default.'''
        self.assertIsNone(self.instance.organization)
        self.assertFalse(self.instance.not_none())

    def test_organization_try_to_set_none(self) -> None:
        '''Test setting organization to None.'''
        with self.assertRaises(ATSTypeError):
            self.instance.organization = None

    def test_organization_try_to_set_wrong_type(self) -> None:
        '''Test wrong type for organization.'''
        with self.assertRaises(ATSTypeError):
            self.instance.organization = True

        with self.assertRaises(ATSTypeError):
            self.instance.organization = 123

        with self.assertRaises(ATSTypeError):
            self.instance.organization = [r'MyOrganization']

        with self.assertRaises(ATSTypeError):
            self.instance.organization = (r'MyOrganization',)

        with self.assertRaises(ATSTypeError):
            self.instance.organization = {'organization': r'MyOrganization'}

    def test_organization_set_to_value(self) -> None:
        '''Test setting organization with value.'''
        self.instance.organization = r'MyOrganization'
        self.assertEqual(self.instance.organization, r'MyOrganization')

    def test_organization_set_twice(self) -> None:
        '''Test setting organization twice.'''
        self.instance.organization = r'MyOrganization'
        self.instance.organization = r'MyOrganization'
        self.assertEqual(self.instance.organization, r'MyOrganization')

    def test_organization_set_then_changed(self) -> None:
        '''Test setting organization then changing it.'''
        self.instance.organization = r'MyOrganization'
        self.assertEqual(self.instance.organization, r'MyOrganization')
        self.instance.organization = r'YourOrganization'
        self.assertEqual(self.instance.organization, r'YourOrganization')

    def test_organization_not_none_after_set(self) -> None:
        '''Test that organization is not None after setting it.'''
        self.instance.organization = r'YourOrganization'
        self.assertTrue(self.instance.not_none())

    def test_organization_string_after_set(self) -> None:
        '''Test that organization is a string after setting it.'''
        self.instance.organization = r'YourOrganization'
        self.assertIsInstance(self.instance.organization, str)

    def test_organization_str_representation(self) -> None:
        '''Test string representation of organization.'''
        self.instance.organization = r'YourOrganization'
        self.assertIsInstance(str(self.instance.organization), str)
        self.assertEqual(str(self.instance.organization), r'YourOrganization')
        self.assertNotEqual(str(self.instance.organization), r'MyOrganization')
        self.assertIsInstance(str(self.instance), str)


if __name__ == '__main__':
    main()
