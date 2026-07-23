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
    Unit tests for Splasher class.
'''

from __future__ import annotations

import os
import tempfile
import unittest
from typing import Any
from unittest.mock import patch, MagicMock

from ats_utilities.context.factory import ContextFactory
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.splasher.engine import Splasher
from ats_utilities.splasher.data import CenterData
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.splasher.setup.factory import SplashFactory
from ats_utilities.splasher.progressbar.progress_bar import ProgressBar

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class EngineTest(unittest.TestCase):
    '''
        Defines class EngineTest with attribute(s) and method(s).
        Tests Splasher logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init_invalid - Tests error cases with None/wrong argument types.
                | test_splasher_disabled - Tests Splasher when enabled=False.
                | test_splasher_github_valid - Tests GitHub infrastructure and logo rendering.
                | test_splasher_github_invalid_logo - Tests error when reading invalid logo file.
                | test_splasher_external_valid - Tests external infrastructure rendering.
                | test_center_disabled_splash - Tests center logic when show_splash is False.
                | test_str - Tests __str__ method.
    '''

    def setUp(self) -> None:
        self.context_bundle = ContextFactory.create_default_bundle()
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
            pass

    def _get_valid_prop(self) -> dict[str, Any]:
        return {
            "enabled": True,
            SplashKeys.ATS_NAME: "ats_utilities",
            SplashKeys.ATS_REPOSITORY: "ats_utilities",
            SplashKeys.ATS_ORGANIZATION: "vroncevic",
            SplashKeys.ATS_LOGO_PATH: self.temp_logo.name,
            SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE: True
        }

    def test_init_invalid(self) -> None:
        with self.assertRaises(ATSValueError):
            Splasher(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            Splasher(object())  # type: ignore

    @patch("sys.stdout.write")
    @patch("sys.stdout.flush")
    def test_splasher_disabled(self, mock_flush: MagicMock, mock_write: MagicMock) -> None:
        prop = {"enabled": False}
        bundle = SplashFactory.create_splash_bundle_from_dict(prop, self.context_bundle)
        splasher = Splasher(bundle)
        self.assertTrue(splasher.is_initialized())
        self.assertIs(splasher.get_context(), self.context_bundle)
        mock_write.assert_not_called()

    @patch("sys.stdout.write")
    @patch("sys.stdout.flush")
    @patch("time.sleep")
    def test_splasher_github_valid(self, mock_sleep: MagicMock, mock_flush: MagicMock, mock_write: MagicMock) -> None:
        prop = self._get_valid_prop()
        bundle = SplashFactory.create_splash_bundle_from_dict(prop, self.context_bundle)
        splasher = Splasher(bundle)
        self.assertTrue(splasher.is_initialized())

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
        bundle = SplashFactory.create_splash_bundle_from_dict(prop, self.context_bundle)
        with self.assertRaises(ATSValueError):
            Splasher(bundle)

    @patch("sys.stdout.write")
    @patch("sys.stdout.flush")
    @patch("time.sleep")
    def test_splasher_external_valid(self, mock_sleep: MagicMock, mock_flush: MagicMock, mock_write: MagicMock) -> None:
        prop = self._get_valid_prop()
        prop[SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE] = False
        bundle = SplashFactory.create_splash_bundle_from_dict(prop, self.context_bundle)
        splasher = Splasher(bundle)
        self.assertTrue(splasher.is_initialized())

        # Check external texts are printed
        printed_content = "".join(call[0][0] for call in mock_write.call_args_list)
        self.assertIn("ats_utilities", printed_content)
        self.assertIn("ats_utilities", printed_content)
        self.assertIn("vroncevic", printed_content)

    @patch("sys.stdout.write")
    def test_center_disabled_splash(self, mock_write: MagicMock) -> None:
        prop = {"enabled": False}
        bundle = SplashFactory.create_splash_bundle_from_dict(prop, self.context_bundle)
        splasher = Splasher(bundle)
        center_data = CenterData(columns=80, additional_shifter=2)
        splasher.center(center_data, "won't show")
        mock_write.assert_not_called()

    def test_splasher_property_not_validated(self) -> None:
        bundle = SplashFactory.create_splash_bundle_from_dict(None, self.context_bundle)  # type: ignore
        splasher = Splasher(bundle)
        self.assertTrue(splasher.is_initialized())

    def test_str(self) -> None:
        prop = {"enabled": False}
        bundle = SplashFactory.create_splash_bundle_from_dict(prop, self.context_bundle)
        splasher = Splasher(bundle)
        self.assertIn("Splasher", str(splasher))


if __name__ == "__main__":
    unittest.main()
