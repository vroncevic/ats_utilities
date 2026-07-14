# -*- coding: UTF-8 -*-

'''
Module
    ats_component_bundle_test.py
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
    Creates test cases for checking InfoComponentBundle.
Execute
    python3 -m unittest -v tests/info/ats_component_bundle_test.py
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import MagicMock

from ats_utilities.info.component_bundle import InfoComponentBundle
from ats_utilities.info.name.iname import IName
from ats_utilities.info.version.iversion import IVersion
from ats_utilities.info.licence.ilicence import ILicence
from ats_utilities.info.build_date.ibuild_date import IBuildDate
from ats_utilities.info.repository.irepository import IRepository
from ats_utilities.info.organization.iorganization import IOrganization
from ats_utilities.info.use_github.iuse_github import IUseGitHub
from ats_utilities.info.logo.ilogo import ILogo
from ats_utilities.info.info_ok.iinfo_ok import IInfoOk
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class InfoComponentBundleTestCase(TestCase):
    '''
        Defines class InfoComponentBundleTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of InfoComponentBundle.
        InfoComponentBundle unit tests.

        It defines:

            :attributes:
                | instance - The InfoComponentBundle instance.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_instance_is_not_none - Test instance is not None.
                | test_info_component_bundle - Test InfoComponentBundle methods.
                | test_info_component_bundle_validation_errors - Test InfoComponentBundle validation errors.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.instance = InfoComponentBundle()

    def tearDown(self) -> None:
        '''Call after test case.'''
        del self.instance

    def test_instance_is_not_none(self) -> None:
        '''By default InfoComponentBundle instance is not None.'''
        self.assertIsNotNone(self.instance)
        self.assertIsNotNone(self.instance.name)
        self.assertIsNotNone(self.instance.version)
        self.assertIsNotNone(self.instance.licence)
        self.assertIsNotNone(self.instance.build_date)
        self.assertIsNotNone(self.instance.repository)
        self.assertIsNotNone(self.instance.organization)
        self.assertIsNotNone(self.instance.use_github)
        self.assertIsNotNone(self.instance.logo)
        self.assertIsNotNone(self.instance.info_ok)
        self.assertIsNotNone(self.instance.context_bundle)
        self.assertIsInstance(self.instance, InfoComponentBundle)
        self.assertIsInstance(self.instance.name, IName)
        self.assertIsInstance(self.instance.version, IVersion)
        self.assertIsInstance(self.instance.licence, ILicence)
        self.assertIsInstance(self.instance.build_date, IBuildDate)
        self.assertIsInstance(self.instance.repository, IRepository)
        self.assertIsInstance(self.instance.organization, IOrganization)
        self.assertIsInstance(self.instance.use_github, IUseGitHub)
        self.assertIsInstance(self.instance.logo, ILogo)
        self.assertIsInstance(self.instance.info_ok, IInfoOk)
        self.assertIsInstance(self.instance.context_bundle, ContextBundle)

    def test_info_component_bundle(self) -> None:
        '''Test InfoComponentBundle methods.'''
        mock_name = MagicMock(spec=IName)
        mock_version = MagicMock(spec=IVersion)
        mock_licence = MagicMock(spec=ILicence)
        mock_build_date = MagicMock(spec=IBuildDate)
        mock_repository = MagicMock(spec=IRepository)
        mock_organization = MagicMock(spec=IOrganization)
        mock_use_github = MagicMock(spec=IUseGitHub)
        mock_logo_path = MagicMock(spec=ILogo)
        mock_info_ok = MagicMock(spec=IInfoOk)

        bundle = InfoComponentBundle(
            name=mock_name,
            version=mock_version,
            licence=mock_licence,
            build_date=mock_build_date,
            repository=mock_repository,
            organization=mock_organization,
            use_github=mock_use_github,
            logo=mock_logo_path,
            info_ok=mock_info_ok
        )

        bundle.validate()
        d = bundle.to_dict()
        self.assertEqual(d['name'], mock_name)

        # Test merge
        bundle1 = InfoComponentBundle()
        bundle1.merge(bundle)
        self.assertEqual(bundle1.name, mock_name)
        self.assertEqual(bundle1.version, mock_version)

    def test_info_component_bundle_validation_errors(self) -> None:
        '''Test InfoComponentBundle validation exceptions.'''
        mock_name = MagicMock(spec=IName)
        mock_version = MagicMock(spec=IVersion)
        mock_licence = MagicMock(spec=ILicence)
        mock_build_date = MagicMock(spec=IBuildDate)
        mock_repository = MagicMock(spec=IRepository)
        mock_organization = MagicMock(spec=IOrganization)
        mock_use_github = MagicMock(spec=IUseGitHub)
        mock_logo = MagicMock(spec=ILogo)
        mock_info_ok = MagicMock(spec=IInfoOk)

        fields = {
            'name': mock_name,
            'version': mock_version,
            'licence': mock_licence,
            'build_date': mock_build_date,
            'repository': mock_repository,
            'organization': mock_organization,
            'use_github': mock_use_github,
            'logo': mock_logo,
            'info_ok': mock_info_ok
        }

        # Test each required field missing raises ValueError
        for field in fields:
            bundle = InfoComponentBundle(**fields)
            setattr(bundle, field, None)

            with self.assertRaises(ATSValueError):
                bundle.validate()

    def test_info_component_bundle_type_validation_errors(self) -> None:
        '''Test InfoComponentBundle validation exceptions.'''
        mock_name = MagicMock(spec=IName)
        mock_version = MagicMock(spec=IVersion)
        mock_licence = MagicMock(spec=ILicence)
        mock_build_date = MagicMock(spec=IBuildDate)
        mock_repository = MagicMock(spec=IRepository)
        mock_organization = MagicMock(spec=IOrganization)
        mock_use_github = MagicMock(spec=IUseGitHub)
        mock_logo = MagicMock(spec=ILogo)
        mock_info_ok = MagicMock(spec=ILogo)

        fields = {
            'name': mock_name,
            'version': mock_version,
            'licence': mock_licence,
            'build_date': mock_build_date,
            'repository': mock_repository,
            'organization': mock_organization,
            'use_github': mock_use_github,
            'logo': mock_logo,
            'info_ok': mock_info_ok
        }

        # Test each required field missing raises ValueError
        bundle = InfoComponentBundle(**fields)
        bundle.context_bundle = MagicMock(spec=ContextBundle)

        with self.assertRaises(ATSTypeError):
            bundle.validate()

    def test_info_component_bundle_merge_with_none(self) -> None:
        '''Test InfoComponentBundle merge with None values.'''
        bundle1 = InfoComponentBundle()
        bundle2 = InfoComponentBundle()
        bundle2.name = None
        bundle1.merge(bundle2)
        self.assertIsNotNone(bundle1.name)



if __name__ == '__main__':
    main()
