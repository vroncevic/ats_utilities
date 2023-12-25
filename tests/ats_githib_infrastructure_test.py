# -*- coding: UTF-8 -*-

'''
Module
    ats_github_infrastructure_test.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class ATSGitHubTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of termanl properties.
Execute
    python3 -m unittest -v ats_github_infrastructure_test
'''

import sys
from typing import List
from unittest import TestCase, main

try:
    from ats_utilities.splash.github_infrastructure import GitHubInfrastructure
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.1.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSGitHubTestCase(TestCase):
    '''
        Defines class ATSGitHubTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of termanl properties.
        GitHubInfrastructure unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_create - Test for create.
                | test_none_property - Test None splash property.
                | test_get_info - Test get info.
                | test_get_issue - Test get issue info.
                | test_get_author - Test get author info.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_create(self) -> None:
        '''Test for create'''
        splash_property: dict[str, str] = {
            'ats_organization': 'App Example',
            'ats_repository': 'app_example'
        }
        self.assertIsNotNone(GitHubInfrastructure(splash_property))

    def test_none_property(self) -> None:
        '''Test None splash property'''
        with self.assertRaises(ATSTypeError):
            GitHubInfrastructure(None)  # type: ignore

    def test_get_info(self) -> None:
        '''Test get info'''
        info: GitHubInfrastructure = GitHubInfrastructure(
            {
                'ats_organization': 'App Example',
                'ats_repository': 'app_example'
            }
        )
        self.assertIsNotNone(info.get_info_text())

    def test_get_issue(self) -> None:
        '''Test get issue info'''
        info: GitHubInfrastructure = GitHubInfrastructure(
            {
                'ats_organization': 'App Example',
                'ats_repository': 'app_example'
            }
        )
        self.assertIsNotNone(info.get_issue_text())

    def test_get_author(self) -> None:
        '''Test get author info'''
        info: GitHubInfrastructure = GitHubInfrastructure(
            {
                'ats_organization': 'App Example',
                'ats_repository': 'app_example'
            }
        )
        self.assertIsNotNone(info.get_author_text())


if __name__ == '__main__':
    main()
