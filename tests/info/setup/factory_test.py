# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
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
    Unit tests for InfoBundleFactory class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.info.setup.factory import InfoBundleFactory
from ats_utilities.info.setup.keys import InfoBundleKeys
from ats_utilities.info.setup.options import InfoBundleOptions
from ats_utilities.context.factory import ContextBundleFactory
from ats_utilities.info.setup.bundle import InfoBundle


class TestInfoFactory(unittest.TestCase):
    """Unit tests for the InfoBundleFactory class."""

    def setUp(self) -> None:
        """Set up options and mock objects for testing."""
        self.context_bundle = ContextBundleFactory.create_bundle()
        self.info_data = {
            InfoBundleKeys.ATS_NAME: "ats_utilities",
            InfoBundleKeys.ATS_VERSION: "3.4.6",
            InfoBundleKeys.ATS_BUILD_DATE: "2026-08-01",
            InfoBundleKeys.ATS_LICENCE: "GPL-3.0",
            InfoBundleKeys.ATS_INFO_OK: True
        }

        self.options = InfoBundleOptions(
            info=self.info_data,
            context_bundle=self.context_bundle
        )

    @patch("ats_utilities.info.setup.factory.InfoBundleRegistry")
    @patch("ats_utilities.info.setup.factory.InfoBundleOptionsValidator")
    def test_create_bundle(self, mock_val: MagicMock, mock_registry: MagicMock) -> None:
        """Test that create_bundle converts options correctly and calls InfoBundleRegistry."""
        mock_bundle = MagicMock(spec=InfoBundle)
        mock_registry.create_bundle.return_value = mock_bundle

        result = InfoBundleFactory.create_bundle(self.options)

        mock_val.validate.assert_called_once_with(self.options)
        mock_registry.create_bundle.assert_called_once()
        self.assertEqual(result, mock_bundle)


if __name__ == '__main__':
    unittest.main()
