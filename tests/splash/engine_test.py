# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
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
    Unit tests for SplashManager class.
'''

from __future__ import annotations

import os
import tempfile
import unittest
from unittest.mock import patch, MagicMock

from ats_utilities.context.factory import ContextFactory
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.splash.engine import SplashManager
from ats_utilities.splash.data import CenterData
from ats_utilities.info.setup.keys import InfoKeys
from ats_utilities.splash.setup.factory import SplashFactory
from ats_utilities.splash.setup.options import SplashOptions
from ats_utilities.splash.progressbar.progress_bar import ProgressBar
from ats_utilities.splash.setup.bundle import SplashBundle
from ats_utilities.splash.property.isplash_property import ISplashProperty
from ats_utilities.splash.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.splash.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splash.progressbar.iprogress_bar import IProgressBar
from ats_utilities.context.bundle import ContextBundle


class EngineTest(unittest.TestCase):
    '''
        Defines class EngineTest with attribute(s) and method(s).
        Tests SplashManager logic.
    '''

    def setUp(self) -> None:
        self.context_bundle = ContextFactory.create_bundle()
        # Create a temporary file to act as the logo
        self.temp_logo = tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8")
        self.temp_logo.write("LOGO LINE 1\n\nLOGO LINE 2\n")
        self.temp_logo.close()
        
        # Patch ProgressBar.__del__ to prevent non-deterministic GC stdout.write calls
        self._orig_pb_del = ProgressBar.__del__
        ProgressBar.__del__ = lambda self: None

    def tearDown(self) -> None:
        ProgressBar.__del__ = self._orig_pb_del
        try:
            os.remove(self.temp_logo.name)
        except OSError:
            ...

    def _get_valid_prop(self) -> dict[str, object]:
        return {
            "enabled": True,
            InfoKeys.ATS_NAME: "ats_utilities",
            InfoKeys.ATS_REPOSITORY: "ats_utilities",
            InfoKeys.ATS_ORGANIZATION: "vroncevic",
            InfoKeys.ATS_LOGO_PATH: self.temp_logo.name,
            InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE: True
        }

    def test_init_invalid(self) -> None:
        with self.assertRaises(ATSValueError):
            SplashManager(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            SplashManager(object())  # type: ignore

    @patch("sys.stdout.write")
    @patch("sys.stdout.flush")
    def test_splasher_disabled(self, mock_flush: MagicMock, mock_write: MagicMock) -> None:
        prop = {"enabled": False}
        options = SplashOptions(prop=prop, context_bundle=self.context_bundle)
        bundle = SplashFactory.create_bundle(options)
        splasher = SplashManager(bundle)
        self.assertTrue(splasher.is_initialized())
        self.assertIs(splasher.get_context(), self.context_bundle)
        splasher.show()
        mock_write.assert_not_called()

    @patch("sys.stdout.write")
    @patch("sys.stdout.flush")
    @patch("time.sleep")
    def test_splasher_github_valid(self, mock_sleep: MagicMock, mock_flush: MagicMock, mock_write: MagicMock) -> None:
        prop = self._get_valid_prop()
        options = SplashOptions(prop=prop, context_bundle=self.context_bundle)
        bundle = SplashFactory.create_bundle(options)
        splasher = SplashManager(bundle)
        self.assertTrue(splasher.is_initialized())
        splasher.show()

        # Check logo lines and infrastructure texts are printed
        printed_content = "".join(call[0][0] for call in mock_write.call_args_list)
        self.assertIn("LOGO LINE 1", printed_content)
        self.assertIn("github.io/ats_utilities", printed_content)
        self.assertIn("github.io/issue", printed_content)
        self.assertIn("vroncevic.github.io", printed_content)

    @patch("sys.stdout.write")
    @patch("sys.stdout.flush")
    @patch("time.sleep")
    @patch("builtins.open")
    def test_splasher_github_invalid_logo(self, mock_open: MagicMock, mock_sleep: MagicMock, mock_flush: MagicMock, mock_write: MagicMock) -> None:
        mock_open.side_effect = OSError("failed to read logo")
        prop = self._get_valid_prop()
        options = SplashOptions(prop=prop, context_bundle=self.context_bundle)
        # Skip validate file exists check in factory by patching it
        with patch("ats_utilities.splash.setup.validator.check_file_exists"):
            bundle = SplashFactory.create_bundle(options)
        splasher = SplashManager(bundle)
        with self.assertRaises(ATSValueError):
            splasher.show()

    @patch("sys.stdout.write")
    @patch("sys.stdout.flush")
    @patch("time.sleep")
    def test_splasher_external_valid(self, mock_sleep: MagicMock, mock_flush: MagicMock, mock_write: MagicMock) -> None:
        prop = self._get_valid_prop()
        prop[InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE] = False
        options = SplashOptions(prop=prop, context_bundle=self.context_bundle)
        bundle = SplashFactory.create_bundle(options)
        splasher = SplashManager(bundle)
        self.assertTrue(splasher.is_initialized())
        splasher.show()

        # Check external texts are printed
        printed_content = "".join(call[0][0] for call in mock_write.call_args_list)
        self.assertIn("ats_utilities", printed_content)
        self.assertIn("ats_utilities", printed_content)
        self.assertIn("vroncevic", printed_content)

    @patch("sys.stdout.write")
    def test_center_disabled_splash(self, mock_write: MagicMock) -> None:
        prop = {"enabled": False}
        options = SplashOptions(prop=prop, context_bundle=self.context_bundle)
        bundle = SplashFactory.create_bundle(options)
        splasher = SplashManager(bundle)
        center_data = CenterData(columns=80, additional_shifter=2)
        splasher.center(center_data, "won't show")
        mock_write.assert_not_called()

    def test_splasher_property_not_validated(self) -> None:
        mock_splash_prop = MagicMock(spec=ISplashProperty)
        mock_splash_prop.is_settings_enabled.return_value = False
        bundle = SplashBundle(
            splash_property=mock_splash_prop,
            terminal_property=MagicMock(spec=ITerminalProperties),
            ext=MagicMock(spec=IExtInfrastructure),
            pb=MagicMock(spec=IProgressBar),
            context_bundle=self.context_bundle
        )
        splasher = SplashManager(bundle)
        self.assertTrue(splasher.is_initialized())

    def test_str(self) -> None:
        prop = {"enabled": False}
        options = SplashOptions(prop=prop, context_bundle=self.context_bundle)
        bundle = SplashFactory.create_bundle(options)
        splasher = SplashManager(bundle)
        self.assertIn("SplashManager", str(splasher))

    def test_get_bundle(self) -> None:
        prop = self._get_valid_prop()
        options = SplashOptions(prop=prop, context_bundle=self.context_bundle)
        bundle = SplashFactory.create_bundle(options)
        splasher = SplashManager(bundle)
        retrieved = splasher.get_bundle()
        self.assertIsInstance(retrieved, SplashBundle)
        self.assertIs(retrieved.context_bundle, self.context_bundle)

    def test_update_bundle(self) -> None:
        prop = self._get_valid_prop()
        options = SplashOptions(prop=prop, context_bundle=self.context_bundle)
        bundle = SplashFactory.create_bundle(options)
        splasher = SplashManager(bundle)
        
        # Valid update
        new_context = ContextFactory.create_bundle()
        new_options = SplashOptions(prop=prop, context_bundle=new_context)
        new_bundle = SplashFactory.create_bundle(new_options)
        self.assertTrue(splasher.update_bundle(new_bundle))
        self.assertIs(splasher.get_context(), new_context)

        # Invalid update
        self.assertFalse(splasher.update_bundle("invalid" * 10))  # type: ignore

    @patch("sys.stdout.write")
    def test_center_empty_or_none_text(self, mock_write: MagicMock) -> None:
        prop = self._get_valid_prop()
        options = SplashOptions(prop=prop, context_bundle=self.context_bundle)
        bundle = SplashFactory.create_bundle(options)
        splasher = SplashManager(bundle)
        
        center_data = CenterData(columns=80, additional_shifter=0)
        # Empty text
        splasher.center(center_data, "")
        mock_write.assert_not_called()
        # None text
        splasher.center(center_data, None)
        mock_write.assert_not_called()

    @patch("sys.stdout.write")
    def test_center_invalid_position(self, mock_write: MagicMock) -> None:
        prop = self._get_valid_prop()
        options = SplashOptions(prop=prop, context_bundle=self.context_bundle)
        bundle = SplashFactory.create_bundle(options)
        splasher = SplashManager(bundle)
        
        # Invalid CenterData (e.g. columns is string)
        center_data = CenterData(columns="invalid", additional_shifter=0)  # type: ignore
        splasher.center(center_data, "hello")
        mock_write.assert_not_called()

    @patch("sys.stdout.write")
    @patch("sys.stdout.flush")
    @patch("time.sleep")
    def test_show_logo_path_none(self, mock_sleep: MagicMock, mock_flush: MagicMock, mock_write: MagicMock) -> None:
        prop = self._get_valid_prop()
        options = SplashOptions(prop=prop, context_bundle=self.context_bundle)
        bundle = SplashFactory.create_bundle(options)
        splasher = SplashManager(bundle)
        
        # Mock get_logo to return None
        splasher._splash_property.get_logo = MagicMock(return_value=None)
        splasher.show()
        
        # Verify it still prints info/issue/author texts, but does not read from file
        printed_content = "".join(call[0][0] for call in mock_write.call_args_list)
        self.assertNotIn("LOGO LINE 1", printed_content)
        self.assertIn("github.io/ats_utilities", printed_content)


if __name__ == "__main__":
    unittest.main()
