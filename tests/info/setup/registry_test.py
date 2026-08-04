# -*- coding: UTF-8 -*-

'''
Module
    registry_test.py
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
    Unit tests for InfoBundleRegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.info.setup.registry import InfoBundleRegistry
from ats_utilities.info.setup.bundle import InfoBundle
from ats_utilities.info.setup.dependencies import InfoBundleDependencies
from ats_utilities.info.name.iname import IName
from ats_utilities.info.version.iversion import IVersion
from ats_utilities.info.licence.ilicence import ILicence
from ats_utilities.info.build_date.ibuild_date import IBuildDate
from ats_utilities.info.info_ok.iinfo_ok import IInfoOk
from ats_utilities.context.bundle import ContextBundle


@patch("ats_utilities.info.setup.registry.InfoBundleValidator")
@patch("ats_utilities.info.setup.registry.InfoBundleDependenciesValidator")
class InfoRegistryTest(unittest.TestCase):
    '''
        Defines class InfoRegistryTest with attribute(s) and method(s).
        Tests InfoBundleRegistry logic.
    '''

    def test_create_bundle(self, mock_dep_val: MagicMock, mock_val: MagicMock) -> None:
        mock_context_bundle = MagicMock(spec=ContextBundle)
        mock_name = MagicMock(spec=IName)
        mock_version = MagicMock(spec=IVersion)
        mock_licence = MagicMock(spec=ILicence)
        mock_build_date = MagicMock(spec=IBuildDate)
        mock_info_ok = MagicMock(spec=IInfoOk)

        params = InfoBundleDependencies(
            name=mock_name,
            version=mock_version,
            licence=mock_licence,
            build_date=mock_build_date,
            info_ok=mock_info_ok,
            context_bundle=mock_context_bundle
        )

        bundle = InfoBundleRegistry.create_bundle(params)
        self.assertIsInstance(bundle, InfoBundle)
        self.assertEqual(bundle.name, mock_name)
        self.assertEqual(bundle.version, mock_version)
        self.assertEqual(bundle.licence, mock_licence)
        self.assertEqual(bundle.build_date, mock_build_date)
        self.assertEqual(bundle.info_ok, mock_info_ok)
        self.assertEqual(bundle.context_bundle, mock_context_bundle)

        mock_dep_val.validate.assert_called_once_with(params)
        mock_val.validate.assert_called_once_with(bundle)


if __name__ == '__main__':
    unittest.main()
